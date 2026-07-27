# AGENTS.md

## Purpose

This file defines how human contributors and AI agents must process sources and modify this repository without mixing evidence, repository interpretation, operational guidance, and navigation metadata.

The repository has four layers:

1. **Evidence** — what external sources report.
2. **Report** — the Subprime Code Crisis synthesis and argument.
3. **Protocols** — operational responses derived from the risk analysis.
4. **Repository maps** — navigation, source status, claim confidence, diagrams, and bibliography.

Do not collapse these layers.

## Read order

Before changing source-related content, read:

1. `README.md` — scope, major claims, maps, and repository structure.
2. `evidence/README.md` — evidence taxonomy and brief standard.
3. `evidence/SOURCES.md` — canonical source inventory and status database.
4. The relevant evidence brief, when one exists.
5. Every relevant file under `report/`.
6. Every relevant file under `protocols/`.
7. `REFERENCES.md` — compact bibliography.
8. `CONTRIBUTING.md` — contributor requirements.

`evidence/SOURCES.md` is canonical. `REFERENCES.md` is not a status database.

## Repository boundaries

### Evidence

Evidence briefs must separate:

- directly observed or documented findings;
- derived calculations;
- model-calibrated estimates;
- source-author interpretation;
- repository interpretation;
- claims not established by the source;
- limitations, conflicts, and external-validity risks.

Never present a repository conclusion as a finding directly reported by a source.

### Report

Every material factual claim must trace to a registered source. Strong or load-bearing claims should trace to a reviewed evidence brief.

Use bounded language when the source design cannot support a causal, universal, or enterprise-wide conclusion.

### Protocols

Protocols are operating patterns, not empirical proof. Do not present a local threshold, role, gate, escalation rule, workflow, or control as universally validated unless evidence directly establishes it.

### Repository maps

Keep these synchronized:

- `evidence/SOURCES.md` — canonical source and status registry;
- evidence-directory indexes — available briefs;
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

`Last verified` contains a date only when `Integration audit = Verified`. Otherwise use `—`.

The existence of a brief, citation, merged PR, or corrected paragraph does not imply verified integration.

## Choose the correct flow first

Select one primary flow before editing anything.

### Flow A — Add a new source

Use when the source is not listed in `evidence/SOURCES.md`.

1. Register and classify it.
2. Set `Evidence review = Registered`, `Integration audit = Not started`, `Last verified = —`.
3. Complete the evidence-review procedure.
4. Complete the integration-audit procedure.
5. Synchronize all records.
6. Mark `Verified` only after all required corrections are merged.

### Flow B — Process a legacy registered source

Use when the source is already cited or registered but lacks a current reviewed brief or completed integration audit.

1. Confirm or correct its ID, class, canonical link, publication status, and proposed `Current use`.
2. Do not create a duplicate registry entry.
3. Complete evidence review if no current reviewed brief exists.
4. Audit every existing repository use.
5. Correct claims, diagrams, references, and protocol implications.
6. Mark `Verified` only after all corrections are merged.

### Flow C — Update a changed or superseded source

Use when a paper, report, filing, dataset, or methodology source changes, is superseded, or becomes peer reviewed.

1. Set `Evidence review = Needs re-review`.
2. Set `Integration audit = Needs re-verification`.
3. Clear `Last verified` to `—`.
4. Record the new version.
5. Re-run evidence review.
6. Re-run the complete integration audit.
7. Restore `Reviewed brief` and `Verified` only after completion.

### Flow D — Re-verify changed repository content

Use when the source itself is unchanged, but a report claim, README diagram, summary, protocol, or derived calculation relying on it changes materially.

1. Keep `Evidence review = Reviewed brief` unless the brief itself is inadequate.
2. Set `Integration audit = Needs re-verification`.
3. Clear `Last verified` to `—`.
4. Re-run the integration audit for the affected source.
5. Restore `Verified` only after the changed repository state is checked and merged.

### Flow E — Discover newer or missing evidence

Use after the current source backlog has been processed far enough to expose real evidence gaps.

1. Identify weak claims, stale evidence, missing primary sources, contradictions, positive evidence, null results, and replication gaps.
2. Search for newer, stronger, original, peer-reviewed, contradictory, null, and positive evidence.
3. Do not insert search results directly into the report.
4. Route every selected source through Flow A.
5. For systematic or claim-critical searches, record rejected candidates and reasons.

Freshness search is not a substitute for validating sources already used by the repository.

## Registration and classification

Register a source before adding or revising report claims. Record:

- stable source ID;
- canonical title and authors or publisher;
- year, version, and publication status;
- canonical URL;
- evidence class;
- both status fields;
- `Last verified`;
- what the source can support;
- known or proposed repository use.

Source ID forms:

- `P-YYYY-NN` — primary empirical research;
- `D-YYYY-NN` — primary documentary source;
- `S-YYYY-NN` — secondary evidence;
- `M-YYYY-NN` — methodology or theory;
- `DS-YYYY-NN` — dataset.

Choose one primary class:

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
Last verified = —
```

For a new or legacy source, keep `Integration audit = Not started`. For Flow C, keep `Needs re-verification` until the audit starts.

Read the original source, not only a summary or the repository's existing interpretation.

### 2. Create or update the brief

The brief must include:

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

Use this audit template:

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
```

A reviewed brief does not complete source processing.

## Integration-audit procedure

### 1. Start the audit

Set in both the registry and brief:

```text
Integration audit = In progress
Last verified = —
```

### 2. Establish source ground truth

Confirm:

- title, authors, date, version, and publication status;
- official URL;
- design, dataset, population, period, and comparator;
- exact metric definitions;
- exact numbers and uncertainty;
- whether results are observed, derived, model-calibrated, self-reported, or interpreted;
- limitations and conflicts.

### 3. Locate every repository use

Search the entire repository for:

- source ID;
- author and organization names;
- title fragments;
- distinctive metric names;
- every attributed number;
- uncited paraphrases;
- diagrams, captions, summaries, and protocol language that implicitly depend on the source.

Inspect at minimum:

- all files under `report/`;
- `README.md`, including tables, captions, diagrams, and claim-confidence entries;
- all files under `protocols/`;
- `REFERENCES.md`;
- `evidence/SOURCES.md`;
- evidence-directory indexes.

Do not trust the existing `Current use` field without confirming actual usage.

### 4. Build a claim-to-source trace

For every material use, record:

| Repository claim | Location | Exact source result | Relationship | Action |
| --- | --- | --- | --- | --- |
| Claim or paraphrase | File and section | Finding or record | Direct, derived, synthesis, scenario, or unsupported | Keep, qualify, correct, relocate, or remove |

The trace must be inspectable and its location recorded in the brief.

### 5. Verify numbers and units

For every number:

- confirm numerator, denominator, unit, population, and time window;
- distinguish percentages from percentage points;
- distinguish cumulative, average, median, short-run, and long-run effects;
- preserve material uncertainty;
- reproduce simple derived calculations where practical;
- do not visually or rhetorically combine different studies, samples, tools, or periods into one observed sequence without explicit labeling;
- remove obsolete or untraceable numbers.

A number in a table, caption, or diagram is a claim.

### 6. Verify argument fit

Check whether the source design supports the repository conclusion.

Ask whether:

- observational evidence is presented as causal;
- bounded tasks are generalized to teams, enterprises, industries, or the economy;
- different developer populations are treated as interchangeable;
- activity is described as productivity, quality, shipped value, or business impact without justification;
- source-author interpretation is presented as an observed result;
- repository synthesis is clearly identified;
- positive, null, mixed, contradictory, and unfavorable findings are treated fairly.

Correct the argument even when this weakens the repository thesis.

### 7. Verify report integration

For every report use:

- explain what the source measured;
- link to the evidence brief;
- separate findings from repository inference;
- expose material limitations near the claim;
- remove inconsistent duplicate retellings;
- update neighboring paragraphs and chapter conclusions when needed.

A corrected citation is insufficient if the surrounding argument remains misleading.

### 8. Verify README and repository maps

Reassess:

- executive summary;
- claim-confidence map;
- Evidence Map;
- Crisis Map and other diagrams;
- repository-level numeric claims;
- source coverage descriptions.

Multi-source diagrams must label source boundaries and must not present unrelated numbers as one measured causal chain.

### 9. Verify protocol implications

Inspect every protocol for explicit or implicit reliance on the source. Document exactly one outcome:

- **No protocol change**
- **Protocol clarification**
- **Protocol change**

Do not change a protocol merely for symmetry with a report change.

### 10. Synchronize records

After corrections:

- update the brief;
- update actual `Current use` locations in `evidence/SOURCES.md`;
- update the relevant evidence index;
- update `REFERENCES.md`;
- verify links;
- record superseded versions and removed claims.

### 11. Set final status

When unresolved problems remain:

```text
Integration audit = Corrections required
Last verified = —
```

Only after every required correction is merged and every completion check passes:

```text
Evidence review = Reviewed brief
Integration audit = Verified
Last verified = YYYY-MM-DD
```

The brief and registry must show the same status and date.

## Completion checklist

A source may be marked `Verified` only when:

- [ ] The correct source version was read.
- [ ] A reviewed evidence brief exists and is indexed.
- [ ] Every repository mention and attributed number was located.
- [ ] A claim-to-source trace exists for all material uses.
- [ ] Numbers, units, populations, and periods were checked.
- [ ] Claim strength matches the source design.
- [ ] Report arguments and nearby conclusions remain valid.
- [ ] README claims, tables, and diagrams were reassessed.
- [ ] Protocol implications have a documented outcome.
- [ ] `Current use` lists actual locations.
- [ ] `REFERENCES.md`, indexes, and links are synchronized.
- [ ] The brief and registry show matching status and date.
- [ ] No unresolved correction remains.

## PR strategy

For substantial source work, prefer separate PRs:

1. registration and evidence brief;
2. report integration and corrections;
3. README or protocol changes, only when required;
4. final verification-status update after all required changes exist on the default branch.

Do not set `Integration audit = Verified` until the default branch reflects the completed state.
