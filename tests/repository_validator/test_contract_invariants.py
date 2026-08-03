from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools.repository_validator.validator import RepositoryValidator
from repository_validator.test_validator import (
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


class ContractInvariantTests(unittest.TestCase):
    def test_missing_required_file_and_heading_are_reported(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, registry_text())
            (root / "AGENTS.md").write_text("# AGENTS.md\n", encoding="utf-8")
            (root / "governance/status-model.md").unlink()
            codes = {
                issue.code
                for issue in RepositoryValidator(root, make_contract()).validate()
            }
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
            codes = {
                issue.code
                for issue in RepositoryValidator(root, make_contract()).validate()
            }
            self.assertIn("evidence-status-model-drift", codes)

    def test_reviewed_brief_link_is_required(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, registry_text(evidence="Reviewed brief"))
            codes = {
                issue.code
                for issue in RepositoryValidator(root, make_contract()).validate()
            }
            self.assertIn("reviewed-brief-link-required", codes)

    def test_reviewed_brief_must_stay_under_evidence(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(
                root,
                registry_text(evidence="[Reviewed brief](../README.md)"),
            )
            codes = {
                issue.code
                for issue in RepositoryValidator(root, make_contract()).validate()
            }
            self.assertIn("reviewed-brief-link-outside-evidence", codes)

    def test_malformed_required_registry_table_is_reported(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            broken = registry_text().replace(
                "| ID | Source | Evidence review | Integration audit | Last verified | Can support | Current use |",
                "| ID | Source | Evidence review |",
            )
            write_fixture(root, broken)
            codes = {
                issue.code
                for issue in RepositoryValidator(root, make_contract()).validate()
            }
            self.assertIn("source-registry-parse", codes)


if __name__ == "__main__":
    unittest.main()
