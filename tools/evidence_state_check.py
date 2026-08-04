from __future__ import annotations

from pathlib import Path
import sys

from tools.repository_validator.contract import load_contract
from tools.repository_validator.evidence_state import (
    EvidenceStateError,
    parse_front_matter,
    registry_current_use_paths,
    validate_brief_state,
    validate_repo_path,
)
from tools.repository_validator.registry import RegistryParseError, parse_source_registry


def check(root: Path) -> tuple[str, ...]:
    contract = load_contract(root / "governance/repository-contract.toml")
    registry_path = root / contract.source_registry
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
        for value in registry_current_use_paths(record.current_use):
            problem = validate_repo_path(root, value)
            if problem:
                errors.append(
                    f"{contract.source_registry}:{record.line}: {record.source_id} "
                    f"Current use path {value!r} {problem}"
                )
        if record.brief_link:
            brief_path = (registry_path.parent / record.brief_link).resolve()
            try:
                relative = brief_path.relative_to(root.resolve()).as_posix()
            except ValueError:
                continue
            linked_briefs.setdefault(relative, set()).add(record.source_id)

    for relative, linked_ids in sorted(linked_briefs.items()):
        path = root / relative
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
            root,
            brief,
            by_id,
            contract.evidence_review_statuses,
            contract.integration_audit_statuses,
            contract.registry.empty_date,
        ):
            errors.append(f"{relative}: {error}")

    return tuple(errors)


def main() -> int:
    errors = check(Path.cwd())
    if errors:
        for error in errors:
            print(f"::error::{error}")
        print(f"Evidence-state integrity failed with {len(errors)} issue(s).")
        return 1
    print("Evidence-state integrity passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
