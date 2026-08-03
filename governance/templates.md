# Governance record templates

These templates are mandatory record shapes when required by [`AGENTS.md`](../AGENTS.md) or an applicable playbook. `AGENTS.md` is canonical and has precedence; templates do not create or override policy.

## Start-of-work declaration

```markdown
## Start-of-work declaration

- Selected primary flow:
- Files in scope:
- Source IDs in scope:
- Evidence review required: Yes | No
- Integration audit required: Yes | No
- Content synchronization assessment required: Yes | No
- Independent reviewer available: Yes | No
- Substantive-change discussion potentially required: Yes | No
- Mandatory playbooks read:
```

## Claim-to-source trace

| Repository claim | Location | Exact source result | Relationship | Action |
| --- | --- | --- | --- | --- |
| Claim or paraphrase | File and section | Finding or record | Direct, derived, synthesis, scenario, or unsupported | Keep, qualify, correct, relocate, or remove |

Record the trace location in the evidence brief.

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
```

Do not list a surface as synchronized merely because it was opened. Record the actual effect, update, or reason it is not applicable.

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
- Content synchronization assessment:
- Synchronized artifacts:
- Changelog: Updated | Not required — <specific reason>

## Human decision

- Approval record:
- Maintainer decisions still required:

## Independent review

- Reviewer:
- Outcome: Confirmed | Corrections required | Unresolved disagreement | Review unavailable
- Corrections or unresolved items:

## Validation

- Commands and results:
- Completion/ready-for-merge claim permitted: Yes | No
```
