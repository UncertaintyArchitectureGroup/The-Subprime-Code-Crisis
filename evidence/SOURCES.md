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
| **P-2026-01** | Demirer, Musolff & Yang, *Writing Code vs. Shipping Code*, NBER WP35275, May 2026 revised September 2026; original PDF pinned, May history retained | [Reviewed brief](primary/2026-writing-code-vs-shipping-code.md) | Verified | 2026-10-21 | September observational outcome estimates, positive releases, calibrated model and separate marketplace proxies; no identified universal bottleneck | `README.md`; `report/01_the_illusion.md` Ch1 synthesis; `report/02_broken_mechanics.md` Ch7 cross-reference; `report/appendices/mechanism-hypotheses.md`; `REFERENCES.md` |
| **P-2025-01** | METR, *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity* | [Reviewed brief](primary/2025-metr-experienced-developer-productivity.md) | Verified | 2026-10-20 | Randomized task-time effect for experienced contributors in familiar mature open-source repositories with early-2025 tools; not a universal seniority effect | `README.md` Evidence Map and outcome boundary; `report/01_the_illusion.md` Chapter 1 and references; `report/03_the_aftermath.md` Chapter 8 opening; `REFERENCES.md`; `evidence/primary/2023-copilot-task-productivity.md` (comparison boundary); `evidence/primary/2026-metr-productivity-design-update.md` (historical result) |
| **P-2026-03** | METR, *We are Changing our Developer Productivity Experiment Design* (2026-02-24) | [Reviewed brief](primary/2026-metr-productivity-design-update.md) | Verified | 2026-10-20 | Follow-up experiment and first-party account of selection and measurement limits; not a reliable estimate of current productivity magnitude | `README.md` Evidence Map; `report/01_the_illusion.md` Chapter 1 and references; `report/03_the_aftermath.md` Chapter 8 opening; `REFERENCES.md`; `evidence/primary/2025-metr-experienced-developer-productivity.md` (interval restatement and temporal update) |
| **P-2025-02** | METR, *Measuring AI Ability to Complete Long Tasks*, arXiv v1 (18 March 2025); author post 19 March with later live-chart data | [Reviewed brief](primary/2025-metr-task-horizon.md) | Verified | 2026-10-21 | Historical v1 benchmark methods/trend and bounded internal-PR scoring evidence; not current-model thresholds, global reliability or production review demand | `README.md`; `report/02_broken_mechanics.md` Ch5; `report/appendices/mechanism-hypotheses.md`; `REFERENCES.md` |
| **P-2025-03** | Xu et al., *AI-Assisted Programming Decreases the Productivity of Experienced Developers* | [Reviewed brief](primary/2025-xu-copilot-oss-activity.md) | Verified | 2026-10-20 | Language-availability DiD estimates of OSS project/contributor activity and rework/review-count proxies; not seniority, review hours or net delivery loss | `README.md` Evidence Map; `report/01_the_illusion.md` Ch1/Ch4 and references; `REFERENCES.md` |
| **P-2026-02** | Agarwal et al., *AI IDEs or Autonomous Agents? Measuring the Impact of Coding Agents* | [Reviewed brief](primary/2026-agarwal-agent-adoption.md) | Verified | 2026-10-20 | Repository-month activity and static-metric estimates by observable adoption history; not per-feature debt, human cognitive load or functional correctness | `README.md` Evidence Map; `report/01_the_illusion.md` Ch1/Ch4 and references; `REFERENCES.md` |
| **P-2023-01** | Peng et al., *The Impact of AI on Developer Productivity* | [Reviewed brief](primary/2023-copilot-task-productivity.md) | Verified | 2026-10-20 | Reduced completion time conditional on completing a standardized JavaScript task; not enterprise throughput or a universal experience effect | `README.md` task-acceleration claim and Evidence Map; `report/01_the_illusion.md` Chapter 1 and references; `report/03_the_aftermath.md` Chapter 8 opening; `REFERENCES.md`; `evidence/primary/2025-metr-experienced-developer-productivity.md` (cross-study interpretation) |
| **P-2025-04** | GitClear, *AI Assistant Code Quality 2025 Research* | [Reviewed brief](primary/2025-gitclear-code-quality.md) | Verified | 2026-10-20 | Descriptive 2020–24 code-operation and sampled clone-commit signals; not identified AI causation, hard context limits or universal maintainability outcomes | `README.md` Evidence Map; `report/01_the_illusion.md` Ch1/Ch4 and relying summaries; `report/02_broken_mechanics.md` Ch6; `report/03_the_aftermath.md` Ch8 boundary; `REFERENCES.md` |
| **P-2025-05** | GitClear, *How Much More Productive Are AI-Powered Developers?* | [Reviewed brief](primary/2025-gitclear-developer-output.md) | Verified | 2026-10-20 | Separate selected-cohort commit, proprietary Diff Delta and monthly added-line comparisons against 2022; not net delivery, universal team doubling or an identified AI effect | `README.md` Evidence Map; `report/01_the_illusion.md` Ch1/Ch2/Ch4 and references; `report/02_broken_mechanics.md` Ch5; `report/03_the_aftermath.md` Ch8 boundary; `REFERENCES.md` |
| **P-2025-06** | Menlo Ventures, *2025: The State of Generative AI in the Enterprise* | [Reviewed brief](primary/2025-menlo-enterprise-ai-spend.md) | Verified | 2026-10-21 | Survey-informed 2025 market-size estimates with a revised 2024 boundary; not maintenance costs or causal AI delivery ROI | `README.md`; `report/01_the_illusion.md`; `report/02_broken_mechanics.md` and `report/03_the_aftermath.md` indirect cost reprises only (H15/H16); `report/appendices/cost-context.md`; `evidence/secondary/2026-inference-cost-commentary.md`; `REFERENCES.md` |
| **P-2025-07** | CloudZero, *The State of AI Costs in 2025* | [Reviewed brief](primary/2025-cloudzero-ai-budget-intentions.md) | Verified | 2026-10-21 | March2025 respondent reports and budget intentions; source-internal threshold discrepancy, not realized spend or causal ROI | `README.md`; `report/01_the_illusion.md`; `report/02_broken_mechanics.md` and `report/03_the_aftermath.md` indirect cost reprises only (H15/H16); `report/appendices/cost-context.md`; `evidence/secondary/2026-inference-cost-commentary.md`; `REFERENCES.md` |
| **P-2025-08** | McKinsey, *The state of AI in 2025: Agents, innovation, and transformation* (2025-11-05) | [Reviewed brief](primary/2025-mckinsey-ai-adoption-value.md) | Verified | 2026-10-21 | Original respondent-reported regular use, EBIT attribution and high-performer classification; not causal ROI or license purchasing | `README.md`; `report/01_the_illusion.md` Ch3; `report/03_the_aftermath.md` Ch10 indirect adoption-pressure and paired-measurement boundaries; `protocols/README.md` and `protocols/04_systemic_cure.md` indirect scenario-boundary clarification; `REFERENCES.md` |
| **P-2025-09** | Deloitte AI Institute, *Now decides next: Generating a new future*, Q4 report (January 2025; fieldwork July–September 2024) | [Reviewed brief](primary/2025-deloitte-genai-q4.md) | Verified | 2026-10-21 | Selected AI-active leaders’ reports of their most advanced initiative and near-term scaling expectations; not an enterprise failure rate | `README.md`; `report/01_the_illusion.md` Ch3; `report/03_the_aftermath.md` Ch10 indirect adoption-pressure and paired-measurement boundaries; `protocols/README.md` and `protocols/04_systemic_cure.md` indirect scenario-boundary clarification; `REFERENCES.md` |
| **P-2024-01** | Stack Overflow, *2024 Developer Survey*, AI section and methodology | [Reviewed brief](primary/2024-stackoverflow-ai-attitudes.md) | Verified | 2026-10-21 | Self-selected respondents’ answers to identified AI attitude questions; not rising fear, overtime or measured productivity | `README.md`; `report/01_the_illusion.md` Ch1; `REFERENCES.md` |

## Primary documentary sources

| ID | Source | Evidence review | Integration audit | Last verified | Can support | Current use |
| --- | --- | --- | --- | --- | --- | --- |
| **D-2019-01** | *Software Engineering at Google* and associated first-party engineering documentation | [Reviewed brief](documentary/2020-google-engineering-practices.md) | Verified | 2026-10-21 | Historical 2020 Google practice descriptions; not a platform budget or causal AI-enabling cost | `README.md`; `report/01_the_illusion.md`; `report/02_broken_mechanics.md` and `report/03_the_aftermath.md` indirect cost reprises only (H15/H16); `report/appendices/cost-context.md`; `REFERENCES.md` |
| **D-2024-01** | Alphabet annual filings | [Reviewed brief](documentary/2024-alphabet-financial-context.md) | Verified | 2026-10-21 | CY2024 company-wide R&D and cash PPE purchases; not AI-coding verification spend | `README.md`; `report/01_the_illusion.md`; `report/02_broken_mechanics.md` and `report/03_the_aftermath.md` indirect cost reprises only (H15/H16); `report/appendices/cost-context.md`; `REFERENCES.md` |
| **D-2024-02** | Meta annual filings | [Reviewed brief](documentary/2024-meta-financial-context.md) | Verified | 2026-10-21 | CY2024 company-wide R&D, cash PPE and separate finance-lease principal; not a customer TCO requirement | `README.md`; `report/01_the_illusion.md`; `report/02_broken_mechanics.md` and `report/03_the_aftermath.md` indirect cost reprises only (H15/H16); `report/appendices/cost-context.md`; `REFERENCES.md` |
| **D-2024-03** | Microsoft annual filings | [Reviewed brief](documentary/2024-microsoft-financial-context.md) | Verified | 2026-10-21 | FY2024 company-wide R&D and cash PPE additions, ended June30; not comparable CY or AI-coding allocation | `README.md`; `report/01_the_illusion.md`; `report/02_broken_mechanics.md` and `report/03_the_aftermath.md` indirect cost reprises only (H15/H16); `report/appendices/cost-context.md`; `REFERENCES.md` |
| **D-2025-05** | Nick Vigier, *“Subprime Code”: How Vibe Coding Could Trigger the Next Great Crash* (2025-09-16) | [Needs re-review](documentary/terminology-provenance.md) | Needs re-verification | — | Current original-page wording/date; not definitive first use or independent development | `TERMINOLOGY_AND_ATTRIBUTION.md`; `GLOSSARY.md` provenance boundary; `README.md` Evidence Map navigation; `REFERENCES.md` |
| **D-2025-06** | Igor Światowski, *The Subprime Code Crisis Has Started* (historical public-profile listing dated 2025-12-16; original access unresolved) | [Needs re-review](documentary/terminology-provenance.md) | Needs re-verification | — | Previously recorded listing and explicit current access gap; no newly read dated original or independent-development finding | `TERMINOLOGY_AND_ATTRIBUTION.md`; `GLOSSARY.md` provenance boundary; `README.md` Evidence Map navigation; `REFERENCES.md` |
| **D-2026-04** | Richard Ewing terminology-provenance collection: historical Subprime titles/date claims and separately observed retitled/redirected/current surfaces (2026-10-21) | [Needs re-review](documentary/terminology-provenance.md) | Needs re-verification | — | Historical observations and current page/author claims; origin dates, revision history and development relationships remain unresolved | `TERMINOLOGY_AND_ATTRIBUTION.md`; `GLOSSARY.md` provenance boundary; `README.md` Evidence Map navigation; `REFERENCES.md` |
| **D-2026-05** | Vitalii Oborskyi, *Ілюзія економії: чому заміна розробників на AI — це шлях до технічного дефолту* (DOU article and preserved discussion thread, 2026-01-05 onward) | [Reviewed brief](documentary/project-provenance.md) | Verified | 2026-10-21 | Dated author-authored precursor and January 8 discussion; current contents, not independent empirical validation or immutable text history | `TERMINOLOGY_AND_ATTRIBUTION.md`; `README.md`; `REFERENCES.md` |
| **D-2026-06** | GitHub REST metadata for `UncertaintyArchitectureGroup/The-Subprime-Code-Crisis` (`created_at` 2026-02-06T17:16:44Z) | [Reviewed brief](documentary/project-provenance.md) | Verified | 2026-10-21 | Repository-object creation timestamp and current public visibility only; no historical public-opening or release date | `TERMINOLOGY_AND_ATTRIBUTION.md`; `README.md`; `REFERENCES.md` |
| **D-2026-07** | Vitalii Oborskyi, *Субпрайм-криза коду: чому AI-асистенти роблять нас повільнішими — і дані це доводять* (DOU, 2026-02-10) | [Reviewed brief](documentary/project-provenance.md) | Verified | 2026-10-21 | Author-reported continuity and current article-to-repository link; no established link-insertion/public-opening time or independent validation | `TERMINOLOGY_AND_ATTRIBUTION.md`; `README.md`; `REFERENCES.md` |
| **D-2025-07** | Microsoft, FY25 Q2 earnings release (2025-01-29; quarter ended 2024-12-31) | [Reviewed brief](documentary/2025-microsoft-fy25q2-ai-run-rate.md) | Verified | 2026-10-21 | Satya Nadella’s statement about overall AI-business annual revenue run rate; not Copilot revenue or customer ROI | `README.md`; `report/01_the_illusion.md` Ch3; `REFERENCES.md` |

## Secondary evidence and industry context

| ID | Source | Evidence review | Integration audit | Last verified | Can support | Current use |
| --- | --- | --- | --- | --- | --- | --- |
| **S-2025-01** | Deloitte enterprise-survey series, legacy moving URL (retired citation) | [Needs re-review](secondary/2025-deloitte-legacy-citation.md) | Needs re-verification | — | Citation history and unresolved historical edition only; the fixed Q4 original is P-2025-09 | `REFERENCES.md` retirement note; `evidence/primary/2025-deloitte-genai-q4.md` citation resolution |
| **S-2025-02** | Banandre, *McKinsey’s 2025 AI Report: 88% Adoption, 6% Impact, The Enterprise AI Theater Continues* (2025-11-22) | [Reviewed brief](secondary/2025-banandre-mckinsey-summary.md) | Verified | 2026-10-21 | Secondary interpretation/citation history; original survey figures now belong to P-2025-08 | `REFERENCES.md` replacement note; `evidence/primary/2025-mckinsey-ai-adoption-value.md` citation history |
| **S-2025-03** | Artur Markus, *The Inference Cost Paradox* | [Reviewed brief](secondary/2026-inference-cost-commentary.md) | Verified | 2026-10-22 | Practitioner price-volume interpretation; underlying market estimates/intentions require separate original-source boundaries | `README.md`; `report/01_the_illusion.md`; `report/02_broken_mechanics.md` and `report/03_the_aftermath.md` indirect cost reprises only (H15/H16); `report/appendices/cost-context.md`; `REFERENCES.md` |
| **S-2026-01** | Andreas Horn, *The Most Important Chart in AI* (2026-02-06 personal post) | [Reviewed brief](secondary/2026-horn-capability-commentary.md) | Verified | 2026-10-21 | Personal forecast and adoption narrative; not IBM endorsement or independent METR evidence | `README.md`; `report/01_the_illusion.md` market-commentary box; `protocols/04_systemic_cure.md` indirect scenario-boundary clarification; `REFERENCES.md` |
| **S-2025-04** | James A. Wondrasek / SoftwareSeni, *Why AI Coding Speed Gains Disappear in Code Reviews* (2025-08-11; current text inspected 2026-10-21) | [Reviewed brief](secondary/2025-softwareseni-review-synthesis.md) | Verified | 2026-10-21 | Practitioner synthesis and discovery leads; no adopted review-time multiplier | `README.md` discovery-record navigation; `REFERENCES.md` discovery/correction note |
| **S-2025-05** | Techno Diaries, *Post-Copilot Burnout* (2025-10-29; accessible introduction only) | [Reviewed brief](secondary/2025-technodiaries-review-anecdote.md) | Verified | 2026-10-21 | One unaudited first-person anecdote and hypothesis generation, with a member-only access gap | `README.md`; `report/01_the_illusion.md` Ch1; `report/02_broken_mechanics.md` Ch5; `protocols/04_systemic_cure.md` indirect demand-boundary clarification; `REFERENCES.md` |
| **S-2026-02** | Andreas Horn, *AI writes code faster than teams can keep up with* (2026-01-28 personal post) | [Reviewed brief](secondary/2026-horn-engineering-commentary.md) | Verified | 2026-10-21 | Personal engineering-risk commentary; no measured prevalence, effect size or organizational endorsement | `README.md`; `report/01_the_illusion.md` market-commentary box; `protocols/04_systemic_cure.md` indirect scenario-boundary clarification; `REFERENCES.md` |

## Theory and methodology

| ID | Source | Evidence review | Integration audit | Last verified | Can support | Current use |
| --- | --- | --- | --- | --- | --- | --- |
| **M-1984-01** | Eliyahu M. Goldratt and Jeff Cox, *The Goal: A Process of Ongoing Improvement*, first published 1984; exact original edition/access unresolved | [Needs re-review](methodology/1984-the-goal.md) | Needs re-verification | — | Bibliographic identity and provisional constraint/inventory lens; no complete original-book review, theorem or empirical AI effect | `README.md`; `report/01_the_illusion.md` Ch4; `report/02_broken_mechanics.md` Ch7; `report/appendices/mechanism-hypotheses.md`; `REFERENCES.md` |

## Datasets

| ID | Source | Evidence review | Integration audit | Last verified | Can support | Current use |
| --- | --- | --- | --- | --- | --- | --- |

Dataset-level entries should be added here and to `datasets/README.md` when the repository independently uses, republishes, or analyzes a dataset. Datasets merely described inside an evidence brief do not need a separate registry entry unless they become reusable repository assets.

Dataset registry entries use `DS-YYYY-NN` IDs and the same `Evidence review`, `Integration audit`, and `Last verified` fields.

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
10. Keep `Current use` synchronized with actual repository usage discovered during the audit. Repository paths in this field must be enclosed in backticks; descriptive prose must remain outside the backticks.
11. Preserve contradictory, null, mixed, and positive evidence; classification and status are independent of whether a source supports the repository thesis.
