# AGENTS.md

## Purpose

This file is the canonical instruction for human contributors and AI agents working in this repository. It defines how to process sources and modify the repository without mixing evidence, repository interpretation, operational guidance, and navigation metadata.

The repository has four layers:

1. **Evidence** — what external sources report.
2. **Report** — the Subprime Code Crisis synthesis and argument.
3. **Protocols** — operational responses derived from the risk analysis.
4. **Repository maps** — navigation, source status, claim confidence, diagrams, and bibliography.

Do not collapse these layers.

## Mandatory start-of-work gate

Before reading, editing, reviewing, searching for evidence, or changing source status, read the current `AGENTS.md` from the target branch in full.

Instructions remembered from an earlier task, conversation, branch, or cached context are not sufficient. The repository version is authoritative.

Before changing anything, state:

- the selected primary flow;
- the files and source IDs in scope;
- whether evidence review, integration audit, or both are required;
- whether an independent reviewer is available.

Then read:

1. `README.md` — scope, major claims, maps, and repository structure.
2. `evidence/README.md` — evidence taxonomy and brief standard.
3. `evidence/SOURCES.md` — canonical source inventory and status registry.
4. The relevant evidence brief, when one exists.
5. Every relevant file under `report/`.
6. Every relevant file under `protocols/`.
7. `REFERENCES.md` — compact human-readable bibliography.
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

Keep synchronized:

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

A brief, citation, merged PR, or corrected paragraph does not imply verified integration.

## Choose the correct primary flow

Select one primary flow before editing anything.

### Flow A — Add a new source

Use when the source is not listed in `evidence/SOURCES.md`.

1. Register and classify it.
2. Set `Evidence review = Registered`, `Integration audit = Not started`, `Last verified = —`.
3. Complete evidence review.
4. Complete the repository-wide integration audit.
5. Synchronize all records.
6. Pass independent review.
7. Mark `Verified` only after all corrections are merged and the independent review outcome is `Confirmed`.

### Flow B — Process a legacy registered source

Use when the source is already cited or registered but lacks a current reviewed brief or completed integration audit.

1. Confirm or correct its ID, class, canonical link, publication status, and proposed `Current use`.
2. Do not create a duplicate registry entry.
3. Complete evidence review if no current reviewed brief exists.
4. Audit every repository use.
5. Correct claims, diagrams, references, and protocol implications.
6. Pass independent review.
7. Mark `Verified` only after all corrections are merged and confirmed.

### Flow C — Update a changed or superseded source

Use when a paper, report, filing, dataset, or methodology source changes, is superseded, or becomes peer reviewed.

1. Set `Evidence review = Needs re-review`.
2. Set `Integration audit = Needs re-verification`.
3. Clear `Last verified` to `—`.
4. Record the new version and preserve version history.
5. Re-run evidence review.
6. Re-run the complete integration audit.
7. Pass independent review.
8. Restore `Reviewed brief` and `Verified` only after completion.

### Flow D — Re-verify changed repository content

Use when the source itself is unchanged, but a report claim, README diagram, summary, protocol, or derived calculation relying on it changes materially.

1. Keep `Evidence review = Reviewed brief` unless the brief itself is inadequate.
2. Set `Integration audit = Needs re-verification`.
3. Clear `Last verified` to `—`.
4. Re-run the integration audit for the affected source.
5. Pass independent review.
6. Restore `Verified` only after the changed repository state is checked and merged.

### Flow E — Discover newer or missing evidence

Use to identify newer, missing, stronger, contradictory, null, or positive evidence relevant to the report. Discovery does not itself add evidence to the report. Accepted candidates enter Flow A.

#### 1. Define the search question

Record:

- the report claim, evidence gap, or topic being investigated;
- inclusion and exclusion criteria;
- relevant populations, tasks, tools, outcomes, and time period;
- preferred evidence types;
- search date and freshness window.

Do not search only for evidence supporting the repository thesis.

#### 2. Search broadly

Search multiple channels. Prioritize:

1. arXiv and other primary preprint repositories;
2. peer-reviewed journals and conference proceedings;
3. original institutional or laboratory publications;
4. official datasets, filings, standards, and technical reports;
5. credible industry research with inspectable methods;
6. secondary synthesis and practitioner commentary for discovery only.

Use query families covering:

- positive, negative, mixed, and null outcomes;
- productivity, quality, review, maintenance, defects, security, release, and business outcomes;
- replications and critiques;
- updated or peer-reviewed versions of known work;
- terminology variants and adjacent disciplines.

Record the databases or sites searched and representative queries.

#### 3. Deduplicate and identify canonical versions

For each candidate:

- find the canonical title, authors, identifier, and URL;
- distinguish preprint, accepted manuscript, published version, dataset, summary, and commentary;
- prefer the latest authoritative version while preserving version history;
- identify duplicates and derivative reporting.

#### 4. Assess relevance

Record:

- relevance: direct, adjacent, contextual, or not relevant;
- which repository claims it may support, weaken, contradict, or contextualize;
- whether it adds a new outcome, population, method, or time period;
- whether it is materially stronger than an existing source.

Title or abstract similarity alone is insufficient.

#### 5. Assess the research entity

Identify:

- authors and affiliations;
- laboratory, company, university, consortium, or public body;
- funding source when disclosed;
- commercial interests or advocacy position;
- prior relevant research record when material;
- whether the entity controls the measured product, platform, or dataset.

Entity reputation is context, not a substitute for methodological review.

#### 6. Assess source quality and publication status

Record:

- source type and publication status;
- peer-review status;
- method transparency;
- data and code availability;
- sample size and selection;
- comparator or baseline;
- preregistration or protocol availability;
- statistical uncertainty;
- conflicts of interest;
- replication or independent validation status;
- major limitations and external-validity risks.

Do not reject arXiv work solely because it is a preprint. Do not treat an arXiv identifier as proof of quality.

#### 7. Define scope and boundaries

For every candidate, state:

- population and experience level;
- task type and complexity;
- tool, model, and version;
- study setting;
- observation period;
- measured outcomes and definitions;
- causal or observational design;
- what the study does not establish;
- limits on generalization to teams, organizations, industries, or the economy.

#### 8. Screen and record candidates

Assign one provisional decision:

- `Accept for Flow A`
- `Hold for comparison or newer version`
- `Context only`
- `Reject`

For systematic or claim-critical searches, keep a candidate log with decision reasons. Rejected sources must not disappear without explanation.

#### 9. Independent discovery review

A second agent or reviewer must independently:

- rerun representative searches;
- check for omitted positive, negative, contradictory, or null evidence;
- verify canonical versions and publication status;
- challenge relevance and source-quality assessments;
- review candidate decisions and rejection reasons.

Unresolved disagreements or material omissions must be discussed with the human user before candidates are accepted.

#### 10. Route accepted evidence

Every accepted candidate enters Flow A. Discovery notes do not substitute for registration, evidence review, an evidence brief, integration audit, or independent verification.

Freshness search is not a substitute for validating sources already used by the repository.

## Registration and classification

Register a source before adding or revising report claims. Record:

- stable source ID;
- canonical title and authors or publisher;
- year, exact version, and publication status;
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
13. An `Independent review` section.

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

- title, authors, date, exact version, and publication status;
- official URL;
- research entity, affiliations, and funding when relevant;
- design, dataset, population, period, and comparator;
- exact metric definitions;
- exact numbers and uncertainty;
- whether results are observed, derived, model-calibrated, self-reported, or interpreted;
- limitations and conflicts.

### 3. Locate every repository use

Search for:

- source ID;
- author and organization names;
- title fragments;
- distinctive metric names;
- every attributed number;
- uncited paraphrases;
- diagrams, captions, summaries, and protocol language implicitly depending on the source.

Inspect at minimum:

- all files under `report/`;
- `README.md`, including tables, captions, diagrams, and claim-confidence entries;
- all files under `protocols/`;
- `REFERENCES.md`;
- `evidence/SOURCES.md`;
- evidence-directory indexes.

Do not trust `Current use` without confirming actual usage.

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
- do not combine different studies, samples, tools, or periods into one observed sequence without explicit labeling;
- remove obsolete or untraceable numbers.

A number in a table, caption, or diagram is a claim.

### 6. Verify argument fit

Check whether:

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

- `No protocol change`
- `Protocol clarification`
- `Protocol change`

Do not change a protocol merely for symmetry with a report change.

### 10. Synchronize records

After corrections:

- update the brief;
- update actual `Current use` locations in `evidence/SOURCES.md`;
- update the relevant evidence index;
- update `REFERENCES.md`;
- verify links;
- record superseded versions and removed claims.

## Independent review gate

Every completed Flow A–E must be reviewed by a second agent or reviewer that did not produce the work.

The reviewer must independently inspect the original source or search results, changed files, status transitions, claim-to-source trace, calculations, and completion checklist. The reviewer must not merely summarize the first agent's notes.

Record one outcome:

- `Confirmed` — no material discrepancy found;
- `Corrections required` — specific defects or omissions found;
- `Unresolved disagreement` — reviewers disagree or material uncertainty remains;
- `Review unavailable` — no independent reviewer could be used.

If corrections are required, return the work to the applicable flow and repeat independent review after correction.

If the outcome is `Unresolved disagreement` or `Review unavailable`, do not guess, average conclusions, or silently choose one interpretation. Escalate to the human user.

`Integration audit = Verified` is forbidden unless the independent review outcome is `Confirmed`.

Use this record:

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

## Human escalation gate

Escalate before finalizing when:

- agents disagree on relevance, source quality, claim strength, calculation, or status;
- a source is ambiguous, inaccessible, superseded, or internally inconsistent;
- repository claims cannot be traced confidently;
- a correction would materially weaken, reverse, or remove a major conclusion;
- a new flow or material instruction change appears necessary;
- the independent reviewer reports unresolved doubt;
- the requested action conflicts with this file.

Present the decision needed, competing interpretations, supporting evidence, and practical consequences.

## User-correction and workflow-maintenance trigger

Whenever the user corrects an agent's result, classify the correction as:

1. **Execution error** — the existing flow was adequate but followed incorrectly.
2. **Missing check** — the flow lacks a required verification step.
3. **Ambiguous instruction** — more than one reasonable interpretation exists.
4. **New recurring work type** — the request does not fit current flows.
5. **One-off preference or scope decision** — no process change is required.

Compare the correction with the current flows and gates.

If categories 2–4 apply, explain the suspected process gap and ask the user whether `AGENTS.md` should be updated. Do not silently change the workflow because of one interaction.

When the user approves a workflow change:

- extend an existing flow when the trigger, state transition, and completion condition remain the same;
- add a new primary flow only when the work has a distinct trigger, procedure, and completion condition;
- keep cross-cutting controls such as independent review and human escalation outside primary source flows;
- update entry points only after the canonical instruction is merged.

## Final status and completion checklist

When unresolved problems remain:

```text
Integration audit = Corrections required
Last verified = —
```

Only after every required correction is merged, independent review is `Confirmed`, and every completion check passes:

```text
Evidence review = Reviewed brief
Integration audit = Verified
Last verified = YYYY-MM-DD
```

The brief and registry must show the same status and date.

A source may be marked `Verified` only when:

- [ ] The current `AGENTS.md` was read before work began.
- [ ] The correct source version was read.
- [ ] A reviewed evidence brief exists and is indexed.
- [ ] Every repository mention and attributed number was located.
- [ ] A claim-to-source trace exists for all material uses.
- [ ] Numbers, units, populations, and periods were checked.
- [ ] Claim strength matches source design.
- [ ] Report arguments and nearby conclusions remain valid.
- [ ] README claims, tables, and diagrams were reassessed.
- [ ] Protocol implications have a documented outcome.
- [ ] `Current use` lists actual locations.
- [ ] `REFERENCES.md`, indexes, and links are synchronized.
- [ ] Independent review outcome is `Confirmed`.
- [ ] The brief and registry show matching status and date.
- [ ] No unresolved correction or human decision remains.

## PR strategy

For substantial source work, prefer separate PRs:

1. registration and evidence brief;
2. report integration and corrections;
3. README or protocol changes, only when required;
4. independent-review corrections, when required;
5. final verification-status update after all required changes exist on the default branch.

Do not set `Integration audit = Verified` until the default branch reflects the completed and independently confirmed state.
