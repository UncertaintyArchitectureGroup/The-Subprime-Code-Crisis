from __future__ import annotations

from dataclasses import dataclass
import re

from .contract import RegistrySectionRequirement
from .markdown import (
    first_link_target,
    is_table_separator_row,
    scan_markdown_lines,
    split_table_row,
    visible_text,
)


_H2_RE = re.compile(r"^##\s+(.+?)\s*#*\s*$")
_MALFORMED_ID_SUFFIX_RE = re.compile(r"^[A-Z0-9._-]*[A-Z0-9][A-Z0-9._-]*$")


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
    current_use_raw: str = ""


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

    for source_line in scan_markdown_lines(text):
        line = source_line.text if source_line.active else ""
        heading = _H2_RE.match(line) if source_line.active else None
        if heading:
            finish()
            current_name = visible_text(heading.group(1))
            current_heading_line = source_line.line
            current_content_start = source_line.line + 1
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


def _source_id_at_row_start(
    line: str,
    source_id_pattern: str,
    source_prefixes: tuple[str, ...],
) -> bool:
    if not line.strip():
        return False

    if "|" in line:
        cells = split_table_row(line)
        if not cells:
            return False
        candidate = visible_text(cells[0])
    else:
        visible = visible_text(line)
        if not visible:
            return False
        candidate = visible.split(maxsplit=1)[0].rstrip(":;,.—–")

    if re.fullmatch(source_id_pattern, candidate) is not None:
        return True

    for prefix in sorted(source_prefixes, key=len, reverse=True):
        if not candidate.startswith(prefix):
            continue
        suffix = candidate[len(prefix) :]
        return _MALFORMED_ID_SUFFIX_RE.fullmatch(suffix) is not None
    return False


def _parse_source_table(
    section: RegistrySection,
    requirement: RegistrySectionRequirement,
    required_columns: tuple[str, ...],
    source_id_pattern: str,
    source_prefixes: tuple[str, ...],
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
                current_use_raw=raw["Current use"].strip(),
            )
        )
        cursor += 1

    for index in range(cursor, len(lines)):
        line = lines[index]
        if _source_id_at_row_start(line, source_id_pattern, source_prefixes):
            raise RegistryParseError(
                f"section '{section.name}' has a source-like row after the table was "
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
    source_id_pattern: str,
) -> tuple[SourceRecord, ...]:
    records: list[SourceRecord] = []
    sections = _h2_sections(text)
    source_prefixes = tuple(section.id_prefix for section in required_sections)

    for requirement in required_sections:
        section = sections.get(requirement.heading)
        if section is None:
            raise RegistryParseError(
                f"required Source Registry section is missing: {requirement.heading}"
            )
        records.extend(
            _parse_source_table(
                section,
                requirement,
                required_columns,
                source_id_pattern,
                source_prefixes,
            )
        )

    return tuple(records)
