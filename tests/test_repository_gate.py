from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
import shutil
import subprocess
import unittest

from tools.repository_gate import (
    GateError,
    classify,
    load_matrix,
    load_work_record,
    validate,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
MATRIX = REPO_ROOT / "governance/synchronization-matrix.toml"


def run_git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if result.returncode:
        raise AssertionError(result.stderr or result.stdout)
    return result.stdout.strip()


def write_record(
    repo: Path,
    name: str = "record.toml",
    *,
    assessed: tuple[str, ...] = ("governance", "contributor-guidance", "history"),
    decision: str = "Updated",
    reason: str = "Required governance history update.",
    independent_review: str = "Review unavailable",
) -> None:
    directory = repo / "governance/work-records"
    directory.mkdir(parents=True, exist_ok=True)
    surfaces = ", ".join(f'"{surface}"' for surface in assessed)
    (directory / name).write_text(
        f'''record_version = 1
title = "Test change"
primary_flow = "Approved governance procedure"
human_decision = "Approved for test"
independent_review = "{independent_review}"

[changelog]
decision = "{decision}"
reason = "{reason}"

[synchronization]
assessed_surfaces = [{surfaces}]

[synchronization.non_applicable]
''',
        encoding="utf-8",
    )


class GitFixture:
    def __init__(self, root: Path):
        self.repo = root / "candidate"
        self.policy = root / "trusted"
        self.repo.mkdir()
        (self.policy / "governance").mkdir(parents=True)
        shutil.copyfile(MATRIX, self.policy / "governance/synchronization-matrix.toml")
        run_git(self.repo, "init")
        run_git(self.repo, "config", "user.name", "Repository Gate Test")
        run_git(self.repo, "config", "user.email", "gate@example.invalid")
        (self.repo / "AGENTS.md").write_text("# AGENTS\n", encoding="utf-8")
        (self.repo / "CHANGELOG.md").write_text("# Changelog\n", encoding="utf-8")
        (self.repo / "governance").mkdir(exist_ok=True)
        shutil.copyfile(MATRIX, self.repo / "governance/synchronization-matrix.toml")
        write_record(self.repo, "historical.toml")
        run_git(self.repo, "add", ".")
        run_git(self.repo, "commit", "-m", "base")
        self.base = run_git(self.repo, "rev-parse", "HEAD")

    def commit(self, message: str = "candidate") -> str:
        run_git(self.repo, "add", "-A")
        run_git(self.repo, "commit", "-m", message)
        return run_git(self.repo, "rev-parse", "HEAD")

    def validate(self, head: str) -> tuple[str, ...]:
        return validate(self.policy, self.repo, self.repo, self.base, head)


class RepositoryGateTests(unittest.TestCase):
    def test_matrix_loads_and_classifies_report(self) -> None:
        _, _, rules = load_matrix(MATRIX)
        primary, required = classify("report/01_the_illusion.md", rules)
        self.assertEqual(primary, "report")
        self.assertIn("source-registry", required)
        self.assertIn("reader-navigation", required)

    def test_unclassified_path_fails_closed(self) -> None:
        _, _, rules = load_matrix(MATRIX)
        with self.assertRaises(GateError):
            classify("unmapped/new.bin", rules)

    def test_work_record_requires_reason_for_no_changelog(self) -> None:
        _, allowed, _ = load_matrix(MATRIX)
        with TemporaryDirectory() as directory:
            path = Path(directory) / "record.toml"
            path.write_text(
                '''record_version = 1
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
''',
                encoding="utf-8",
            )
            with self.assertRaises(GateError):
                load_work_record(path, allowed)

    def test_independent_review_is_exact_enum(self) -> None:
        _, allowed, _ = load_matrix(MATRIX)
        with TemporaryDirectory() as directory:
            repo = Path(directory)
            write_record(repo, independent_review="Looks good")
            with self.assertRaisesRegex(GateError, "independent_review must be one of"):
                load_work_record(repo / "governance/work-records/record.toml", allowed)

    def test_critical_deletion_is_blocked(self) -> None:
        with TemporaryDirectory() as directory:
            fixture = GitFixture(Path(directory))
            (fixture.repo / "AGENTS.md").unlink()
            write_record(fixture.repo)
            (fixture.repo / "CHANGELOG.md").write_text("# Changelog\n\nGate test.\n", encoding="utf-8")
            errors = fixture.validate(fixture.commit())
            self.assertIn("critical path may not be deleted or renamed: AGENTS.md", errors)

    def test_critical_rename_is_blocked(self) -> None:
        with TemporaryDirectory() as directory:
            fixture = GitFixture(Path(directory))
            run_git(fixture.repo, "mv", "AGENTS.md", "AGENT_RULES.md")
            write_record(fixture.repo)
            (fixture.repo / "CHANGELOG.md").write_text("# Changelog\n\nGate test.\n", encoding="utf-8")
            errors = fixture.validate(fixture.commit())
            self.assertIn("critical path may not be deleted or renamed: AGENTS.md", errors)

    def test_candidate_cannot_weaken_trusted_critical_paths(self) -> None:
        with TemporaryDirectory() as directory:
            fixture = GitFixture(Path(directory))
            candidate_matrix = fixture.repo / "governance/synchronization-matrix.toml"
            candidate_matrix.write_text(
                candidate_matrix.read_text(encoding="utf-8").replace('  "AGENTS.md",\n', ""),
                encoding="utf-8",
            )
            (fixture.repo / "AGENTS.md").unlink()
            write_record(fixture.repo)
            (fixture.repo / "CHANGELOG.md").write_text("# Changelog\n\nGate test.\n", encoding="utf-8")
            errors = fixture.validate(fixture.commit())
            self.assertIn("critical path may not be deleted or renamed: AGENTS.md", errors)

    def test_historical_work_record_modification_is_blocked(self) -> None:
        with TemporaryDirectory() as directory:
            fixture = GitFixture(Path(directory))
            historical = fixture.repo / "governance/work-records/historical.toml"
            historical.write_text(historical.read_text(encoding="utf-8") + "\n# rewritten\n", encoding="utf-8")
            write_record(fixture.repo)
            (fixture.repo / "CHANGELOG.md").write_text("# Changelog\n\nGate test.\n", encoding="utf-8")
            errors = fixture.validate(fixture.commit())
            self.assertIn(
                "historical work record may not be modified or deleted: governance/work-records/historical.toml",
                errors,
            )

    def test_historical_work_record_deletion_is_blocked(self) -> None:
        with TemporaryDirectory() as directory:
            fixture = GitFixture(Path(directory))
            (fixture.repo / "governance/work-records/historical.toml").unlink()
            write_record(fixture.repo)
            (fixture.repo / "CHANGELOG.md").write_text("# Changelog\n\nGate test.\n", encoding="utf-8")
            errors = fixture.validate(fixture.commit())
            self.assertIn(
                "historical work record may not be modified or deleted: governance/work-records/historical.toml",
                errors,
            )

    def test_historical_work_record_rename_is_blocked(self) -> None:
        with TemporaryDirectory() as directory:
            fixture = GitFixture(Path(directory))
            run_git(
                fixture.repo,
                "mv",
                "governance/work-records/historical.toml",
                "governance/work-records/renamed.toml",
            )
            write_record(fixture.repo)
            (fixture.repo / "CHANGELOG.md").write_text("# Changelog\n\nGate test.\n", encoding="utf-8")
            errors = fixture.validate(fixture.commit())
            self.assertIn(
                "historical work record may not be renamed: governance/work-records/historical.toml",
                errors,
            )

    def test_exactly_one_new_work_record_is_required(self) -> None:
        with TemporaryDirectory() as directory:
            fixture = GitFixture(Path(directory))
            (fixture.repo / "CHANGELOG.md").write_text("# Changelog\n\nNo record.\n", encoding="utf-8")
            errors = fixture.validate(fixture.commit())
            self.assertEqual(
                errors,
                ("exactly one new governance/work-records/*.toml file is required",),
            )

    def test_missing_required_synchronization_surface_is_reported(self) -> None:
        with TemporaryDirectory() as directory:
            fixture = GitFixture(Path(directory))
            (fixture.repo / "report").mkdir()
            (fixture.repo / "report/example.md").write_text("# Report\n", encoding="utf-8")
            write_record(fixture.repo, assessed=("history",))
            (fixture.repo / "CHANGELOG.md").write_text("# Changelog\n\nReport added.\n", encoding="utf-8")
            errors = fixture.validate(fixture.commit())
            message = next(error for error in errors if error.startswith("work record omits"))
            self.assertIn("report", message)
            self.assertIn("reader-navigation", message)
            self.assertIn("source-registry", message)

    def test_updated_changelog_decision_requires_changed_file(self) -> None:
        with TemporaryDirectory() as directory:
            fixture = GitFixture(Path(directory))
            write_record(fixture.repo, decision="Updated")
            errors = fixture.validate(fixture.commit())
            self.assertIn(
                "changelog decision is Updated but CHANGELOG.md did not change",
                errors,
            )

    def test_not_required_decision_rejects_changelog_change(self) -> None:
        with TemporaryDirectory() as directory:
            fixture = GitFixture(Path(directory))
            write_record(
                fixture.repo,
                assessed=("history",),
                decision="Not required",
                reason="Mechanical test fixture only.",
            )
            (fixture.repo / "CHANGELOG.md").write_text("# Changelog\n\nChanged.\n", encoding="utf-8")
            errors = fixture.validate(fixture.commit())
            self.assertIn(
                "CHANGELOG.md changed while the work record says Not required",
                errors,
            )

    def test_malformed_matrix_fails_closed(self) -> None:
        with TemporaryDirectory() as directory:
            path = Path(directory) / "matrix.toml"
            path.write_text("matrix_version = 1\ncritical_paths = []\n", encoding="utf-8")
            with self.assertRaises(GateError):
                load_matrix(path)

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
