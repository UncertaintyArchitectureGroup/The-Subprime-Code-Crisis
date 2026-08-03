from __future__ import annotations

from dataclasses import dataclass
import re

from .markdown import first_link_target, parse_markdown_tables, visible_text


_H2_RE = re.compile(r"^##\s+(.+?)\s*#*\s*$")


class RegistryParseError(ValueError):
    """Raised when the Source Registry table cannot be parsed."""


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


def parse_source_registry(
    text: str,
    required_columns: tuple[str, ...],
    required_sections: tuple[str, ...],
) -> tuple[SourceRecord, ...]:
    records: list[SourceRecord] = []
    sections = _h2_sections(text)
    expected = " | ".join(required_columns)

    for section_name in required_sections:
        section = sections.get(section_name)
        if section is None:
            raise RegistryParseError(
                f"required Source Registry section is missing: {section_name}"
            )

        tables = parse_markdown_tables(section.text)
        if len(tables) != 1:
            raise RegistryParseError(
                f"section '{section_name}' must contain exactly one source table; "
                f"found {len(tables)}"
            )

        table = tables[0]
        if table.headers != required_columns:
            actual = " | ".join(table.headers)
            raise RegistryParseError(
                f"section '{section_name}' has invalid columns; expected "
                f"'{expected}', found '{actual}'"
            )

        for offset, row in enumerate(table.rows, start=2):
            raw = dict(zip(table.headers, row, strict=True))
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
                    line=(
                        section.content_start_line
                        + table.start_line
                        + offset
                        - 1
                    ),
                )
            )

    if not records:
        raise RegistryParseError("Source Registry contains no source records")
    return tuple(records)
