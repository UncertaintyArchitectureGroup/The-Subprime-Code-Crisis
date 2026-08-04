from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools.repository_validator.contract import ContractError, load_contract
from tools.repository_validator.validator import RepositoryValidator
from repository_validator.test_validator import (
    REPO_ROOT,
    STATUS_MODEL,
    make_contract,
    registry_text,
)


def write_fixture(root: Path, registry: str) -> None:
    (root / "evidence/primary").mkdir(parents=True)
    (root / "governance").mkdir(parents=True)
    (root / "AGENTS.md").write_text(
        "# AGENTS.md\n\n## Repository Constitution\n", encoding="utf-8"
    )
    (root / "evidence/SOURCES.md").write_text(registry, encoding="utf-8")
    (root / "evidence/primary/example.md").write_text(
        "# Example brief\n", encoding="utf-8"
    )
    (root / "governance/status-model.md").write_text(
        STATUS_MODEL, encoding="utf-8"
    )


def validation_codes(root: Path) -> set[str]:
    return {
        issue.code
        for issue in RepositoryValidator(root, make_contract()).validate()
    }


def write_contract_variant(root: Path, old: str, new: str) -> Path:
    source = (REPO_ROOT / "governance/repository-contract.toml").read_text(
        encoding="utf-8"
    )
    if old not in source:
        raise AssertionError(f"contract fixture text not found: {old}")
    path = root / "repository-contract.toml"
    path.write_text(source.replace(old, new, 1), encoding="utf-8")
    return path


class ContractInvariantTests(unittest.TestCase):
    def test_missing_required_file_and_heading_are_reported(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, registry_text())
            (root / "AGENTS.md").write_text("# AGENTS.md\n", encoding="utf-8")
            (root / "governance/status-model.md").unlink()
            codes = validation_codes(root)
            self.assertIn("required-file-missing", codes)
            self.assertIn("required-heading-missing", codes)

    def test_status_model_drift_is_reported(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, registry_text())
            (root / "governance/status-model.md").write_text(
                STATUS_MODEL.replace("- `Needs re-review`\n", ""),
                encoding="utf-8",
            )
            self.assertIn("evidence-status-model-drift", validation_codes(root))

    def test_noncanonical_extra_status_is_not_ignored(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, registry_text())
            (root / "governance/status-model.md").write_text(
                STATUS_MODEL.replace(
                    "- `Needs re-review`\n",
                    "- `Needs re-review`\n- **Archived**\n",
                ),
                encoding="utf-8",
            )
            codes = validation_codes(root)
            self.assertIn("evidence-status-noncanonical-syntax", codes)
            self.assertIn("evidence-status-model-drift", codes)

    def test_alternate_status_markers_are_not_ignored(self) -> None:
        for marker in ("*", "+", "1."):
            with self.subTest(marker=marker):
                with TemporaryDirectory() as directory:
                    root = Path(directory)
                    write_fixture(root, registry_text())
                    (root / "governance/status-model.md").write_text(
                        STATUS_MODEL.replace(
                            "- `Needs re-review`\n",
                            f"- `Needs re-review`\n{marker} Archived\n",
                        ),
                        encoding="utf-8",
                    )
                    codes = validation_codes(root)
                    self.assertIn("evidence-status-noncanonical-syntax", codes)
                    self.assertIn("evidence-status-model-drift", codes)

    def test_duplicate_status_is_reported(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, registry_text())
            (root / "governance/status-model.md").write_text(
                STATUS_MODEL.replace(
                    "- `Registered`\n",
                    "- `Registered`\n- `Registered`\n",
                    1,
                ),
                encoding="utf-8",
            )
            codes = validation_codes(root)
            self.assertIn("duplicate-evidence-status", codes)
            self.assertIn("evidence-status-model-drift", codes)

    def test_reviewed_brief_link_is_required(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, registry_text(evidence="Reviewed brief"))
            self.assertIn("reviewed-brief-link-required", validation_codes(root))

    def test_reviewed_brief_must_stay_under_evidence(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(
                root,
                registry_text(evidence="[Reviewed brief](../README.md)"),
            )
            self.assertIn(
                "reviewed-brief-link-outside-evidence", validation_codes(root)
            )

    def test_reviewed_brief_cannot_be_class_index(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(
                root,
                registry_text(evidence="[Reviewed brief](primary/README.md)"),
            )
            (root / "evidence/primary/README.md").write_text(
                "# Primary evidence index\n", encoding="utf-8"
            )
            self.assertIn(
                "reviewed-brief-index-prohibited", validation_codes(root)
            )

    def test_reviewed_brief_must_match_evidence_class(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(
                root,
                registry_text(
                    evidence="[Reviewed brief](documentary/example.md)"
                ),
            )
            (root / "evidence/documentary").mkdir(parents=True)
            (root / "evidence/documentary/example.md").write_text(
                "# Documentary brief\n", encoding="utf-8"
            )
            self.assertIn("reviewed-brief-wrong-class", validation_codes(root))

    def test_malformed_required_registry_header_is_reported(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            broken = registry_text().replace(
                "| ID | Source | Evidence review | Integration audit | Last verified | Can support | Current use |",
                "| ID | Source | Evidence review |",
            )
            write_fixture(root, broken)
            self.assertIn("source-registry-parse", validation_codes(root))

    def test_malformed_middle_registry_row_is_reported(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            valid = registry_text()
            original_row = next(
                line for line in valid.splitlines() if line.startswith("| **P-")
            )
            broken_row = "| **P-2025-99** | Broken source | Registered |"
            later_row = (
                "| **P-2025-02** | Later source | Registered | Not started | — | "
                "Bounded finding | `report/01_the_illusion.md` |"
            )
            broken = valid.replace(
                original_row,
                original_row + "\n" + broken_row + "\n" + later_row,
            )
            write_fixture(root, broken)
            self.assertIn("source-registry-parse", validation_codes(root))

    def test_interrupted_registry_table_is_reported(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            valid = registry_text()
            original_row = next(
                line for line in valid.splitlines() if line.startswith("| **P-")
            )
            later_row = (
                "| **P-2025-02** | Later source | Registered | Not started | — | "
                "Bounded finding | `report/01_the_illusion.md` |"
            )
            broken = valid.replace(
                original_row,
                original_row + "\n\n" + later_row,
            )
            write_fixture(root, broken)
            self.assertIn("source-registry-parse", validation_codes(root))

    def test_required_registry_section_cannot_be_empty(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            registry = registry_text()
            row = next(
                line for line in registry.splitlines() if line.startswith("| **P-")
            )
            write_fixture(root, registry.replace(row + "\n", ""))
            self.assertIn("source-registry-parse", validation_codes(root))

    def test_source_id_must_match_registry_section(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, registry_text(source_id="D-2026-01"))
            self.assertIn("source-id-section-mismatch", validation_codes(root))

    def test_verified_requires_reviewed_brief(self) -> None:
        for evidence_status in ("Registered", "Brief in progress", "Needs re-review"):
            with self.subTest(evidence_status=evidence_status):
                with TemporaryDirectory() as directory:
                    root = Path(directory)
                    write_fixture(
                        root,
                        registry_text(
                            evidence=evidence_status,
                            integration="Verified",
                            verified="2026-07-27",
                        ),
                    )
                    self.assertIn(
                        "verified-requires-reviewed-brief",
                        validation_codes(root),
                    )

    def test_contract_rejects_invalid_regex(self) -> None:
        with TemporaryDirectory() as directory:
            path = write_contract_variant(
                Path(directory),
                r"source_id_pattern = '^(?:P|D|S|M)-\d{4}-\d{2}$'",
                "source_id_pattern = '['",
            )
            with self.assertRaises(ContractError):
                load_contract(path)

    def test_contract_rejects_unprotected_canonical_reference(self) -> None:
        with TemporaryDirectory() as directory:
            path = write_contract_variant(
                Path(directory),
                '  "AGENTS.md",\n',
                "",
            )
            with self.assertRaises(ContractError):
                load_contract(path)

    def test_contract_rejects_incompatible_registry_prefix(self) -> None:
        with TemporaryDirectory() as directory:
            path = write_contract_variant(
                Path(directory),
                'id_prefix = "P-"',
                'id_prefix = "X-"',
            )
            with self.assertRaises(ContractError):
                load_contract(path)

    def test_contract_rejects_nested_brief_directory(self) -> None:
        with TemporaryDirectory() as directory:
            path = write_contract_variant(
                Path(directory),
                'brief_directory = "primary"',
                'brief_directory = "primary/nested"',
            )
            with self.assertRaises(ContractError):
                load_contract(path)


if __name__ == "__main__":
    unittest.main()
