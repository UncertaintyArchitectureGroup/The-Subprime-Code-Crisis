from __future__ import annotations

from dataclasses import dataclass
import re


_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_HTML_RE = re.compile(r"<[^>]+>")
_TABLE_SEPARATOR_RE = re.compile(r"^:?-{3,}:?$")
_INLINE_CODE_RE = re.compile(r"`([^`]+)`")


@dataclass(frozen=True)
class MarkdownTable:
    headers: tuple[str, ...]
    rows: tuple[tuple[str, ...], ...]
    start_line: int


def visible_text(value: str) -> str:
    """Return a stable visible-text representation of simple Markdown."""
    value = _LINK_RE.sub(r"\1", value)
    value = _INLINE_CODE_RE.sub(r"\1", value)
    value = _HTML_RE.sub("", value)
    for marker in ("**", "__", "*", "_", "~~"):
        value = value.replace(marker, "")
    return " ".join(value.strip().split())


def first_link_target(value: str) -> str | None:
    match = _LINK_RE.search(value)
    return match.group(2).strip() if match else None


def extract_headings(text: str) -> tuple[str, ...]:
    headings: list[str] = []
    in_fence = False
    fence_marker = ""
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith(("```", "~~~")):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = ""
            continue
        if in_fence:
            continue
        match = _HEADING_RE.match(line)
        if match:
            headings.append(visible_text(match.group(2)))
    return tuple(headings)


def _split_table_row(line: str) -> tuple[str, ...]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    cells = re.split(r"(?<!\\)\|", stripped)
    return tuple(cell.replace(r"\|", "|").strip() for cell in cells)


def _is_separator_row(cells: tuple[str, ...]) -> bool:
    return bool(cells) and all(
        _TABLE_SEPARATOR_RE.fullmatch(cell.strip()) for cell in cells
    )


def parse_markdown_tables(text: str) -> tuple[MarkdownTable, ...]:
    lines = text.splitlines()
    tables: list[MarkdownTable] = []
    index = 0
    in_fence = False
    fence_marker = ""

    while index < len(lines):
        stripped = lines[index].lstrip()
        if stripped.startswith(("```", "~~~")):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = ""
            index += 1
            continue
        if in_fence or "|" not in lines[index] or index + 1 >= len(lines):
            index += 1
            continue

        headers = _split_table_row(lines[index])
        separator = _split_table_row(lines[index + 1])
        if (
            len(headers) < 2
            or len(headers) != len(separator)
            or not _is_separator_row(separator)
        ):
            index += 1
            continue

        rows: list[tuple[str, ...]] = []
        cursor = index + 2
        while cursor < len(lines):
            line = lines[cursor]
            if not line.strip() or "|" not in line:
                break
            cells = _split_table_row(line)
            if len(cells) != len(headers):
                break
            rows.append(cells)
            cursor += 1

        tables.append(
            MarkdownTable(
                headers=tuple(visible_text(header) for header in headers),
                rows=tuple(rows),
                start_line=index + 1,
            )
        )
        index = cursor

    return tuple(tables)


def inline_code_bullets_under_heading(text: str, heading: str) -> tuple[str, ...]:
    """Extract `value` bullets below one heading until the next heading."""
    lines = text.splitlines()
    target_level: int | None = None
    collecting = False
    values: list[str] = []
    in_fence = False
    fence_marker = ""

    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith(("```", "~~~")):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = ""
            continue
        if in_fence:
            continue

        heading_match = _HEADING_RE.match(line)
        if heading_match:
            level = len(heading_match.group(1))
            current = visible_text(heading_match.group(2))
            if collecting and target_level is not None and level <= target_level:
                break
            if current == heading:
                collecting = True
                target_level = level
            continue

        if collecting:
            bullet = re.match(r"^\s*-\s+`([^`]+)`\s*$", line)
            if bullet:
                values.append(bullet.group(1))

    return tuple(values)
