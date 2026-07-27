# AGENTS.md

## Canonical status and precedence

This file is the canonical operating specification for human contributors and AI agents working in this repository.

Before performing any repository work, read this file in full from the target branch. Instructions remembered from an earlier task, conversation, branch, cached context, model memory, entry point, or supporting document are not sufficient. This file has precedence over every supporting governance playbook. The playbooks under [`governance/`](governance/README.md) are mandatory procedural extensions when the selected flow requires them; they do not override this file. Resolve every conflict in favor of `AGENTS.md` and escalate unresolved ambiguity.

After reading this file, read only the playbooks required by the selected flow, plus the repository materials required by the [start-of-work gate](#mandatory-start-of-work-gate).

## Repository Constitution

The following principles govern all repository work. They take precedence over individual flows, local convenience, agent preference, and remembered instructions.

No contributor or agent may weaken, bypass, reinterpret, or replace these principles without an explicit decision from the repository maintainer, a reviewable change to `AGENTS.md`, and independent review.

1. **Original evidence over summaries.** The original source is authoritative for what it reports. Search snippets, secondary summaries, repository text, and prior agent notes are not substitutes.
2. **Every material claim must remain traceable.** A material factual claim must trace to a registered source, its reviewed evidence brief when required, and the repository locations where it is used.
3. **Evidence review is not integration audit.** Understanding a source and verifying every repository use of that source are separate activities with separate states and completion conditions.
4. **Evidence strength governs claim strength.** Repository language, confidence, and scope must follow source design, uncertainty, limitations, and external validity.
5. **Contradictory evidence remains visible.** Positive, negative, null, mixed, contradictory, replication, and limiting evidence must be treated fairly and must not be removed for rhetorical convenience.
6. **Humans approve substantive repository changes.** Agents may identify, analyze, and propose substantive changes, but the repository maintainer must explicitly approve them before implementation.
7. **Workflow changes require prior discussion.** Changes to flows, gates, statuses, governance, contributor obligations, or repository architecture must be discussed with the repository maintainer before `AGENTS.md` is edited.
8. **Repository arguments evolve through evidence, not agent preference.** Agents must not change arguments, conclusions, confidence, or protocol logic merely because an alternative formulation appears more persuasive or convenient.
9. **Important decisions remain inspectable.** Material changes must preserve the triggering evidence or problem, alternatives considered, human decision, implementation, and independent-review outcome.
10. **`AGENTS.md` is the canonical operating specification.** Entry points, supporting documents, and agent memory must not override it.
11. **Verification cannot be inferred.** A citation, evidence brief, corrected paragraph, completed PR, or plausible result does not by itself establish reviewed or verified status.
12. **No silent governance change.** `AGENTS.md` must never be updated silently. Every proposed workflow or constitutional change must first be discussed with the repository maintainer and explicitly approved.

## Repository purpose and boundaries

The repository maintains a credible, inspectable, and operationally useful account of how AI-assisted software development changes software-delivery systems, including review capacity, rework, quality, security, release performance, maintenance, and organizational control.

It is an evidence-governed research synthesis, structured argument, operational protocol library, and inspectable record of sources, interpretations, confidence, and uncertainty. It is not an anti-AI manifesto, vendor ranking, citation collection without source review, proof that one study represents the industry, or a claim that every protocol is empirically validated or universally applicable. Speed, volume, persuasiveness, and citation count are not success criteria.

The repository is healthy only when material factual claims trace to registered sources; source findings remain separate from source-author interpretation and repository inference; important sources have reviewed evidence briefs; every repository use has been integration-audited; arguments match evidence strength and scope; protocols are identified as evidence-backed, systems-derived, or proposed practice; contradictory and limiting evidence remains visible; source status, bibliography, indexes, diagrams, and current-use records remain synchronized; and substantive changes remain subject to human judgment and explicit approval.

Keep these five layers distinct:

```text
External source material
        ↓
Evidence registry and evidence briefs
        ↓
Report synthesis and argument
        ↓
Operational protocols
        ↓
Repository maps and navigation
```

- Original papers, datasets, filings, standards, and institutional reports are authoritative for what they report.
- `evidence/SOURCES.md` is the canonical source identity, status, verification-date, and `Current use` registry. `REFERENCES.md` is only a compact bibliography.
- Evidence briefs document source design, findings, calculations, interpretations, limitations, scope, and repository use.
- Report synthesis may make systems-level inferences only when distinguishable from findings and bounded by the evidence.
- Protocols are adaptable operating patterns, not empirical proof. A source may motivate a control without proving a threshold, role, gate, escalation rule, workflow, or control universally valid.
- Maps and navigation artifacts must not introduce stronger claims than the evidence and report support.

## Mandatory start-of-work gate

Before reading other repository files, editing, reviewing, searching for evidence, or changing source status:

1. Read the current `AGENTS.md` from the target branch in full.
2. State the selected primary flow; files and source IDs in scope; whether evidence review, integration audit, or both are required; whether an independent reviewer is available; and whether substantive-change discussion may be triggered. Use the [start-of-work template](governance/templates.md#start-of-work-declaration).
3. Read the playbooks marked mandatory for the selected flow in the [flow table](#flow-selection-table).
4. Then read `README.md`, `evidence/README.md`, `evidence/SOURCES.md`, the relevant evidence brief when one exists, every relevant file under `report/` and `protocols/`, `REFERENCES.md`, and `CONTRIBUTING.md`.

Do not rely on remembered instructions. `evidence/SOURCES.md` is canonical for source state; `REFERENCES.md` is not a status database.

## Human approval and substantive-change gate

Agents may discover evidence, identify inconsistencies, calculate implications, and propose changes. They must stop before editing any substantive artifact when work may alter:

- report logic, a material argument, causal framing, major conclusion, or claim-confidence classification;
- the Executive Summary, Crisis Map, Evidence Map, or another load-bearing synthesis;
- evidence interpretation, source scope, or repository inference;
- protocol logic, controls, roles, thresholds, gates, or escalation rules;
- source-state definitions, verification requirements, governance, contributor obligations, flows, or repository architecture;
- the visibility of contradictory evidence or limitations.

Before implementation, present the current position, triggering evidence or problem, exact proposal, reasonable alternatives including no change, consequences for evidence briefs/report/protocols/maps/statuses/workflows/contributors, unresolved uncertainty and reversibility, the decision required, and the recommended next action. A proposal is not approval. Only explicit maintainer approval authorizes implementation. Record the decision using the [human decision record](governance/templates.md#human-decision-record).

Safe editorial or mechanical changes that do not alter meaning, interpretation, logic, status, or obligations may proceed without a separate proposal; examples are spelling, formatting, broken links, exact synchronization of already-approved text or metadata, navigation maintenance without new claims, mechanical relocation with references updated, and objectively verifiable transcription corrections requiring no interpretation. Safe changes still require normal verification and must not disguise substantive edits. When classification is uncertain, treat the change as substantive and escalate.

## Evidence and claim-type rules

- Every material factual claim must trace to a registered source. Strong or load-bearing claims should trace to a reviewed evidence brief.
- Read the original source whenever accessible; search snippets, summaries, repository interpretations, and prior notes cannot establish source ground truth.
- Separate directly observed or documented findings, derived calculations, model-calibrated estimates, source-author interpretation, repository interpretation, claims not established by the source, and limitations/conflicts/external-validity risks.
- Never present a repository conclusion as a finding directly reported by a source.
- Use bounded language when a source cannot support a causal, universal, enterprise-wide, industry-wide, or economic conclusion.
- Preserve positive, negative, null, mixed, contradictory, replication, critique, and limiting evidence. Do not search only for confirmation.
- A number in a table, caption, or diagram is a claim. Multi-source diagrams must label source boundaries and must not depict unrelated numbers as one observed causal chain.
- Workflow correctness governs speed: registration, evidence review, integration audit, synchronization, human escalation, and independent review must not be skipped.

## Canonical source state model

Every source has separate `Evidence review` and `Integration audit` states. Allowed statuses, transitions, reset behavior, and `Last verified` rules are defined once in the mandatory [`status-model.md`](governance/status-model.md).

In summary, full processing requires `Evidence review = Reviewed brief` and `Integration audit = Verified`. `Last verified` contains a date only when integration is `Verified`; otherwise it is `—`. `Verified` is prohibited unless every correction is merged, every completion gate passes, and independent review is `Confirmed`. A brief, citation, corrected paragraph, PR, merge, or plausible result cannot establish verification by inference.

## Flow selection table

Select exactly one primary flow before editing. Cross-cutting governance work follows the [governance change procedure](#governance-change-procedure), not an invented source flow.

| Flow | Trigger | Evidence review? | Integration audit? | Independent review? | Human discussion potentially required? | Mandatory playbooks | Completion status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **A — Add source** | Evidence object is not registered | Yes | Yes, repository-wide | Yes | Yes | [status](governance/status-model.md), [evidence review](governance/evidence-review.md), [integration audit](governance/integration-audit.md), [independent review](governance/independent-review.md), [templates](governance/templates.md) | `Reviewed brief` + `Verified`, only after corrections are merged and review is `Confirmed` |
| **B — Legacy source** | Registered/cited source lacks a current reviewed brief or completed audit | If no current reviewed brief | Yes, every use | Yes | Yes | [status](governance/status-model.md), [evidence review](governance/evidence-review.md) when required, [integration audit](governance/integration-audit.md), [independent review](governance/independent-review.md), [templates](governance/templates.md) | `Reviewed brief` + `Verified`, only after corrections are merged and confirmed |
| **C — Changed source** | Source changes, is corrected, retracted, superseded, or becomes peer reviewed | Re-review | Re-verification, complete audit | Yes | Yes | [status](governance/status-model.md), [evidence review](governance/evidence-review.md), [integration audit](governance/integration-audit.md), [independent review](governance/independent-review.md), [templates](governance/templates.md) | Restore `Reviewed brief` + `Verified` only after the new version is fully processed and confirmed |
| **D — Changed repository use** | Source unchanged, but a relying claim, summary, calculation, diagram, map, or protocol changes materially | No, unless brief is inadequate | Re-verification of affected source | Yes | Yes | [status](governance/status-model.md), [integration audit](governance/integration-audit.md), [independent review](governance/independent-review.md), [templates](governance/templates.md) | Restore `Verified` only after changed repository state is checked, merged, and confirmed |
| **E — Discover evidence** | Defined claim, gap, uncertainty, contradiction, replication, landscape, or freshness search | No; accepted items route onward | No; accepted items route onward | Yes, Independent Search Review | Yes, if disagreement/unavailable or later substance | [discovery](governance/evidence-discovery.md), [independent review](governance/independent-review.md), [templates](governance/templates.md) | Complete only when the full discovery checklist passes and Independent Search Review is `Confirmed` |

### Short flow rules

- **Flow A:** Register and classify before review. Initialize the states exactly as required by the status model; then complete evidence review, repository-wide audit, synchronization, and independent review.
- **Flow B:** Confirm/correct identity, class, canonical link, publication status, and proposed `Current use`; never create a duplicate entry. Review the evidence if needed, audit every use, correct all implications, synchronize, and obtain confirmation.
- **Flow C:** Immediately reset both dimensions and `Last verified`, preserve version history, then rerun complete evidence review and integration audit. Do not restore final states early.
- **Flow D:** Keep `Reviewed brief` unless inadequate; reset integration and `Last verified`, audit the affected source against changed repository state, and restore `Verified` only after merge and confirmation.
- **Flow E:** Discovery is not acceptance. It must not directly change report claims, protocols, source statuses, confidence classifications, or maps. Every accepted new object routes to Flow A; every changed, corrected, peer-reviewed, retracted, or superseding registered object routes to Flow C. Notes, abstracts, summaries, and Candidate Register entries cannot substitute for registration, review, a brief, audit, or verification.

## Required playbooks by flow

Playbooks are normative procedural extensions of this file when listed as mandatory in the flow table:

- [`governance/evidence-review.md`](governance/evidence-review.md) — registration, acquisition, source assessment, brief, and evidence-review completion.
- [`governance/integration-audit.md`](governance/integration-audit.md) — repository-wide trace, numeric/argument checks, correction handling, and synchronization.
- [`governance/evidence-discovery.md`](governance/evidence-discovery.md) — complete Flow E search, screening, Candidate Register, routing, and Independent Search Review method.
- [`governance/independent-review.md`](governance/independent-review.md) — reviewer independence, materials, outcomes, correction loop, escalation, and relationship to verification.
- [`governance/status-model.md`](governance/status-model.md) — the only definitions of allowed source states and transition rules.
- [`governance/templates.md`](governance/templates.md) — mandatory record shapes when the applicable procedure requires them.

## Synchronization requirements

After approved corrections, synchronize the evidence brief, actual `Current use` in `evidence/SOURCES.md`, the relevant evidence-directory index, `REFERENCES.md`, README claims/tables/diagrams and other maps, report usage, protocol implications, links, superseded-version history, and removed claims. These artifacts must reflect actual repository state and must not silently drift or strengthen claims.

## Completion and verification gates

Every completed Flow A–E and every substantive repository change requires review by a second agent or reviewer who did not produce the work, using [`independent-review.md`](governance/independent-review.md). Allowed outcomes are `Confirmed`, `Corrections required`, `Unresolved disagreement`, and `Review unavailable`.

- `Corrections required` returns work to the applicable flow and requires repeated independent review after correction.
- `Unresolved disagreement` and `Review unavailable` require human escalation; neither equals `Confirmed`.
- `Integration audit = Verified` is forbidden unless the independent-review outcome is `Confirmed`.
- When unresolved integration problems remain, use `Integration audit = Corrections required` and `Last verified = —`.
- A merged PR alone does not establish review, integration verification, or Flow completion.

A source may be marked `Verified` only after every item in the [integration-audit completion checklist](governance/integration-audit.md#completion-checklist) and [independent-review gate](governance/independent-review.md#relationship-to-verification) passes, all corrections are merged, the brief and registry match, and no unresolved correction or human decision remains. Final verification status must reflect the completed, independently confirmed default-branch state.

## PR and implementation rules

- Implement approved substantive work in a reviewable PR and preserve its trigger, alternatives, human decision, implementation, and independent-review outcome.
- For substantial source work, prefer separate PRs for registration/brief, integration/corrections, separately approved README or protocol changes, independent-review corrections, and final default-branch verification status.
- Do not set `Integration audit = Verified` until the default branch reflects the completed and independently confirmed state.
- Use the [PR completion summary](governance/templates.md#pr-completion-summary). A PR must disclose unresolved decisions and independent review status; it must not be described as complete or ready for merge when review is not `Confirmed`.
- Follow `CONTRIBUTING.md` for contributor mechanics. It cannot override this file.

## Escalation and conflict handling

Escalate before finalizing if reviewers disagree; a source is ambiguous, inaccessible, superseded, or inconsistent; claims cannot be confidently traced; evidence suggests a substantive change; a correction would materially weaken, reverse, or remove a major conclusion; a new flow or material instruction appears necessary; independent review has unresolved doubt or is unavailable; or a request/supporting playbook conflicts with this file.

Present the decision, competing interpretations, supporting evidence, and practical consequences. Do not guess, average conclusions, silently select an interpretation, or implement a substantive change before explicit approval. Preserve the stricter current interpretation when ambiguity cannot be resolved without a maintainer decision.

## Governance change procedure

User corrections, execution failures, recurring inconsistencies, missing checks, new artifacts, and repeated clarifications are signals—not permission to edit governance automatically. Classify each signal as exactly one of: execution error; missing step; new recurring pattern; workflow ambiguity; recurring repository inconsistency; new repository artifact or boundary; or one-off preference/scope decision.

Before proposing governance change:

1. Identify the existing flow or gate, compare the failure with its trigger/procedure/completion conditions, and determine whether non-compliance caused the problem.
2. Correct execution errors through the existing flow. Do not add rules merely because one execution was poor.
3. Extend a flow only when its trigger and completion condition remain the same but a necessary step/check is missing; add a flow only for a distinct recurring trigger, procedure, state transition, and completion condition; clarify/restructure only for genuine ambiguity or inconsistency; do not change workflow for one-off preferences.
   When a signal does not justify a workflow change but remains unresolved, record the local scope decision explicitly. Do not silently generalize it into a repository-wide rule.
4. Search for equivalent instructions to avoid duplication or contradiction. Cross-cutting constitutional, approval, escalation, and independent-review controls remain outside source-specific flows.
5. Present a proposal under the [human approval gate](#human-approval-and-substantive-change-gate), including the signal classification, existing boundary, adequacy analysis, whether the proposal extends/adds/removes/clarifies, migration/synchronization work, and alternatives.
6. Obtain explicit maintainer approval before editing `AGENTS.md`. Approval must clearly distinguish the accepted direction from rejected alternatives.
7. After approval, update `AGENTS.md` in a reviewable PR, update supporting entry points only after the canonical rule exists, avoid unrelated cleanup, and independently review implementation against the approved proposal and Constitution.
8. Do not treat the new workflow as canonical until merged. If implementation exposes a materially different decision, stop and return to the maintainer.

No supporting playbook may independently change governance behavior. Any playbook change that would alter an obligation, gate, status, transition, completion condition, or contributor duty requires prior discussion, explicit maintainer approval, corresponding canonical `AGENTS.md` treatment where necessary, a reviewable PR, and independent review.
