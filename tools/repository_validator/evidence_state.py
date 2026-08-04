from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path, PurePosixPath
import re
import tomllib

from .registry import SourceRecord


FRONT_MATTER_DELIMITER = "+++"
REVIEW_OUTCOMES = (
    "Confirmed",
    "Corrections required",
    "Unresolved disagreement",
    "Review unavailable",
)


class EvidenceStateError(ValueError):
    pass


@dataclass(frozen=True)
class BriefState:
    path: str
    source_ids: tuple[str, ...]
    evidence_review: str
    integration_audit: str
    last_verified: str
    independent_review: str
    current_use: tuple[str, ...]


def parse_front_matter(text: str, path: str) -> BriefState:
    lines = text.splitlines()
    if not lines or lines[0].strip() != FRONT_MATTER_DELIMITER:
        raise EvidenceStateError(
            "evidence brief must start with TOML front matter delimited by +++"
        )
    try:
        end = next(
            i
            for i, line in enumerate(lines[1:], start=1)
            if line.strip() == FRONT_MATTER_DELIMITER
        )
    except StopIteration as exc:
        raise EvidenceStateError(
            "evidence brief front matter has no closing +++ delimiter"
        ) from exc
    if end == 1:
        raise EvidenceStateError("evidence brief front matter is empty")
    try:
        data = tomllib.loads("\n".join(lines[1:end]))
    except tomllib.TOMLDecodeError as exc:
        raise EvidenceStateError(
            f"invalid evidence brief TOML front matter: {exc}"
        ) from exc

    def string(name: str) -> str:
        value = data.get(name)
        if not isinstance(value, str) or not value.strip():
            raise EvidenceStateError(
                f"front matter field {name} must be a non-empty string"
            )
        return value.strip()

    def strings(name: str, *, allow_empty: bool = False) -> tuple[str, ...]:
        value = data.get(name)
        if not isinstance(value, list) or (not value and not allow_empty):
            qualifier = "an array" if allow_empty else "a non-empty array"
            raise EvidenceStateError(f"front matter field {name} must be {qualifier}")
        if any(not isinstance(item, str) or not item.strip() for item in value):
            raise EvidenceStateError(
                f"front matter field {name} must contain non-empty strings"
            )
        values = tuple(item.strip() for item in value)
        if len(values) != len(set(values)):
            raise EvidenceStateError(
                f"front matter field {name} must not contain duplicates"
            )
        return values

    return BriefState(
        path=path,
        source_ids=strings("source_ids"),
        evidence_review=string("evidence_review"),
        integration_audit=string("integration_audit"),
        last_verified=string("last_verified"),
        independent_review=string("independent_review"),
        current_use=strings("current_use", allow_empty=True),
    )


def registry_current_use_paths(value: str) -> tuple[str, ...]:
    return tuple(dict.fromkeys(re.findall(r"`([^`]+)`", value)))


def validate_repo_path(root: Path, value: str) -> str | None:
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        return "must be a relative repository path without '..'"
    target = root.joinpath(*path.parts)
    if not target.exists():
        return "does not exist"
    return None


def validate_brief_state(
    root: Path,
    brief: BriefState,
    records: dict[str, SourceRecord],
    evidence_statuses: tuple[str, ...],
    integration_statuses: tuple[str, ...],
    empty_date: str,
) -> tuple[str, ...]:
    errors: list[str] = []
    if brief.evidence_review not in evidence_statuses:
        errors.append(
            f"unsupported front matter evidence_review: {brief.evidence_review}"
        )
    if brief.integration_audit not in integration_statuses:
        errors.append(
            f"unsupported front matter integration_audit: {brief.integration_audit}"
        )
    if brief.independent_review not in REVIEW_OUTCOMES:
        errors.append(
            f"unsupported front matter independent_review: {brief.independent_review}"
        )

    if brief.integration_audit == "Verified":
        if brief.evidence_review != "Reviewed brief":
            errors.append("Verified requires evidence_review = Reviewed brief")
        if brief.independent_review != "Confirmed":
            errors.append("Verified requires independent_review = Confirmed")
        try:
            date.fromisoformat(brief.last_verified)
        except ValueError:
            errors.append("Verified requires a valid YYYY-MM-DD last_verified date")
    elif brief.last_verified != empty_date:
        errors.append(f"non-Verified brief requires last_verified = {empty_date}")

    for path in brief.current_use:
        problem = validate_repo_path(root, path)
        if problem:
            errors.append(f"current_use path {path!r} {problem}")

    for source_id in brief.source_ids:
        record = records.get(source_id)
        if record is None:
            errors.append(f"front matter Source ID is not registered: {source_id}")
            continue
        expected = (
            record.evidence_review,
            record.integration_audit,
            record.last_verified,
        )
        actual = (
            brief.evidence_review,
            brief.integration_audit,
            brief.last_verified,
        )
        if actual != expected:
            errors.append(
                f"registry and brief state differ for {source_id}: "
                f"registry={expected}, brief={actual}"
            )
        registry_paths = set(registry_current_use_paths(record.current_use))
        brief_paths = set(brief.current_use)
        if registry_paths != brief_paths:
            errors.append(
                f"registry and brief current_use paths differ for {source_id}: "
                f"registry={sorted(registry_paths)}, brief={sorted(brief_paths)}"
            )
    return tuple(errors)


def validate_transition(old: SourceRecord, new: SourceRecord) -> tuple[str, ...]:
    errors: list[str] = []

    source_identity_changed = old.source != new.source
    if source_identity_changed:
        if new.evidence_review != "Needs re-review":
            errors.append("changed source identity requires Evidence review = Needs re-review")
        if new.integration_audit != "Needs re-verification":
            errors.append(
                "changed source identity requires Integration audit = Needs re-verification"
            )
        if new.last_verified != "—":
            errors.append("changed source identity requires Last verified = —")

    if old.evidence_review == "Reviewed brief" and new.evidence_review == "Registered":
        errors.append("Reviewed brief may not transition directly to Registered")
    if old.integration_audit == "Verified" and new.integration_audit not in {
        "Verified",
        "Needs re-verification",
    }:
        errors.append("Verified may transition only to Verified or Needs re-verification")
    if (
        old.evidence_review != new.evidence_review
        and new.evidence_review == "Needs re-review"
        and new.integration_audit != "Needs re-verification"
    ):
        errors.append(
            "Needs re-review requires integration_audit = Needs re-verification"
        )
    if old.integration_audit != "Verified" and new.integration_audit == "Verified":
        if new.evidence_review != "Reviewed brief":
            errors.append("transition to Verified requires Reviewed brief")
        if new.last_verified == old.last_verified or new.last_verified == "—":
            errors.append("transition to Verified requires a new verification date")
    if (
        old.integration_audit == "Verified"
        and new.integration_audit == "Needs re-verification"
        and new.last_verified != "—"
    ):
        errors.append("reset from Verified requires Last verified = —")
    return tuple(errors)
