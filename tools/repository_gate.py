from __future__ import annotations

import argparse
from dataclasses import dataclass
from fnmatch import fnmatch
from pathlib import Path
import subprocess
import sys
import tomllib


INDEPENDENT_REVIEW_STATUSES = (
    "Confirmed",
    "Corrections required",
    "Unresolved disagreement",
    "Review unavailable",
)


class GateError(ValueError):
    pass


@dataclass(frozen=True)
class Change:
    status: str
    path: str
    old_path: str | None = None


@dataclass(frozen=True)
class Rule:
    name: str
    patterns: tuple[str, ...]
    primary_surface: str
    requires: tuple[str, ...]


def _git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode:
        raise GateError(result.stderr.strip() or "git command failed")
    return result.stdout


def changed_paths(repo: Path, base: str, head: str) -> tuple[Change, ...]:
    output = _git(repo, "diff", "--name-status", "--find-renames", f"{base}...{head}")
    changes: list[Change] = []
    for line in output.splitlines():
        parts = line.split("\t")
        if not parts:
            continue
        status = parts[0]
        if status.startswith("R"):
            if len(parts) != 3:
                raise GateError(f"malformed rename record: {line}")
            changes.append(Change(status="R", old_path=parts[1], path=parts[2]))
        elif len(parts) == 2:
            changes.append(Change(status=status[0], path=parts[1]))
        else:
            raise GateError(f"malformed change record: {line}")
    return tuple(changes)


def _nonempty_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise GateError(f"{label} must be a non-empty string")
    return value


def _string_array(value: object, label: str, *, allow_empty: bool = False) -> tuple[str, ...]:
    if not isinstance(value, list) or (not value and not allow_empty):
        raise GateError(f"{label} must be a non-empty array")
    if any(not isinstance(item, str) or not item.strip() for item in value):
        raise GateError(f"{label} must contain only non-empty strings")
    if len(value) != len(set(value)):
        raise GateError(f"{label} must not contain duplicates")
    return tuple(value)


def load_matrix(path: Path) -> tuple[tuple[str, ...], tuple[str, ...], tuple[Rule, ...]]:
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    if data.get("matrix_version") != 1:
        raise GateError("synchronization matrix version must be 1")

    critical = _string_array(data.get("critical_paths"), "critical_paths")
    allowed = _string_array(
        data.get("allowed_surfaces", {}).get("values")
        if isinstance(data.get("allowed_surfaces"), dict)
        else None,
        "allowed_surfaces.values",
    )

    raw_rules = data.get("classifiers")
    if not isinstance(raw_rules, list) or not raw_rules:
        raise GateError("classifiers must contain at least one rule")

    rules: list[Rule] = []
    names: set[str] = set()
    known = set(allowed)
    for index, item in enumerate(raw_rules):
        if not isinstance(item, dict):
            raise GateError(f"classifiers[{index}] must be a table")
        name = _nonempty_string(item.get("name"), f"classifiers[{index}].name")
        if name in names:
            raise GateError(f"duplicate classifier name: {name}")
        names.add(name)
        patterns = _string_array(item.get("patterns"), f"classifier {name}.patterns")
        primary = _nonempty_string(
            item.get("primary_surface"), f"classifier {name}.primary_surface"
        )
        requires = _string_array(item.get("requires"), f"classifier {name}.requires")
        if primary not in known or not set(requires) <= known:
            raise GateError(f"classifier {name} references an unknown surface")
        rules.append(
            Rule(
                name=name,
                patterns=patterns,
                primary_surface=primary,
                requires=requires,
            )
        )

    return critical, allowed, tuple(rules)


def classify(path: str, rules: tuple[Rule, ...]) -> tuple[str, tuple[str, ...]]:
    matching = [rule for rule in rules if any(fnmatch(path, pattern) for pattern in rule.patterns)]
    if not matching:
        raise GateError(f"changed path is not classified: {path}")
    required: set[str] = set()
    for rule in matching:
        required.update(rule.requires)
    return matching[0].primary_surface, tuple(sorted(required))


def load_work_record(path: Path, allowed_surfaces: tuple[str, ...]) -> dict:
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    if data.get("record_version") != 1:
        raise GateError("work record version must be 1")

    for key in ("title", "primary_flow", "human_decision"):
        _nonempty_string(data.get(key), f"work record field {key}")

    independent_review = _nonempty_string(
        data.get("independent_review"), "work record field independent_review"
    )
    if independent_review not in INDEPENDENT_REVIEW_STATUSES:
        raise GateError(
            "independent_review must be one of: "
            + ", ".join(INDEPENDENT_REVIEW_STATUSES)
        )

    changelog = data.get("changelog")
    if not isinstance(changelog, dict):
        raise GateError("changelog must be a table")
    decision = changelog.get("decision")
    if decision not in {"Updated", "Not required"}:
        raise GateError("changelog.decision must be Updated or Not required")
    reason = changelog.get("reason", "")
    if decision == "Not required" and (
        not isinstance(reason, str) or not reason.strip()
    ):
        raise GateError("Not required changelog decision needs a specific reason")
    if decision == "Updated" and reason is not None and not isinstance(reason, str):
        raise GateError("changelog.reason must be a string when present")

    sync = data.get("synchronization")
    if not isinstance(sync, dict):
        raise GateError("synchronization must be a table")
    assessed = _string_array(
        sync.get("assessed_surfaces"), "synchronization.assessed_surfaces"
    )
    unknown = set(assessed) - set(allowed_surfaces)
    if unknown:
        raise GateError(
            "work record contains unknown surfaces: " + ", ".join(sorted(unknown))
        )

    non_applicable = sync.get("non_applicable", {})
    if not isinstance(non_applicable, dict):
        raise GateError("synchronization.non_applicable must be a table")
    for surface, explanation in non_applicable.items():
        if (
            surface not in assessed
            or not isinstance(explanation, str)
            or not explanation.strip()
        ):
            raise GateError(f"invalid non-applicable synchronization record: {surface}")
    return data


def validate(
    policy_root: Path,
    candidate_root: Path,
    repo: Path,
    base: str,
    head: str,
) -> tuple[str, ...]:
    matrix_path = policy_root / "governance/synchronization-matrix.toml"
    critical, allowed, rules = load_matrix(matrix_path)
    changes = changed_paths(repo, base, head)
    errors: list[str] = []

    for change in changes:
        removed = change.old_path if change.status == "R" else change.path
        if change.status in {"D", "R"} and removed in critical:
            errors.append(f"critical path may not be deleted or renamed: {removed}")

    record_changes = [
        change
        for change in changes
        if change.path.startswith("governance/work-records/")
        and change.path.endswith(".toml")
        and change.status == "A"
    ]
    if len(record_changes) != 1:
        errors.append("exactly one new governance/work-records/*.toml file is required")
        return tuple(errors)

    record_path = candidate_root / record_changes[0].path
    try:
        record = load_work_record(record_path, allowed)
    except (OSError, UnicodeError, tomllib.TOMLDecodeError, GateError) as exc:
        errors.append(f"invalid work record: {exc}")
        return tuple(errors)

    required_surfaces: set[str] = set()
    for change in changes:
        try:
            _, required = classify(change.path, rules)
            required_surfaces.update(required)
            if change.old_path:
                _, old_required = classify(change.old_path, rules)
                required_surfaces.update(old_required)
        except GateError as exc:
            errors.append(str(exc))

    assessed = set(record["synchronization"]["assessed_surfaces"])
    missing = required_surfaces - assessed
    if missing:
        errors.append(
            "work record omits required synchronization surfaces: "
            + ", ".join(sorted(missing))
        )

    decision = record["changelog"]["decision"]
    changelog_changed = any(change.path == "CHANGELOG.md" for change in changes)
    if decision == "Updated" and not changelog_changed:
        errors.append("changelog decision is Updated but CHANGELOG.md did not change")
    if decision == "Not required" and changelog_changed:
        errors.append("CHANGELOG.md changed while the work record says Not required")

    return tuple(errors)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate PR process and synchronization contract"
    )
    parser.add_argument("--policy-root", type=Path, required=True)
    parser.add_argument("--candidate-root", type=Path, required=True)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", required=True)
    args = parser.parse_args(argv)
    try:
        errors = validate(
            args.policy_root.resolve(),
            args.candidate_root.resolve(),
            args.repo.resolve(),
            args.base,
            args.head,
        )
    except (GateError, OSError, UnicodeError, tomllib.TOMLDecodeError) as exc:
        errors = (str(exc),)
    if errors:
        for error in errors:
            print(f"::error::{error}")
        print(f"Repository Gate failed with {len(errors)} issue(s).")
        return 1
    print("Repository Gate passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
