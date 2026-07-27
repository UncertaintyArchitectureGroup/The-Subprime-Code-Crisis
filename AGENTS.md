# AGENTS.md

## Purpose

This file defines how human contributors and AI agents should read, modify, and extend this repository without mixing evidence, interpretation, operational guidance, and navigation metadata.

The repository has four distinct layers:

1. **Evidence** — what external sources actually report.
2. **Report** — the Subprime Code Crisis synthesis and argument.
3. **Protocols** — practical controls derived from the risk analysis.
4. **Repository maps** — navigation, claim confidence, source status, diagrams, and bibliography.

Do not collapse these layers.

## Read order

Before making changes, read:

1. `README.md` — scope, major claims, maps, and repository structure.
2. `evidence/README.md` — evidence taxonomy and brief standard.
3. `evidence/SOURCES.md` — canonical source registry and status database.
4. The relevant evidence brief, when one exists.
5. Every relevant file under `report/`.
6. Every relevant file under `protocols/`.
7. `REFERENCES.md` — compact bibliography.
8. `CONTRIBUTING.md` — contribution expectations.

`evidence/SOURCES.md` is the canonical source inventory and status database. `REFERENCES.md` is only a human-readable bibliography.

## Repository boundaries

### Evidence layer

Evidence briefs must separate:

- directly observed or documented findings;
- derived calculations;
- model-calibrated estimates;
- source-author interpretation;
- repository interpretation;
- claims not established by the source;
- limitations, conflicts, and external-validity risks.

Never write a repository conclusion as though it were reported directly by a source.

### Report layer

The report may combine multiple sources and systems reasoning. Every material factual claim must trace to a registered source. Strong or load-bearing claims should trace to a reviewed evidence brief.

Use bounded language when the source design cannot support a causal, universal, or enterprise-wide conclusion.

### Protocol layer

Protocols are operating patterns, not empirical proof. A source may motivate a protocol, but no local threshold, role, gate, workflow, escalation rule, or control is universally validated unless evidence directly establishes that claim.

### Repository maps

The following must remain synchronized:

- `evidence/SOURCES.md` — canonical source and status registry;
- evidence-directory indexes — briefs available in each evidence class;
- `REFERENCES.md` — compact bibliography;
- `README.md` — repository-level claims, diagrams, source coverage, and navigation.

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

The existence of a brief does not imply that repository integration has been verified.

`Last verified` contains a date only when `Integration audit = Verified`. Use `—` for every other state.

## Choose the correct flow first

Before editing anything, select exactly one primary flow.

### Flow A — Add a new source

Use when the source is not yet listed in `evidence/SOURCES.md`.

Sequence:

1. Register and classify the source.
2. Set `Evidence review = Registered`, `Integration audit = Not started`, and `Last verified = —`.
3. Complete the evidence-review procedure.
4. Complete the integration-audit procedure.
5. Synchronize all maps and records.
6. Mark `Verified` only after all required corrections are merged.

### Flow B — Process a legacy registered source

Use when the source is already cited or registered but has no reviewed brief or no completed integration audit.

Sequence:

1. Confirm or correct its source ID, class, canonical link, publication status, and `Current use` hypothesis.
2. Do not create a duplicate registry entry.
3. Complete the evidence-review procedure if no current reviewed brief exists.
4. Complete the integration-audit procedure across all existing repository uses.
5. Correct report claims, diagrams, references, and protocol implications.
6. Mark `Verified` only after all corrections are merged.

### Flow C — Update a changed source

Use when a working paper, report, filing, dataset, or methodology source has changed, been superseded, or become peer reviewed.

Sequence:

1. Set `Evidence review = Needs re-review`.
2. Set `Integration audit = Needs re-verification`.
3. Clear `Last verified` to `—`.
4. Record the new version in the evidence brief.
5. Re-run the evidence-review procedure.
6. Re-run the complete integration audit.
7. Restore `Reviewed brief` and `Verified` only after completion.

### Flow D — Change repository content that relies on a verified source

Use when the source itself has not changed, but a report claim, README diagram, summary, protocol, or calculation relying on it changes materially.

Sequence:

1. Keep `Evidence review = Reviewed brief` unless the brief itself is now inadequate.
2. Set `Integration audit = Needs re-verification`.
3. Clear `Last verified` to `—`.
4. Re-run the integration audit for the affected source.
5. Restore `Verified` only after the changed repository state has been checked and merged.

### Flow E — Discover newer or missing evidence

Use only after the currently registered source backlog has been processed far enough to understand the evidence gaps.

Sequence:

1. Identify unresolved claims, weak source classes, stale evidence, missing positive evidence, contradictions, and replication gaps.
2. Search for newer, stronger, original, peer-reviewed, contradictory, null, and positive evidence.
3. Do not add search results directly to the report.
4. Route every selected source through Flow A.
5. Record rejected candidate sources and the reason when the search was systematic or claim-critical.

Freshness search is not a substitute for validating the sources already used by the repository.

## Registering and classifying a source

Before adding or revising report claims, register the source in `evidence/SOURCES.md` with:

- stable source ID;
- canonical title and authors or publisher;
- year and publication status;
- canonical URL;
- evidence class;
- both status fields;
- `Last verified`;
- what the source can support;
- known or proposed repository use.

Use IDs in the form:

- `P-YYYY-NN` — primary empirical research;
- `D-YYYY-NN` — primary documentary source;
- `S-YYYY-NN` — secondary evidence;
- `M-YYYY-NN` — methodology or theory;
- `DS-YYYY-NN` — dataset.

Choose exactly one primary class:

- `evidence/primary/`
- `evidence/documentary/`
- `evidence/secondary/`
- `evidence/methodology/`
- `evidence/datasets/`

Classification describes what the source is, not whether it supports the repository thesis.

## Evidence-review procedure

### 1. Start review

Set:

```text
Evidence review = Brief in progress
Integration audit = Not started
Last verified = —
```

For Flow C, retain `Needs re-verification` until the integration audit begins.

Read the original source, not only a summary or the repository's current interpretation.

### 2. Create or update the evidence brief

Create a kebab-case Markdown file in the correct evidence directory. Include:

1. Source ID and full citation.
2. Publication status and exact version.
3. Research question or documentary purpose.
4. Scope, dataset, population, period, comparator, and methodology.
5. Directly observed or documented findings.
6. Derived or model-calibrated findings.
7. Source-author interpretation.
8. Repository interpretation.
9. What the source does not establish.
10. Limitations, conflicts, and external-validity risks.
11. Known repository locations using the source.
12. A `Repository integration audit` section.

Use this template:

```markdown
## Repository integration audit

- Integration status: Not started | In progress | Corrections required | Verified | Needs re-verification
- Repository search completed:
- Claim-to-source trace location:
- Report mentions checked:
- Numeric claims checked:
- README claims and diagrams checked:
- Protocol outcome: No change | Clarification | Operational change
- Corrections made:
- Current-use locations confirmed:
- Verification date:
```

### 3. Complete evidence review

Add the brief to the relevant evidence-directory index and set:

```text
Evidence review = Reviewed brief
Integration audit = Not started
Last verified = —
```

For Flow C, the integration state may remain `Needs re-verification` until the audit starts.

A reviewed brief is not completion of the source-processing flow.

## Integration-audit procedure

### 1. Start the audit

Set:

```text
Integration audit = In progress
Last verified = —
```

Update the same status in the evidence brief.

### 2. Establish source ground truth

Record from the original source:

- canonical title, authors, date, version, and publication status;
- official publisher or author URL;
- design, dataset, population, period, and comparator;
- exact metric definitions;
- exact numbers and uncertainty;
- whether each result is observed, derived, model-calibrated, self-reported, or interpreted;
- stated limitations and conflicts.

### 3. Locate every repository use

Search the entire repository for:

- source ID;
- author and organization names;
- title fragments;
- distinctive metric names;
- every attributed number;
- paraphrases that may not contain a citation;
- diagrams, captions, summaries, or protocol language that implicitly depend on the source.

Inspect at minimum:

- all files under `report/`;
- `README.md`, including tables, captions, diagrams, and claim-confidence entries;
- all files under `protocols/`;
- `REFERENCES.md`;
- `evidence/SOURCES.md`;
- evidence-directory indexes.

Do not rely on the existing `Current use` field. Confirm actual usage and correct it.

### 4. Build a claim-to-source trace

For every material repository statement supported by the source, record:

| Repository claim | Location | Exact source result | Relationship | Action |
| --- | --- | --- | --- | --- |
| Claim or paraphrase | File and section | Finding or record | Direct, derived, synthesis, scenario, or unsupported | Keep, qualify, correct, relocate, or remove |

The trace must be inspectable. Put it in the evidence brief, PR description, or a linked review artifact. Record its location in the brief.

### 5. Verify numbers and units

For every number:

- confirm numerator, denominator, unit, population, and time window;
- distinguish percentages from percentage points;
- distinguish cumulative, average, median, short-run, and long-run effects;
- preserve uncertainty where material;
- reproduce simple derived calculations where practical;
- do not combine different samples, studies, tools, or periods into one apparent sequence without explicit labeling;
- remove obsolete or untraceable numbers.

A number in a table, caption, or diagram is a claim and must be checked exactly like prose.

### 6. Verify argument fit

Check whether the repository uses the source for a conclusion its design can support.

Ask:

- Is observational evidence presented as causal?
- Is a bounded task result generalized to teams, enterprises, industries, or the economy?
- Are different developer populations treated as interchangeable?
- Is activity described as productivity, quality, shipped value, or business impact without justification?
- Is source-author interpretation presented as an observed result?
- Is repository synthesis clearly identified?
- Are positive, null, mixed, contradictory, and unfavorable results treated fairly?

Correct the argument even when the correction weakens the repository thesis.

### 7. Verify report integration

For every report use:

- explain what the source actually measured;
- link to the evidence brief;
- separate source findings from repository inference;
- expose material limitations near the claim;
- remove inconsistent duplicate retellings;
- update neighboring paragraphs and chapter conclusions when needed.

A corrected citation is not enough if the surrounding argument remains misleading.

### 8. Verify repository-level integration

Reassess `README.md` when the source contributes to:

- the executive summary;
- claim-confidence map;
- Evidence Map;
- Crisis Map or another diagram;
- repository-level numeric claims;
- source coverage descriptions.

Multi-source diagrams must label source boundaries. Do not visually connect unrelated numbers as one observed causal chain.

### 9. Verify protocol implications

Inspect all protocols for explicit or implicit reliance on the source.

Choose and document exactly one outcome:

- **No protocol change**
- **Protocol clarification**
- **Protocol change**

Do not modify a protocol merely for symmetry with a report change.

### 10. Synchronize records

After corrections:

- update the evidence brief;
- update `Current use` in `evidence/SOURCES.md`;
- update the relevant evidence-directory index;
- update `REFERENCES.md`;
- verify internal and external links;
- record superseded versions and removed claims.

### 11. Set the final status

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

Update the evidence brief with the same status, protocol outcome, locations, corrections, trace location, and date.

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

Never mark a source `Verified` merely because a brief, citation, corrected paragraph, or PR exists.

## Evidence-strength rules

- Prefer primary sources over summaries.
- Prefer official publisher or author links over reposts.
- Do not infer causality from descriptive evidence without explicit justification.
- Do not present sentiment or adoption as production impact.
- Do not treat arXiv or working-paper status as peer review.
- Do not treat company marketing as independent evidence.
- Do not use one team's threshold as a universal standard.
- Preserve null, mixed, contradictory, positive, and unfavorable evidence.

## PR strategy

For a substantial source, use separate PRs when practical:

1. source registration and evidence brief;
2. report integration and source-wide corrections;
3. repository-map or protocol changes, only when required;
4. final verification-status update after all required changes are present on the default branch.

A single PR may combine these steps for a small source, but it must not set `Integration audit = Verified` before the default branch reflects the complete checked state.

## PR checklist

Before opening or completing a source PR, confirm:

- [ ] The correct flow was selected.
- [ ] The source is registered with both status fields.
- [ ] Its evidence class is correct.
- [ ] Publication status and version are explicit.
- [ ] Findings and repository interpretation are separated.
- [ ] Evidence-review status matches the actual brief state.
- [ ] Integration-audit status matches the actual audit state.
- [ ] All repository uses and attributed numbers were searched.
- [ ] A claim-to-source trace exists and its location is recorded.
- [ ] Numeric values, units, samples, and periods were checked.
- [ ] Report language matches the source design.
- [ ] README claims and diagrams were reassessed.
- [ ] Protocol implications have an explicit outcome.
- [ ] `Current use`, `REFERENCES.md`, and indexes are synchronized.
- [ ] The brief and registry show matching status and date.
- [ ] Navigation links work.
- [ ] The PR description lists boundaries, corrections, and unresolved work.
