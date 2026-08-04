from __future__ import annotations

from pathlib import Path
import tomllib
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

    def test_evidence_state_contour_is_required_and_critical(self) -> None:
        expected = {
            "tools/evidence_state_check.py",
            "tools/evidence_transition_gate.py",
            "tools/repository_validator/evidence_state.py",
            "tests/test_evidence_state_integrity.py",
        }
        contract = load_contract(REPO_ROOT / "governance/repository-contract.toml")
        matrix = tomllib.loads(
            (REPO_ROOT / "governance/synchronization-matrix.toml").read_text(
                encoding="utf-8"
            )
        )
        self.assertTrue(expected <= set(contract.required_files))
        self.assertTrue(expected <= set(matrix["critical_paths"]))

    def test_github_enforcement_contour_is_required_and_critical(self) -> None:
        expected = {
            ".github/CODEOWNERS",
            "governance/github-enforcement.toml",
            "governance/github-enforcement.md",
        }
        contract = load_contract(REPO_ROOT / "governance/repository-contract.toml")
        matrix = tomllib.loads(
            (REPO_ROOT / "governance/synchronization-matrix.toml").read_text(
                encoding="utf-8"
            )
        )
        self.assertTrue(expected <= set(contract.required_files))
        self.assertTrue(expected <= set(matrix["critical_paths"]))

    def test_github_enforcement_review_gates_are_conditional(self) -> None:
        policy = tomllib.loads(
            (REPO_ROOT / "governance/github-enforcement.toml").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(policy["pull_requests"]["required_approving_review_count"], 0)
        self.assertFalse(policy["pull_requests"]["require_code_owner_review"])
        self.assertFalse(policy["pull_requests"]["require_last_push_approval"])
        self.assertFalse(policy["reviewer_pool"]["team_required"])
        self.assertEqual(policy["reviewer_pool"]["team_slug"], "")

    def test_github_enforcement_playbook_headings_are_part_of_contract(self) -> None:
        contract = load_contract(REPO_ROOT / "governance/repository-contract.toml")
        requirements = {document.path: document for document in contract.documents}
        playbook = requirements["governance/github-enforcement.md"]
        self.assertEqual(
            playbook.required_headings,
            (
                "Status and precedence",
                "Protected branch",
                "Required checks and freshness",
                "Pull request requirements",
                "Merge strategy",
                "CODEOWNERS",
                "Activation boundary",
            ),
        )

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

    def test_agents_makes_evidence_state_obligations_canonical(self) -> None:
        agents = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("TOML front matter", agents)
        self.assertIn("registry and brief state must remain synchronized", agents)
        self.assertIn("machine-readable `Current use` paths", agents)
        self.assertIn("changed verified integration surface", agents)


if __name__ == "__main__":
    unittest.main()
