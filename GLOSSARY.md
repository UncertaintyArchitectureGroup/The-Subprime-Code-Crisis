# Glossary

## Status and use

This glossary defines the canonical meaning of recurring terms used by *The Subprime Code Crisis* repository.

It standardizes language; it does not provide empirical evidence, change source status, or override [`AGENTS.md`](AGENTS.md). Where a source uses a term differently, preserve the source's meaning and identify the difference.

When introducing a project-defined term in a report, protocol, evidence brief, diagram, or public summary, link to this glossary where practical and preserve the claim boundary defined in [`DOCTRINE.md`](DOCTRINE.md).

## Terms

### Bottleneck migration

A **systems inference** that acceleration or automation at one stage shifts the effective delivery constraint to another stage, such as review, testing, security validation, architecture, release, operations, or maintenance.

Bottleneck migration is not automatically a source-reported causal finding. It must be bounded by the evidence and local system context.

### Claim confidence

The repository's current assessment of how strongly a specific claim is supported by the available evidence and reasoning.

Claim confidence:

- applies to claims, not sources;
- is not a numerical probability unless explicitly modeled;
- may change when evidence, scope, or interpretation changes; and
- does not replace the underlying source review.

### Delivery system

The end-to-end socio-technical system that turns an intended change into operated and maintained software.

It includes task selection, requirements, design, implementation, review, testing, security, architecture, integration, release, production operation, maintenance, people, incentives, tools, policies, and decision rights.

### Documentary source

A first-party record used to establish what an organization, standard, filing, product, public record, or documented system states.

Examples include regulatory filings, official documentation, standards, organizational records, and dated public publications. Documentary sources can establish records and statements; they do not automatically prove causal effects or independent validity.

### Documented fact

A statement directly contained in an authoritative first-party documentary source.

A documented fact establishes that the record says or reports something. It does not necessarily establish that the statement is complete, unbiased, causal, or independently confirmed.

### Derived result

A calculation reproduced from source-reported values without introducing an additional causal claim.

The inputs, formula, units, assumptions, and rounding should remain inspectable.

### Empirical finding

A result directly reported by an empirical source from its observed data or analysis.

An empirical finding must remain bounded by the source's population, setting, period, tools, methods, outcomes, uncertainty, and publication status.

### Evidence-backed inference

A repository conclusion supported by relevant empirical or documentary evidence but not directly measured as a complete end-to-end result by one source.

It is stronger than a theory-only interpretation but must not be described as a direct finding.

### Evidence brief

A source-oriented review that records a source's identity, version, publication status, question or purpose, methods, findings, calculations, author interpretation, repository interpretation, limitations, external-validity boundaries, and repository use.

An evidence brief reviews the source. It does not by itself establish that every repository use has been checked.

### Evidence review

The process and status dimension concerned with understanding and documenting the source itself.

A completed evidence review may produce a **Reviewed brief**. It remains separate from the **Integration audit**.

### Independent conceptual convergence

The possibility that different authors independently develop similar terminology, metaphors, or conclusions while examining related conditions, without documented derivation from one another.

In this repository, the term is used for provenance framing, not as proof that influence was impossible. See [`TERMINOLOGY_AND_ATTRIBUTION.md`](TERMINOLOGY_AND_ATTRIBUTION.md).

### Integration audit

The repository-wide check of every material use of a source, including claims, numbers, diagrams, summaries, references, protocol implications, source status, and `Current use` records.

An integration audit answers whether the source is used correctly across the repository. It is distinct from evidence review and cannot be inferred from the existence of an evidence brief or merged PR.

### Local productivity

Improvement measured within a bounded activity or stage, such as code generation speed, task completion, accepted suggestions, commits, or developer-reported time savings.

Local productivity does not by itself establish better end-to-end delivery throughput, reliability, maintainability, or total engineering economics.

### Model-calibrated result

An estimate produced by a fitted, simulated, or calibrated model rather than directly observed as a raw outcome.

The model, assumptions, calibration data, uncertainty, and validation limits should be visible.

### Observed

Directly reported from empirical measurement or inspection in the cited source.

The label does not mean universal, causal, replicated, or free from measurement error.

### Primary evidence

An umbrella term for material closest to the original observation or authoritative record.

In this repository it includes:

- **primary empirical research**, which directly reports methods and measured results; and
- **primary documentary sources**, which provide first-party records.

Primary does not automatically mean strong, unbiased, peer reviewed, or broadly generalizable.

### Production attenuation

The reduction in translation from upstream coding activity to downstream project, release, adoption, or marketplace outcomes.

The repository uses the term most directly for the bounded pattern reported in P-2026-01, where increased upstream activity attenuated toward downstream outcomes in the studied setting. Broader uses must be labeled as repository interpretation rather than treated as a universal measured law.

### Protocol

An adaptable operating pattern that translates identified risks into controls, roles, signals, gates, decision rights, escalation paths, or feedback loops.

A protocol is not empirical proof or universal policy. Its suitability depends on local risk, architecture, regulation, reversibility, and verification capacity.

### Repository interpretation

The project's synthesis, application, systems inference, or bounded extrapolation from one or more sources, methods, and delivery-system concepts.

A repository interpretation is authored by the project and must remain distinguishable from an empirical finding, documented fact, or source-author interpretation.

### Risk scenario

A plausible adverse trajectory used to explore what may happen under specified conditions and to motivate monitoring, controls, or contingency planning.

A risk scenario is not a prediction or an observed industry-wide outcome.

### Secondary evidence

Material that synthesizes, interprets, surveys, reviews, or reports on primary evidence or practitioner experience.

Examples include reviews, industry surveys, practitioner analyses, reporting, and commentary. Secondary evidence can provide triangulation and context but should not replace an accessible primary source for load-bearing factual claims.

### Source-author interpretation

The explanation, implication, or conclusion offered by the authors of an external source beyond its directly reported observations or records.

It should be attributed to the source authors and not silently converted into either an empirical finding or a repository conclusion.

### Source Registry

[`evidence/SOURCES.md`](evidence/SOURCES.md), the canonical inventory for source identity, classification, evidence-review status, integration-audit status, verification date, support boundaries, and actual repository use.

It is not a bibliography or narrative synthesis.

### Subprime Code Bubble

A repository risk metaphor for a growing inventory of plausible and valuable-looking code whose verification, integration, maintenance, and operational costs are deferred or transferred downstream.

It is a risk model and analytical metaphor, not a measured market quantity or claim that every AI-generated change is defective.

### Systems inference

A repository interpretation based on system structure, theory, and available evidence rather than on a directly measured end-to-end causal result.

Examples include bottleneck migration, verification-capacity mismatch, and deferred-cost accumulation when the full mechanism has not been observed in one study.

### Technical Bankruptcy

A **warning scenario** in which accumulated technical debt, verification deficits, lost system understanding, and maintenance burden materially reduce an organization's ability to change software safely and economically.

The repository does not present Technical Bankruptcy as an empirically observed industry-wide final outcome. It is more severe than ordinary technical debt and should remain explicitly labeled as a scenario or hypothesis.

### Throughput

The rate at which useful, verified, releasable, and maintainable change moves through the complete delivery system.

Raw code volume, suggestion acceptance, commits, or task completion are not equivalent to throughput unless the downstream boundary is defined and measured.

### Verification capacity

The available human, automated, organizational, and infrastructural ability to understand, review, test, secure, integrate, release, operate, and maintain candidate changes.

Verification capacity includes not only test execution but also architecture judgment, context, accountability, and exception handling.

### Warning scenario

A lower-confidence, high-consequence form of risk scenario used to expose a possible systemic failure that warrants attention or controls.

A warning scenario must be clearly distinguished from an empirical finding, forecast, or assertion that the outcome is inevitable.

## Usage rule

Do not use a stronger term merely because it is more memorable. In particular:

- do not replace **repository interpretation** with **finding**;
- do not replace **risk scenario** with **prediction**;
- do not replace **warning scenario** with **observed outcome**;
- do not equate **local productivity** with **throughput**; and
- do not equate **Reviewed brief** with **Verified integration**.
