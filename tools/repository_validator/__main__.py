from __future__ import annotations

import argparse
from pathlib import Path
import sys

from .contract import ContractError
from .validator import validate_repository


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate the executable repository contract."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="repository root (default: current directory)",
    )
    parser.add_argument(
        "--contract",
        type=Path,
        default=None,
        help="contract path (default: <root>/governance/repository-contract.toml)",
    )
    parser.add_argument(
        "--format",
        choices=("text", "github"),
        default="text",
        help="output format",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    contract_path = args.contract
    if contract_path is not None and not contract_path.is_absolute():
        contract_path = args.root / contract_path

    try:
        issues = validate_repository(args.root, contract_path)
    except ContractError as exc:
        if args.format == "github":
            print(
                "::error file=governance/repository-contract.toml::"
                f"[contract-invalid] {exc}"
            )
        else:
            print(f"governance/repository-contract.toml: [contract-invalid] {exc}")
        return 2

    if issues:
        for issue in issues:
            print(issue.github_annotation() if args.format == "github" else issue.text())
        print(f"Repository contract failed with {len(issues)} issue(s).")
        return 1

    print("Repository contract passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
