from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools.repository_validator.validator import RepositoryValidator
from repository_validator.test_validator import (
    STATUS_MODEL,
    dataset_registry_text,
    make_contract,
    make_dataset_contract,
    registry_text,
)


def write_fixture(root: Path, registry: str, status_model: str = STATUS_MODEL) -> None:
    (root / "evidence/primary").mkdir(parents=True)
    (root / "governance").mkdir(parents=True)
    (root / "AGENTS.md").write_text(
        "# AGENTS.md\n\n## Repository Constitution\n", encoding="utf-8"
    )
    (root / "evidence/SOURCES.md").write_text(registry, encoding="utf-8")
    (root / "governance/status-model.md").write_text(
        status_model, encoding="utf-8"
    )


def validation_codes(root: Path, contract=None) -> set[str]:
    contract = contract or make_contract()
    return {
        issue.code
        for issue in RepositoryValidator(root, contract).validate()
    }


class ExactSemanticValidationTests(unittest.TestCase):
    def test_canonical_status_values_preserve_internal_markers(self) -> None:
        replacements = (
            ("- `Registered`", "- `Regis*tered`"),
            ("- `Needs re-review`", "- `Needs_ re-review`"),
        )
        for old, new in replacements:
            with self.subTest(value=new):
                with TemporaryDirectory() as directory:
                    root = Path(directory)
                    status_model = STATUS_MODEL.replace(old, new, 1)
                    write_fixture(
                        root,
                        registry_text(
                            evidence="Registered",
                            integration="Not started",
                            verified="—",
                        ),
                        status_model,
                    )
                    self.assertIn(
                        "evidence-status-model-drift",
                        validation_codes(root),
                    )

    def test_registry_source_id_preserves_internal_markers(self) -> None:
        for source_id in ("P-2026-0_1", "P-2026-*01*"):
            with self.subTest(source_id=source_id):
                with TemporaryDirectory() as directory:
                    root = Path(directory)
                    write_fixture(
                        root,
                        registry_text(
                            source_id=source_id,
                            evidence="Registered",
                            integration="Not started",
                            verified="—",
                        ),
                    )
                    self.assertIn("invalid-source-id", validation_codes(root))

    def test_registry_status_preserves_internal_markers(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(
                root,
                registry_text(
                    evidence="Regis*tered",
                    integration="Not started",
                    verified="—",
                ),
            )
            self.assertIn("invalid-evidence-status", validation_codes(root))

    def test_reviewed_brief_requires_raw_exact_source_id(self) -> None:
        for malformed in ("P-2026-0_1", "P-2026-*01*"):
            with self.subTest(malformed=malformed):
                with TemporaryDirectory() as directory:
                    root = Path(directory)
                    write_fixture(root, registry_text())
                    (root / "evidence/primary/example.md").write_text(
                        f"# Example brief\n\nSource ID: {malformed}\n",
                        encoding="utf-8",
                    )
                    self.assertIn(
                        "reviewed-brief-source-id-missing",
                        validation_codes(root),
                    )

    def test_table_rows_with_malformed_primary_prefix_fail_closed(self) -> None:
        malformed_rows = (
            "| **P-abc** | Broken source | Registered |",
            "| **P-2026/01** | Broken source | Registered |",
        )
        for malformed_row in malformed_rows:
            with self.subTest(row=malformed_row):
                with TemporaryDirectory() as directory:
                    root = Path(directory)
                    registry = registry_text(
                        evidence="Registered",
                        integration="Not started",
                        verified="—",
                    ).rstrip() + f"\n\n{malformed_row}\n"
                    write_fixture(root, registry)
                    self.assertIn("source-registry-parse", validation_codes(root))

    def test_table_rows_with_malformed_dataset_prefix_fail_closed(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            registry = (
                dataset_registry_text("DS-2026-01").rstrip()
                + "\n\n| **DS-invalid** | Broken dataset | Registered |\n"
            )
            write_fixture(root, registry)
            self.assertIn(
                "source-registry-parse",
                validation_codes(root, make_dataset_contract()),
            )


if __name__ == "__main__":
    unittest.main()
