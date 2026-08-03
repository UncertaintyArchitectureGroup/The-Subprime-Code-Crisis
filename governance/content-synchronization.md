# Content synchronization

## Status and precedence

This playbook is a mandatory procedural extension of [`AGENTS.md`](../AGENTS.md) for every substantive repository change.

`AGENTS.md` is canonical and has precedence. This playbook does not create source states, evidence-review outcomes, integration-verification outcomes, or exceptions to human approval and independent review.

## Purpose

Repository content is intentionally distributed across evidence records, report chapters, maps, protocols, foundation documents, contributor guidance, citation and attribution artifacts, and governance.

A change can therefore be locally correct while leaving the repository globally inconsistent. The content-synchronization assessment exists to identify affected surfaces, update only those that are genuinely impacted, and record why other surfaces are not applicable.

The assessment is not a requirement to edit every listed file. Symmetry is not correctness.

## Trigger

Complete this assessment for every substantive repository change, including documentation, content-architecture, evidence-integration, report, map, protocol, attribution, citation, contributor, governance, tooling, automation, or dataset-schema changes.

The assessment is normally not required for a strictly mechanical change that does not alter meaning, behavior, status, navigation structure, or reader understanding, such as:

- spelling or punctuation correction;
- formatting or final-newline repair;
- replacement of an objectively broken link;
- internal refactoring invisible to readers and contributors.

When classification is uncertain, treat the assessment as required. Source-state, `Current use`, evidence-integration, and verification changes are not mechanical exceptions merely because the final edit is metadata-shaped.

## Core rule

For every applicable change:

1. identify the canonical artifact or approved decision being changed;
2. inspect every potentially affected synchronization surface;
3. update only artifacts whose meaning, navigation, status, or obligations are actually affected;
4. record non-applicable surfaces and the reason they were not changed;
5. make an explicit `CHANGELOG.md` decision;
6. validate that no synchronized artifact silently strengthens, weakens, or reclassifies the underlying claim or rule.

## Synchronization surfaces

| Surface | Inspect when the change affects | Typical artifacts |
| --- | --- | --- |
| **Scope and content model** | research boundary, adjacent topics, claim classes, interpretation rules, artifact roles | `SCOPE.md`, `DOCTRINE.md`, `GLOSSARY.md`, `ARTIFACT_MODEL.md` |
| **Reader entry points** | repository purpose, major claims, reading order, maps, navigation, practical starting points | `README.md`, report navigation, protocol navigation, evidence and governance indexes |
| **Evidence state and traceability** | source identity, status, findings, limitations, current use, or bibliography | `evidence/SOURCES.md`, evidence briefs, evidence-class indexes, `REFERENCES.md` |
| **Report argument** | material claims, causal framing, calculations, conclusions, mechanisms, scenarios | `report/`, Executive Summary, Claim confidence map |
| **Maps and diagrams** | node meaning, arrows, classifications, attributed numbers, or system relationships | Evidence Map, Crisis Map, protocol diagrams, report diagrams |
| **Operational protocols** | controls, roles, metrics, gates, thresholds, escalation, decision rights, implementation feedback | `protocols/` and protocol index |
| **Attribution and citation** | repository title, authorship, reuse guidance, terminology provenance, contribution boundary | `TERMINOLOGY_AND_ATTRIBUTION.md`, `CITATION.cff`, README citation guidance |
| **Governance and contribution** | workflow, gate, obligation, status, template, review, escalation, contributor behavior | `AGENTS.md`, `governance/`, `CONTRIBUTING.md` |
| **History** | material reader-facing or governance change | `CHANGELOG.md` |

## Change-specific checks

### Source or evidence change

Inspect:

- Source Registry identity and states;
- evidence brief and evidence-class index;
- every actual report, README, map, protocol, citation, and bibliography use;
- claim-confidence implications;
- changelog need when the integrated repository position materially changes.

This assessment does not replace Flow A–D or an integration audit.

### Report claim or conclusion change

Inspect:

- supporting sources and evidence briefs;
- Executive Summary and adjacent report argument;
- Claim confidence map;
- Evidence Map and Crisis Map;
- protocol implications;
- Scope, Doctrine, and Glossary where a boundary or canonical term changes;
- changelog.

### Protocol change

Inspect:

- protocol index and related protocol layers;
- report risk or mechanism that motivates the control;
- evidence and interpretation boundaries;
- README Risk Mitigation section;
- roles, gates, metrics, escalation, and decision records;
- changelog.

### Scope, doctrine, terminology, or artifact change

Inspect:

- the changed canonical or dedicated reference;
- README and contributor entry points;
- relevant evidence, report, protocol, governance, reference, and attribution indexes;
- usages of changed canonical terminology;
- changelog.

### Governance or contributor-obligation change

Inspect:

- canonical treatment in `AGENTS.md` first;
- applicable playbooks and templates;
- governance index;
- `CONTRIBUTING.md` and reader-facing statements about repository procedure;
- changelog.

A supporting playbook or contributor guide cannot independently create an obligation that is absent from `AGENTS.md`.

### Attribution or citation change

Inspect:

- documentary evidence and Source Registry where factual provenance changes;
- `TERMINOLOGY_AND_ATTRIBUTION.md`;
- README attribution and citation guidance;
- `CITATION.cff` when repository identity metadata changes;
- changelog.

## Changelog decision

Update [`CHANGELOG.md`](../CHANGELOG.md) in the same PR when a change proposed for merge would materially affect:

- repository scope, doctrine, artifact relationships, or canonical terminology;
- major report claims, conclusions, confidence, Evidence Map, or Crisis Map;
- protocol controls, roles, gates, decision rules, or the protocol stack;
- evidence integration that changes the reader-facing repository position;
- governance, workflows, gates, status definitions or the source-state model, contributor obligations, or templates;
- terminology provenance, attribution boundaries, citation identity, or licensing presentation;
- repository structure or navigation in a way that materially changes how readers or contributors use the project.

A changelog entry is normally not required for:

- spelling, punctuation, formatting, or final-newline fixes;
- objectively broken-link repair;
- navigation-only maintenance with no material routing change;
- exact source-state synchronization that does not change status definitions, `Current use`, claim meaning, or the reader-facing position;
- internal refactoring with no material reader or contributor effect.

Every substantive PR must record one of:

- `Changelog: Updated`
- `Changelog: Not required — <specific reason>`

Do not use `Not required` merely because the change is documentation-only.

## Required record

Use the [Content synchronization assessment](templates.md#content-synchronization-assessment) template.

The record must identify:

- the canonical change;
- surfaces assessed;
- artifacts updated;
- artifacts considered but not applicable, with reasons;
- changelog decision;
- validation performed;
- unresolved drift or maintainer decision;
- whether the assessment record itself is complete.

## Assessment-record completion

The assessment record is complete only when:

- all reasonably affected surfaces have been inspected;
- affected artifacts are synchronized;
- non-applicable surfaces are explicitly justified;
- the changelog decision is recorded and implemented when required;
- links and terminology are consistent;
- no synchronized text introduces a stronger claim, new status, or new obligation than the canonical change.

Completing the assessment record does not establish completion, verification, or merge readiness of the substantive repository change. The change remains subject to human decisions, independent review, source-flow completion, and every other applicable gate in [`AGENTS.md`](../AGENTS.md).

A clean local diff, a completed assessment record, or a merged PR does not by itself demonstrate repository-wide completion or verification.
