# Governance record templates

These templates are mandatory record shapes when required by [`AGENTS.md`](../AGENTS.md) or an applicable playbook. `AGENTS.md` is canonical and has precedence; templates do not create or override policy.

## Start-of-work declaration

```markdown
## Start-of-work declaration

- Active issue and live master plan:
- Maintainer approval of this issue's scope/acceptance (reference/date):
- Selected primary flow:
- Files in scope:
- Source IDs in scope:
- Evidence review required: Yes | No
- Integration audit required: Yes | No
- Content synchronization assessment required: Yes | No — <specific reason>
- Independent reviewer available: Yes | No
- Substantive-change discussion potentially required: Yes | No
- Mandatory playbooks read:
```

When content synchronization is declared `No`, state why the work is strictly mechanical and does not alter meaning, status, behavior, navigation structure, or reader understanding. Do not use `No` merely because the final edit is small or metadata-shaped.

## Claim-to-source trace

| Repository claim | Location | Exact source result | Relationship | Action |
| --- | --- | --- | --- | --- |
| Claim or paraphrase | File and section | Finding or record | Direct, derived, synthesis, scenario, or unsupported | Keep, qualify, correct, relocate, or remove |

Record the trace location in the evidence brief.

## SDLC node assessment

Use within the existing hypothesis register or owning issue/review artifact under
[the evaluation method](hypothesis-evaluation.md). Do not create a second register.

```markdown
## Node and hypothesis assessment

- Node and stable hypothesis IDs; input/output boundaries:
- Actual previous workflow, population/risk context and observation horizon:
- Intended functions versus demonstrated/weak/absent/unmeasured baseline delivery:
- AI intervention; removed/added/transferred functions and receiving owners:

| Function/outcome | Baseline evidence | Change or substitute | Measure/proxy, unit, comparator and horizon | Effect, uncertainty and missing evidence |
| --- | --- | --- | --- | --- |
| Product/team/system function | Actual delivery or unknown | Named mechanism/owner | Observable and source/test | Gain/loss/tradeoff/unknown |

- Adverse hypothesis, independent trigger, alternatives and weakening observation:
- Remedy hypothesis, defined intervention, comparator and weakening observation:
- Critical outcomes, justified margins, accepted tradeoffs and decision owner:
- Downstream user benefit, team capability and full lifecycle economics:
- Source IDs/versions; independent evidence families; counterevidence/search:
- Verdict and rationale, remaining gaps, date and next evidence issue:
```

Review includes both quality and competent shared ownership. An unmeasured outcome
is neither preserved nor harmed by default. A study can support a bounded outcome
without measuring the whole inventory. Verdicts do not change source status.

## Post-merge plan checkpoint

```markdown
## Completed issue and current plan

- Issue and accepted scope; exact merged refs and current-main checks:
- Acceptance/review evidence and surviving gaps:
- Live master plan reread (URL and as-of date):
- What the result changes about thesis/process/dependencies/order:
- Plan changes with reason, or reasoned no-change decision:
- Current ordered plan:
- One proposed next issue and concrete scope/acceptance:
- Dependencies and material decisions still open:
- Next-issue approval: Awaiting maintainer | Approved — reference/date
```

Present this checkpoint to the maintainer after completing the current issue.
Do not begin the next issue while approval is awaiting. Existing authorization
continues to cover routine completion steps within the current issue.

## Integration audit record

```markdown
## Repository integration audit

- Source ID and exact version:
- Audit owner:
- Audit scope and search terms:
- Repository locations inspected:
- Claim-to-source trace location:
- Numeric checks and reproduced calculations:
- Argument-fit findings:
- Report implications:
- README/map/diagram implications:
- Protocol outcome: No protocol change | Protocol clarification | Protocol change proposed
- Corrections required and locations:
- Approved corrections completed:
- Synchronization completed:
- Integration status:
- Last verified:
- Completion-checklist result:
```

## Independent review record

```markdown
## Independent review

- Primary agent or reviewer:
- Independent reviewer:
- Flow reviewed:
- Materials independently checked:
- Outcome: Confirmed | Corrections required | Unresolved disagreement | Review unavailable
- Discrepancies found:
- Corrections completed:
- Human decision required:
- Review date:
```

## Candidate Register

Maintain this table for every claim-critical, systematic, or multi-source Flow E task. Candidates must remain traceable when excluded, held, rejected, or deduplicated.

| Field | Required record |
| --- | --- |
| Candidate ID | Temporary search identifier |
| Citation | Title, authors or entity, year |
| Canonical URL | Best current authoritative link |
| Canonical version | Version and publication state |
| Search provenance | Database, site, query, and search date |
| Relevance | Direct, adjacent, contextual, or not relevant |
| Relationship | May support, weaken, contradict, replicate, or contextualize |
| Inclusion result | Included, excluded, or held |
| Decision reason | Specific screening rationale |
| Research entity | Authors, affiliations, and responsible organization |
| Funding | Disclosed, absent, or unknown |
| Conflicts | Disclosed, inferred risk, none declared, or unknown |
| Scope | Population, task, tool, setting, period, and outcome |
| External validity | Main generalization boundaries |
| Replication | Independent, partial, failed, mixed, same-entity, or unavailable |
| Proposed routing | Flow A, Flow C, context only, hold, or reject |

## Human decision record

```markdown
## Human decision

- Current repository position or rule:
- Triggering evidence, inconsistency, failure, or recurring need:
- Classification, if a workflow signal:
- Exact proposed change:
- Alternatives considered, including preserving current state:
- Expected consequences for briefs, report, protocols, maps, statuses, workflows, and contributors:
- Migration or synchronization required:
- Unresolved uncertainty and reversibility:
- Decision required:
- Recommended next action:
- Maintainer decision and date:
- Accepted direction and rejected alternatives:
- Independent-review outcome:
```

## Content synchronization assessment

```markdown
## Content synchronization assessment

- Canonical change or approved decision:
- Surfaces assessed:
- Artifacts updated:
- Artifacts considered but not applicable, with reasons:
- Changelog: Updated | Not required — <specific reason>
- Validation performed:
- Unresolved drift or maintainer decision:
- Assessment record status: Completed | Incomplete — <specific reason>
```

Do not list a surface as synchronized merely because it was opened. Record the actual effect, update, or reason it is not applicable. `Assessment record status: Completed` does not establish independent-review completion, verification, or merge readiness.

## PR completion summary

```markdown
## Scope

- Primary flow or approved governance procedure:
- Files and source IDs:
- Out-of-scope artifacts:

## Changes and moved sections

- Changes implemented:
- Sections moved and destinations:
- Rules that could not be safely deduplicated:

## Status and synchronization

- Evidence review status, if applicable:
- Integration audit status, if applicable:
- Last verified, if applicable:
- Content synchronization record: Completed | Incomplete — <specific reason>
- Synchronized artifacts:
- Changelog: Updated | Not required — <specific reason>
- Overall governance completion: Achieved | Not achieved — <specific reason>

## Human decision

- Approval record:
- Maintainer decisions still required:
- Post-merge master-plan checkpoint: Pending | Completed — issue/plan reference
- Proposed next issue and approval state (not inferred from this PR):

## Independent review

- Reviewer:
- Outcome: Confirmed | Corrections required | Unresolved disagreement | Review unavailable
- Corrections or unresolved items:

## Validation

- Commands and results:
- Completion/ready-for-merge claim permitted: Yes | No
```
