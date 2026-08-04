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
_FENCE_OPEN_RE = re.compile(r"^ {0,3}(?P<marker>`{3,}|~{3,})")
_INDENTED_CODE_RE = re.compile(r"^(?:\t| {4,})")


@dataclass(frozen=True)
class MarkdownSourceLine:
    text: str
    line: int
    active: bool


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


def _strip_html_comments(line: str, in_comment: bool) -> tuple[str, bool]:
    visible: list[str] = []
    cursor = 0
    while cursor < len(line):
        if in_comment:
            end = line.find("-->", cursor)
            if end == -1:
                return "".join(visible), True
            cursor = end + 3
            in_comment = False
            continue

        start = line.find("<!--", cursor)
        if start == -1:
            visible.append(line[cursor:])
            break
        visible.append(line[cursor:start])
        cursor = start + 4
        in_comment = True

    return "".join(visible), in_comment


def _closes_fence(line: str, fence_character: str, fence_length: int) -> bool:
    stripped = line.lstrip(" ")
    if len(line) - len(stripped) > 3 or not stripped.startswith(fence_character):
        return False
    marker_length = len(stripped) - len(stripped.lstrip(fence_character))
    return marker_length >= fence_length and not stripped[marker_length:].strip()


def scan_markdown_lines(text: str) -> tuple[MarkdownSourceLine, ...]:
    """Return source lines with inactive Markdown constructs blanked out."""
    scanned: list[MarkdownSourceLine] = []
    in_comment = False
    in_fence = False
    fence_character = ""
    fence_length = 0

    for line_number, original in enumerate(text.splitlines(), start=1):
        if in_fence:
            if _closes_fence(original, fence_character, fence_length):
                in_fence = False
                fence_character = ""
                fence_length = 0
            scanned.append(MarkdownSourceLine("", line_number, False))
            continue

        without_comments, in_comment = _strip_html_comments(original, in_comment)
        fence = _FENCE_OPEN_RE.match(without_comments)
        if fence:
            marker = fence.group("marker")
            in_fence = True
            fence_character = marker[0]
            fence_length = len(marker)
            scanned.append(MarkdownSourceLine("", line_number, False))
            continue

        if without_comments.strip() and _INDENTED_CODE_RE.match(without_comments):
            scanned.append(MarkdownSourceLine("", line_number, False))
            continue

        active = bool(without_comments.strip())
        scanned.append(
            MarkdownSourceLine(
                text=without_comments,
                line=line_number,
                active=active,
            )
        )

    return tuple(scanned)


def extract_headings(text: str) -> tuple[str, ...]:
    headings: list[str] = []
    for source_line in scan_markdown_lines(text):
        if not source_line.active:
            continue
        match = _HEADING_RE.match(source_line.text)
        if match:
            headings.append(visible_text(match.group(2)))
    return tuple(headings)


def heading_lines(text: str, heading: str) -> tuple[int, ...]:
    """Return line numbers for every active occurrence of one Markdown heading."""
    lines: list[int] = []
    for source_line in scan_markdown_lines(text):
        if not source_line.active:
            continue
        match = _HEADING_RE.match(source_line.text)
        if match and visible_text(match.group(2)) == heading:
            lines.append(source_line.line)
    return tuple(lines)


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
    source_lines = scan_markdown_lines(text)
    lines = [source_line.text if source_line.active else "" for source_line in source_lines]
    tables: list[MarkdownTable] = []
    index = 0

    while index < len(lines):
        if "|" not in lines[index] or index + 1 >= len(lines):
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
                start_line=source_lines[index].line,
            )
        )
        index = cursor

    return tuple(tables)


def list_items_under_heading(text: str, heading: str) -> tuple[MarkdownListItem, ...]:
    """Return every active Markdown list item in one heading block."""
    collecting = False
    items: list[MarkdownListItem] = []

    for source_line in scan_markdown_lines(text):
        if not source_line.active:
            continue

        heading_match = _HEADING_RE.match(source_line.text)
        if heading_match:
            current = visible_text(heading_match.group(2))
            if collecting:
                break
            if current == heading:
                collecting = True
            continue

        if not collecting:
            continue
        bullet = _LIST_ITEM_RE.match(source_line.text)
        if not bullet:
            continue
        marker = bullet.group("marker")
        raw = bullet.group("body").strip()
        canonical = (
            marker == "-" and _CANONICAL_STATUS_ITEM_RE.fullmatch(raw) is not None
        )
        items.append(
            MarkdownListItem(
                value=visible_text(raw),
                raw=raw,
                marker=marker,
                line=source_line.line,
                canonical_inline_code=canonical,
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
