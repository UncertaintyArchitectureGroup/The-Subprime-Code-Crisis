# Contributing to The Subprime Code Crisis

Thank you for contributing evidence, analysis, corrections, or operational practices.

This repository values traceability, claim discipline, and transparent uncertainty over volume or rhetorical strength.

## Before contributing

Read [`AGENTS.md`](AGENTS.md) first.

Then follow the mandatory start-of-work read order defined there. The following links are supporting entry points, not a competing canonical sequence:

- [`DOCTRINE.md`](DOCTRINE.md) — research philosophy, claim boundaries, and artifact principles.
- [`SCOPE.md`](SCOPE.md) — explicit in-scope, out-of-scope, and adjacent-topic boundaries.
- [`ARTIFACT_MODEL.md`](ARTIFACT_MODEL.md) — reader-facing map of repository artifacts and relationships.
- [`GLOSSARY.md`](GLOSSARY.md) — canonical repository vocabulary.
- [`CHANGELOG.md`](CHANGELOG.md) — selected material repository history.
- [`README.md`](README.md) — repository purpose, major claims, maps, and navigation.
- [`evidence/README.md`](evidence/README.md) — evidence taxonomy and evidence-brief standard.
- [`evidence/SOURCES.md`](evidence/SOURCES.md) — canonical source inventory and status registry.
- [`REFERENCES.md`](REFERENCES.md) — compact human-readable bibliography and navigation aid.

`AGENTS.md` governs workflow and contributor obligations. `DOCTRINE.md` governs content principles and artifact boundaries. `SCOPE.md` expands the subject boundary. `ARTIFACT_MODEL.md` expands the reader-facing artifact map. `GLOSSARY.md` governs repository terminology. `CHANGELOG.md` records selected material changes but is not a source-status or evidence record. `evidence/SOURCES.md` is canonical for source identity and status. `REFERENCES.md` is a bibliography and navigation aid, not a source-status database.

## Contribution principles

### Distinguish evidence from interpretation

Good contributions distinguish:

- what a source directly reports;
- what a source author interprets;
- what this repository infers;
- what remains unknown.

### Stay within the repository boundary

Use [`SCOPE.md`](SCOPE.md) to determine whether a proposed contribution belongs in this repository. An adjacent topic should be included only when it has a direct, bounded relationship to an in-scope research question.

In scope does not mean established, and out of scope does not mean false or unimportant. Do not broaden the repository into a general AI, economic, legal, or management framework through an isolated contribution.

### Use canonical terminology

Use the meanings defined in [`GLOSSARY.md`](GLOSSARY.md) for project terms such as **repository interpretation**, **evidence brief**, **integration audit**, **risk scenario**, **warning scenario**, **production attenuation**, and **Technical Bankruptcy**.

When a source uses the same term differently, preserve and attribute the source's meaning rather than silently normalizing it. Do not strengthen a claim by substituting a more certain label.

### Preserve artifact boundaries

Use [`ARTIFACT_MODEL.md`](ARTIFACT_MODEL.md) to determine where a contribution belongs. A source record is not an evidence brief, an evidence brief is not a report chapter, a repository interpretation is not a source finding, and a protocol is not empirical proof.

### Synchronize substantive changes

Every substantive contribution must complete the [content synchronization assessment](governance/content-synchronization.md). Inspect the affected repository surfaces, update only those that are actually impacted, explain why other considered surfaces are not applicable, and record one explicit changelog decision.

Do not edit unrelated artifacts merely to make the diff look comprehensive. Do not omit the assessment merely because the change is documentation-only.

### AI assistance is allowed; unverified output is not

AI tools may be used for search support, outlining, editing, or drafting. The contributor remains responsible for every claim, number, citation, and link.

## Ways to contribute

### Add or improve evidence

Evidence contributions may include:

- peer-reviewed research;
- high-quality preprints;
- first-party filings or technical documentation;
- transparent datasets;
- systematic reviews;
- replication or contradiction;
- well-documented industry measurements;
- corrections to existing evidence briefs.

Follow the applicable source flow in `AGENTS.md`. Do not add a citation directly to the report without registering and processing the source.

### Improve the report

Report contributions may:

- correct a factual or interpretive error;
- qualify an overbroad claim;
- improve causal or systems reasoning;
- expose contradictory evidence;
- clarify uncertainty or external-validity boundaries;
- improve traceability to evidence briefs.

### Improve the protocols

Protocol contributions may:

- add a measurable control;
- clarify decision rights;
- define escalation or pause conditions;
- add failure modes;
- improve implementation feedback;
- identify unsupported thresholds or universal claims.

### Contribute datasets or analysis

Dataset contributions should include:

- provenance and license;
- collection method;
- schema and units;
- missingness and known bias;
- reproducible transformations;
- explicit limits on interpretation.

### Report issues

Issues are welcome for:

- broken links;
- citation mismatches;
- unsupported claims;
- contradictory evidence;
- outdated source versions;
- unclear terminology;
- protocol failure modes;
- governance inconsistencies.

## Evidence workflow expectations

For source-related work:

1. select the applicable flow in `AGENTS.md`;
2. register or reconcile the source in `evidence/SOURCES.md`;
3. use the original source whenever accessible;
4. create or update the evidence brief;
5. distinguish findings, calculations, interpretations, limitations, and repository inference;
6. search every repository use;
7. audit numeric and argument fit;
8. reassess README-level claims and diagrams;
9. document exactly one protocol outcome: `No protocol change`, `Protocol clarification`, or `Protocol change proposed`;
10. synchronize `Current use`, indexes, links, and `REFERENCES.md`;
11. complete the content synchronization assessment and changelog decision;
12. pass independent review;
13. resolve all corrections;
14. mark integration `Verified` only when the independent-review outcome is `Confirmed` and all required corrections exist on the default branch.

Do not add a citation directly to the report without registering the source.

## Report-change expectations

Report changes should:

- remain within the boundary in [`SCOPE.md`](SCOPE.md);
- trace material factual claims to registered sources;
- link to reviewed evidence briefs where possible;
- distinguish empirical findings and evidence-backed inferences from systems inference and warning scenarios;
- use the claim boundaries in [`DOCTRINE.md`](DOCTRINE.md#claim-boundaries);
- preserve artifact relationships in [`ARTIFACT_MODEL.md`](ARTIFACT_MODEL.md);
- use canonical terms from [`GLOSSARY.md`](GLOSSARY.md);
- weaken or remove claims when the evidence does not support them;
- trigger re-verification when a material use of a previously verified source changes;
- update the claim-confidence map when a major conclusion changes;
- complete the content synchronization assessment and changelog decision.

## Protocol-change expectations

Protocol changes should explain:

- the risk or failure mode being addressed;
- the proposed control;
- owner and decision rights;
- measurable signals;
- failure modes;
- conditions for escalation, pause, or reversal;
- whether the change is evidence-backed, systems-derived, or a proposed practice;
- which source integrations, if any, require re-verification;
- which repository surfaces and changelog entry are affected.

Protocols are adaptable operating patterns, not universal thresholds. Follow the protocol principles in [`DOCTRINE.md`](DOCTRINE.md#protocol-principles), the repository boundary in [`SCOPE.md`](SCOPE.md), the artifact relationship rules in [`ARTIFACT_MODEL.md`](ARTIFACT_MODEL.md), and the [content synchronization](governance/content-synchronization.md) playbook.

## Pull-request expectations

Every substantive PR should include the [Content synchronization assessment](governance/templates.md#content-synchronization-assessment), including:

- surfaces assessed;
- artifacts updated;
- artifacts considered but not applicable, with reasons;
- `Changelog: Updated` or `Changelog: Not required — <specific reason>`;
- unresolved drift or maintainer decisions;
- assessment record status.

The PR completion summary must separately state overall governance completion. A completed synchronization record does not establish independent-review completion, verification, or merge readiness.

A source-related PR should also state:

- which flow from `AGENTS.md` applies;
- files changed and why;
- source IDs in scope;
- evidence-review and integration-audit status;
- numeric checks and calculations;
- report, map, and protocol implications;
- independent-review outcome;
- unresolved decisions;
- whether a ready-for-merge claim is permitted.

## Review expectations

Reviewers should verify:

- source identity and version;
- claim-to-source trace;
- numeric accuracy;
- distinction between findings and inference;
- visibility of contradictory evidence;
- repository-wide use and synchronization;
- protocol implications;
- source-state correctness;
- compliance with `AGENTS.md` and mandatory playbooks.

A review that only checks prose quality is insufficient for substantive evidence or governance work.

## Licensing

By contributing, you agree that your contribution may be distributed under the repository's applicable license terms.
