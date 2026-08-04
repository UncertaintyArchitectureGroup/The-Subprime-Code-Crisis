from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys

from tools.repository_validator.contract import load_contract
from tools.repository_validator.evidence_state import validate_transition
from tools.repository_validator.registry import RegistryParseError, parse_source_registry


def git_show(repo: Path, ref: str, path: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), "show", f"{ref}:{path}"],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode:
        raise ValueError(result.stderr.strip() or f"cannot read {path} at {ref}")
    return result.stdout


def parse_records(text: str, contract):
    return parse_source_registry(
        text,
        contract.registry.required_columns,
        contract.registry.sections,
        contract.registry.source_id_pattern,
    )


def check(policy_root: Path, candidate_root: Path, repo: Path, base: str) -> tuple[str, ...]:
    contract = load_contract(policy_root / "governance/repository-contract.toml")
    registry_path = contract.source_registry
    try:
        old_records = parse_records(git_show(repo, base, registry_path), contract)
        new_records = parse_records(
            (candidate_root / registry_path).read_text(encoding="utf-8"), contract
        )
    except (OSError, UnicodeError, ValueError, RegistryParseError) as exc:
        return (f"cannot compare evidence states: {exc}",)

    old = {record.source_id: record for record in old_records}
    new = {record.source_id: record for record in new_records}
    errors: list[str] = []
    removed = sorted(set(old) - set(new))
    if removed:
        errors.append("registered sources may not be removed: " + ", ".join(removed))
    for source_id in sorted(set(old) & set(new)):
        for error in validate_transition(old[source_id], new[source_id]):
            errors.append(f"{source_id}: {error}")
    return tuple(errors)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--policy-root", type=Path, required=True)
    parser.add_argument("--candidate-root", type=Path, required=True)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--base", required=True)
    args = parser.parse_args()
    errors = check(args.policy_root, args.candidate_root, args.repo, args.base)
    if errors:
        for error in errors:
            print(f"::error::{error}")
        return 1
    print("Evidence-state transitions passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
