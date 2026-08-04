from __future__ import annotations

from pathlib import Path
import unittest

from tools.repository_validator.contract import load_contract


REPO_ROOT = Path(__file__).resolve().parents[1]


class PRGovernanceContractTests(unittest.TestCase):
    def test_pr_governance_files_are_protected_by_repository_contract(self) -> None:
        contract = load_contract(REPO_ROOT / "governance/repository-contract.toml")
        expected = {
            ".github/pull_request_template.md",
            ".github/workflows/repository-gate.yml",
            "governance/pr-process-and-synchronization.md",
            "governance/synchronization-matrix.toml",
            "governance/work-records/README.md",
            "tools/repository_gate.py",
            "tests/test_repository_gate.py",
            "tests/test_pr_governance_contract.py",
        }
        self.assertTrue(expected <= set(contract.required_files))

    def test_pr_playbook_headings_are_part_of_executable_contract(self) -> None:
        contract = load_contract(REPO_ROOT / "governance/repository-contract.toml")
        requirements = {document.path: document for document in contract.documents}
        playbook = requirements["governance/pr-process-and-synchronization.md"]
        self.assertEqual(
            playbook.required_headings,
            (
                "Status and precedence",
                "Pull request records",
                "Changed-path classification",
                "Changelog decision",
                "Critical deletion protection",
                "Repository Gate",
            ),
        )

    def test_agents_makes_pr_gate_obligations_canonical(self) -> None:
        agents = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("exactly one new machine-readable", agents)
        self.assertIn("governance/work-records/*.toml", agents)
        self.assertIn("status check named `Repository Gate`", agents)
        self.assertIn(
            "A passing Repository Gate does not establish maintainer approval",
            agents,
        )


if __name__ == "__main__":
    unittest.main()
