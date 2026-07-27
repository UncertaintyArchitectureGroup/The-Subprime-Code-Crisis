# Source Registry

This file is the canonical registry for external material used by the repository.

`REFERENCES.md` is the compact human-readable bibliography. Evidence subdirectories contain reviewed briefs. This registry records classification and review status for every source, including sources whose briefs are still pending.

## Status values

- **Reviewed brief** — a source-oriented brief exists and has been integrated with explicit limitations.
- **Registered; brief pending** — the source is used or proposed, but the full evidence brief has not yet been completed.
- **Documentary entry** — the source supports a factual record rather than an empirical effect estimate.
- **Methodology entry** — the source provides an interpretive framework rather than direct evidence of AI effects.

## Primary empirical research

| ID | Source | Status | Can support | Current use |
| --- | --- | --- | --- | --- |
| **P-2026-01** | Demirer, Musolff & Yang, *Writing Code vs. Shipping Code: Productivity Effects Across Generations of AI Coding Tools*, NBER Working Paper 35275 | [Reviewed brief](primary/2026-writing-code-vs-shipping-code.md) | Measured attenuation from coding activity toward projects, releases, and early marketplace use within the studied setting | `report/01_the_illusion.md`; `report/02_broken_mechanics.md` |
| **P-2025-01** | METR, *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity* | Registered; brief pending | Randomized evidence about experienced developers completing familiar open-source tasks with early-2025 tools | Report claims about experienced-developer task completion |
| **P-2025-02** | METR, *Measuring AI Ability to Complete Long Tasks* | Registered; brief pending | Agent task-completion performance as task duration increases under the study's benchmark design | Agent capability and task-horizon discussion |
| **P-2025-03** | Xu et al., *AI-Assisted Programming Decreases the Productivity of Experienced Developers* | Registered; brief pending | Large-scale developer-output and review-load associations reported by the authors | Senior-load and productivity discussion |
| **P-2026-02** | Agarwal et al., *AI IDEs or Autonomous Agents? Measuring the Impact of Coding Agents* | Registered; brief pending | Reported static-analysis and code-structure differences in the study sample | Complexity and quality-risk discussion |
| **P-2023-01** | Peng et al., *The Impact of AI on Developer Productivity* | Registered; brief pending | Controlled evidence of task-completion acceleration in a bounded greenfield task | Positive productivity evidence and boundary conditions |
| **P-2025-04** | GitClear, *AI Assistant Code Quality 2025 Research* | Registered; brief pending | Original commercial measurement of code-change patterns, subject to methodology and conflict review | Churn, duplication, and reuse discussion |
| **P-2025-05** | GitClear, *How Much More Productive Are AI-Powered Developers?* | Registered; brief pending | Original commercial productivity measurement, subject to methodology and conflict review | Net-output and rework discussion |

## Primary documentary sources

| ID | Source | Status | Can support | Current use |
| --- | --- | --- | --- | --- |
| **D-2019-01** | *Software Engineering at Google* and associated first-party engineering documentation | Documentary entry; brief pending | Descriptions of Google's engineering infrastructure and practices | Infrastructure and verification-capacity discussion |
| **D-2024-01** | Alphabet annual filings | Documentary entry; brief pending | Alphabet-reported capital expenditure and business records | AI infrastructure-spending discussion |
| **D-2024-02** | Meta annual filings | Documentary entry; brief pending | Meta-reported capital expenditure and business records | AI infrastructure-spending discussion |
| **D-2024-03** | Microsoft annual filings | Documentary entry; brief pending | Microsoft-reported capital expenditure and business records | AI infrastructure-spending discussion |

## Secondary evidence and industry context

| ID | Source | Status | Can support | Current use |
| --- | --- | --- | --- | --- |
| **S-2025-01** | Deloitte, *State of Generative AI in the Enterprise* | Registered; brief pending | Surveyed enterprise adoption, expectations, and reported constraints | Adoption and organizational-context discussion |
| **S-2025-02** | McKinsey enterprise AI reporting, currently linked through a third-party summary | Registered; replacement primary link required | Context on reported adoption and impact; not load-bearing until the original report is linked and reviewed | Market-sentiment discussion |
| **S-2025-03** | Artur Markus, *The Inference Cost Paradox* | Registered; brief pending | Practitioner interpretation of enterprise AI spending and Jevons-style effects | Cost-paradox discussion |
| **S-2026-01** | Andreas Horn, *The Most Important Chart in AI* | Registered; brief pending | Practitioner framing and visual interpretation | Market and capability narrative context |
| **S-2025-04** | SoftwareSeni, *Why AI Coding Speed Gains Disappear in Code Reviews* | Registered; brief pending | Practitioner synthesis about review bottlenecks | Review-bottleneck framing |
| **S-2025-05** | TechnoDiaries, *Post-Copilot Burnout* | Registered; brief pending | Practitioner reporting and hypothesis generation | Senior-bottleneck and burnout context |

## Theory and methodology

| ID | Source | Status | Can support | Current use |
| --- | --- | --- | --- | --- |
| **M-1984-01** | Eliyahu M. Goldratt, *The Goal: A Process of Ongoing Improvement* | Methodology entry; brief pending | Theory of Constraints concepts such as bottlenecks, inventory, and local optimization | Delivery-system interpretation throughout the report |

## Datasets

Dataset-level entries should be added to `datasets/README.md` when the repository independently uses, republishes, or analyzes a dataset. Datasets merely described inside an evidence brief do not need a separate registry entry unless they become reusable repository assets.

## Registry maintenance rules

1. Register a source before adding it to the report.
2. Do not mark a source `Reviewed brief` until a source-oriented brief exists.
3. A pending brief may support provisional or low-load claims, but strong claims should link to a reviewed brief.
4. Replace secondary links with original sources whenever possible.
5. When publication status or source content changes, update this registry, the brief, report usage, and `REFERENCES.md` together.
6. Preserve contradictory and negative evidence; classification is independent of whether a source supports the repository thesis.