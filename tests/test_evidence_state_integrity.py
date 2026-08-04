from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
import shutil
import unittest

from tools.evidence_state_check import check
from tools.repository_validator.evidence_state import (
    BriefState,
    EvidenceStateError,
    parse_front_matter,
    registry_current_use_paths,
    validate_brief_state,
    validate_registry_current_use,
    validate_transition,
)
from tools.repository_validator.registry import SourceRecord


REPO_ROOT = Path(__file__).resolve().parents[1]


def record(
    *,
    source_id: str = "P-2026-01",
    source: str = "Example",
    evidence: str = "Reviewed brief",
    integration: str = "Verified",
    verified: str = "2026-07-27",
    current_use: str = "`README.md`",
    brief_link: str | None = "primary/example.md",
) -> SourceRecord:
    return SourceRecord(
        source_id=source_id,
        source=source,
        evidence_review=evidence,
        integration_audit=integration,
        last_verified=verified,
        can_support="Example",
        current_use=current_use,
        brief_link=brief_link,
        section="Primary empirical research",
        expected_prefix="P-",
        expected_brief_directory="primary",
        line=1,
    )


def brief(
    *,
    source_ids: tuple[str, ...] = ("P-2026-01",),
    evidence: str = "Reviewed brief",
    integration: str = "Verified",
    verified: str = "2026-07-27",
    independent: str = "Confirmed",
    current_use: tuple[str, ...] = ("README.md",),
) -> BriefState:
    return BriefState(
        path="evidence/primary/example.md",
        source_ids=source_ids,
        evidence_review=evidence,
        integration_audit=integration,
        last_verified=verified,
        independent_review=independent,
        current_use=current_use,
    )


class EvidenceStateIntegrityTests(unittest.TestCase):
    def test_repository_evidence_state_passes(self) -> None:
        self.assertEqual(check(REPO_ROOT), ())

    def test_front_matter_is_required(self) -> None:
        with self.assertRaises(EvidenceStateError):
            parse_front_matter("# Brief\n", "evidence/primary/example.md")

    def test_verified_requires_confirmed(self) -> None:
        state = brief(independent="Review unavailable")
        errors = validate_brief_state(
            REPO_ROOT,
            state,
            {"P-2026-01": record()},
            ("Registered", "Brief in progress", "Reviewed brief", "Needs re-review"),
            (
                "Not started",
                "In progress",
                "Corrections required",
                "Verified",
                "Needs re-verification",
            ),
            "—",
        )
        self.assertIn("Verified requires independent_review = Confirmed", errors)

    def test_invalid_calendar_date_is_rejected(self) -> None:
        errors = validate_brief_state(
            REPO_ROOT,
            brief(verified="2026-02-31"),
            {"P-2026-01": record(verified="2026-02-31")},
            ("Reviewed brief",),
            ("Verified",),
            "—",
        )
        self.assertIn("Verified requires a valid YYYY-MM-DD last_verified date", errors)

    def test_unregistered_front_matter_source_id_is_rejected(self) -> None:
        errors = validate_brief_state(
            REPO_ROOT,
            brief(source_ids=("P-2099-99",)),
            {"P-2026-01": record()},
            ("Reviewed brief",),
            ("Verified",),
            "—",
        )
        self.assertIn(
            "front matter Source ID is not registered: P-2099-99",
            errors,
        )

    def test_registry_and_brief_state_mismatch_is_rejected(self) -> None:
        errors = validate_brief_state(
            REPO_ROOT,
            brief(integration="In progress", verified="—", independent="Review unavailable"),
            {"P-2026-01": record()},
            ("Reviewed brief",),
            ("In progress", "Verified"),
            "—",
        )
        self.assertTrue(any("registry and brief state differ" in error for error in errors))

    def test_missing_current_use_path_is_rejected(self) -> None:
        missing = "does/not/exist.md"
        errors = validate_brief_state(
            REPO_ROOT,
            brief(current_use=(missing,)),
            {"P-2026-01": record(current_use=f"`{missing}`")},
            ("Reviewed brief",),
            ("Verified",),
            "—",
        )
        self.assertIn(f"current_use path {missing!r} does not exist", errors)

    def test_shared_brief_requires_identical_registry_states(self) -> None:
        records = {
            "P-2026-01": record(),
            "P-2026-02": record(
                source_id="P-2026-02",
                integration="In progress",
                verified="—",
            ),
        }
        errors = validate_brief_state(
            REPO_ROOT,
            brief(source_ids=("P-2026-01", "P-2026-02")),
            records,
            ("Reviewed brief",),
            ("In progress", "Verified"),
            "—",
        )
        self.assertTrue(
            any("registry and brief state differ for P-2026-02" in error for error in errors)
        )

    def test_verified_reset_requires_empty_date(self) -> None:
        errors = validate_transition(
            record(),
            record(integration="Needs re-verification", verified="2026-07-27"),
        )
        self.assertIn("reset from Verified requires Last verified = —", errors)

    def test_transition_to_verified_requires_new_date(self) -> None:
        errors = validate_transition(
            record(integration="In progress", verified="—"),
            record(integration="Verified", verified="—"),
        )
        self.assertIn("transition to Verified requires a new verification date", errors)

    def test_needs_rereview_requires_reverification(self) -> None:
        errors = validate_transition(
            record(),
            record(
                evidence="Needs re-review",
                integration="In progress",
                verified="—",
            ),
        )
        self.assertIn(
            "Needs re-review requires integration_audit = Needs re-verification",
            errors,
        )

    def test_changed_source_identity_requires_full_reset(self) -> None:
        errors = validate_transition(
            record(source="Original source"),
            record(source="Replacement source"),
        )
        self.assertIn(
            "changed source identity requires Evidence review = Needs re-review",
            errors,
        )
        self.assertIn(
            "changed source identity requires Integration audit = Needs re-verification",
            errors,
        )
        self.assertIn(
            "changed source identity requires Last verified = —",
            errors,
        )

    def test_added_current_use_path_requires_verified_reset(self) -> None:
        errors = validate_transition(
            record(current_use="`README.md`"),
            record(current_use="`README.md`; `report/01_the_illusion.md`"),
        )
        self.assertIn(
            "changed verified integration surface requires Integration audit = Needs re-verification",
            errors,
        )

    def test_removed_current_use_path_requires_verified_reset(self) -> None:
        errors = validate_transition(
            record(current_use="`README.md`; `report/01_the_illusion.md`"),
            record(current_use="`README.md`"),
        )
        self.assertIn(
            "changed verified integration surface requires Last verified = —",
            errors,
        )

    def test_changed_brief_link_requires_verified_reset(self) -> None:
        errors = validate_transition(
            record(brief_link="primary/old.md"),
            record(brief_link="primary/new.md"),
        )
        self.assertIn(
            "changed verified integration surface requires Integration audit = Needs re-verification",
            errors,
        )

    def test_changed_integration_surface_accepts_full_reset(self) -> None:
        errors = validate_transition(
            record(current_use="`README.md`"),
            record(
                current_use="`README.md`; `report/01_the_illusion.md`",
                integration="Needs re-verification",
                verified="—",
            ),
        )
        self.assertNotIn(
            "changed verified integration surface requires Integration audit = Needs re-verification",
            errors,
        )
        self.assertNotIn(
            "changed verified integration surface requires Last verified = —",
            errors,
        )

    def test_backtick_path_is_accepted(self) -> None:
        self.assertEqual(validate_registry_current_use("Used in `README.md`."), ())
        self.assertEqual(registry_current_use_paths("Used in `README.md`."), ("README.md",))

    def test_path_without_backticks_is_rejected(self) -> None:
        self.assertIn(
            "Current use repository paths must be enclosed in backticks",
            validate_registry_current_use("Used in README.md."),
        )

    def test_descriptive_prose_without_path_is_allowed(self) -> None:
        self.assertEqual(validate_registry_current_use("Used for conceptual framing."), ())
        self.assertEqual(registry_current_use_paths("Used for conceptual framing."), ())

    def test_multiple_backtick_paths_are_extracted(self) -> None:
        value = "Used in `README.md` and `report/01_the_illusion.md`."
        self.assertEqual(validate_registry_current_use(value), ())
        self.assertEqual(
            registry_current_use_paths(value),
            ("README.md", "report/01_the_illusion.md"),
        )

    def test_non_path_inline_code_is_rejected(self) -> None:
        self.assertIn(
            "Current use inline code 'concept' must contain exactly one repository path",
            validate_registry_current_use("Used for `concept`."),
        )

    def test_multiple_values_in_one_inline_code_span_are_rejected(self) -> None:
        self.assertIn(
            "Current use inline code 'README.md report/01_the_illusion.md' must contain exactly one repository path",
            validate_registry_current_use(
                "Used in `README.md report/01_the_illusion.md`."
            ),
        )

    def test_candidate_checker_tampering_does_not_change_trusted_check(self) -> None:
        with TemporaryDirectory() as directory:
            candidate = Path(directory) / "candidate"
            shutil.copytree(REPO_ROOT, candidate)
            checker = candidate / "tools/evidence_state_check.py"
            checker.write_text("def check(*args, **kwargs):\n    return ()\n", encoding="utf-8")
            self.assertEqual(check(REPO_ROOT, candidate), ())


if __name__ == "__main__":
    unittest.main()
