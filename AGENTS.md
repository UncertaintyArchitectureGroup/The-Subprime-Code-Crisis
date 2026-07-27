# AGENTS.md

## Canonical status

This file is the canonical operating specification for human contributors and AI agents working in this repository.

Before performing any repository work, read this file in full from the target branch. Instructions remembered from an earlier task, conversation, branch, cached context, or model memory are not sufficient. When remembered instructions conflict with this file, this file wins.

## Repository Constitution

The following principles govern all repository work. They take precedence over individual flows, local convenience, agent preference, and remembered instructions.

No contributor or agent may weaken, bypass, reinterpret, or replace these principles.

1. **Original evidence over summaries.** The original source is authoritative for what it reports. Search snippets, secondary summaries, repository text, and prior agent notes are not substitutes.
2. **Every material claim must remain traceable.** A material factual claim must trace to a registered source, its reviewed evidence brief when required, and the repository locations where it is used.
3. **Evidence review is not integration audit.** Understanding a source and verifying every repository use of that source are separate activities with separate states and completion conditions.
4. **Evidence strength governs claim strength.** Repository language, confidence, and scope must follow source design, uncertainty, limitations, and external validity.
5. **Contradictory evidence remains visible.** Positive, negative, null, mixed, contradictory, replication, and limiting evidence must be treated fairly and must not be removed for rhetorical convenience.
6. **Humans approve substantive repository changes.**
7. **Workflow changes require prior discussion.**
8. **Repository arguments evolve through evidence, not agent preference.** Agents must not change arguments, conclusions, confidence, or protocol logic merely because an alternative formulation appears more persuasive or convenient.
9. **Important decisions remain inspectable.** Material changes must preserve the triggering evidence or problem, alternatives considered, human decision, implementation, and independent-review outcome.
10. **`AGENTS.md` is the canonical operating specification.** Entry points, supporting documents, and agent memory must not override it.
11. **Verification cannot be inferred.** A citation, evidence brief, corrected paragraph, completed PR, or plausible result does not by itself establish reviewed or verified status.
12. **No silent governance change.**

The operational procedures that enforce these principles are defined under `Repository Governance` and `Workflow Evolution`.

## Repository overview

The Subprime Code Crisis repository examines how AI-assisted software development changes software-delivery systems.

It focuses on the gap between local code-generation speed and end-to-end delivery outcomes such as review capacity, rework, quality, security, release performance, maintenance, and organizational control.

The repository is:

- an evidence-governed research synthesis;
- a structured argument about delivery-system risks;
- an operational protocol library for engineering organizations;
- an inspectable record of sources, interpretations, confidence, and unresolved uncertainty.

The repository is not:

- an anti-AI manifesto;
- a vendor ranking or benchmark leaderboard;
- a collection of citations without source review;
- proof that one study, tool, team, or metric represents the software industry;
- a claim that every protocol is empirically validated or universally applicable.

Mixed, positive, null, contradictory, and unfavorable evidence is part of the repository's subject matter and must be treated fairly.

## Repository goal

The goal is to maintain a credible, inspectable, and operationally useful account of AI-assisted software-delivery risk.

The repository is healthy when:

1. every material factual claim traces to a registered source;
2. source findings are separated from source-author interpretation and repository inference;
3. important sources have reviewed evidence briefs;
4. every repository use of a source has been integration-audited;
5. report arguments match the strength and scope of the evidence;
6. protocols are clearly identified as evidence-backed, systems-derived, or proposed practice;
7. contradictory and limiting evidence remains visible;
8. source status, bibliography, indexes, diagrams, and current-use records remain synchronized;
9. substantive changes remain subject to human judgment and explicit approval.

Speed, volume of changes, persuasive language, and number of citations are not success criteria.

## Repository architecture

The repository has five connected layers.

```text
External source material
        ↓
Evidence registry and evidence briefs
        ↓
Report synthesis and argument
        ↓
Operational protocols
        ↓
Repository maps and navigation
```

### Layer 1 — External source material

Original papers, datasets, filings, standards, institutional reports, and other external records.

The original source is authoritative for what it reports. Repository text, summaries, search snippets, and prior agent notes are not substitutes.

### Layer 2 — Evidence registry and briefs

- `evidence/SOURCES.md` is the canonical source inventory and status registry.
- Evidence briefs document source design, findings, calculations, interpretation, limitations, scope, and repository use.
- Evidence review determines whether the source itself has been understood and documented accurately.

### Layer 3 — Report

Files under `report/` synthesize multiple sources and develop the Subprime Code Crisis argument.

The report may make systems-level inferences, but those inferences must be distinguishable from source findings and bounded by the underlying evidence.

### Layer 4 — Protocols

Files under `protocols/` translate the risk analysis into adaptable operating practices.

Protocols are not empirical proof. A source may motivate a control without proving that a specific threshold, role, gate, or escalation rule is universally valid.

### Layer 5 — Repository maps and navigation

This includes:

- the root `README.md`;
- claim-confidence and evidence maps;
- diagrams, including the Crisis Map;
- evidence-directory indexes;
- `REFERENCES.md`, the compact human-readable bibliography.

These artifacts summarize and navigate the repository. They must not silently introduce stronger claims than the evidence and report support.

Do not collapse these layers.

## Design principles

### Original source over summary

Read the original source whenever accessible. Secondary summaries and repository interpretations may help locate material but cannot establish source ground truth.

### Evidence before rhetoric

Claim strength must follow source design, scope, uncertainty, and external-validity limits. Correct or weaken the repository argument when the evidence requires it.

### Findings, interpretation, and inference remain separate

Always distinguish:

- directly observed or documented findings;
- derived calculations;
- model-calibrated estimates;
- source-author interpretation;
- repository interpretation;
- claims not established by the source.

### Mixed evidence is expected

Do not search only for confirming evidence. Preserve positive, null, mixed, contradictory, replication, and critique evidence.

### Every material claim remains inspectable

A reader must be able to trace a material claim to its source, evidence brief, relationship type, repository location, and current status.

### Workflow correctness over speed

Do not skip registration, review, integration audit, independent review, synchronization, or human escalation to complete work faster.

### Human-curated substantive logic

Agents may discover evidence, identify inconsistencies, calculate implications, and propose changes.

Classify proposed edits using `Safe vs Substantive Changes` under `Repository Governance`. Substantive changes are governed by the canonical `Human Escalation`, `Repository Change Proposal`, and `Independent Review` procedures in that section. Apply `Workflow Evolution` as well when the proposed change affects repository governance or workflow architecture.

## Design rationale

### Why evidence review and integration audit are separate

Understanding and documenting a source is different from verifying every place where the repository uses that source.

A correct evidence brief does not prove that report claims, diagrams, calculations, protocols, and navigation artifacts use the source correctly. Therefore the two activities have independent states and completion conditions.

### Why `evidence/SOURCES.md` is canonical

The registry is the machine- and human-readable inventory of source identity, classification, evidence-review status, integration-audit status, verification date, and current repository use.

`REFERENCES.md` is intentionally a compact bibliography. Treating it as a status database would mix navigation with workflow state and allow inconsistencies to remain hidden.

### Why discovery does not update the report directly

Search results are candidates, not evidence accepted by the repository. Each selected candidate must receive explicit routing. A previously unregistered evidence object enters Flow A. A changed, corrected, peer-reviewed, retracted, or superseding version of an already registered source enters Flow C. The applicable flow must be completed before the source can support report claims.

### Why independent review is required

The same agent that produced a search, brief, calculation, or integration audit may repeat its own assumptions. Independent review creates a separate attempt to find omissions, misreadings, contradictory evidence, status errors, and misleading synthesis.

### Why substantive changes require human discussion

Evidence can support more than one reasonable interpretation, and repository arguments and protocols contain normative and strategic judgments. Agents may expose the decision but must not silently replace the maintainer's judgment with their own.

### Why user corrections can change the workflow

A user correction may reveal an execution mistake, a missing check, an ambiguous instruction, or a new recurring work type. The agent must classify the correction and propose workflow evolution when appropriate, but `AGENTS.md` itself must not change silently.

## Mandatory start-of-work gate

Before reading other repository files, editing, reviewing, searching for evidence, or changing source status, read the current `AGENTS.md` from the target branch in full.

Instructions remembered from an earlier task, conversation, branch, or cached context are not sufficient. The repository version is authoritative.

Before changing anything, state:

- the selected primary flow;
- the files and source IDs in scope;
- whether evidence review, integration audit, or both are required;
- whether an independent reviewer is available;
- whether the task may trigger a substantive-change discussion.

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

Use Flow E to identify evidence candidates relevant to a defined repository claim, evidence gap, uncertainty, or freshness requirement.

Discovery is not evidence acceptance. Flow E must not directly change report claims, protocols, source statuses, confidence classifications, or repository maps. Every accepted candidate must receive explicit routing. A previously unregistered evidence object enters Flow A. A changed, corrected, peer-reviewed, retracted, or superseding version of an already registered source enters Flow C.

#### 1. Search Strategy

Before searching, create a written strategy that records:

- the repository claim, evidence gap, uncertainty, or topic being investigated;
- the purpose of the search: freshness, contradiction testing, replication search, gap filling, or broader landscape review;
- the search date and freshness window;
- databases, indexes, repositories, institutional sites, and other channels to search;
- representative queries and terminology variants;
- target evidence types and publication periods;
- populations, tasks, tools, outcomes, and settings of interest;
- known blind spots and expected search limitations.

Use multiple query families that deliberately seek positive, negative, null, mixed, contradictory, replication, and critique evidence. A search designed only to confirm the repository thesis is invalid.

Prioritize original and inspectable sources:

1. peer-reviewed journals and conference proceedings;
2. authoritative preprint repositories;
3. original institutional or laboratory publications;
4. official datasets, filings, standards, and technical reports;
5. credible industry research with inspectable methods;
6. secondary synthesis and practitioner commentary for discovery only.

Record enough detail for another reviewer to rerun representative searches.

#### 2. Inclusion

Define inclusion criteria before candidate selection. Criteria should address:

- direct or material relevance to the search question;
- identifiable authorship or responsible publishing entity;
- accessible abstract, methods, dataset description, or full text sufficient for screening;
- clear publication date and version;
- identifiable population, task, intervention or exposure, comparator, and outcome where applicable;
- evidence type allowed by the search strategy;
- time period and language boundaries;
- minimum methodological transparency appropriate to the source type.

A source may be included for contradiction, limitation, replication, context, or null results. Inclusion does not mean that the source supports the repository thesis.

#### 3. Exclusion

Define exclusion criteria before final screening. Common reasons include:

- duplicate or derivative reporting when an original source is available;
- promotional material without inspectable methods or underlying evidence;
- inaccessible claims that cannot be checked beyond a search snippet;
- unclear authorship, date, version, or source identity;
- irrelevance to the defined population, task, outcome, or repository claim;
- commentary presented as empirical evidence;
- superseded versions when the authoritative version is available;
- unverifiable numbers or claims with no traceable source;
- material methodological opacity that prevents even bounded interpretation.

Do not exclude a source merely because it is unfavorable, null, contradictory, industry-funded, a preprint, or produced by a vendor. Record the concern and assess it explicitly.

Every excluded candidate in a claim-critical or systematic search must retain an exclusion reason in the Candidate Register.

#### 4. Research Entity Assessment

For every candidate that survives initial screening, identify:

- authors and affiliations;
- laboratory, university, company, consortium, standards body, public agency, or other responsible entity;
- whether the entity created, owns, sells, funds, administers, or controls the studied product, platform, benchmark, or dataset;
- prior relevant research or publication record when material;
- disclosed advocacy, policy, commercial, or institutional position;
- independence of data collection and analysis where determinable.

Entity reputation is context, not evidence quality. A prestigious institution does not cure weak methods, and a commercial affiliation does not automatically invalidate results.

#### 5. Publication Status

Record the exact publication state:

- working paper;
- preprint;
- submitted manuscript;
- accepted manuscript;
- peer-reviewed conference paper;
- peer-reviewed journal article;
- institutional report;
- technical report;
- dataset or data release;
- standard, filing, or other documentary source;
- correction, retraction, expression of concern, or superseded version.

Verify peer-review claims from the publisher or venue when practical. An arXiv, SSRN, DOI, repository page, or conference upload does not by itself establish peer review.

Publication status affects confidence and review depth but is not a binary acceptance rule.

#### 6. Funding

Record:

- disclosed funders and grant identifiers;
- employer sponsorship or internal company research;
- provision of tools, compute, data, recruitment, or researcher access;
- funder role in study design, analysis, publication, or approval;
- absence of a funding statement when one would normally be expected;
- whether the measured vendor or platform financed the work.

Funding is a risk and context signal, not an automatic reason for inclusion or exclusion.

#### 7. Conflicts

Record disclosed and reasonably identifiable conflicts, including:

- employment, consulting, equity, patents, advisory roles, or vendor relationships;
- ownership or commercial interest in the evaluated product or method;
- control over the measured dataset or benchmark;
- advocacy or policy commitments directly related to the conclusion;
- publication approval rights or contractual restrictions;
- conflicts declared absent by the authors;
- conflicts that remain unknown.

Separate documented conflicts from repository inference. Do not imply misconduct without evidence.

#### 8. Scope

For each candidate, state the exact evidence boundary:

- population and experience level;
- sample size and selection mechanism;
- task type, duration, and complexity;
- tool, model, version, configuration, and access conditions;
- study or operational setting;
- comparator or baseline;
- observation period;
- outcomes and metric definitions;
- causal, experimental, quasi-experimental, observational, documentary, or theoretical design;
- unit of analysis;
- what the source directly establishes;
- what the source does not establish.

Title, abstract, or headline similarity is insufficient for scope classification.

#### 9. External Validity

Assess whether and how the source may generalize beyond its observed setting. Examine:

- representativeness of participants, organizations, tasks, tools, and environments;
- artificial or benchmark conditions versus production work;
- short-term measurement versus maintenance and lifecycle effects;
- individual activity versus team, delivery-system, organizational, industry, or economic outcomes;
- differences between novice, intermediate, and expert populations;
- model, product, and workflow version dependence;
- selection, survivorship, novelty, and observer effects;
- geographic, organizational, and regulatory boundaries;
- whether claimed generalization exceeds the measured unit of analysis.

Record external validity as a bounded assessment, not a single quality score. A narrow study may be rigorous and still support only a narrow claim.

#### 10. Replication

Search explicitly for:

- direct replications;
- conceptual replications;
- independent reanalyses;
- corrections and critiques;
- contradictory studies using comparable outcomes;
- follow-up studies with different populations, tools, tasks, or periods;
- repeated findings from the same authors or organization;
- evidence that the result has not yet been independently tested.

Record whether replication is independent, partial, failed, mixed, contested, or unavailable. Repeated vendor or laboratory publications are not independent replication unless data collection and analysis are genuinely independent.

Replication status must inform candidate priority and later claim confidence, but absence of replication does not automatically exclude a new source.

#### 11. Canonical Version

For every candidate:

- identify the canonical title, authors, date, identifier, and URL;
- distinguish preprint, accepted manuscript, published version, dataset, appendix, correction, summary, and commentary;
- prefer the latest authoritative version for review;
- preserve links and dates for materially different earlier versions;
- identify retractions, corrections, expressions of concern, and superseding publications;
- avoid registering the same research object as multiple independent sources;
- record when no authoritative canonical version can be established.

When versions materially differ, route the source through Flow C after registration or document the version relationship before Flow A begins.

#### 12. Candidate Register

Maintain a Candidate Register for every claim-critical, systematic, or multi-source discovery task.

Each entry must contain:

| Field | Required record |
| --- | --- |
| Candidate ID | Temporary search identifier |
| Citation | Title, authors or entity, year |
| Canonical URL | Best current authoritative link |
| Canonical version | Version and publication state |
| Search provenance | Database, site, query, and search date |
| Relevance | Direct, adjacent, contextual, or not relevant |
| Relationship | May support, weaken, contradict, replicate, or contextualize |
| Inclusion result | Included, excluded, or held |
| Decision reason | Specific screening rationale |
| Research entity | Authors, affiliations, and responsible organization |
| Funding | Disclosed, absent, or unknown |
| Conflicts | Disclosed, inferred risk, none declared, or unknown |
| Scope | Population, task, tool, setting, period, and outcome |
| External validity | Main generalization boundaries |
| Replication | Independent, partial, failed, mixed, same-entity, or unavailable |
| Proposed routing | Flow A, Flow C, context only, hold, or reject |

Candidates must not disappear from the record because they are inconvenient, unfavorable, duplicated, or rejected. Deduplicate them while preserving the decision trail.

#### 13. Candidate Decision and Routing

Assign exactly one provisional outcome:

- `Accept for Flow A` — a new evidence object warrants registration and full review;
- `Route to Flow C` — an existing registered source has a newer, corrected, peer-reviewed, or superseding version;
- `Hold` — potentially relevant but awaiting access, clarification, comparison, or authoritative publication;
- `Context only` — useful for terminology, landscape, or interpretation but not accepted as evidence for a material claim;
- `Reject` — does not meet inclusion criteria or meets an exclusion criterion.

For each accepted candidate, state which repository claim it may support, weaken, contradict, replicate, or contextualize. Acceptance into Flow A is not permission to cite the source in the report.

#### 14. Independent Search Review

A second agent or reviewer that did not perform the primary search must independently:

- read the Search Strategy, Inclusion, and Exclusion criteria;
- rerun representative queries across more than one search channel;
- search specifically for omitted positive, negative, null, mixed, contradictory, replication, and critique evidence;
- verify a sample of excluded and held candidates;
- verify canonical versions and publication statuses;
- challenge Research Entity, Funding, Conflicts, Scope, External Validity, and Replication assessments;
- inspect Candidate Register completeness and deduplication;
- assess whether candidate routing follows the declared criteria.

Record one outcome:

- `Confirmed`;
- `Corrections required`;
- `Unresolved disagreement`;
- `Review unavailable`.

If corrections are required, update the search and Candidate Register, then repeat independent review. If disagreement remains or independent review is unavailable, escalate to the human user before accepting candidates.

For Flow E, Independent Search Review satisfies the repository-wide Independent Review requirement when it:

- reviews the complete Flow E output;
- is performed by a reviewer who did not conduct the primary search;
- uses the standard repository review outcomes;
- records the required review metadata.

A separate second reviewer is not required when the Independent Search Review already covers the complete Flow E output and meets these conditions.

Flow E is complete only when:

- the Search Strategy is recorded;
- Inclusion and Exclusion criteria are explicit;
- all screened candidates are traceable in the Candidate Register;
- canonical versions, publication status, research entity, funding, conflicts, scope, external validity, and replication are assessed for accepted candidates;
- candidate routing is explicit;
- Independent Search Review is `Confirmed`;
- unresolved disagreements and material omissions are absent.

Accepted new sources enter Flow A. Changed or superseding versions of registered sources enter Flow C. Flow E notes, abstracts, summaries, or Candidate Register entries do not substitute for registration, evidence review, an evidence brief, integration audit, or repository-wide verification.

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

When this check reveals a possible need to change report logic, a major conclusion, claim confidence, protocol logic, or a load-bearing repository map, follow the `Human Escalation` gate under `Repository Governance`.

### 7. Verify report integration

For every report use:

- explain what the source measured;
- link to the evidence brief;
- separate findings from repository inference;
- expose material limitations near the claim;
- remove inconsistent duplicate retellings;
- identify neighboring paragraphs and chapter conclusions that may require change.

A corrected citation is insufficient if the surrounding argument remains misleading.

For substantive report changes, apply `Safe vs Substantive Changes`, `Human Escalation`, and `Repository Change Proposal` under `Repository Governance`.

### 8. Verify README and repository maps

Reassess:

- executive summary;
- claim-confidence map;
- Evidence Map;
- Crisis Map and other diagrams;
- repository-level numeric claims;
- source coverage descriptions.

Multi-source diagrams must label source boundaries and must not present unrelated numbers as one measured causal chain.

For changes to load-bearing synthesis or claim confidence, apply `Safe vs Substantive Changes`, `Human Escalation`, and `Repository Change Proposal` under `Repository Governance`.

### 9. Verify protocol implications

Inspect every protocol for explicit or implicit reliance on the source. Document exactly one outcome:

- `No protocol change`
- `Protocol clarification`
- `Protocol change proposed`

Do not change a protocol merely for symmetry with a report change.

For a proposed protocol clarification or protocol change, apply `Safe vs Substantive Changes`, `Human Escalation`, and `Repository Change Proposal` under `Repository Governance`.

### 10. Synchronize records

After approved corrections:

- update the brief;
- update actual `Current use` locations in `evidence/SOURCES.md`;
- update the relevant evidence index;
- update `REFERENCES.md`;
- verify links;
- record superseded versions and removed claims.

## Repository Governance

### Independent Review

Every completed Flow A–E and every substantive repository change must be reviewed by a second agent or reviewer that did not produce the work.

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

### Human Escalation

Escalate before finalizing when:

- agents disagree on relevance, source quality, claim strength, calculation, or status;
- a source is ambiguous, inaccessible, superseded, or internally inconsistent;
- repository claims cannot be traced confidently;
- evidence suggests changing the current report logic, material argument, major conclusion, claim confidence, protocol logic, or load-bearing repository map;
- a correction would materially weaken, reverse, or remove a major conclusion;
- a new flow or material instruction change appears necessary;
- the independent reviewer reports unresolved doubt;
- the requested action conflicts with this file.

Present the decision needed, competing interpretations, supporting evidence, and practical consequences in the active interaction with the human user.

Implementation may begin only after the human user explicitly approves the substantive change.

### Repository Change Proposal

Before implementing any substantive change, prepare a Repository Change Proposal in the active interaction or in a dedicated proposal artifact when the change spans multiple review cycles.

The proposal must include:

- the current repository position or rule;
- the evidence, inconsistency, failure, or recurring need that triggered the proposal;
- the exact change proposed;
- reasonable alternatives, including preserving the current state;
- expected consequences for evidence briefs, report logic, protocols, maps, source statuses, workflows, and contributors;
- unresolved uncertainty and reversibility;
- the decision required from the human maintainer;
- the recommended next action.

A proposal is not approval. Apply the `Human Escalation` approval gate before implementation.

After approval, record the decision in the PR description, proposal artifact, or affected document so the rationale remains inspectable.

### Safe vs Substantive Changes

Classify every proposed repository edit before implementation.

Safe changes do not alter meaning, evidence interpretation, decision logic, status, or contributor obligations. Examples include:

- spelling, grammar, formatting, and broken-link fixes;
- exact synchronization of already-approved text or metadata;
- bibliography, index, and navigation maintenance that introduces no new claim;
- mechanical renaming or relocation with all references updated;
- correction of an objectively verifiable transcription error when no interpretation is required.

Safe changes may proceed without a separate Repository Change Proposal, but they still require normal verification and must not be used to disguise a substantive edit.

Substantive changes alter meaning, repository position, decision logic, confidence, obligations, or architecture. Examples include:

- report arguments, causal framing, major conclusions, or claim confidence;
- evidence interpretation, source scope, or repository inference;
- protocol controls, roles, thresholds, gates, or escalation rules;
- the Executive Summary, Crisis Map, Evidence Map, or other load-bearing synthesis;
- source-state definitions or verification requirements;
- repository architecture, primary flows, governance, or contributor obligations;
- removal or weakening of contradictory evidence or limitations.

For substantive changes, apply `Human Escalation`, `Repository Change Proposal`, and `Independent Review` in this section, and implement the approved change in a reviewable PR.

When classification is uncertain, treat the change as substantive and escalate.

## Workflow Evolution

User corrections, repeated execution failures, recurring repository inconsistencies, missing checks, new repository artifacts, and recurring manual clarifications are inputs to workflow evolution. They are not permission to edit governance automatically.

Use this decision path:

```text
User correction or recurring process signal
        ↓
Classify the observation
        ↓
Does an existing flow cover this work type?
        ├─ Yes
        │    ↓
        │  Was the existing flow followed correctly?
        │    ├─ No → execution error; follow and correct through the existing flow
        │    └─ Yes
        │         ↓
        │  Is a required step, check, transition, or completion condition missing?
        │    ├─ Yes → propose an extension to the existing flow
        │    └─ No
        │         ↓
        │  Is the current workflow ambiguous or internally inconsistent?
        │    ├─ Yes → propose clarification or restructuring
        │    └─ No → treat as a one-off preference or scope decision
        └─ No
             ↓
        Is this a new recurring work pattern with its own trigger,
        procedure, state transition, and completion condition?
             ├─ Yes → propose a new flow
             └─ No → treat as a one-off preference or unresolved boundary
             ↓
Apply Human Escalation and Repository Change Proposal
under Repository Governance
        ↓
Implement the approved AGENTS.md change in a reviewable PR
        ↓
Apply Independent Review under Repository Governance
        ↓
Merge and treat the new workflow as canonical
```

### 1. Classify the correction or signal

Use exactly one primary classification:

1. **Execution error** — the existing flow was adequate but was followed incorrectly.
2. **Missing step** — the existing flow lacks a necessary action, verification check, state transition, or completion condition.
3. **New recurring pattern** — a recurring work type has a distinct trigger, procedure, and completion condition not covered by current flows.
4. **Workflow ambiguity** — more than one reasonable interpretation of the current instruction exists, or two instructions conflict.
5. **Recurring repository inconsistency** — artifacts repeatedly drift because ownership, synchronization, or verification rules are incomplete.
6. **New repository artifact or boundary** — the current architecture does not define how a new artifact is created, reviewed, synchronized, or governed.
7. **One-off preference or scope decision** — the existing workflow does not need to change.

### 2. Test the existing workflow first

Before proposing a change:

- identify the current flow or gate that should govern the work;
- compare the observed failure with the written trigger, procedure, and completion conditions;
- determine whether the problem was non-compliance rather than missing governance;
- avoid adding a rule merely because one execution was poor;
- search for equivalent instructions elsewhere in `AGENTS.md` to avoid duplication or contradiction.

The existence of an applicable flow does not prove that the flow is complete. First determine whether the flow was followed. Then determine whether following it still exposed a missing step, missing check, ambiguous obligation, or incomplete completion condition.

An execution error should normally be corrected through the existing flow, not through new governance.

### 3. Decide whether to extend, add, or clarify

- **Extend an existing flow** when the trigger and completion condition remain the same but a necessary step or check is missing.
- **Add a new primary flow** only when the work has a distinct recurring trigger, procedure, state transition, and completion condition.
- **Clarify or restructure governance** when existing language permits multiple reasonable interpretations or creates inconsistent obligations.
- **Do not change the workflow** for one-off preferences, temporary scope choices, or failures caused by ignoring an adequate instruction.

When the signal does not justify a workflow change but remains unresolved, record the local scope decision explicitly. Do not silently generalize it into a repository-wide rule.

Cross-cutting controls such as independent review, human escalation, safe-versus-substantive classification, and constitutional principles must remain outside source-specific flows.

### 4. Apply Repository Governance

Use `Human Escalation` and `Repository Change Proposal` under `Repository Governance` before editing `AGENTS.md`. In the proposal, include the signal's classification, the existing flow or missing governance boundary, whether the proposal extends, adds, removes, or clarifies a rule, and any migration or synchronization work. The remaining proposal content and approval gate are defined only in `Repository Governance`.

### 5. Human decision before implementation

**Never update `AGENTS.md` silently.**

Discuss proposed workflow changes with the repository maintainer through `Human Escalation` and `Repository Change Proposal` under `Repository Governance`. A user correction, repeated failure, agent confidence, apparent improvement, or successful local experiment does not replace those gates or authorize a governance edit.

### 6. Implement and verify

After approval through `Repository Governance`:

- update `AGENTS.md` in a reviewable PR;
- update affected entry points only after the canonical rule is present;
- avoid unrelated governance cleanup in the same PR;
- document the trigger, classification, decision, and expected consequences in the PR;
- apply `Independent Review` under `Repository Governance` against the approved proposal and the Repository Constitution;
- do not treat the new workflow as canonical until the PR is merged.

If implementation exposes a materially different decision than the one approved, stop and return to the repository maintainer.

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
- [ ] Report arguments and nearby conclusions were assessed.
- [ ] Any substantive report, protocol, map, or governance change passed the applicable `Repository Governance` gates before implementation.
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
3. README or protocol changes, only when required and approved;
4. independent-review corrections, when required;
5. final verification-status update after all required changes exist on the default branch.

Do not set `Integration audit = Verified` until the default branch reflects the completed and independently confirmed state.
