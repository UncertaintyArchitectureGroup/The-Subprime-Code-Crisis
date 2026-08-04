from __future__ import annotations

import argparse
from pathlib import Path
import sys

from tools.repository_validator.contract import load_contract
from tools.repository_validator.evidence_state import (
    EvidenceStateError,
    parse_front_matter,
    registry_current_use_paths,
    validate_brief_state,
    validate_registry_current_use,
    validate_repo_path,
)
from tools.repository_validator.registry import RegistryParseError, parse_source_registry


def check(policy_root: Path, candidate_root: Path | None = None) -> tuple[str, ...]:
    policy_root = policy_root.resolve()
    candidate_root = (candidate_root or policy_root).resolve()
    contract = load_contract(policy_root / "governance/repository-contract.toml")
    registry_path = candidate_root / contract.source_registry
    try:
        records = parse_source_registry(
            registry_path.read_text(encoding="utf-8"),
            contract.registry.required_columns,
            contract.registry.sections,
            contract.registry.source_id_pattern,
        )
    except (OSError, UnicodeError, RegistryParseError) as exc:
        return (f"{contract.source_registry}: {exc}",)

    by_id = {record.source_id: record for record in records}
    errors: list[str] = []
    linked_briefs: dict[str, set[str]] = {}

    for record in records:
        current_use_source = record.current_use_raw or record.current_use
        for issue in validate_registry_current_use(current_use_source):
            errors.append(
                f"{contract.source_registry}:{record.line}: {record.source_id} {issue}"
            )
        for value in registry_current_use_paths(current_use_source):
            problem = validate_repo_path(candidate_root, value)
            if problem:
                errors.append(
                    f"{contract.source_registry}:{record.line}: {record.source_id} "
                    f"Current use path {value!r} {problem}"
                )
        if record.brief_link:
            brief_path = (registry_path.parent / record.brief_link).resolve()
            try:
                relative = brief_path.relative_to(candidate_root).as_posix()
            except ValueError:
                errors.append(
                    f"{contract.source_registry}:{record.line}: {record.source_id} "
                    "brief link escapes the candidate repository"
                )
                continue
            linked_briefs.setdefault(relative, set()).add(record.source_id)

    for relative, linked_ids in sorted(linked_briefs.items()):
        path = candidate_root / relative
        try:
            brief = parse_front_matter(path.read_text(encoding="utf-8"), relative)
        except (OSError, UnicodeError, EvidenceStateError) as exc:
            errors.append(f"{relative}: {exc}")
            continue
        if set(brief.source_ids) != linked_ids:
            errors.append(
                f"{relative}: front matter source_ids {sorted(brief.source_ids)} do not "
                f"match registry links {sorted(linked_ids)}"
            )
        for error in validate_brief_state(
            candidate_root,
            brief,
            by_id,
            contract.evidence_review_statuses,
            contract.integration_audit_statuses,
            contract.registry.empty_date,
        ):
            errors.append(f"{relative}: {error}")

    return tuple(errors)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate registry and evidence-brief state integrity"
    )
    parser.add_argument("--policy-root", type=Path, default=Path.cwd())
    parser.add_argument("--candidate-root", type=Path)
    args = parser.parse_args(argv)
    errors = check(args.policy_root, args.candidate_root)
    if errors:
        for error in errors:
            print(f"::error::{error}")
        print(f"Evidence-state integrity failed with {len(errors)} issue(s).")
        return 1
    print("Evidence-state integrity passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
