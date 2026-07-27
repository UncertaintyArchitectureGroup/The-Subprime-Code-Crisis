# Contributing to the Subprime Code Crisis

This repository is an independent research synthesis and operational-guidance project about AI-assisted software-delivery risk.

Contributions are welcome from engineers, researchers, delivery leaders, QA and security practitioners, and organizations willing to publish inspectable results.

Before contributing, read:

1. [`README.md`](README.md) — repository scope and claim boundaries.
2. [`evidence/README.md`](evidence/README.md) — evidence taxonomy and brief standard.
3. [`evidence/SOURCES.md`](evidence/SOURCES.md) — canonical source and status registry.
4. [`AGENTS.md`](AGENTS.md) — flow selector, evidence review, integration audit, and status transitions.

## Contribution principles

### Evidence before rhetoric

Do not submit unsupported claims, promotional language, or criticism based only on intuition.

Good contributions distinguish:

- what was directly observed or documented;
- what was derived or model-calibrated;
- what the source author concluded;
- what this repository infers;
- what remains unknown.

### AI assistance is allowed; unverified output is not

AI tools may support search, outlining, editing, or drafting. The contributor remains responsible for every claim, citation, number, and link.

Do not submit text that has not been checked against the cited source. Remove fabricated citations, unsupported certainty, generic filler, and repetitive model-generated phrasing.

### Preserve mixed and contradictory evidence

A source does not need to support the Subprime Code Crisis thesis. Positive productivity evidence, null results, critiques, replications, contradictions, and unfavorable results are necessary for a credible synthesis.

### Protect confidential information

For internal case studies:

- remove company and client identifiers unless publication is authorized;
- remove proprietary code and data;
- disclose the measurement window and relevant context;
- explain how metrics were calculated;
- avoid presenting one team as representative of an industry.

## Ways to contribute

### Add, process, or update a source

First select the correct flow in [`AGENTS.md`](AGENTS.md):

- **Flow A** — new source;
- **Flow B** — legacy registered source;
- **Flow C** — changed or superseded source;
- **Flow D** — repository content changed while the source did not;
- **Flow E** — systematic search for newer or missing evidence.

Every source contribution must preserve two independent states in `evidence/SOURCES.md`:

- `Evidence review`;
- `Integration audit`.

A source is not complete merely because a brief exists. It is fully processed only when:

```text
Evidence review = Reviewed brief
Integration audit = Verified
```

The required lifecycle is:

1. register or confirm the source entry;
2. classify it;
3. create or update the evidence brief;
4. update the evidence-class index;
5. start the repository-wide integration audit;
6. locate every repository use and attributed number;
7. build a claim-to-source trace;
8. correct report claims and surrounding argument where needed;
9. reassess README claims and diagrams;
10. document one explicit protocol outcome;
11. synchronize `Current use`, indexes, and `REFERENCES.md`;
12. mark `Verified` only after all required corrections are merged.

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

Anecdotes may support hypothesis generation, but must not be presented as empirical proof.

### Improve the report

Report changes should:

- trace material factual claims to registered sources;
- link to reviewed evidence briefs where possible;
- distinguish findings from systems inference and warning scenarios;
- weaken or remove claims when the evidence does not support them;
- trigger `Needs re-verification` for any previously verified source whose integration materially changes;
- update the claim-confidence map when a major conclusion changes.

### Improve the protocols

Protocol changes should explain:

- the operational problem;
- the proposed control or decision rule;
- intended scope;
- required evidence or signals;
- failure modes;
- conditions for escalation, pause, or reversal;
- whether the change is evidence-backed, systems-derived, or proposed practice;
- which source integration audits, if any, require re-verification.

Protocols are adaptable operating patterns, not universal thresholds.

## Pull-request expectations

A source-related PR should state:

- which flow from `AGENTS.md` applies;
- files changed and why;
- source IDs affected;
- evidence-review and integration-audit states before and after;
- claims added, removed, corrected, or reclassified;
- claim-to-source trace location;
- evidence boundaries and what the sources do not establish;
- README and protocol outcomes;
- unresolved source-quality, link, or correction issues.

For substantial evidence, prefer separate PRs for:

1. registration and evidence brief;
2. report integration and corrections;
3. repository-map or protocol changes, only when required;
4. final verification-status update after all required changes exist on the default branch.

## License and conduct

By contributing, you agree that your contribution will be licensed under **CC BY-SA 4.0**, unless a specific repository file states otherwise.

Critique claims, tools, methods, incentives, and operating models—not individuals. Disclose commercial or institutional conflicts when they may affect interpretation.
