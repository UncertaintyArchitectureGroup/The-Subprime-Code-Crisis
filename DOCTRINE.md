# Repository Doctrine

## Status and precedence

This document defines the content doctrine of *The Subprime Code Crisis*: how the repository separates evidence, interpretation, claims, scenarios, and operating practices.

[`AGENTS.md`](AGENTS.md) remains the canonical operating specification for workflows, approval gates, source states, verification, contributor obligations, and independent review. This doctrine does not override it, create an alternative workflow, or change evidence status.

[`GLOSSARY.md`](GLOSSARY.md) defines the repository's canonical vocabulary. [`SCOPE.md`](SCOPE.md) expands the repository's subject boundary. [`ARTIFACT_MODEL.md`](ARTIFACT_MODEL.md) provides the dedicated reader-facing map of artifact relationships defined by this doctrine. [`evidence/SOURCES.md`](evidence/SOURCES.md) remains the canonical source identity and status registry. Original sources remain authoritative for what they report.

## Repository philosophy

The repository treats AI-assisted coding as a change to a software-delivery system, not merely as a faster way to produce syntax.

Its purpose is to maintain an inspectable account of how local acceleration can interact with review, testing, security, architecture, release, operations, maintenance, incentives, and organizational control. The detailed subject boundary is maintained in [`SCOPE.md`](SCOPE.md).

The repository is therefore four things at once:

1. an evidence-governed research synthesis;
2. a structured systems argument;
3. an operational protocol library; and
4. an inspectable record of sources, interpretations, confidence, limitations, and change.

It is not an anti-AI manifesto, a vendor ranking, a prediction that every adoption will fail, or proof that every protocol is universally valid.

## Research principles

### 1. The delivery system is the unit of analysis

Code generation is one activity inside a larger system. The relevant outcome is not how quickly code-like output appears, but whether useful, understandable, secure, maintainable software moves through the complete delivery path.

### 2. Local productivity is not system throughput

An improvement at one step may increase queues, review load, rework, coordination cost, or maintenance exposure elsewhere. Local acceleration must not be presented as end-to-end improvement without downstream evidence.

### 3. Strong rhetoric does not strengthen evidence

The repository may use a direct practitioner voice, but tone cannot substitute for source quality, method, scope, or uncertainty. Claim strength must follow evidence strength.

### 4. Contradictory evidence is part of the model

Positive, negative, null, mixed, contradictory, replication, and limiting evidence must remain visible. The repository should become more accurate when challenged, not merely more persuasive.

### 5. The argument must remain falsifiable and correctable

Claims, mechanisms, maps, and protocols should be stated so that new evidence or implementation feedback can qualify, weaken, revise, or reject them.

### 6. Scope must remain explicit

A related topic belongs in the repository only when it directly supports the core research question and its relationship is bounded. Popularity, rhetorical usefulness, or general importance does not by itself make a topic in scope.

`SCOPE.md` expands this principle into explicit in-scope, out-of-scope, and adjacent-topic rules. Out of scope does not mean false or unimportant; it means the repository is not the appropriate place to establish or govern the topic.

## Evidence principles

### Original sources over summaries

Original papers, datasets, filings, standards, documentation, and first-party records are authoritative for what they report. Search snippets, media summaries, repository prose, and prior agent notes are navigation aids, not source ground truth.

### Source class does not equal source quality

Primary evidence may be weak, biased, preliminary, or narrow. Secondary evidence may be useful and rigorous. Classification describes the relationship to the underlying observation or record; it does not automatically determine confidence.

### Evidence review and integration audit are distinct

An evidence brief establishes what a source reports, how it was produced, and what it does not establish. An integration audit checks how that source is used throughout the repository. One cannot be inferred from the other.

### Evidence boundaries must remain visible

Every important use should preserve population, setting, period, tool, outcome, method, uncertainty, and external-validity limits where they materially affect interpretation.

### Numbers are claims

A number in prose, a table, a caption, or a diagram requires the same traceability and scope discipline as any other material factual statement.

## Interpretation principles

### Findings and repository interpretation are different artifacts

A source finding is what the source directly reports. A repository interpretation is the project's synthesis, systems inference, application, or bounded extrapolation from one or more sources and methods.

Repository interpretations must be labeled or written so that readers cannot reasonably mistake them for source-reported findings.

### Mechanisms are not automatically causal findings

The repository may propose mechanisms such as bottleneck migration, verification overload, deferred cost, or maintenance accumulation. Unless a source directly establishes the full causal chain, these remain systems interpretations or scenarios.

### Maps are explanatory models

Repository maps and summaries are bounded views over the underlying artifacts. They answer different questions and must not be treated as interchangeable scorecards or as one empirically measured causal sequence:

- the README's **repository map** routes readers to the relevant artifacts;
- the **Claim confidence map** assesses the class and current support of selected report claims;
- the **Evidence Map** classifies sources, repository interpretation, and protocols by role;
- the **Crisis Map** visualizes a proposed systems mechanism and bounded scenarios;
- protocol diagrams visualize operating controls and relationships.

No map or summary replaces the Source Registry, evidence briefs, report argument, or a protocol's documented controls, assumptions, and limits. When a claim is condensed, copied, or visualized, its class, scope, uncertainty, attribution, and source boundary must remain intact. A summary view must not silently strengthen a claim, convert repository synthesis into a source finding, or remove a limitation merely to improve readability.

### Confidence belongs to claims, not slogans

Claim confidence expresses the repository's current assessment of how strongly a specific conclusion is supported. It is not a probability, a permanent rating, or a substitute for reading the underlying evidence.

### Terminology must not smuggle in certainty

Terms such as *crisis*, *bubble*, *bankruptcy*, and *collapse* are analytical metaphors or scenarios unless explicitly supported as observed outcomes. The repository must state their status and boundaries.

## Protocol principles

### Protocols translate risk into operating practice

Protocols convert the repository's risk analysis into adaptable controls, roles, gates, metrics, disclosure practices, and escalation paths.

### Protocols are not empirical proof

A source may motivate a control without proving that a particular threshold, role, workflow, or escalation rule is universally correct.

### Controls must match local risk

Teams should adapt protocols to architecture, regulation, criticality, reversibility, delivery context, and available verification capacity.

### Controls must be observable and reversible

A useful protocol makes its intended outcome, signals, decision rights, exceptions, pause conditions, and feedback path inspectable.

### Implementation feedback returns to the evidence system

Operational experience may support, weaken, qualify, or redesign a protocol. Anecdotes should remain anecdotes; measured case studies should disclose context, methods, limitations, and confounders.

## Claim boundaries

The repository distinguishes the following claim and interpretation classes:

| Class | Meaning | Appropriate use |
| --- | --- | --- |
| **Empirical finding** | Directly reported result from an empirical source | Describe the measured result within the source's scope and current review status |
| **Documented fact** | Statement contained in a first-party documentary source | Describe what an organization, standard, filing, or public record states |
| **Derived result** | Reproducible calculation from reported values without a new causal claim | Make the calculation and its assumptions inspectable |
| **Evidence-backed inference** | Repository conclusion supported by one or more relevant findings but not directly measured end to end | Explain a bounded implication and preserve source boundaries |
| **Systems inference** | Interpretation based on system structure, theory, and available evidence | Propose a mechanism without presenting it as directly observed |
| **Risk scenario** | Plausible adverse trajectory requiring further validation | Support monitoring, control design, and contingency planning |
| **Warning scenario** | Lower-confidence, high-consequence scenario used to expose potential failure | Communicate urgency while explicitly denying prediction or observed status |

A claim must not be silently relabeled as more directly evidenced or more certain when copied into a summary, map, protocol, presentation, or social post.

## Repository artifact model

The repository separates a core flow of evidence, interpretation, claims, and operating response:

```text
External source material
        ↓
Source Registry
        ↓
Evidence briefs
        ↓
Repository interpretation
        ↓
Report claims and synthesis
        ↓
Operational protocols
        ↓
Implementation feedback and new evidence
```

The Claim confidence map and explanatory maps assess, classify, or visualize report claims; they are cross-cutting views rather than mandatory sequential stages between the report and protocols.

The dedicated [`ARTIFACT_MODEL.md`](ARTIFACT_MODEL.md) expands this model with artifact purposes, boundaries, relationship rules, and reader navigation. It is subordinate to this doctrine and does not create an evidence layer, workflow, source state, or claim.

## Change discipline

The doctrine should evolve only when the repository's content model, scope principles, claim boundaries, or artifact relationships genuinely change. Editorial preferences and one-off wording decisions do not justify doctrine expansion.

Any substantive doctrine change remains subject to the approval and independent-review requirements in [`AGENTS.md`](AGENTS.md).
