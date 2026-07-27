# Evidence review playbook

This playbook is a mandatory procedural extension of [`AGENTS.md`](../AGENTS.md) for evidence review in Flows A–C. `AGENTS.md` is canonical and has precedence; resolve conflicts in its favor. Read it in full before this playbook. Evidence review establishes source ground truth; it does not verify repository integration.

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

## Source acquisition and assessment

- Obtain and read the original, canonical source whenever accessible; repository summaries and search snippets are not substitutes. Preserve materially different version links and dates.
- Confirm the exact publication state and version. Verify peer-review claims through the publisher or venue when practical; a DOI or repository upload alone does not establish peer review.
- Record the research or documentary purpose, methodology/design, dataset, population, selection, period, comparator, unit of analysis, outcomes, and metric definitions.
- Record directly observed/documented findings separately from derived calculations and model-calibrated estimates. Reproduce simple calculations where practical and state inputs, formulas, assumptions, units, and uncertainty.
- Separate source-author interpretation from repository interpretation and explicitly state what the source does not establish.
- Record limitations and conflicts. When relevant, record funding and employer/tool/data support. Separate documented conflicts from repository inference; do not imply misconduct without evidence.
- Assess external-validity boundaries, including representativeness, task realism, duration/lifecycle coverage, unit-of-analysis generalization, participant experience, tool/version dependence, selection/novelty effects, and geographic/organizational/regulatory scope.

## Completion checklist

- [ ] Correct original and canonical version read.
- [ ] Identity, publication status, source class, canonical URL, and version history recorded.
- [ ] Method, scope, dataset/population/period/comparator, metrics, and uncertainty recorded.
- [ ] Findings, calculations, source-author interpretation, repository interpretation, and unsupported claims separated.
- [ ] Limitations, conflicts, external-validity risks, and relevant funding/support recorded.
- [ ] Known repository uses recorded without assuming completeness.
- [ ] Brief contains `Repository integration audit` and `Independent review` sections.
- [ ] Brief indexed and `Evidence review = Reviewed brief`.
- [ ] Integration state remains separate and is not inferred from brief completion.
