# The Subprime Code Crisis

![crisis_cover](assets/crisis_cover.png)

**An independent research synthesis on AI-assisted software delivery risk**

**Our research thesis: AI coding tools have changed the capacity to produce candidate software faster than delivery systems have adapted their ability to select, understand, verify, integrate, operate and obtain value from it. This imbalance calls for reassessing the whole SDLC.**

**Primary author:** [Vitalii Oborskyi](https://www.linkedin.com/in/vitaliioborskyi) · **Project:** [Uncertainty Architecture Group](https://github.com/UncertaintyArchitectureGroup)

> **Navigation:** [Read the Report](report/01_the_illusion.md) | [Hypotheses](report/appendices/mechanism-hypotheses.md) | [Evidence Library](evidence/README.md) | [Operational Protocols](protocols/README.md) | [Live Work Plan](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/84)

## The research thesis

The unit of analysis is the complete software-delivery lifecycle:

**Intent → requirements → design → code → review → test → integration → deployment → operation → realized user outcomes → business economics → feedback to Intent.**

These are recurring functions, not a mandatory waterfall. AI can change several of them. The proposed mechanism is that faster candidate production can increase admitted work faster than complementary capability adapts. Under those conditions, local gains may become waiting, rework or obligations that surface later. Rebalancing means finding the actual constraint and testing a useful response: better automation, clearer intent, smaller changes, stronger capability, less unnecessary work or retaining an already adequate process.

Each node contributes more than an artifact. It also supplies decisions, learning, coordination, understanding, ownership and feedback. **[Review is both a quality gate and an ownership gate](report/appendices/mechanism-hypotheses.md#review--rev-1-and-rev-2):** the receiving team needs to assess the change and be able to explain, diagnose, modify and recover the system. An approval click does not establish those abilities. The research compares all relevant outcomes with the actual previous process, whose strengths and weaknesses must also be measured.

The purpose is **useful software for users, sustainable team capability and justified lifecycle cost and risk**. More code or releases do not by themselves establish user benefit, competitive advantage or ROI. Delivering the same useful service at lower cost can also be a gain. The [canonical hypothesis register](report/appendices/mechanism-hypotheses.md#the-thesis-and-the-outcome-that-matters) separates the premise, mechanisms, consequences and remedies, with observations that could support or weaken each.

## Quick Start

| Need | Start here |
| --- | --- |
| Read the argument in order | [1. Evidence and Delivery Outcomes](report/01_the_illusion.md) → [2. Verification and Delivery Mechanisms](report/02_broken_mechanics.md) → [3. Scenarios and Adoption Decisions](report/03_the_aftermath.md) |
| Examine a particular SDLC function or challenge the thesis | [Hypothesis register](report/appendices/mechanism-hypotheses.md), its [node index](report/appendices/mechanism-hypotheses.md#node-index), and the [evaluation method](governance/hypothesis-evaluation.md) |
| Trace a claim to its source and processing state | [Evidence Library](evidence/README.md), [Source Registry](evidence/SOURCES.md), and [References](REFERENCES.md) |
| Inspect the economic assumptions and reproduce the illustrative calculation | [Appendices and analytical tools](#appendices-and-analytical-tools) |
| Apply practical controls | [Operational Protocols](protocols/README.md) |
| Understand the research and reasoning boundaries | [Scope](SCOPE.md), [Doctrine](DOCTRINE.md), and [Artifact Model](ARTIFACT_MODEL.md) |
| Contribute evidence, a correction or implementation feedback | [`AGENTS.md`](AGENTS.md), [Contributing](CONTRIBUTING.md), and [governance playbooks](governance/README.md) |

The [live master work plan #84](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/84) owns the work sequence and dependencies. The working cycle is one approved issue through review, merge and verification, followed by a plan checkpoint and approval of the next issue. New inputs enter through [Issues](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues); the [issue workflow](governance/issue-workflow.md) explains intake and completion. The [backlog audit](governance/issue-backlog-audit.md) is a dated snapshot, and the [repository ownership map](governance/repository-map.md) identifies related projects.

## Key Takeaways

1. **Empirical finding:** AI tools can accelerate isolated coding work.
2. **Systems inference:** Local code-generation speed does not guarantee end-to-end software-delivery throughput.
3. **Systems hypothesis:** Additional admitted work may strain a downstream stage when effective capacity and work policies cannot absorb it; successful adaptation can preserve useful gains.
4. **Repository risk framing:** Delivery risk depends on task selection, tool behavior, verification capacity and deployment choices.
5. **Proposed practice:** Assess the delivery system and adjust controls where evidence identifies a gap; reuse adequate existing capability.

The current evidence supports parts of this argument. [September NBER](evidence/primary/2026-writing-code-vs-shipping-code.md) reports positive release gains alongside larger coding-activity gains in selected cohorts. [Chen–Stratton](evidence/primary/2026-chen-stratton-firm-production.md) adds a distinct firm setting with positive agent coding-activity estimates, a smaller uncertain tracked-completion estimate and changes in review-process measures. The [register's evidence assessment](report/appendices/mechanism-hypotheses.md#existing-evidence-and-its-exact-coverage) preserves positive, negative, null and context-dependent findings.

**The complete causal chain remains a research hypothesis.** Independently identified capacity shortfalls, lost understanding, persistent debt, exhaustion, higher TCO and the effectiveness of proposed remedies each require their own evidence. Elapsed merge time does not measure active review labor or ownership. The [claim boundaries](DOCTRINE.md#claim-boundaries) and [Repository Scope](SCOPE.md) distinguish source findings, repository inference and conditional scenarios.

## Repository Map

| Area | Purpose | Start here |
| --- | --- | --- |
| **Report** | Evidence, conditional delivery mechanisms, alternative scenarios and adoption decisions | [Part 1](report/01_the_illusion.md), [Part 2](report/02_broken_mechanics.md), [Part 3](report/03_the_aftermath.md) |
| **Hypotheses and appendices** | Complete node outcomes, falsifiable propositions, source context and inspectable calculations | [Hypothesis register](report/appendices/mechanism-hypotheses.md) and [appendix guide](#appendices-and-analytical-tools) |
| **Evidence** | Source registry, evidence taxonomy, source-oriented briefs, limitations, and integration status | [Evidence Library](evidence/README.md) |
| **Protocols** | Adaptable controls for engineers, teams, public evidence, and organizations | [Operational Protocols](protocols/README.md) |
| **Scope and Doctrine** | Subject boundaries, evidence principles, claim boundaries, and reasoning rules | [Scope](SCOPE.md) and [Doctrine](DOCTRINE.md) |
| **Artifact Model and Glossary** | Repository structure, artifact relationships, and canonical terminology | [Artifact Model](ARTIFACT_MODEL.md) and [Glossary](GLOSSARY.md) |
| **Governance and work plan** | Workflows, approval, source states, verification, synchronization, independent review and current priorities | [`AGENTS.md`](AGENTS.md), [governance playbooks](governance/README.md), and [live plan #84](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/84) |
| **Citation and attribution** | Repository citation metadata, terminology provenance, and attribution boundaries | [`CITATION.cff`](CITATION.cff) and [Terminology & Attribution](TERMINOLOGY_AND_ATTRIBUTION.md) |
| **History and review records** | Material evolution, dated assessments and inspectable work records | [Changelog](CHANGELOG.md), [dated reviews](governance/reviews/), and [work records](governance/work-records/) |

`AGENTS.md` governs repository work. The Doctrine governs content principles and claim boundaries. Scope and the Artifact Model expand those boundaries for readers. The Glossary governs recurring repository vocabulary. None of these documents overrides original source evidence or the canonical source-state rules.

### Appendices and analytical tools

| Material | What to use it for |
| --- | --- |
| [SDLC hypothesis register](report/appendices/mechanism-hypotheses.md) | Thesis, complete node-function inventories, current evidence coverage, alternatives, weakening observations and proposed remedy tests |
| [Cost context](report/appendices/cost-context.md) | Historical company records, market estimates and budget intentions, with their accounting and inference boundaries |
| [Conditional cost sensitivity](report/appendices/tco-sensitivity.md) | A hypothetical pilot-cost example with declared assumptions; it is not an empirical TCO estimate or ROI calculation |
| [Model inputs](report/appendices/tco-scenarios.json), [reproduced results](report/appendices/tco-results.json), and [calculator](tools/tco_sensitivity.py) | Inspect and reproduce the illustrative arithmetic using the appendix's [reproduction instructions](report/appendices/tco-sensitivity.md#reproduction-and-validation) |

## Claim confidence map

The **Claim confidence map** evaluates selected repository conclusions: what kind of claim each statement is and how strongly the current evidence supports it. It does not classify sources.

| Claim                                                                                          | Type                      | Confidence  |
| ---------------------------------------------------------------------------------------------- | ------------------------- | ----------- |
| AI tools can accelerate isolated coding tasks                                                  | Empirical finding         | High        |
| Local code generation speed does not guarantee SDLC throughput                                 | Systems inference         | High        |
| Additional admitted work may strain downstream verification under the stated conditions | Systems inference | Conditional; stage and prevalence not established |
| Unresolved verification or maintenance work may accumulate under the stated conditions | Risk scenario | Conditional; magnitude and prevalence not established |
| Industry-wide “technical bankruptcy” under aggressive cost-cutting adoption models | Warning scenario | Not estimated; no calibrated probability |

Canonical definitions for these claim types are maintained in the [Glossary](GLOSSARY.md); their use is governed by the [Repository Doctrine](DOCTRINE.md#claim-boundaries).

The debt-risk row describes a [conditional local scenario](report/03_the_aftermath.md#local-delivery-deterioration), not a measured debt balance or probability. Rework and structural metrics motivate investigation; they do not alone establish persistent maintenance burden. Test accumulation and recovery over a defined period alongside useful delivery, total effort and quality.

## 🧾 Evidence Map

The **Evidence Map** classifies materials by role. It answers a different question from the Claim confidence map: not *how confident are we in a claim?*, but *what kind of source, interpretation, or operational artifact is this?*

Browse the [Evidence Library](evidence/README.md) through its class indexes: [primary empirical research](evidence/primary/README.md), [primary documentary sources](evidence/documentary/README.md), [secondary evidence](evidence/secondary/README.md), [theory and methodology](evidence/methodology/README.md), and [datasets](evidence/datasets/README.md). The coverage below points to the briefs behind the report; source-processing states remain in the [Source Registry](evidence/SOURCES.md).

| Layer | Purpose | Current coverage in this repository |
| --- | --- | --- |
| **Primary empirical research: coding and delivery** | Original task and delivery studies with inspectable methods and results | [NBER: September revision, positive releases and bounded attenuation](evidence/primary/2026-writing-code-vs-shipping-code.md); [Peng bounded Copilot experiment](evidence/primary/2023-copilot-task-productivity.md); [METR early-2025 task-time RCT](evidence/primary/2025-metr-experienced-developer-productivity.md) and [2026 follow-up with identification limits](evidence/primary/2026-metr-productivity-design-update.md); [METR v1 long-task methods and verification limits](evidence/primary/2025-metr-task-horizon.md) |
| **Primary empirical research: firm production and review** | Firm-level activity, tracked completion and review-process estimates | [Chen–Stratton, August 2026 (P-2026-04)](evidence/primary/2026-chen-stratton-firm-production.md): positive agent coding-activity estimates, a smaller uncertain Jira-completion estimate, longer PR submission-to-merge elapsed time, and more formal change requests, comments and reviewer participation. Observational design and pre-period movements constrain causality; earlier assistant estimates differ. These measures establish neither active review labor nor competent ownership. See the [hypothesis assessment](report/appendices/mechanism-hypotheses.md#e-chen-stratton) |
| **Primary empirical research: activity and structure** | Observational activity, rework and structural measures with source-specific boundaries | [Xu OSS activity/rework with proxy and uncertainty limits](evidence/primary/2025-xu-copilot-oss-activity.md); [Agarwal adoption-mode activity/structure estimates](evidence/primary/2026-agarwal-agent-adoption.md); [GitClear historical code-change/clone signals](evidence/primary/2025-gitclear-code-quality.md) and [separate developer-output measures](evidence/primary/2025-gitclear-developer-output.md) |
| **Primary empirical research: spending and reported outcomes** | Market estimates, adoption and respondent reports, distinct from measured delivery effects | [Menlo market-size estimates](evidence/primary/2025-menlo-enterprise-ai-spend.md) and [CloudZero budget intentions](evidence/primary/2025-cloudzero-ai-budget-intentions.md), distinct from delivery outcomes; [McKinsey 2025 adoption/value](evidence/primary/2025-mckinsey-ai-adoption-value.md), [Deloitte Q4 reported ROI/scaling expectations](evidence/primary/2025-deloitte-genai-q4.md) and [Stack Overflow 2024 attitudes](evidence/primary/2024-stackoverflow-ai-attitudes.md), distinct respondent-reported outcomes |
| **Primary documentary sources** | First-party records used for infrastructure, spending, organizational, and terminology-provenance claims | [Alphabet CY2024](evidence/documentary/2024-alphabet-financial-context.md), [Meta CY2024](evidence/documentary/2024-meta-financial-context.md) and [Microsoft FY2024](evidence/documentary/2024-microsoft-financial-context.md) company-wide filings; [Google historical engineering practices](evidence/documentary/2020-google-engineering-practices.md); [Microsoft FY25Q2 AI-business run rate](evidence/documentary/2025-microsoft-fy25q2-ai-run-rate.md), distinct from Copilot revenue/customer ROI; [terminology provenance records](evidence/documentary/terminology-provenance.md); [project-analysis provenance](evidence/documentary/project-provenance.md) |
| **Secondary evidence and industry context** | Reviews, practitioner analyses, and synthesis used for context without treating them as independent measurements | [Techno Diaries single accessible anecdote](evidence/secondary/2025-technodiaries-review-anecdote.md); Horn’s personal [capability forecast](evidence/secondary/2026-horn-capability-commentary.md) and [engineering commentary](evidence/secondary/2026-horn-engineering-commentary.md); [Markus cost commentary](evidence/secondary/2026-inference-cost-commentary.md); [SoftwareSeni discovery/correction record](evidence/secondary/2025-softwareseni-review-synthesis.md), without live report/protocol use |
| **Theory and methodology** | Frameworks used to interpret delivery-system behavior rather than to measure AI effects directly | [Goldratt/Cox methodology and original-access gap](evidence/methodology/1984-the-goal.md) |
| **Datasets** | Documented data sources and datasets used by cited studies or future independent analysis | [Dataset registry](evidence/datasets/README.md); GitHub activity and marketplace datasets documented in cited studies |
| **Repository interpretation** | The Subprime Code Crisis synthesis: bottleneck migration, production attenuation, risk scenarios, and system-level implications | [Report](report/01_the_illusion.md), [hypothesis register](report/appendices/mechanism-hypotheses.md), [Claim confidence map](#claim-confidence-map), and [Crisis Map](#-the-crisis-map) |
| **Protocols** | Practical responses, controls, metrics, and decision rules derived from the risk analysis | [Operational Protocols](protocols/README.md) |

The canonical source inventory and status registry is [`evidence/SOURCES.md`](evidence/SOURCES.md). [`REFERENCES.md`](REFERENCES.md) is a compact bibliography and navigation aid. The [Artifact Model](ARTIFACT_MODEL.md) explains the complete relationship among sources, briefs, interpretation, claims, protocols, and feedback.

## 📊 The Crisis Map

The Crisis Map is an **explanatory systems synthesis**, not a chronology, an evidence scorecard, or a causal chain measured by one study. Each node states its claim type. Solid arrows show the repository's proposed system mechanism; they do not imply that one population, tool, period, or metric was followed from end to end.

```mermaid
flowchart TD
    classDef empirical fill:#d9edf7,stroke:#31708f,stroke-width:2px;
    classDef synthesis fill:#eeeeee,stroke:#555,stroke-width:2px;
    classDef scenario fill:#f2dede,stroke:#a94442,stroke-width:2px,stroke-dasharray: 5 5;

    A["AI-assisted generation: synthesis starting condition"]
    B["Lower cost of candidate output: repository synthesis"]
    C["Higher upstream activity: September estimates, P-2026-01"]
    D["Capacity may not scale proportionally: repository synthesis"]
    E["Review, QA, security or architecture constraint: risk hypothesis"]
    F["Rework and maintenance exposure: conditional risk synthesis"]
    G["Accumulated delivery-system risk: repository synthesis"]
    H["Technical Bankruptcy: warning scenario and repository hypothesis"]

    A --> B
    B --> D
    C -->|empirical support for upstream-growth premise| D
    D -->|If admitted demand strains effective capacity| E
    E -->|"If context loss or inadequate checks add work or defects"| F
    F -->|"If costs persist beyond recovery and adaptation"| G
    E -->|"Effective adaptation"| I
    D -->|Headroom, controlled intake or useful assistance| I["Useful gains with stable quality: alternative synthesis outcome"]
    G -. possible scenario, not an observed outcome .-> H

    class C empirical;
    class A,B,D,E,F,G,I synthesis;
    class H scenario;
```

### Evidence boundary for the map

- **P-2026-01, September 2026 revision:** selected public GitHub tool cohorts, matched event studies and agent-authored interrupted time series. Coding and release estimates are positive, with outcome-specific populations, uncertainty and magnitude sensitivity. Separate marketplace series use three early-usage proxies, including modest Android growth; SourceForge contributes only an entry comparison. The [brief](evidence/primary/2026-writing-code-vs-shipping-code.md) pins the original and keeps older versions as history. These data support bounded attenuation, not identification of a particular verification stage.
- The capacity branch depends on admitted work/risk mix, effective capacity, utilization/variation and WIP/release policy. Headroom and successful adaptation may produce useful gains. The [SDLC hypothesis register](report/appendices/mechanism-hypotheses.md) contains the full function/outcome inventory and retains the [earlier claim graph and tests](report/appendices/mechanism-hypotheses.md#claim-classes-and-permitted-edges). These are repository synthesis with separate trigger, endpoint and net-benefit tests; they assign no scenario probabilities.
- The arrows after the empirical node are **repository synthesis, not one measured causal chain**. P-2026-01 does not establish general code-quality decline, review as the only bottleneck, technical debt, security effects, or Technical Bankruptcy.
- **Technical Bankruptcy** remains a warning scenario and repository hypothesis, not an empirically measured outcome. The adverse branch ends in **Accumulated delivery-system risk**; useful gains and recovery remain possible.

The Doctrine defines why these maps remain bounded views rather than substitutes for evidence, report argument, or source status.

## 🛡️ Operational Response

The repository organizes its practical response as a four-layer control stack:

| Layer | Protocol | Primary question |
| --- | --- | --- |
| **Engineer** | [Personal Defense](protocols/01_personal_defense.md) | What verification is required before generated output changes durable code, data, or operations? |
| **Team** | [Operational Defense](protocols/02_operational_defense.md) | Is local acceleration improving or degrading delivery-system outcomes? |
| **Public evidence** | [Public Evidence and Disclosure](protocols/03_public_defense.md) | What can be claimed, with what support, limitations, and correction path? |
| **Organization** | [Organizational Control Model](protocols/04_systemic_cure.md) | Who owns adoption policy, capacity, exceptions, escalation, and learning? |

These are adaptable operating patterns, not universal thresholds or empirical proof. Teams should adapt them to local risk, architecture, regulation, and delivery constraints, then return measured implementation feedback to the evidence system.

## Project provenance

The public records for this repository's own analysis are documented separately from phrase history. The [2026-01-05 DOU precursor](https://dou.ua/forums/topic/57244/) by Vitalii Oborskyi discusses generation/review asymmetry and downstream delivery constraints. The [2026-02-10 Subprime Code publication](https://dou.ua/forums/topic/57846/) attributes its follow-up investigation to work on that article and reader discussion. This is the author's documented continuity account, not independent empirical validation. GitHub records repository-object creation at `2026-02-06T17:16:44Z`; it does not establish when the repository became public. The currently inspected February-dated DOU page links the repository, but the link's insertion date and historical public-opening time remain unestablished.

See the [project provenance brief](evidence/documentary/project-provenance.md) and [Terminology & Attribution](TERMINOLOGY_AND_ATTRIBUTION.md) for the source record and boundaries. This chronology documents development of this project's delivery-system synthesis; it is **not** a claim that the repository invented the general phrase **Subprime Code Crisis** or that similar work elsewhere was derived from it.

## Citation, Attribution, and History

> Oborskyi, Vitalii, and contributors. *The Subprime Code Crisis: An Independent Research Synthesis on AI-Assisted Software Delivery Risk*. Uncertainty Architecture Group, 2026. https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis

Use [`CITATION.cff`](CITATION.cff) with GitHub's **Cite this repository** function. When reusing a specific diagram, report chapter, evidence brief, or protocol, cite that artifact in addition to the repository. See [Terminology & Attribution](TERMINOLOGY_AND_ATTRIBUTION.md) for name provenance and contribution boundaries, and [Changelog](CHANGELOG.md) for selected material history.

This repository does not claim ownership of, or exclusive authorship over, the phrase **Subprime Code Crisis**. Its attributable contribution is the evidence-governed delivery-system synthesis, claim boundaries, risk mechanism, maps, and operational protocols.

---
*License: [CC-BY-SA 4.0](LICENSE.md)*
