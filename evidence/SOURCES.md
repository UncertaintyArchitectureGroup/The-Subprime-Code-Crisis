# Source Registry

This file is the canonical registry for external material used by the repository.

`REFERENCES.md` is the compact human-readable bibliography. Evidence subdirectories contain source-oriented briefs. This registry records both evidence-review status and repository-integration status for every source.

A source is fully processed only when:

- **Evidence review** is `Reviewed brief`; and
- **Integration audit** is `Verified`.

These are separate states. Creating a brief does not prove that every report claim, number, diagram, reference, and protocol implication has been checked.

## Evidence-review status

- **Registered** — the source is known to the repository but no brief is complete.
- **Brief in progress** — active review is underway.
- **Reviewed brief** — a source-oriented brief exists and records methods, findings, limitations, and repository interpretation.
- **Needs re-review** — the source changed, was superseded, or requires material correction.

Documentary and methodology sources use the same review lifecycle. Their briefs evaluate records or frameworks rather than empirical effects.

## Integration-audit status

- **Not started** — no repository-wide source integration audit has been performed.
- **In progress** — repository mentions, numbers, arguments, diagrams, references, and protocol implications are being checked.
- **Corrections required** — the audit found unresolved problems.
- **Verified** — the complete procedure in `AGENTS.md` has been completed and all required corrections have been integrated.
- **Needs re-verification** — a source version, repository claim, diagram, or relevant protocol changed after the last verification.

`Last verified` is the date on which the integration audit reached `Verified`. Leave it as `—` for every other status.

## Primary empirical research

| ID | Source | Evidence review | Integration audit | Last verified | Can support | Current use |
| --- | --- | --- | --- | --- | --- | --- |
| **P-2026-01** | Demirer, Musolff & Yang, *Writing Code vs. Shipping Code: Productivity Effects Across Generations of AI Coding Tools*, NBER Working Paper 35275 | [Reviewed brief](primary/2026-writing-code-vs-shipping-code.md) | Verified | 2026-07-27 | Measured attenuation from coding activity toward projects, releases, and early marketplace use within the studied setting | `README.md` Crisis Map and evidence boundary; `report/01_the_illusion.md`; `report/02_broken_mechanics.md` |
| **P-2025-01** | METR, *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity* | Registered | Not started | — | Randomized evidence about experienced developers completing familiar open-source tasks with early-2025 tools | Report claims about experienced-developer task completion |
| **P-2025-02** | METR, *Measuring AI Ability to Complete Long Tasks* | Registered | Not started | — | Agent task-completion performance as task duration increases under the study's benchmark design | Agent capability and task-horizon discussion |
| **P-2025-03** | Xu et al., *AI-Assisted Programming Decreases the Productivity of Experienced Developers* | Registered | Not started | — | Large-scale developer-output and review-load associations reported by the authors | Senior-load and productivity discussion |
| **P-2026-02** | Agarwal et al., *AI IDEs or Autonomous Agents? Measuring the Impact of Coding Agents* | Registered | Not started | — | Reported static-analysis and code-structure differences in the study sample | Complexity and quality-risk discussion |
| **P-2023-01** | Peng et al., *The Impact of AI on Developer Productivity* | Registered | Not started | — | Controlled evidence of task-completion acceleration in a bounded greenfield task | Positive productivity evidence and boundary conditions |
| **P-2025-04** | GitClear, *AI Assistant Code Quality 2025 Research* | Registered | Not started | — | Original commercial measurement of code-change patterns, subject to methodology and conflict review | Churn, duplication, and reuse discussion |
| **P-2025-05** | GitClear, *How Much More Productive Are AI-Powered Developers?* | Registered | Not started | — | Original commercial productivity measurement, subject to methodology and conflict review | Net-output and rework discussion |

## Primary documentary sources

| ID | Source | Evidence review | Integration audit | Last verified | Can support | Current use |
| --- | --- | --- | --- | --- | --- | --- |
| **D-2019-01** | *Software Engineering at Google* and associated first-party engineering documentation | Registered | Not started | — | Descriptions of Google's engineering infrastructure and practices | Infrastructure and verification-capacity discussion |
| **D-2024-01** | Alphabet annual filings | Registered | Not started | — | Alphabet-reported capital expenditure and business records | AI infrastructure-spending discussion |
| **D-2024-02** | Meta annual filings | Registered | Not started | — | Meta-reported capital expenditure and business records | AI infrastructure-spending discussion |
| **D-2024-03** | Microsoft annual filings | Registered | Not started | — | Microsoft-reported capital expenditure and business records | AI infrastructure-spending discussion |

## Secondary evidence and industry context

| ID | Source | Evidence review | Integration audit | Last verified | Can support | Current use |
| --- | --- | --- | --- | --- | --- | --- |
| **S-2025-01** | Deloitte, *State of Generative AI in the Enterprise* | Registered | Not started | — | Surveyed enterprise adoption, expectations, and reported constraints | Adoption and organizational-context discussion |
| **S-2025-02** | McKinsey enterprise AI reporting, currently linked through a third-party summary | Registered | Not started | — | Context only until the original McKinsey publication is identified, registered, and reviewed | Market-sentiment discussion |
| **S-2025-03** | Artur Markus, *The Inference Cost Paradox* | Registered | Not started | — | Practitioner interpretation of enterprise AI spending and Jevons-style effects | Cost-paradox discussion |
| **S-2026-01** | Andreas Horn, *The Most Important Chart in AI* | Registered | Not started | — | Practitioner framing and visual interpretation | Market and capability narrative context |
| **S-2025-04** | SoftwareSeni, *Why AI Coding Speed Gains Disappear in Code Reviews* | Registered | Not started | — | Practitioner synthesis about review bottlenecks | Review-bottleneck framing |
| **S-2025-05** | TechnoDiaries, *Post-Copilot Burnout* | Registered | Not started | — | Practitioner reporting and hypothesis generation | Senior-bottleneck and burnout context |

## Theory and methodology

| ID | Source | Evidence review | Integration audit | Last verified | Can support | Current use |
| --- | --- | --- | --- | --- | --- | --- |
| **M-1984-01** | Eliyahu M. Goldratt, *The Goal: A Process of Ongoing Improvement* | Registered | Not started | — | Theory of Constraints concepts such as bottlenecks, inventory, and local optimization | Delivery-system interpretation throughout the report |

## Datasets

Dataset-level entries should be added to `datasets/README.md` when the repository independently uses, republishes, or analyzes a dataset. Datasets merely described inside an evidence brief do not need a separate registry entry unless they become reusable repository assets.

Dataset registry entries must use the same `Evidence review`, `Integration audit`, and `Last verified` fields.

## Registry maintenance rules

1. Register a source before adding it to the report.
2. Set `Evidence review` to `Reviewed brief` only after a source-oriented brief exists and is indexed.
3. Set `Integration audit` to `Verified` only after completing every step in the **Integration-audit procedure** in `AGENTS.md`.
4. Never infer `Verified` from the existence of a brief, citation, or prior PR.
5. Record the verification date only when the status becomes `Verified`.
6. If a source version changes, set `Evidence review` to `Needs re-review` and `Integration audit` to `Needs re-verification` until both procedures are rerun.
7. If a report claim, README diagram, or protocol materially relying on a source changes, set its integration status to `Needs re-verification`.
8. A pending brief may support provisional or low-load claims, but strong claims should link to a reviewed brief.
9. Replace secondary links with original sources whenever possible.
10. Keep `Current use` synchronized with actual repository usage discovered during the audit.
11. Preserve contradictory, null, mixed, and positive evidence; classification and status are independent of whether a source supports the repository thesis.
