# Evidence Library

> **Navigation:** [Home](../README.md) | [Doctrine](../DOCTRINE.md) | [Glossary](../GLOSSARY.md) | [Source Registry](SOURCES.md) | [Report](../report/01_the_illusion.md) | [Protocols](../protocols/README.md) | [References](../REFERENCES.md)

This directory separates empirical and documentary sources from the report's interpretation and from the repository's operational protocols.

The goal is not to flatten every source into a single confidence level. Different materials answer different questions and support different kinds of claims.

Canonical definitions for evidence classes, evidence briefs, repository interpretation, evidence review, and integration audit are maintained in [`GLOSSARY.md`](../GLOSSARY.md). Their content boundaries are defined in [`DOCTRINE.md`](../DOCTRINE.md).

## Evidence classes

### [Primary empirical research](primary/README.md)

Original studies, working papers, controlled experiments, and large-scale observational analyses that directly report methods and results.

Use these sources for claims about measured effects. Record publication status, dataset, method, directly observed findings, model-derived estimates, and limitations.

### [Primary documentary sources](documentary/README.md)

First-party records such as annual filings, standards, official documentation, and published engineering-system descriptions.

Use these sources for factual records and institutional descriptions, not as independent proof of causal effects.

### [Secondary evidence](secondary/README.md)

Industry reports, practitioner analyses, replications, reviews, surveys, and other materials that synthesize or interpret primary data.

Use these sources for triangulation and context, not as substitutes for an available primary source.

### [Theory and methodology](methodology/README.md)

Analytical frameworks used to interpret evidence, such as production theory, bottleneck analysis, and software-productivity frameworks.

These sources structure reasoning but do not directly measure the effects of AI coding tools unless they also contain empirical analysis.

### [Datasets](datasets/README.md)

Public or documented datasets used by cited research or maintained for independent analysis.

Dataset entries should describe provenance, coverage, transformations, access conditions, and the claims the data can and cannot support.

## Canonical registry

[`SOURCES.md`](SOURCES.md) is the canonical registry for every source.

It tracks two separate states:

- **Evidence review** — whether a source-oriented brief exists and is current.
- **Integration audit** — whether every use of the source across the report, README, diagrams, references, and protocols has been checked.

A source is fully processed only when:

```text
Evidence review = Reviewed brief
Integration audit = Verified
```

The existence of a brief does not imply verified integration.

## Relationship to the rest of the repository

- `DOCTRINE.md` defines the research, evidence, interpretation, protocol, and claim-boundary principles.
- `GLOSSARY.md` defines canonical repository vocabulary.
- `report/` contains the Subprime Code Crisis argument and synthesis.
- `protocols/` contains operational responses and decision rules.
- `evidence/` contains source-oriented briefs that distinguish reported findings from repository interpretation.
- `evidence/SOURCES.md` contains classification, review status, integration status, verification date, and current use.
- `REFERENCES.md` is the compact bibliography and navigation index.
- `AGENTS.md` defines the mandatory source-processing and integration-verification procedure.

`AGENTS.md` has precedence for workflow and status. The doctrine and glossary do not change source state or establish evidence.

## Evidence brief standard

Each evidence brief should include:

1. Full citation and canonical links.
2. Source ID.
3. Publication status and version.
4. Research question or documentary purpose.
5. Dataset, population, period, comparator, and methodology where applicable.
6. Directly observed or documented findings.
7. Derived or model-calibrated findings.
8. Source-author interpretation.
9. Repository interpretation.
10. What the source does not establish.
11. Limitations, conflicts, and external-validity risks.
12. Repository locations using the source.
13. A `Repository integration audit` section matching the status in `SOURCES.md`.
14. An `Independent review` section matching the outcome required by `AGENTS.md`.

Use the canonical meanings in [`GLOSSARY.md`](../GLOSSARY.md); do not treat a repository interpretation as a source finding or a reviewed brief as verified integration.

Use this audit template:

```markdown
## Repository integration audit

- Integration status: Not started | In progress | Corrections required | Verified | Needs re-verification
- Repository search completed:
- Report mentions checked:
- Numeric claims checked:
- README claims and diagrams checked:
- Protocol outcome: No protocol change | Protocol clarification | Protocol change proposed
- Corrections made:
- Current-use locations confirmed:
- Verification date:
```

Use this independent-review template:

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

## Interpretation labels

The canonical definitions are in [`GLOSSARY.md`](../GLOSSARY.md). Use these labels where useful:

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

`Verified` requires the complete repository-wide procedure in `AGENTS.md`, synchronized status in the brief and `SOURCES.md`, a `Confirmed` independent-review outcome, and a recorded verification date.
