# Contributing to the Subprime Code Crisis

This repository is an independent research synthesis and operational guidance project about AI-assisted software-delivery risk.

Contributions are welcome from engineers, researchers, delivery leaders, QA and security practitioners, and organizations willing to publish inspectable results.

Read [`AGENTS.md`](AGENTS.md) first.

Then follow the mandatory start-of-work read order defined there. The following links are supporting entry points, not a competing canonical sequence:

- [`DOCTRINE.md`](DOCTRINE.md) — research philosophy, claim boundaries, and artifact principles.
- [`SCOPE.md`](SCOPE.md) — explicit in-scope, out-of-scope, and adjacent-topic boundaries.
- [`ARTIFACT_MODEL.md`](ARTIFACT_MODEL.md) — reader-facing map of repository artifacts and relationships.
- [`GLOSSARY.md`](GLOSSARY.md) — canonical repository vocabulary.
- [`README.md`](README.md) — repository purpose, major claims, maps, and navigation.
- [`evidence/README.md`](evidence/README.md) — evidence taxonomy and evidence-brief standard.
- [`evidence/SOURCES.md`](evidence/SOURCES.md) — canonical source inventory and status registry.
- [`REFERENCES.md`](REFERENCES.md) — compact human-readable bibliography and navigation aid.

`AGENTS.md` governs workflow and contributor obligations. `DOCTRINE.md` governs content principles and artifact boundaries. `SCOPE.md` expands the subject boundary. `ARTIFACT_MODEL.md` expands the reader-facing artifact map. `GLOSSARY.md` governs repository terminology. `evidence/SOURCES.md` is canonical for source identity and status. `REFERENCES.md` is a bibliography and navigation aid, not a source-status database.

## Contribution principles

### Evidence before rhetoric

Do not submit unsupported claims, promotional language, or criticism based only on intuition.

Good contributions distinguish:

- what was directly observed or documented;
- what was derived or model-calibrated;
- what the source author concluded;
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

### AI assistance is allowed; unverified output is not

AI tools may be used for search support, outlining, editing, or drafting. The contributor remains responsible for every claim, number, citation, and link.

Do not submit text that has not been checked against the cited source. Remove fabricated citations, generic filler, unsupported certainty, and repetitive model-generated phrasing.

### Preserve mixed and contradictory evidence

A source does not need to support the Subprime Code Crisis thesis to be included. Positive productivity evidence, null results, critiques, contradictions, and replications are necessary for a credible synthesis.

### Protect confidential information

For internal case studies:

- remove company and client identifiers unless publication is authorized;
- remove proprietary code and data;
- disclose the measurement window and relevant context;
- explain how metrics were calculated;
- avoid presenting one team as representative of the industry.

## Ways to contribute

### Add, process, or update a source

Select the correct primary flow in [`AGENTS.md`](AGENTS.md) before editing source-related content:

- **Flow A — New source:** the source is not yet registered.
- **Flow B — Legacy registered source:** the source is already cited or registered but lacks a current reviewed brief or completed integration audit.
- **Flow C — Changed source:** the source itself changed, was superseded, or changed publication status.
- **Flow D — Repository use changed:** the source is unchanged, but a claim, diagram, protocol, summary, or calculation relying on it changed materially.
- **Flow E — Discover newer or missing evidence:** search for stronger, newer, contradictory, positive, null, or replication evidence after real gaps are identified.

Every registered source has two independent states:

- **Evidence review** — whether the source itself has been reviewed and documented in a current evidence brief.
- **Integration audit** — whether every material use of that source across the repository has been checked.

A source is fully processed only when:

```text
Evidence review = Reviewed brief
Integration audit = Verified
```

**Reviewed brief does not mean verified integration.** A brief, citation, merged PR, or corrected paragraph does not by itself establish that every repository use has been checked.

For source-related work:

1. select the applicable flow;
2. register or confirm the source entry in `evidence/SOURCES.md`;
3. create or update the evidence brief when required;
4. update the relevant evidence-class index;
5. run the repository-wide integration audit when required;
6. build an inspectable claim-to-source trace;
7. correct report claims and surrounding argument;
8. reassess README-level claims and diagrams;
9. document exactly one protocol outcome: `No protocol change`, `Protocol clarification`, or `Protocol change proposed`;
10. synchronize `Current use`, indexes, links, and `REFERENCES.md`;
11. pass independent review;
12. resolve all corrections;
13. mark integration `Verified` only when the independent-review outcome is `Confirmed` and all required corrections exist on the default branch.

Do not add a citation directly to the report without registering the source.

### Submit a measured case study

Open an issue or PR with:

- context and system boundary;
- adoption intervention;
- observation period;
- comparator or baseline;
- metric definitions;
- measured results;
- confounders and limitations;
- operational response;
- disclosure and anonymization status.

Anecdotes may be useful for hypothesis generation, but must be labeled as anecdotes rather than empirical proof.

### Improve the report

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
- update the claim-confidence map when a major conclusion changes.

### Improve the protocols

Protocol changes should explain:

- the operational problem;
- the control or decision rule;
- the intended scope;
- required evidence or signals;
- failure modes;
- conditions for escalation, pause, or reversal;
- whether the change is evidence-backed, systems-derived, or a proposed practice;
- which source integrations, if any, require re-verification.

Protocols are adaptable operating patterns, not universal thresholds. Follow the protocol principles in [`DOCTRINE.md`](DOCTRINE.md#protocol-principles), the repository boundary in [`SCOPE.md`](SCOPE.md), and the artifact relationship rules in [`ARTIFACT_MODEL.md`](ARTIFACT_MODEL.md).

## Pull-request expectations

A source-related PR should state:

- which flow from `AGENTS.md` applies;
- files changed and why;
- source IDs affected;
- evidence-review and integration-audit states before and after;
- claims added, removed, corrected, or reclassified;
- claim-to-source trace location;
- evidence boundaries and what the sources do not establish;
- whether README claims, diagrams, or protocols were reassessed;
- unresolved source-quality, link, or correction issues.

For substantial source work, prefer separate PRs for:

1. registration and evidence brief;
2. report integration and corrections;
3. README or protocol changes, only when required and approved;
4. independent-review corrections, when required;
5. final verification-status update after the complete state exists on the default branch.

## License and conduct

By contributing, you agree that your contribution will be licensed under **CC BY-SA 4.0**, unless a specific repository file states otherwise.

Critique claims, tools, methods, incentives, and operating models—not individuals. Disclose commercial or institutional conflicts when they may affect interpretation.
