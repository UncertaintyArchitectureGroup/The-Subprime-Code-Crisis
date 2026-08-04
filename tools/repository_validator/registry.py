from __future__ import annotations

from dataclasses import dataclass
import re

from .contract import RegistrySectionRequirement
from .markdown import (
    first_link_target,
    is_table_separator_row,
    split_table_row,
    visible_text,
)


_H2_RE = re.compile(r"^##\s+(.+?)\s*#*\s*$")


class RegistryParseError(ValueError):
    """Raised when the Source Registry cannot be parsed without ambiguity."""


@dataclass(frozen=True)
class SourceRecord:
    source_id: str
    source: str
    evidence_review: str
    integration_audit: str
    last_verified: str
    can_support: str
    current_use: str
    brief_link: str | None
    section: str
    expected_prefix: str
    expected_brief_directory: str
    line: int


@dataclass(frozen=True)
class RegistrySection:
    name: str
    heading_line: int
    content_start_line: int
    text: str


def _h2_sections(text: str) -> dict[str, RegistrySection]:
    sections: dict[str, RegistrySection] = {}
    current_name: str | None = None
    current_heading_line = 0
    current_content_start = 0
    current_lines: list[str] = []
    in_fence = False
    fence_marker = ""

    def finish() -> None:
        nonlocal current_name, current_lines
        if current_name is None:
            return
        if current_name in sections:
            raise RegistryParseError(
                f"duplicate level-two Source Registry heading: {current_name}"
            )
        sections[current_name] = RegistrySection(
            name=current_name,
            heading_line=current_heading_line,
            content_start_line=current_content_start,
            text="\n".join(current_lines),
        )
        current_name = None
        current_lines = []

    for line_number, line in enumerate(text.splitlines(), start=1):
        stripped = line.lstrip()
        if stripped.startswith(("```", "~~~")):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = ""
            if current_name is not None:
                current_lines.append(line)
            continue

        heading = None if in_fence else _H2_RE.match(line)
        if heading:
            finish()
            current_name = visible_text(heading.group(1))
            current_heading_line = line_number
            current_content_start = line_number + 1
            continue

        if current_name is not None:
            current_lines.append(line)

    finish()
    return sections


def _table_candidates(lines: list[str]) -> list[int]:
    candidates: list[int] = []
    for index in range(len(lines) - 1):
        if "|" not in lines[index]:
            continue
        headers = split_table_row(lines[index])
        separator = split_table_row(lines[index + 1])
        if (
            len(headers) >= 2
            and len(headers) == len(separator)
            and is_table_separator_row(separator)
        ):
            candidates.append(index)
    return candidates


def _looks_like_later_source_row(
    line: str,
    required_columns: tuple[str, ...],
) -> bool:
    if "|" not in line:
        return False
    return len(split_table_row(line)) == len(required_columns)


def _parse_source_table(
    section: RegistrySection,
    requirement: RegistrySectionRequirement,
    required_columns: tuple[str, ...],
) -> tuple[SourceRecord, ...]:
    lines = section.text.splitlines()
    candidates = _table_candidates(lines)

    if len(candidates) != 1:
        raise RegistryParseError(
            f"section '{section.name}' must contain exactly one source table; "
            f"found {len(candidates)}"
        )

    header_index = candidates[0]
    raw_headers = split_table_row(lines[header_index])
    headers = tuple(visible_text(header) for header in raw_headers)
    if headers != required_columns:
        expected = " | ".join(required_columns)
        actual = " | ".join(headers)
        raise RegistryParseError(
            f"section '{section.name}' has invalid columns; expected '{expected}', "
            f"found '{actual}'"
        )

    records: list[SourceRecord] = []
    cursor = header_index + 2
    while cursor < len(lines):
        line = lines[cursor]
        if not line.strip() or "|" not in line:
            break
        cells = split_table_row(line)
        if len(cells) != len(required_columns):
            raise RegistryParseError(
                f"section '{section.name}' has a malformed source row on line "
                f"{section.content_start_line + cursor}; expected "
                f"{len(required_columns)} columns, found {len(cells)}"
            )
        raw = dict(zip(required_columns, cells, strict=True))
        records.append(
            SourceRecord(
                source_id=visible_text(raw["ID"]),
                source=visible_text(raw["Source"]),
                evidence_review=visible_text(raw["Evidence review"]),
                integration_audit=visible_text(raw["Integration audit"]),
                last_verified=visible_text(raw["Last verified"]),
                can_support=visible_text(raw["Can support"]),
                current_use=visible_text(raw["Current use"]),
                brief_link=first_link_target(raw["Evidence review"]),
                section=section.name,
                expected_prefix=requirement.id_prefix,
                expected_brief_directory=requirement.brief_directory,
                line=section.content_start_line + cursor,
            )
        )
        cursor += 1

    for index in range(cursor, len(lines)):
        line = lines[index]
        if _looks_like_later_source_row(line, required_columns):
            raise RegistryParseError(
                f"section '{section.name}' has a source row after the table was "
                f"interrupted on line {section.content_start_line + index}"
            )

    if len(records) < requirement.minimum_rows:
        raise RegistryParseError(
            f"section '{section.name}' must contain at least "
            f"{requirement.minimum_rows} source row(s); found {len(records)}"
        )
    return tuple(records)


def parse_source_registry(
    text: str,
    required_columns: tuple[str, ...],
    required_sections: tuple[RegistrySectionRequirement, ...],
) -> tuple[SourceRecord, ...]:
    records: list[SourceRecord] = []
    sections = _h2_sections(text)

    for requirement in required_sections:
        section = sections.get(requirement.heading)
        if section is None:
            raise RegistryParseError(
                f"required Source Registry section is missing: {requirement.heading}"
            )
        records.extend(
            _parse_source_table(section, requirement, required_columns)
        )

    if not records:
        raise RegistryParseError("Source Registry contains no source records")
    return tuple(records)
