from __future__ import annotations

from dataclasses import dataclass

from .markdown import first_link_target, parse_markdown_tables, visible_text


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


def parse_source_registry(
    text: str, required_columns: tuple[str, ...]
) -> tuple[SourceRecord, ...]:
    records: list[SourceRecord] = []
    matching_tables = 0

    for table in parse_markdown_tables(text):
        if table.headers != required_columns:
            continue
        matching_tables += 1
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
                    line=table.start_line + offset,
                )
            )

    if matching_tables == 0:
        expected = " | ".join(required_columns)
        raise RegistryParseError(
            f"no Source Registry tables found with required columns: {expected}"
        )
    if not records:
        raise RegistryParseError("Source Registry contains no source records")
    return tuple(records)
