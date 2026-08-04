from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools.evidence_state_check import check
from tools.repository_validator.evidence_state import (
    EvidenceStateError,
    parse_front_matter,
    validate_transition,
)
from tools.repository_validator.registry import SourceRecord


REPO_ROOT = Path(__file__).resolve().parents[1]


def record(
    *,
    evidence: str = "Reviewed brief",
    integration: str = "Verified",
    verified: str = "2026-07-27",
) -> SourceRecord:
    return SourceRecord(
        source_id="P-2026-01",
        source="Example",
        evidence_review=evidence,
        integration_audit=integration,
        last_verified=verified,
        can_support="Example",
        current_use="`README.md`",
        brief_link="primary/example.md",
        section="Primary empirical research",
        expected_prefix="P-",
        expected_brief_directory="primary",
        line=1,
    )


class EvidenceStateIntegrityTests(unittest.TestCase):
    def test_repository_evidence_state_passes(self) -> None:
        self.assertEqual(check(REPO_ROOT), ())

    def test_front_matter_is_required(self) -> None:
        with self.assertRaises(EvidenceStateError):
            parse_front_matter("# Brief\n", "evidence/primary/example.md")

    def test_verified_requires_confirmed(self) -> None:
        text = '''+++
source_ids = ["P-2026-01"]
evidence_review = "Reviewed brief"
integration_audit = "Verified"
last_verified = "2026-07-27"
independent_review = "Review unavailable"
current_use = ["README.md"]
+++
# Brief
'''
        state = parse_front_matter(text, "evidence/primary/example.md")
        self.assertEqual(state.integration_audit, "Verified")
        self.assertNotEqual(state.independent_review, "Confirmed")

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


if __name__ == "__main__":
    unittest.main()
