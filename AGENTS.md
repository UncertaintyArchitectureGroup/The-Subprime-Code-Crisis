# AGENTS.md

## Purpose

This file defines how human contributors and AI agents should read, modify, and extend this repository without mixing evidence, interpretation, and operational guidance.

The repository has four distinct layers:

1. **Evidence** — what external sources actually report.
2. **Report** — the Subprime Code Crisis synthesis and argument.
3. **Protocols** — practical controls derived from the risk analysis.
4. **Repository maps** — navigation, claim confidence, and source indexes.

Do not collapse these layers.

## Read order

Before making changes, read in this order:

1. `README.md` — scope, claim-confidence map, evidence map, and repository structure.
2. `evidence/README.md` — source taxonomy and evidence-brief standard.
3. `evidence/SOURCES.md` — canonical source registry and review status.
4. Relevant evidence brief under `evidence/`.
5. Relevant chapter under `report/`.
6. Relevant operational response under `protocols/`.
7. `CONTRIBUTING.md` — contribution and disclosure requirements.

Use `REFERENCES.md` for human-readable bibliography navigation, not as the canonical source-classification database.

## Repository boundaries

### Evidence layer

Evidence entries describe external material. They must separate:

- directly observed findings;
- derived calculations;
- model-calibrated estimates;
- source-author interpretation;
- repository interpretation;
- claims not established by the source;
- limitations and external-validity risks.

Never write a repository conclusion as though it were a finding reported by a source.

### Report layer

The report may combine multiple sources and systems reasoning. Every material factual claim should trace to:

- a reviewed evidence brief; or
- a registered source whose brief is explicitly marked pending.

When a source is not strong enough for a causal claim, use bounded language such as `suggests`, `is consistent with`, `may indicate`, or `supports the risk hypothesis`.

### Protocol layer

Protocols are operating patterns, not empirical proof. A protocol may be motivated by evidence and systems analysis, but it must not present a local threshold, role, gate, or workflow as universally validated unless a source directly establishes that claim.

### Repository maps

`README.md`, `evidence/SOURCES.md`, and `REFERENCES.md` must remain mutually consistent:

- `evidence/SOURCES.md` is the canonical registry;
- evidence subdirectory indexes list reviewed briefs;
- `REFERENCES.md` is a compact bibliography generated from the registry;
- `README.md` summarizes source families and major claims.

## Adding a new source

Use this sequence. Do not skip directly to editing the report.

### Step 1 — Register the source

Add the source to `evidence/SOURCES.md` with:

- stable source ID;
- full title and authors or publishing organization;
- year and publication status;
- canonical URL;
- evidence class;
- current review status;
- report locations where it is used or proposed;
- short note on what it can support.

Use IDs in the form:

- `P-YYYY-NN` — primary empirical research;
- `D-YYYY-NN` — primary documentary source;
- `S-YYYY-NN` — secondary evidence;
- `M-YYYY-NN` — methodology or theory;
- `DS-YYYY-NN` — dataset.

### Step 2 — Classify it

Choose exactly one primary class:

- `evidence/primary/` — original empirical research or original measurement with inspectable methods;
- `evidence/documentary/` — first-party filings, official documentation, standards, and organizational records;
- `evidence/secondary/` — surveys, reviews, practitioner analysis, critiques, and industry synthesis;
- `evidence/methodology/` — theories and analytical frameworks used to interpret evidence;
- `evidence/datasets/` — datasets and data registries.

Classification describes what the source is, not whether its conclusions are favorable to the repository thesis.

### Step 3 — Create an evidence brief

Create a kebab-case Markdown file in the correct evidence directory. Include:

1. Source ID and full citation.
2. Publication status.
3. Research question or documentary purpose.
4. Scope, dataset, and methodology where applicable.
5. Directly observed or documented findings.
6. Derived or model-calibrated findings.
7. Repository-relevant interpretation.
8. What the source does not establish.
9. Limitations, conflicts of interest, and external-validity risks.
10. Links to report sections using the source.

A source may be registered before the brief is complete, but it must be marked `Brief pending` and should not become a load-bearing source for a strong claim.

### Step 4 — Update the evidence index

Add the reviewed brief to the relevant directory `README.md` and change its status in `evidence/SOURCES.md` to `Reviewed brief`.

### Step 5 — Integrate it into the report

Edit only the chapter where the source materially changes the argument.

For each integration:

- state what the source actually measured;
- separate findings from repository inference;
- link to the evidence brief;
- add visible limitations where the finding could be overgeneralized;
- remove or weaken older claims if the new source contradicts them.

Do not add a source merely as citation decoration.

### Step 6 — Reassess repository-level claims

Update `README.md` only when the new source changes:

- the claim-confidence map;
- the evidence map coverage;
- the executive summary;
- a major repository-level conclusion.

Do not update the README for every minor source.

### Step 7 — Reassess protocols

Update protocols only when the evidence changes an operational decision, such as:

- a risk boundary;
- a metric definition;
- a gate;
- an escalation rule;
- a disclosure requirement;
- an organizational control.

New evidence does not automatically require a protocol change.

### Step 8 — Update bibliography and navigation

After the source is registered and integrated:

- update `REFERENCES.md`;
- verify links from the relevant evidence index;
- verify links from report sections;
- verify navigation in any changed files.

## Updating an existing source

When a working paper becomes peer reviewed, a report is revised, or a dataset changes:

1. Update `evidence/SOURCES.md`.
2. Update the evidence brief and clearly note the new version.
3. Recheck every report claim that uses the source.
4. Reassess claim confidence.
5. Update `REFERENCES.md`.
6. Record corrections rather than silently preserving obsolete numbers.

## Evidence-strength rules

- Prefer the primary source over summaries when available.
- Prefer official publisher or author links over reposts.
- Do not infer causality from descriptive or observational evidence without explicit justification.
- Do not present self-reported adoption or sentiment as production impact.
- Do not treat arXiv status as peer review.
- Do not treat company marketing as independent evidence.
- Do not use one team's threshold as a universal standard.
- Preserve null, mixed, and contradictory results.

## Change checklist

Before opening a PR, confirm:

- [ ] The source is registered in `evidence/SOURCES.md`.
- [ ] Its evidence class is correct.
- [ ] Findings and repository interpretation are separated.
- [ ] Publication status is explicit.
- [ ] Strong claims link to reviewed briefs where possible.
- [ ] Report language matches the source design.
- [ ] README claim confidence was reassessed.
- [ ] Protocol implications were considered but not forced.
- [ ] `REFERENCES.md` and indexes are synchronized.
- [ ] Navigation links work.
- [ ] The PR description lists evidence boundaries and what the source does not establish.

## Preferred PR structure

For a substantial new source, use separate PRs when practical:

1. source registration and evidence brief;
2. report integration;
3. repository-map or protocol updates, only if needed.

This keeps evidence review separate from argument and policy changes.