from __future__ import annotations

from dataclasses import replace
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools.repository_validator.contract import (
    DocumentRequirement,
    RegistryRequirement,
    RegistrySectionRequirement,
    RepositoryContract,
    StatusModelRequirement,
    load_contract,
)
from tools.repository_validator.markdown import (
    extract_headings,
    list_items_under_heading,
    parse_markdown_tables,
)
from tools.repository_validator.registry import (
    RegistryParseError,
    parse_source_registry,
)
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
            sections=(
                RegistrySectionRequirement(
                    heading="Primary empirical research",
                    id_prefix="P-",
                    brief_directory="primary",
                    minimum_rows=1,
                ),
            ),
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
            source_id_pattern=r"^(?:DS|P|D|S|M)-\d{4}-\d{2}$",
            date_pattern=r"^\d{4}-\d{2}-\d{2}$",
            empty_date="—",
            verified_status="Verified",
            verified_requires_evidence_status="Reviewed brief",
            local_brief_link_required_for=("Reviewed brief",),
        ),
        documents=(
            DocumentRequirement(
                path="AGENTS.md",
                required_headings=("Repository Constitution",),
            ),
        ),
    )


def make_dataset_contract() -> RepositoryContract:
    contract = make_contract()
    return replace(
        contract,
        registry=replace(
            contract.registry,
            sections=(
                RegistrySectionRequirement(
                    heading="Datasets",
                    id_prefix="DS-",
                    brief_directory="datasets",
                    minimum_rows=0,
                ),
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


def dataset_registry_text(source_id: str | None = None) -> str:
    row = ""
    if source_id is not None:
        row = (
            f"| **{source_id}** | Example dataset | Registered | Not started | — | "
            "Dataset-level analysis | `evidence/datasets/README.md` |\n"
        )
    return f"""# Source Registry

## Datasets

| ID | Source | Evidence review | Integration audit | Last verified | Can support | Current use |
| --- | --- | --- | --- | --- | --- | --- |
{row}"""


class MarkdownTests(unittest.TestCase):
    def test_headings_ignore_fenced_examples(self) -> None:
        text = """# Real

```markdown
## Not real
```

## Actual
"""
        self.assertEqual(extract_headings(text), ("Real", "Actual"))

    def test_headings_ignore_comments_and_indented_code(self) -> None:
        text = """# Real

<!--
## Commented
-->

    ## Indented code

## Actual
"""
        self.assertEqual(extract_headings(text), ("Real", "Actual"))

    def test_table_parser_returns_visible_headers(self) -> None:
        tables = parse_markdown_tables(registry_text())
        self.assertEqual(len(tables), 1)
        self.assertEqual(tables[0].headers[0], "ID")

    def test_table_parser_ignores_inactive_tables(self) -> None:
        table = """| ID | Source |
| --- | --- |
| P-2026-01 | Example |
"""
        text = (
            f"```markdown\n{table}```\n"
            f"<!--\n{table}-->\n"
            + "\n".join(f"    {line}" for line in table.splitlines())
        )
        self.assertEqual(parse_markdown_tables(text), ())

    def test_status_list_parser_includes_noncanonical_items(self) -> None:
        text = STATUS_MODEL.replace(
            "- `Needs re-review`\n",
            "- `Needs re-review`\n- **Archived**\n",
        )
        items = list_items_under_heading(
            text, "Allowed Evidence review statuses"
        )
        self.assertEqual(items[-1].value, "Archived")
        self.assertFalse(items[-1].canonical_inline_code)

    def test_status_list_parser_ignores_commented_items(self) -> None:
        text = """### Allowed Evidence review statuses

<!--
- `Registered`
- `Brief in progress`
- `Reviewed brief`
- `Needs re-review`
-->
"""
        self.assertEqual(
            list_items_under_heading(text, "Allowed Evidence review statuses"),
            (),
        )


class RegistryTests(unittest.TestCase):
    def test_parser_extracts_status_brief_link_and_section_boundary(self) -> None:
        contract = make_contract()
        records = parse_source_registry(
            registry_text(),
            contract.registry.required_columns,
            contract.registry.sections,
            contract.registry.source_id_pattern,
        )
        self.assertEqual(records[0].source_id, "P-2026-01")
        self.assertEqual(records[0].evidence_review, "Reviewed brief")
        self.assertEqual(records[0].brief_link, "primary/example.md")
        self.assertEqual(records[0].expected_prefix, "P-")
        self.assertEqual(records[0].expected_brief_directory, "primary")

    def test_parser_allows_prose_before_and_after_source_table(self) -> None:
        contract = make_contract()
        text = registry_text().replace(
            "## Primary empirical research\n\n",
            "## Primary empirical research\n\nRegistered empirical sources follow.\n\n",
        ).rstrip() + "\n\nPublication details remain in each evidence brief.\n"
        records = parse_source_registry(
            text,
            contract.registry.required_columns,
            contract.registry.sections,
            contract.registry.source_id_pattern,
        )
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].source_id, "P-2026-01")

    def test_empty_dataset_section_is_valid(self) -> None:
        contract = make_dataset_contract()
        records = parse_source_registry(
            dataset_registry_text(),
            contract.registry.required_columns,
            contract.registry.sections,
            contract.registry.source_id_pattern,
        )
        self.assertEqual(records, ())

    def test_dataset_record_uses_dataset_mapping(self) -> None:
        contract = make_dataset_contract()
        records = parse_source_registry(
            dataset_registry_text("DS-2026-01"),
            contract.registry.required_columns,
            contract.registry.sections,
            contract.registry.source_id_pattern,
        )
        self.assertEqual(records[0].source_id, "DS-2026-01")
        self.assertEqual(records[0].expected_prefix, "DS-")
        self.assertEqual(records[0].expected_brief_directory, "datasets")

    def test_inactive_source_tables_do_not_satisfy_registry_section(self) -> None:
        contract = make_contract()
        table = registry_text().split("## Primary empirical research\n\n", 1)[1]
        for wrapped in (
            f"```markdown\n{table}```\n",
            f"<!--\n{table}-->\n",
            "\n".join(f"    {line}" for line in table.splitlines()),
        ):
            with self.subTest(wrapped=wrapped[:12]):
                text = f"# Source Registry\n\n## Primary empirical research\n\n{wrapped}"
                with self.assertRaises(RegistryParseError):
                    parse_source_registry(
                        text,
                        contract.registry.required_columns,
                        contract.registry.sections,
                        contract.registry.source_id_pattern,
                    )


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

    def test_valid_dataset_fixture_passes(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_fixture(root, dataset_registry_text("DS-2026-01"))
            self.assertEqual(
                RepositoryValidator(root, make_dataset_contract()).validate(),
                (),
            )

    def test_dataset_source_must_use_dataset_prefix(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_fixture(root, dataset_registry_text("P-2026-01"))
            codes = {
                issue.code
                for issue in RepositoryValidator(
                    root, make_dataset_contract()
                ).validate()
            }
            self.assertIn("source-id-section-mismatch", codes)

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
        headings = tuple(section.heading for section in contract.registry.sections)
        self.assertIn("Primary empirical research", headings)
        self.assertIn("Datasets", headings)
        primary = next(
            section
            for section in contract.registry.sections
            if section.id_prefix == "P-"
        )
        datasets = next(
            section
            for section in contract.registry.sections
            if section.id_prefix == "DS-"
        )
        self.assertEqual(primary.brief_directory, "primary")
        self.assertEqual(datasets.brief_directory, "datasets")
        self.assertEqual(datasets.minimum_rows, 0)
        self.assertRegex("DS-2026-01", contract.registry.source_id_pattern)
        self.assertIn("LICENSE.md", contract.required_files)
        self.assertIn("evidence/datasets/README.md", contract.required_files)

    @unittest.skipUnless(
        (REPO_ROOT / "AGENTS.md").exists(),
        "full repository checkout is required",
    )
    def test_repository_baseline_passes(self) -> None:
        contract = load_contract(REPO_ROOT / "governance/repository-contract.toml")
        self.assertEqual(RepositoryValidator(REPO_ROOT, contract).validate(), ())


if __name__ == "__main__":
    unittest.main()
