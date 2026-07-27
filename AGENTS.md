# AGENTS.md

## Purpose

This file defines how human contributors and AI agents should read, modify, and extend this repository without mixing evidence, interpretation, and operational guidance.

The repository has four distinct layers:

1. **Evidence** — what external sources actually report.
2. **Report** — the Subprime Code Crisis synthesis and argument.
3. **Protocols** — practical controls derived from the risk analysis.
4. **Repository maps** — navigation, claim confidence, source status, and bibliography.

Do not collapse these layers.

## Read order

Before making changes, read in this order:

1. `README.md` — scope, major claims, evidence map, and repository structure.
2. `evidence/README.md` — source taxonomy and evidence-brief standard.
3. `evidence/SOURCES.md` — canonical source registry, evidence-review status, integration-audit status, and current use.
4. The relevant evidence brief under `evidence/`, when one exists.
5. Every relevant chapter under `report/`.
6. Every relevant operational response under `protocols/`.
7. `REFERENCES.md` — compact bibliography.
8. `CONTRIBUTING.md` — contribution and disclosure requirements.

`REFERENCES.md` is not the canonical status database. `evidence/SOURCES.md` is.

## Repository boundaries

### Evidence layer

Evidence entries describe external material. They must separate:

- directly observed or documented findings;
- derived calculations;
- model-calibrated estimates;
- source-author interpretation;
- repository interpretation;
- claims not established by the source;
- limitations, conflicts, and external-validity risks.

Never write a repository conclusion as though it were a finding reported by a source.

### Report layer

The report may combine multiple sources and systems reasoning. Every material factual claim must trace to:

- a reviewed evidence brief; or
- a registered source whose brief is explicitly marked pending.

Use bounded language when the design cannot support a strong causal or general claim.

### Protocol layer

Protocols are operating patterns, not empirical proof. A source may motivate a protocol, but no local threshold, gate, role, workflow, or control is universally validated unless evidence directly supports that claim.

### Repository maps

The following must remain synchronized:

- `evidence/SOURCES.md` — canonical source and status registry;
- evidence directory indexes — reviewed briefs available in each class;
- `REFERENCES.md` — compact bibliography;
- `README.md` — repository-level claims, maps, diagrams, and source coverage.

## Source state model

Every source has two independent states in `evidence/SOURCES.md`.

### Evidence review

Allowed values:

- `Registered`
- `Brief in progress`
- `Reviewed brief`
- `Needs re-review`

### Integration audit

Allowed values:

- `Not started`
- `In progress`
- `Corrections required`
- `Verified`
- `Needs re-verification`

A source is fully processed only when:

```text
Evidence review = Reviewed brief
Integration audit = Verified
```

The existence of a brief does not imply that report integration has been verified.

`Last verified` must contain a date only when `Integration audit = Verified`. Otherwise use `—`.

## Mandatory source-processing flow

Use this flow for every new source and every legacy source already used by the repository.

Do not skip steps, and do not mark the source complete after creating the brief.

### Step 1 — Register the source

Add the source to `evidence/SOURCES.md` before adding or revising report claims.

Record:

- stable source ID;
- canonical title and authors or publisher;
- year and publication status;
- canonical URL;
- evidence class;
- `Evidence review = Registered`;
- `Integration audit = Not started`;
- `Last verified = —`;
- what the source can support;
- known or proposed repository use.

Use IDs in the form:

- `P-YYYY-NN` — primary empirical research;
- `D-YYYY-NN` — primary documentary source;
- `S-YYYY-NN` — secondary evidence;
- `M-YYYY-NN` — methodology or theory;
- `DS-YYYY-NN` — dataset.

### Step 2 — Classify the source

Choose exactly one primary class:

- `evidence/primary/`
- `evidence/documentary/`
- `evidence/secondary/`
- `evidence/methodology/`
- `evidence/datasets/`

Classification describes what the source is, not whether it supports the repository thesis.

### Step 3 — Start the evidence review

When review begins, set:

```text
Evidence review = Brief in progress
Integration audit = Not started
Last verified = —
```

Read the original source, not only a summary or the repository's existing interpretation.

### Step 4 — Create the evidence brief

Create a kebab-case Markdown file in the correct evidence directory.

Include:

1. Source ID and full citation.
2. Publication status and version.
3. Research question or documentary purpose.
4. Scope, dataset, population, time period, comparator, and methodology.
5. Directly observed or documented findings.
6. Derived or model-calibrated findings.
7. Source-author interpretation.
8. Repository-relevant interpretation.
9. What the source does not establish.
10. Limitations, conflicts, and external-validity risks.
11. Known repository locations using the source.
12. A `Repository integration audit` section.

Use this section template:

```markdown
## Repository integration audit

- Integration status: Not started | In progress | Corrections required | Verified | Needs re-verification
- Repository search completed:
- Report mentions checked:
- Numeric claims checked:
- README claims and diagrams checked:
- Protocol outcome: No change | Clarification | Operational change
- Corrections made:
- Current-use locations confirmed:
- Verification date:
```

When the brief is complete and indexed, set:

```text
Evidence review = Reviewed brief
Integration audit = Not started
Last verified = —
```

This is not completion of the source-processing flow.

### Step 5 — Start the integration audit

Before changing report text, set:

```text
Integration audit = In progress
Last verified = —
```

Then execute the complete procedure below.

## Verifying the integration of each source

### 1. Establish source ground truth

Record from the original source:

- canonical title, authors, date, version, and publication status;
- official publisher or author URL;
- design, dataset, population, period, and comparator;
- exact metric definitions;
- exact numbers and uncertainty;
- whether each result is observed, derived, model-calibrated, self-reported, or interpreted;
- stated limitations and conflicts.

### 2. Locate every repository use

Search the entire repository for:

- source ID;
- author names;
- title fragments;
- distinctive metric names;
- every attributed number;
- paraphrases that may not contain a citation.

Inspect at minimum:

- all files under `report/`;
- `README.md`, including tables, captions, diagrams, and claim-confidence entries;
- all files under `protocols/`;
- `REFERENCES.md`;
- `evidence/SOURCES.md`;
- evidence directory indexes.

Do not rely only on the existing `Current use` field. Confirm actual usage and correct the field.

### 3. Build a claim-to-source trace

For every material repository statement supported by the source, record:

| Repository claim | Location | Exact source result | Relationship | Action |
| --- | --- | --- | --- | --- |
| Claim or paraphrase | File and section | Finding or record | Direct, derived, synthesis, scenario, or unsupported | Keep, qualify, correct, relocate, or remove |

The trace may live in the brief, PR description, or review notes, but it must be inspectable.

### 4. Verify numbers and units

For every number:

- confirm numerator, denominator, unit, population, and time window;
- distinguish percentages from percentage points;
- distinguish cumulative, average, median, short-run, and long-run effects;
- preserve uncertainty where material;
- reproduce simple derived calculations where practical;
- do not combine different samples, studies, tools, or periods into one apparent sequence without explicit labeling;
- remove obsolete or untraceable numbers.

A number in a table, caption, or diagram is a claim and must be checked exactly like prose.

### 5. Verify argument fit

Check whether the repository uses the source for a conclusion its design can support.

Ask:

- Is observational evidence presented as causal?
- Is a bounded task result generalized to teams, enterprises, industries, or the economy?
- Are different developer populations treated as interchangeable?
- Is activity described as productivity, quality, shipped value, or business impact without justification?
- Is source-author interpretation presented as an observed result?
- Is repository synthesis clearly identified?
- Are positive, null, mixed, and contradictory results treated fairly?

Correct the argument even when the correction weakens the repository thesis.

### 6. Verify report integration

For every report use:

- explain what the source actually measured;
- link to the evidence brief;
- separate source findings from repository inference;
- expose material limitations near the claim;
- remove inconsistent duplicate retellings;
- update neighboring paragraphs and chapter conclusions when needed.

A corrected citation is not enough if the surrounding argument remains misleading.

### 7. Verify repository-level integration

Reassess `README.md` when the source contributes to:

- the executive summary;
- claim-confidence map;
- Evidence Map;
- Crisis Map or another diagram;
- repository-level numeric claims;
- source coverage descriptions.

Multi-source diagrams must label source boundaries. Do not visually connect unrelated numbers as one observed causal chain.

### 8. Verify protocol implications

Inspect all protocols for explicit or implicit reliance on the source.

Choose and document exactly one outcome:

- **No protocol change**
- **Protocol clarification**
- **Protocol change**

Do not modify a protocol merely for symmetry with a report change.

### 9. Synchronize records

After corrections:

- update the evidence brief;
- update `Current use` in `evidence/SOURCES.md`;
- update the relevant evidence index;
- update `REFERENCES.md`;
- verify internal and external links;
- record superseded versions and removed claims.

### 10. Set the final status

When unresolved problems remain, set:

```text
Integration audit = Corrections required
Last verified = —
```

Only after every required correction is merged and every completion check passes, set:

```text
Evidence review = Reviewed brief
Integration audit = Verified
Last verified = YYYY-MM-DD
```

Also update the brief's `Repository integration audit` section with the same status, outcome, locations, corrections, and date.

The status in the brief and `evidence/SOURCES.md` must match.

## Completion checklist

A source may be marked `Verified` only when:

- [ ] The original source and correct version were read.
- [ ] A reviewed evidence brief exists and is indexed.
- [ ] Every repository mention and attributed number was located.
- [ ] A claim-to-source trace exists for all material uses.
- [ ] Numbers, units, populations, and periods were checked.
- [ ] Claim strength matches the source design.
- [ ] Report arguments and nearby conclusions remain valid after corrections.
- [ ] README tables and diagrams were reassessed.
- [ ] Protocol implications have an explicit documented outcome.
- [ ] `Current use` lists actual repository locations.
- [ ] `REFERENCES.md`, indexes, and links are synchronized.
- [ ] The brief records the integration status and verification date.
- [ ] `evidence/SOURCES.md` records `Integration audit = Verified` and the same date.
- [ ] No unresolved correction remains.

Never mark a source `Verified` merely because a brief, citation, or PR exists.

## Updating an existing source

When a working paper becomes peer reviewed, a report is revised, a dataset changes, or a relevant repository claim changes:

1. Set `Evidence review = Needs re-review` when the source itself changed materially.
2. Set `Integration audit = Needs re-verification` when the source, report use, README diagram, or protocol implication changed materially.
3. Clear `Last verified` to `—`.
4. Update the evidence brief and record the new version.
5. Re-run the entire integration procedure.
6. Apply corrections.
7. Restore `Reviewed brief` and `Verified` only after completion.
8. Record the new verification date.

Do not preserve obsolete numbers silently.

## Evidence-strength rules

- Prefer primary sources over summaries.
- Prefer official publisher or author links over reposts.
- Do not infer causality from descriptive evidence without explicit justification.
- Do not present sentiment or adoption as production impact.
- Do not treat arXiv or working-paper status as peer review.
- Do not treat company marketing as independent evidence.
- Do not use one team's threshold as a universal standard.
- Preserve null, mixed, contradictory, and positive evidence.

## PR checklist

Before opening or completing a source PR, confirm:

- [ ] The source is registered with both status fields.
- [ ] Its evidence class is correct.
- [ ] Publication status and version are explicit.
- [ ] Findings and repository interpretation are separated.
- [ ] Evidence-review status matches the actual brief state.
- [ ] Integration-audit status matches the actual audit state.
- [ ] All repository uses and attributed numbers were searched.
- [ ] A claim-to-source trace exists.
- [ ] Numeric values, units, samples, and periods were checked.
- [ ] Report language matches the source design.
- [ ] README claims and diagrams were reassessed.
- [ ] Protocol implications have an explicit outcome.
- [ ] `Current use`, `REFERENCES.md`, and indexes are synchronized.
- [ ] The brief and registry show matching status and date.
- [ ] Navigation links work.
- [ ] The PR description lists boundaries, corrections, and unresolved work.

## Preferred PR structure

For a substantial source, use separate PRs when practical:

1. source registration and evidence brief;
2. report integration and source-wide verification;
3. repository-map or protocol updates, only when required.

Do not set `Integration audit = Verified` until all required PRs are merged and the repository's default branch reflects the completed state.
