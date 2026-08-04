from __future__ import annotations

from dataclasses import dataclass
import re


_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_HTML_RE = re.compile(r"<[^>]+>")
_TABLE_SEPARATOR_RE = re.compile(r"^:?-{3,}:?$")
_INLINE_CODE_RE = re.compile(r"`([^`]+)`")
_LIST_ITEM_RE = re.compile(
    r"^\s*(?P<marker>[-+*]|\d+[.)])\s+(?P<body>.*?)\s*$"
)
_CANONICAL_STATUS_ITEM_RE = re.compile(r"^`([^`]+)`$")


@dataclass(frozen=True)
class MarkdownTable:
    headers: tuple[str, ...]
    rows: tuple[tuple[str, ...], ...]
    start_line: int


@dataclass(frozen=True)
class MarkdownListItem:
    value: str
    raw: str
    marker: str
    line: int
    canonical_inline_code: bool


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


def split_table_row(line: str) -> tuple[str, ...]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    cells = re.split(r"(?<!\\)\|", stripped)
    return tuple(cell.replace(r"\|", "|").strip() for cell in cells)


def is_table_separator_row(cells: tuple[str, ...]) -> bool:
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

        headers = split_table_row(lines[index])
        separator = split_table_row(lines[index + 1])
        if (
            len(headers) < 2
            or len(headers) != len(separator)
            or not is_table_separator_row(separator)
        ):
            index += 1
            continue

        rows: list[tuple[str, ...]] = []
        cursor = index + 2
        while cursor < len(lines):
            line = lines[cursor]
            if not line.strip() or "|" not in line:
                break
            cells = split_table_row(line)
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


def list_items_under_heading(text: str, heading: str) -> tuple[MarkdownListItem, ...]:
    """Return every Markdown list item in one heading block."""
    collecting = False
    items: list[MarkdownListItem] = []
    in_fence = False
    fence_marker = ""

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
            continue
        if in_fence:
            continue

        heading_match = _HEADING_RE.match(line)
        if heading_match:
            current = visible_text(heading_match.group(2))
            if collecting:
                break
            if current == heading:
                collecting = True
            continue

        if not collecting:
            continue
        bullet = _LIST_ITEM_RE.match(line)
        if not bullet:
            continue
        marker = bullet.group("marker")
        raw = bullet.group("body").strip()
        canonical = marker == "-" and _CANONICAL_STATUS_ITEM_RE.fullmatch(raw)
        items.append(
            MarkdownListItem(
                value=visible_text(raw),
                raw=raw,
                marker=marker,
                line=line_number,
                canonical_inline_code=canonical is not None,
            )
        )

    return tuple(items)


def inline_code_bullets_under_heading(text: str, heading: str) -> tuple[str, ...]:
    """Compatibility helper returning only canonical inline-code list values."""
    return tuple(
        item.value
        for item in list_items_under_heading(text, heading)
        if item.canonical_inline_code
    )
