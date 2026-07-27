# Independent review playbook

This playbook is a mandatory procedural extension of [`AGENTS.md`](../AGENTS.md) for every completed Flow A–E and every substantive repository change. `AGENTS.md` is canonical and has precedence; resolve conflicts in its favor. Read it in full before this playbook.

## Reviewer independence

The reviewer must be a second agent or reviewer who did not produce the work. The reviewer must independently test the work and must not merely summarize or endorse the primary reviewer's notes. The same reviewer may satisfy Flow E's Independent Search Review and repository-wide Independent Review only when that review covers the complete Flow E output and all requirements below.

## Materials to inspect

As applicable, independently inspect:

- the current `AGENTS.md` and mandatory playbooks;
- the original source or complete search results, exact version, and publication status;
- Search Strategy, Inclusion/Exclusion criteria, Candidate Register, routing, and representative rerun queries for Flow E;
- changed files and repository-wide uses;
- evidence brief and evidence-directory index;
- source identity, status transitions, `Last verified`, and `Current use`;
- claim-to-source trace and relationship classifications;
- attributed numbers, units, calculations, uncertainty, and diagrams;
- report argument fit, README/maps, protocol implications, synchronization, and completion checklists;
- human approval and decision record for substantive work.

The reviewer must actively seek omissions, misreadings, contradictory evidence, status errors, misleading synthesis, and incomplete synchronization.

## Allowed outcomes

Record exactly one:

- `Confirmed` — no material discrepancy found;
- `Corrections required` — specific defects or omissions found;
- `Unresolved disagreement` — reviewers disagree or material uncertainty remains;
- `Review unavailable` — no independent reviewer could be used.

No other outcome substitutes for these values.

## Correction loop

For `Corrections required`, identify each defect and affected artifact, return work to the applicable flow, complete corrections, rerun affected checks, and repeat independent review. The primary reviewer cannot self-confirm the correction.

For `Unresolved disagreement`, do not guess, average conclusions, or silently choose an interpretation. Record competing interpretations and evidence and escalate to the maintainer.

For `Review unavailable`, disclose the missing review and escalate. Work must not be described as independently confirmed, complete, verified, or ready for merge. `Review unavailable` does not equal `Confirmed`.

## Required metadata

Use the [independent review record](templates.md#independent-review-record) and record the primary reviewer, independent reviewer, flow, materials independently checked, outcome, discrepancies, corrections, human decision required, and review date.

## Relationship to verification

`Integration audit = Verified` is forbidden unless independent review is `Confirmed`, every correction is merged, and every completion gate passes. A completed or merged PR does not itself establish review or verification. For substantive governance changes, the new workflow is not canonical until merged; absence of confirmation prevents describing the refactor as complete or ready for merge.
