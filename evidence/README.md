# Evidence Library

This directory separates empirical sources from the report's interpretation and from the repository's operational protocols.

The goal is not to flatten every source into a single confidence level. Different materials answer different questions and support different kinds of claims.

## Evidence classes

### [Primary empirical research](primary/README.md)
Original studies, working papers, controlled experiments, and large-scale observational analyses that directly report methods and results.

Use these sources for claims about measured effects. Record the publication status, dataset, method, directly observed findings, model-derived estimates, and limitations.

### [Secondary evidence](secondary/README.md)
Industry reports, practitioner analyses, replications, reviews, and other materials that synthesize or interpret primary data.

Use these sources for triangulation and context, not as substitutes for the underlying study when the primary source is available.

### [Datasets](datasets/README.md)
Public or documented datasets used by cited research or maintained for independent analysis.

Dataset entries should describe provenance, coverage, known transformations, access conditions, and the claims the data can and cannot support.

## Relationship to the rest of the repository

- `report/` contains the Subprime Code Crisis argument and synthesis.
- `protocols/` contains operational responses and decision rules.
- `evidence/` contains source-oriented briefs that distinguish reported findings from repository interpretation.
- `REFERENCES.md` remains the compact bibliography and navigation index.

## Evidence brief standard

Each evidence brief should include:

1. Full citation and source links.
2. Publication status, including whether the work is peer reviewed.
3. Research question and scope.
4. Dataset and methodology.
5. Directly observed findings.
6. Model-calibrated or derived findings.
7. Interpretation relevant to this repository.
8. What the source does not establish.
9. Limitations and external-validity risks.
10. Links to any local source copy retained in the repository.

## Interpretation labels

Use these labels where useful:

- **Observed:** directly reported from the study's empirical analysis.
- **Derived:** calculated from reported results without adding a new causal claim.
- **Model-calibrated:** produced by a fitted or calibrated model rather than directly measured.
- **Repository interpretation:** the Subprime Code Crisis project's synthesis or application of the evidence.
- **Not established:** a plausible claim that the source does not itself demonstrate.
