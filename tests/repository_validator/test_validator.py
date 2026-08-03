from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools.repository_validator.contract import (
    DocumentRequirement,
    RegistryRequirement,
    RepositoryContract,
    StatusModelRequirement,
    load_contract,
)
from tools.repository_validator.markdown import (
    extract_headings,
    inline_code_bullets_under_heading,
    parse_markdown_tables,
)
from tools.repository_validator.registry import parse_source_registry
from tools.repository_validator.validator import RepositoryValidator


REPO_ROOT = Path(__file__).resolve().parents[2]


def make_contract() -> RepositoryContract:
    return RepositoryContract(
        version=1,
        policy_authority="AGENTS.md",
        source_registry="evidence/SOURCES.md",
        required_files=(
            "AGENTS.md",
            "evidence/SOURCES.md",
            "governance/status-model.md",
        ),
        evidence_review_statuses=(
            "Registered",
            "Brief in progress",
            "Reviewed brief",
            "Needs re-review",
        ),
        integration_audit_statuses=(
            "Not started",
            "In progress",
            "Corrections required",
            "Verified",
            "Needs re-verification",
        ),
        status_model=StatusModelRequirement(
            path="governance/status-model.md",
            evidence_heading="Allowed Evidence review statuses",
            integration_heading="Allowed Integration audit statuses",
        ),
        registry=RegistryRequirement(
            table_sections=("Primary empirical research",),
            required_columns=(
                "ID",
                "Source",
                "Evidence review",
                "Integration audit",
                "Last verified",
                "Can support",
                "Current use",
            ),
            required_nonempty_columns=(
                "ID",
                "Source",
                "Evidence review",
                "Integration audit",
                "Last verified",
                "Can support",
                "Current use",
            ),
            source_id_pattern=r"^(?:P|D|S|M)-\d{4}-\d{2}$",
            date_pattern=r"^\d{4}-\d{2}-\d{2}$",
            empty_date="—",
            verified_status="Verified",
            local_brief_link_required_for=("Reviewed brief",),
        ),
        documents=(
            DocumentRequirement(
                path="AGENTS.md",
                required_headings=("Repository Constitution",),
            ),
        ),
    )


STATUS_MODEL = """# Source status model

### Allowed Evidence review statuses

- `Registered`
- `Brief in progress`
- `Reviewed brief`
- `Needs re-review`

### Allowed Integration audit statuses

- `Not started`
- `In progress`
- `Corrections required`
- `Verified`
- `Needs re-verification`
"""


def registry_text(
    *,
    source_id: str = "P-2026-01",
    evidence: str = "[Reviewed brief](primary/example.md)",
    integration: str = "Verified",
    verified: str = "2026-07-27",
) -> str:
    return f"""# Source Registry

## Primary empirical research

| ID | Source | Evidence review | Integration audit | Last verified | Can support | Current use |
| --- | --- | --- | --- | --- | --- | --- |
| **{source_id}** | Example source | {evidence} | {integration} | {verified} | Bounded finding | `README.md` |
"""


class MarkdownTests(unittest.TestCase):
    def test_headings_ignore_fenced_examples(self) -> None:
        text = """# Real

```markdown
## Not real
```

## Actual
"""
        self.assertEqual(extract_headings(text), ("Real", "Actual"))

    def test_table_parser_returns_visible_headers(self) -> None:
        tables = parse_markdown_tables(registry_text())
        self.assertEqual(len(tables), 1)
        self.assertEqual(tables[0].headers[0], "ID")

    def test_status_bullets_are_scoped_to_heading(self) -> None:
        self.assertEqual(
            inline_code_bullets_under_heading(
                STATUS_MODEL, "Allowed Evidence review statuses"
            ),
            ("Registered", "Brief in progress", "Reviewed brief", "Needs re-review"),
        )


class RegistryTests(unittest.TestCase):
    def test_parser_extracts_status_and_brief_link(self) -> None:
        contract = make_contract()
        records = parse_source_registry(
            registry_text(),
            contract.registry.required_columns,
            contract.registry.table_sections,
        )
        self.assertEqual(records[0].source_id, "P-2026-01")
        self.assertEqual(records[0].evidence_review, "Reviewed brief")
        self.assertEqual(records[0].brief_link, "primary/example.md")


class ValidatorTests(unittest.TestCase):
    def _write_fixture(self, root: Path, registry: str) -> None:
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

    def test_valid_fixture_passes(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_fixture(root, registry_text())
            self.assertEqual(RepositoryValidator(root, make_contract()).validate(), ())

    def test_invalid_status_and_date_are_reported(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_fixture(
                root,
                registry_text(
                    evidence="Registered",
                    integration="Not a status",
                    verified="2026-07-27",
                ),
            )
            codes = {
                issue.code
                for issue in RepositoryValidator(root, make_contract()).validate()
            }
            self.assertIn("invalid-integration-status", codes)
            self.assertIn("unverified-date-prohibited", codes)

    def test_duplicate_source_id_is_reported(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            registry = registry_text()
            row = next(
                line for line in registry.splitlines() if line.startswith("| **P-")
            )
            self._write_fixture(root, registry.rstrip() + "\n" + row + "\n")
            codes = {
                issue.code
                for issue in RepositoryValidator(root, make_contract()).validate()
            }
            self.assertIn("duplicate-source-id", codes)

    def test_contract_file_loads(self) -> None:
        contract = load_contract(REPO_ROOT / "governance/repository-contract.toml")
        self.assertEqual(contract.policy_authority, "AGENTS.md")
        self.assertIn("Verified", contract.integration_audit_statuses)
        self.assertIn("Primary empirical research", contract.registry.table_sections)

    @unittest.skipUnless(
        (REPO_ROOT / "AGENTS.md").exists(),
        "full repository checkout is required",
    )
    def test_repository_baseline_passes(self) -> None:
        contract = load_contract(REPO_ROOT / "governance/repository-contract.toml")
        self.assertEqual(RepositoryValidator(REPO_ROOT, contract).validate(), ())


if __name__ == "__main__":
    unittest.main()
