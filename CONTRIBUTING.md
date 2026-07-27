# Contributing to the Subprime Code Crisis

This repository is an independent research synthesis and operational guidance project about AI-assisted software-delivery risk.

Contributions are welcome from engineers, researchers, delivery leaders, QA and security practitioners, and organizations willing to publish inspectable results.

Before contributing, read:

1. [`README.md`](README.md) — repository scope and claim boundaries.
2. [`evidence/README.md`](evidence/README.md) — evidence taxonomy.
3. [`evidence/SOURCES.md`](evidence/SOURCES.md) — canonical source registry.
4. [`AGENTS.md`](AGENTS.md) — end-to-end workflow for sources, report changes, and protocol updates.

## Contribution principles

### Evidence before rhetoric

Do not submit unsupported claims, promotional language, or criticism based only on intuition.

Good contributions distinguish:

- what was directly observed;
- what was derived or modeled;
- what the source author concluded;
- what this repository infers;
- what remains unknown.

### AI assistance is allowed; unverified output is not

AI tools may be used for search support, outlining, editing, or drafting. The contributor remains responsible for every claim, citation, and link.

Do not submit text that has not been checked against the cited source. Remove fabricated citations, generic filler, unsupported certainty, and repetitive model-generated phrasing.

### Preserve mixed and contradictory evidence

A source does not need to support the Subprime Code Crisis thesis to be included. Positive productivity evidence, null results, critiques, and replications are necessary for a credible synthesis.

### Protect confidential information

For internal case studies:

- remove company and client identifiers unless publication is authorized;
- remove proprietary code and data;
- disclose the measurement window and relevant context;
- explain how metrics were calculated;
- avoid presenting one team as representative of the industry.

## Ways to contribute

### Add or update a source

Follow the source lifecycle in [`AGENTS.md`](AGENTS.md):

1. register the source in `evidence/SOURCES.md`;
2. classify it;
3. create an evidence brief;
4. update the evidence-class index;
5. integrate it into the report only where relevant;
6. reassess README-level claims and protocols;
7. update `REFERENCES.md` last.

Do not add a citation directly to the report without registering it.

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

- link to reviewed evidence briefs where possible;
- distinguish evidence-backed findings from systems inference and warning scenarios;
- weaken or remove claims when the evidence does not support them;
- update the claim-confidence map when a major conclusion changes.

### Improve the protocols

Protocol changes should explain:

- the operational problem;
- the control or decision rule;
- the intended scope;
- required evidence or signals;
- failure modes;
- conditions for escalation, pause, or reversal;
- whether the change is evidence-backed, systems-derived, or a proposed practice.

Protocols are adaptable operating patterns, not universal thresholds.

## Pull-request expectations

A PR should state:

- files changed and why;
- source IDs affected;
- claims added, removed, or reclassified;
- evidence boundaries;
- what the cited sources do not establish;
- whether README claims or protocols were reassessed;
- any unresolved source-quality or link issues.

For substantial new evidence, prefer separate PRs for:

1. registration and evidence brief;
2. report integration;
3. repository-map or protocol changes, only when required.

## License and conduct

By contributing, you agree that your contribution will be licensed under **CC BY-SA 4.0**, unless a specific repository file states otherwise.

Critique claims, tools, methods, incentives, and operating models—not individuals. Disclose commercial or institutional conflicts when they may affect interpretation.