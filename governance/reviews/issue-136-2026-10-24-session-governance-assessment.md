# Issue #136 — Within-issue checkpoint governance assessment

Date: 2026-10-24. Approved owner: [#136](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/136), from the maintainer's explicit instruction to add this rule to `AGENTS.md`. Existing master plan: [#84](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/84). Inspected base `main` `d062cd95db8f5b0f69bdb305b9d815cebcb02415` before editing.

## Start-of-work and governance classification

- Primary procedure: maintainer-approved **clarification/extension of an existing issue lifecycle**, under `AGENTS.md#governance-change-procedure`, not a source Flow A–E.
- Trigger classification: **missing step** in the existing per-issue lifecycle. Current `AGENTS.md` defines one issue and the post-completion plan/approval checkpoint; the supporting issue workflow describes resumption and final acceptance but does not explicitly require a durable, prioritized *within-issue* plan and a session-by-session user report.
- Human decision: user expressly requested the repository-level rule, with progress returned to the active issue, plan correction and optional maintainer consultation, a closing status and the next task **within the issue** plus a full prioritized task list. No extra approval for this exact direction is presumed necessary; changing the approved scope would be separate.
- Out of scope: all research/source statuses and briefs, scientific conclusions, alternative hypotheses, publishing, report rewrite #124, new workflows/gates/issue status enums, universal templates and hidden background execution.
- Source IDs: none. Evidence review: No. Integration audit: No. Content synchronization: Yes, because contributor/workflow behavior changes. Separate independent reviewer: required; unavailable at candidate preparation time. New source flow: none.

## Alternatives and decision

1. **Selected:** append a focused checkpoint subsection to the existing AGENTS one-issue lifecycle, with small read-through additions to the issue-workflow and contributing entry points.
2. **Rejected:** no change. The existing post-closure checkpoint does not guarantee useful status after a session ends with the issue unfinished.
3. **Rejected:** a new issue state machine, separate plan registry, workflow or extra gate. This creates duplicate authority/maintenance and was not requested.

The selected approach is reversible through a separately approved, reviewed governance PR. It preserves independent review, source verification and the maintainer's pre-existing approval boundaries.

## Exact behavior to verify

- One selected issue stays current until all acceptance/merge/main verification completes.
- After meaningful subtasks and at deliberate breaks, progress and the full status/priority/dependency list are updated **in that issue**, with real evidence and one next internal step.
- The user sees the issue's actual progress, remaining acceptance, next subtask and complete internal priority list, plus a **separate** status/priority list from master #84.
- Normal in-scope reprioritization is recorded; material scope, AC, dependency or priority-commitment changes require maintainer decision.
- Unexpected interruption cannot be retroactively recorded as a completed checkpoint; resume from live issue/PR/main evidence.
- A partial PR, CI success or report does not equal accepted issue completion. No unobserved independent review is asserted.

## Content synchronization assessment

| Surface | Disposition |
| --- | --- |
| `AGENTS.md` | **Updated**, canonical within-issue session checkpoint under existing issue lifecycle. |
| `governance/issue-workflow.md` | **Updated**, short supporting link/repetition, no independent new obligation. |
| `CONTRIBUTING.md` | **Updated**, contributors can find the same required checkpoint from their normal entry point. |
| `CHANGELOG.md` | **Updated**, material change to contributor obligations. |
| `governance/memory.md` | **Updated**, stale 123-pending snapshot corrected against inspected live main; #136 remains in progress and #124 not started. |
| `governance/work-records/` and this assessment | **Updated**, one new PR record and the rationale/impact trace. |
| `governance/repository-intelligence/agent-context.json` | **Refresh required** after changed inputs; regeneration and verification are separate from independent review. |
| `governance/README.md`, `governance/templates.md`, PR template | **No change**: current issue-workflow links and PR declaration shape remain sufficient; no template or new action introduced. |
| `README.md`, `DOCTRINE.md`, `GLOSSARY.md`, `SCOPE.md`, `ARTIFACT_MODEL.md` | **No change**: public research thesis, terms and artifact roles untouched. |
| `report/`, `protocols/`, evidence registry/briefs/indexes, `REFERENCES.md`, publication | **No change**: neither source interpretation nor content/use, tools, site or evidence status changed. |

Changelog: **Updated** (new contributor session-checkpoint duty). Content synchronization decision: recorded; current completion remains conditional on fresh RI, independent review, checks and merge. The assessment alone does not establish acceptance.

## Implementation and verification checkpoint

Candidate file scope: `AGENTS.md`, `governance/issue-workflow.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `governance/memory.md`, this review record, one machine-readable work record, and the generated RI context. Existing work records are append-only and remain unchanged.

Separate reviewer must assess exact changed text versus the user's request, absence of duplicate plan, no unintended escalation/approval change, accurate source/RI/status boundaries, updated entry points, code/prose diff, work record, and actual PR CI. Outcome currently **Review unavailable**, not Confirmed. Do not merge/close until it is independently accepted and exact-main verification is recorded.
