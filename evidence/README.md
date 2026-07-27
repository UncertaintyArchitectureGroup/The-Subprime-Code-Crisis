# Evidence Library

This directory separates empirical and documentary sources from the report's interpretation and from the repository's operational protocols.

The goal is not to flatten every source into a single confidence level. Different materials answer different questions and support different kinds of claims.

## Evidence classes

### [Primary empirical research](primary/README.md)

Original studies, working papers, controlled experiments, and large-scale observational analyses that directly report methods and results.

Use these sources for claims about measured effects. Record publication status, dataset, method, directly observed findings, model-derived estimates, and limitations.

### [Primary documentary sources](documentary/README.md)

First-party records such as annual filings, standards, official documentation, and published engineering-system descriptions.

Use these sources for factual records and institutional descriptions, not as independent proof of causal effects.

### [Secondary evidence](secondary/README.md)

Industry reports, practitioner analyses, replications, reviews, surveys, and materials that synthesize or interpret primary data.

Use these sources for triangulation and context, not as substitutes for an available primary source.

### [Theory and methodology](methodology/README.md)

Analytical frameworks used to interpret evidence, such as production theory, bottleneck analysis, and software-productivity frameworks.

These sources structure reasoning but do not directly measure AI-tool effects unless they also contain empirical analysis.

### [Datasets](datasets/README.md)

Public or documented datasets used by cited research or maintained for independent analysis.

Dataset entries should describe provenance, coverage, transformations, access conditions, and the claims the data can and cannot support.

## Canonical registry

[`SOURCES.md`](SOURCES.md) is the canonical inventory and status database for every source.

It tracks two separate states:

- **Evidence review** — whether a source-oriented brief exists and is current.
- **Integration audit** — whether every use of the source across the report, README, diagrams, references, and protocols has been checked.

A source is fully processed only when:

```text
Evidence review = Reviewed brief
Integration audit = Verified
```

The existence of a brief does not imply verified integration.

## Source flows

[`AGENTS.md`](../AGENTS.md) defines five distinct flows:

- **Flow A** — add a new source;
- **Flow B** — process a legacy registered source;
- **Flow C** — update a changed or superseded source;
- **Flow D** — re-verify repository content that relies on a verified source;
- **Flow E** — search systematically for newer or missing evidence.

Flow E never bypasses evidence review. Every selected new source returns to Flow A.

## Relationship to the rest of the repository

- `report/` contains the Subprime Code Crisis argument and synthesis.
- `protocols/` contains operational responses and decision rules.
- `evidence/` contains source-oriented briefs.
- `evidence/SOURCES.md` contains classification, review status, integration status, verification date, and current use.
- `REFERENCES.md` is the compact bibliography.
- `AGENTS.md` defines the mandatory source flows and verification procedure.

## Evidence brief standard

Each evidence brief should include:

1. Full citation and canonical links.
2. Source ID.
3. Publication status and exact version.
4. Research question or documentary purpose.
5. Dataset, population, period, comparator, and methodology where applicable.
6. Directly observed or documented findings.
7. Derived or model-calibrated findings.
8. Source-author interpretation.
9. Repository interpretation.
10. What the source does not establish.
11. Limitations, conflicts, and external-validity risks.
12. Repository locations using the source.
13. A `Repository integration audit` section matching `SOURCES.md`.

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

## Interpretation labels

Use these labels where useful:

- **Observed:** directly reported from empirical analysis.
- **Documented:** stated in an authoritative first-party record.
- **Derived:** calculated from reported results without adding a new causal claim.
- **Model-calibrated:** produced by a fitted or calibrated model rather than directly measured.
- **Source-author interpretation:** interpretation offered by the source authors.
- **Repository interpretation:** the Subprime Code Crisis project's synthesis or application.
- **Not established:** a plausible claim that the source does not itself demonstrate.

## Completion rule

Do not mark a source `Verified` merely because:

- a brief exists;
- a citation was added;
- a PR was merged;
- a report paragraph was corrected.

`Verified` requires the complete integration-audit procedure in `AGENTS.md`, a claim-to-source trace, synchronized status in the brief and `SOURCES.md`, and a recorded verification date after all required changes exist on the default branch.
