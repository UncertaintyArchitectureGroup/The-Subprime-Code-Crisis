from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
import subprocess
import unittest

from tools.repository_gate import GateError, classify, load_matrix, load_work_record


REPO_ROOT = Path(__file__).resolve().parents[1]


class RepositoryGateTests(unittest.TestCase):
    def test_matrix_loads_and_classifies_report(self) -> None:
        _, _, rules = load_matrix(REPO_ROOT / "governance/synchronization-matrix.toml")
        primary, required = classify("report/01_the_illusion.md", rules)
        self.assertEqual(primary, "report")
        self.assertIn("source-registry", required)
        self.assertIn("reader-navigation", required)

    def test_unclassified_path_fails_closed(self) -> None:
        _, _, rules = load_matrix(REPO_ROOT / "governance/synchronization-matrix.toml")
        with self.assertRaises(GateError):
            classify("unmapped/new.bin", rules)

    def test_work_record_requires_reason_for_no_changelog(self) -> None:
        _, allowed, _ = load_matrix(REPO_ROOT / "governance/synchronization-matrix.toml")
        with TemporaryDirectory() as directory:
            path = Path(directory) / "record.toml"
            path.write_text(
                """record_version = 1
title = "Example"
primary_flow = "Mechanical"
human_decision = "Not applicable"
independent_review = "Review unavailable"
[changelog]
decision = "Not required"
reason = ""
[synchronization]
assessed_surfaces = ["history"]
[synchronization.non_applicable]
""",
                encoding="utf-8",
            )
            with self.assertRaises(GateError):
                load_work_record(path, allowed)

    def test_gate_script_compiles(self) -> None:
        result = subprocess.run(
            ["python3", "-m", "py_compile", str(REPO_ROOT / "tools/repository_gate.py")],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
