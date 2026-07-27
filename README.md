# The Subprime Code Crisis
![crisis_cover](assets/crisis_cover.png)


# An independent research synthesis on AI-assisted software delivery risk

How AI code assistants can create local productivity gains while shifting cost into review, QA, security, architecture, maintenance, and production stability.

>**Navigation:**  [📉 **Read the Report**](report/01_the_illusion.md) | [🧾 **Evidence Library**](evidence/README.md) | [🛡️ **Operational Protocols**](protocols/README.md) | [📚 **References**](REFERENCES.md) | [📊 **Contributing Data**](CONTRIBUTING.md)

## Research framing

This repository is an independent research synthesis on AI-assisted software delivery risk.

It aggregates public empirical studies, industry reports, and delivery-system analysis to examine one core hypothesis:

AI-assisted coding can create local productivity gains while shifting cost into downstream delivery constraints such as code review, QA, security validation, architecture, maintenance, and production stability.

This is not an argument against AI-assisted development. The goal is to prevent poor adoption models from creating technical debt, organizational backlash, and loss of trust in a genuinely important technology.

The report is written in a strong practitioner voice, but its claims should be read across three levels:

- evidence-backed findings;
- system-level inferences;
- risk scenarios requiring further validation.

## What this is

This is a delivery-system risk analysis of AI-assisted software development.

It focuses on what happens when organizations treat faster code generation as equivalent to faster software delivery, without rebalancing the surrounding system: code review, QA, security validation, architecture, deployment, maintenance, and governance.

## What this is not

This is not a claim that AI coding tools are useless.

This is not an argument against AI-assisted software development.

This is not a prediction that every organization will fail.

This is not a rejection of developer productivity gains in isolated tasks.

It is a warning that local acceleration does not automatically become system-level throughput.


## Executive Summary

AI code assistants are powerful tools, but their current adoption model is often incomplete.

Most enterprise rollouts measure local productivity gains: faster code generation, faster task completion, more output per developer. But software delivery is not limited by typing speed. In mature engineering organizations, the real constraints often sit downstream: code review, testing, security validation, architecture, deployment, maintenance, and production stability.

This report argues that unmanaged AI-assisted coding can create a Subprime Code Bubble: a growing volume of plausible, syntactically valid, but insufficiently reviewed and poorly integrated code that shifts cost into the future.

The risk is not caused by AI alone. It emerges from the collision of two forces:

1. Tool behavior: AI code assistants reduce the effort required to generate code-like output, but they do not reduce the verification burden at the same rate.
2. Market behavior: organizations often adopt AI tools as productivity multipliers without redesigning the operating model around the increased output flow.

The result is a dangerous mismatch: code generation scales faster than the organization’s capacity to review, test, understand, secure, and maintain that code.

The alternative is not to reject AI-assisted development. The alternative is to govern it as a delivery-system change.

## Claim confidence map

The **Claim confidence map** evaluates the repository's conclusions: what kind of claim each statement is and how strongly the current body of evidence supports it. It does not classify sources.

| Claim                                                                                          | Type                      | Confidence  |
| ---------------------------------------------------------------------------------------------- | ------------------------- | ----------- |
| AI tools can accelerate isolated coding tasks                                                  | Empirical finding         | High        |
| Local code generation speed does not guarantee SDLC throughput                                 | Systems inference         | High        |
| AI-assisted coding can shift bottlenecks into review, QA, security, and maintenance            | Evidence-backed inference | Medium-High |
| Unmanaged adoption may inflate technical debt                                                  | Risk scenario             | Medium      |
| Industry-wide “technical bankruptcy” is possible under aggressive cost-cutting adoption models | Warning scenario          | Medium-Low  |

## 🧾 Evidence Map

The **Evidence Map** classifies the materials used to build those claims. It answers a different question from the Claim confidence map: not *how confident are we in a claim?*, but *what kind of source, interpretation, or operational artifact is this?*

The table below is a repository-level map, not a replacement for the canonical source inventory and status registry in [`evidence/SOURCES.md`](evidence/SOURCES.md). [`REFERENCES.md`](REFERENCES.md) remains a compact human-readable bibliography and navigation aid.

| Layer | Purpose | Current coverage in this repository |
| --- | --- | --- |
| **Primary empirical research** | Original studies and measurement reports with inspectable methods and results | [NBER: Writing Code vs. Shipping Code](evidence/primary/2026-writing-code-vs-shipping-code.md); METR developer-productivity RCT and long-task measurement; Xu et al. large-scale developer study; Agarwal et al. code-structure analysis; Peng et al. Copilot RCT; GitClear code-change and productivity measurement reports |
| **Primary documentary sources** | First-party records used for infrastructure, spending, and organizational claims | Alphabet, Meta, and Microsoft filings; official product and engineering documentation; published engineering-system descriptions |
| **Secondary evidence and industry context** | Reviews, surveys, practitioner analyses, and synthesis used for triangulation or context | DORA reports; McKinsey and Deloitte enterprise surveys; SoftwareSeni review analysis; TechnoDiaries practitioner reporting; Andreas Horn industry commentary |
| **Theory and methodology** | Frameworks used to interpret delivery-system behavior rather than to measure AI effects directly | Goldratt's Theory of Constraints; software-engineering productivity frameworks; weak-link and production-hierarchy reasoning |
| **Datasets** | Documented data sources and datasets used by cited studies or future independent analysis | [Dataset registry](evidence/datasets/README.md); GitHub activity and marketplace datasets documented in cited studies |
| **Repository interpretation** | The Subprime Code Crisis synthesis: bottleneck migration, production attenuation, risk scenarios, and system-level implications | [Report](report/01_the_illusion.md), Claim confidence map, and the Crisis Map below |
| **Protocols** | Practical responses, controls, metrics, and decision rules derived from the risk analysis | [Operational protocols](protocols/README.md) |

```mermaid
flowchart LR
    P[Primary Empirical Research<br/>Measured effects]
    F[Primary Documentary Sources<br/>Filings and first-party records]
    S[Secondary Evidence<br/>Surveys, reviews, industry context]
    T[Theory and Methodology<br/>Interpretive frameworks]
    D[Datasets<br/>Provenance and coverage]
    I[Repository Interpretation<br/>Subprime Code Crisis synthesis]
    C[Claim Confidence Map<br/>Claim type and support level]
    R[Report Claims<br/>Findings, inferences, scenarios]
    O[Protocols<br/>Operational responses]

    D --> P
    P --> I
    F --> I
    S --> I
    T --> I
    I --> C
    C --> R
    R --> O

    P -. claim boundaries .-> R
    O -. implementation feedback .-> I
```

The evidence flow is intentionally directional:

1. **Sources report findings, records, or context.**
2. **The repository interprets those materials.**
3. **The Claim confidence map labels the resulting claims and their current support level.**
4. **The report develops bounded findings, inferences, and risk scenarios.**
5. **Protocols translate those risks into operating practices.**

A protocol is therefore not empirical proof, a repository interpretation is not a finding directly reported by a source, and a confidence rating is not a source category. Detailed classification rules and evidence-brief standards are documented in the [Evidence Library](evidence/README.md). The canonical source inventory and status registry is [`evidence/SOURCES.md`](evidence/SOURCES.md); [`REFERENCES.md`](REFERENCES.md) is the compact human-readable bibliography and navigation aid.

## 📊 The Crisis Map

The Crisis Map is an **explanatory systems synthesis**, not a chronology, an evidence
scorecard, or a causal chain measured by one study. Each node states its claim type.
Solid arrows show the repository's proposed system mechanism; they do not imply that
one population, tool, period, or metric was followed from end to end.

```mermaid
flowchart TD
    classDef empirical fill:#d9edf7,stroke:#31708f,stroke-width:2px;
    classDef inference fill:#fcf8e3,stroke:#8a6d3b,stroke-width:2px;
    classDef synthesis fill:#eeeeee,stroke:#555,stroke-width:2px;
    classDef scenario fill:#f2dede,stroke:#a94442,stroke-width:2px,stroke-dasharray: 5 5;

    A[AI-assisted generation<br/><b>Repository synthesis: starting condition</b>]
    B[Lower cost of producing code-like output<br/><b>Evidence-backed inference</b>]
    C[Higher upstream coding activity in studied settings<br/><b>Empirical finding: P-2026-01</b>]
    D[Verification capacity may not scale proportionally<br/><b>Repository synthesis</b>]
    E[Review / QA / security / architecture bottlenecks<br/><b>Repository synthesis: risk mechanism</b>]
    F[More rework, uncertainty, and maintenance exposure<br/><b>Repository synthesis: conditional risk</b>]
    G[Accumulated delivery-system risk<br/><b>Repository synthesis</b>]
    H[Technical Bankruptcy<br/><b>Warning scenario / repository hypothesis</b>]

    A --> B --> C --> D --> E --> F --> G
    G -. possible scenario, not an observed outcome .-> H

    class C empirical;
    class B inference;
    class A,D,E,F,G synthesis;
    class H scenario;
```

### Evidence boundary for the map

- **P-2026-01** is a 2022–2026 observational matched event study of more than
  100,000 developers, supplemented by Microsoft telemetry and four application
  marketplaces. It reports increased upstream activity after adoption of successive
  AI-tool generations and attenuation toward projects and releases. The map does not
  reproduce its percentages because they refer to distinct outcomes, samples, and
  specifications; see the [reviewed evidence brief](evidence/primary/2026-writing-code-vs-shipping-code.md).
- The arrows after the empirical node are **repository synthesis, not a single
  measured causal chain**. P-2026-01 does not establish general code-quality decline,
  review as the only bottleneck, technical debt, security effects, or Technical
  Bankruptcy.
- The former `+50%`, `+131%`, `8x`, `x2`, and `-19%` nodes have been removed. They
  came from different sources, populations, periods, units, and metric definitions;
  placing them in sequence overstated what the combined evidence measured.
- **Technical Bankruptcy** remains only as a warning scenario and repository
  hypothesis. It is not an empirically measured final outcome. The map's final
  synthesis outcome is **Accumulated delivery-system risk**.
## How to read this report

This report is intentionally written for engineering leaders, senior developers, architects, QA leaders, delivery managers, and AI adoption decision-makers.

It can be read in three ways:

- As a warning about unmanaged AI-assisted coding adoption.
- As a delivery-system analysis of bottleneck migration.
- As a starting point for engineering governance patterns around AI-generated code.

Readers looking for the evidence base should start with the [Evidence Library](evidence/README.md), use the canonical [Source Registry](evidence/SOURCES.md) for inventory and status, and use [References](REFERENCES.md) as the compact human-readable bibliography and navigation aid.

Readers looking for immediate operating practices should start with the [Operational Protocols](protocols/README.md).
## 📂 Report Structure

The analysis is divided into three parts, covering the data, the mechanics of the failure, and the projected economic outcomes.

*   **[Part 1: The Illusion](report/01_the_illusion.md)**
    *   **Ch 1: The Great Illusion.** Why we feel faster but deliver slower (Analysis of METR, Xu et al. & GitClear).
    *   **Ch 2: The Missing Price Tag.** The invisible infrastructure costs (30-120x multiplier) required to make AI safe.
    *   **Ch 3: The "Free Lunch" Trap.** Why Boards choose a strategy of degradation (The Execution Mandate).
    *   **Ch 4: Anatomy of the Break.** How the "Safe Scenario" kills the SDLC (Theory of Constraints applied to AI).
*   **[Part 2: Broken Mechanics](report/02_broken_mechanics.md)**
    *   **Ch 5:** The death of Code Review and the "Senior Penalty."
    *   **Ch 6:** A Case Study in Complexity (Why AI Agents won't fix the mess).
    *   **Ch 7:** The chain reaction across the Value Stream (Product, QA, Maintenance).
*   **[Part 3: The Aftermath](report/03_the_aftermath.md)**
    *   **Ch 8:** The Paradox of Local Solutions.
    *   **Ch 9:** End Game Scenarios: The Crash vs. The Slow Rot.
    *   **Ch 10:** The Architecture of Unintended Consequences.

## 🛡️ Risk Mitigation

The repository's operational response is organized as a four-layer control stack:

```mermaid
flowchart LR
    A[Engineer<br/>Boundaries and verification]
    --> B[Team<br/>Metrics, gates, escalation]
    --> C[Public evidence<br/>Disclosure and correction]
    --> D[Organization<br/>Ownership, policy, capacity]
```

| Layer | Protocol | Primary question |
| --- | --- | --- |
| **Engineer** | [Personal Defense](protocols/01_personal_defense.md) | What generated output may cross into durable code, and under what verification? |
| **Team** | [Operational Defense](protocols/02_operational_defense.md) | Is local acceleration improving or degrading delivery-system outcomes? |
| **Public evidence** | [Public Evidence and Disclosure](protocols/03_public_defense.md) | What can be claimed, with what support, limitations, and correction path? |
| **Organization** | [Systemic Cure](protocols/04_systemic_cure.md) | Who owns adoption policy, capacity, exceptions, escalation, and learning? |

These are practical operating patterns, not universal thresholds or empirical proof. Teams should adapt them to local risk, architecture, regulation, and delivery constraints, then feed implementation results back into the evidence base.

👉 **[ACCESS OPERATIONAL PROTOCOLS](protocols/README.md)**

---
*License: CC-BY-SA 4.0*
