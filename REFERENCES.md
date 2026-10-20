# Bibliography and Data Sources

> **Navigation:** [Home](README.md) | [Scope](SCOPE.md) | [Artifact Model](ARTIFACT_MODEL.md) | [Doctrine](DOCTRINE.md) | [Glossary](GLOSSARY.md) | [Evidence Library](evidence/README.md) | [Canonical Source Registry](evidence/SOURCES.md) | [Read the Report](report/01_the_illusion.md)

This file is the compact human-readable bibliography for the repository.

[`evidence/SOURCES.md`](evidence/SOURCES.md) is the canonical source inventory and status registry. It records classification, evidence-review status, integration-audit status, verification date, and actual repository use. This bibliography provides readable citations and navigation; it is not a source-status database.

Detailed source evaluation lives in evidence briefs under `evidence/`. Canonical meanings for source classes, evidence briefs, repository interpretation, evidence review, and integration audit are maintained in [`GLOSSARY.md`](GLOSSARY.md); their boundaries are defined in [`DOCTRINE.md`](DOCTRINE.md). The repository's subject boundary and artifact relationships are expanded in [`SCOPE.md`](SCOPE.md) and [`ARTIFACT_MODEL.md`](ARTIFACT_MODEL.md).

A source appearing here is not automatically peer reviewed, independently validated, supported by a reviewed brief, or verified across every repository use. Follow the source-registry and evidence-brief links for current status, boundaries, and limitations.

## Primary empirical research

### P-2026-01 — Writing Code vs. Shipping Code

- Demirer, Musolff & Yang. [*Writing Code vs. Shipping Code: Productivity Effects Across Generations of AI Coding Tools*](https://www.nber.org/papers/w35275). NBER Working Paper 35275, 2026.
- Status: working paper; not peer reviewed.
- [Reviewed evidence brief](evidence/primary/2026-writing-code-vs-shipping-code.md).

### P-2025-01 — Experienced open-source developer productivity

- Becker, Rush, Barnes & Rein. [*Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*](https://arxiv.org/abs/2507.09089v2). arXiv v2, 25 July 2025 (v1: 12 July); [METR author report](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), 10 July 2025.
- Status: preprint and first-party research report; peer review not established here. [Evidence brief](evidence/primary/2025-metr-experienced-developer-productivity.md) records design, uncertainty and temporal limits.

### P-2026-03 — METR productivity experiment follow-up

- Becker, Rush, Cunningham, Rein & Mahamud. [*We are Changing our Developer Productivity Experiment Design*](https://metr.org/blog/2026-02-24-uplift-update/). METR, 24 February 2026; accessed 20 October 2026.
- Status: first-party original research update, separately registered from the 2025 trial; peer review not established. [Evidence brief](evidence/primary/2026-metr-productivity-design-update.md) preserves the authors' selection and measurement warnings.

### P-2025-02 — Long-task capability measurement

- METR. [*Measuring AI Ability to Complete Long Tasks*](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/). March 2025.
- Status: original measurement report; detailed repository brief pending.

### P-2025-03 — Copilot availability and OSS activity

- Xu, Medappa, Tunc, Vroegindeweij & Fransoo. [*AI-Assisted Programming Decreases the Productivity of Experienced Developers by Increasing the Technical Debt and Maintenance Burden*](https://arxiv.org/abs/2510.10165v3). arXiv v3, 28 January 2026 (v1: 11 October 2025).
- Status: preprint edition reviewed; presentations do not establish peer review. [Evidence brief](evidence/primary/2025-xu-copilot-oss-activity.md) records positive project activity, activity-quartile differences, uncertainty and source-internal reporting limits.

### P-2026-02 — AI IDEs and autonomous agents

- Agarwal, He & Vasilescu. [*AI IDEs or Autonomous Agents? Measuring the Impact of Coding Agents on Software Development*](https://arxiv.org/abs/2601.13597v2). Reviewed text: arXiv v2, 27 January 2026 (v1: 20 January).
- Publication: MSR 2026 Mining Challenge, 13–14 April; [ACM DOI](https://doi.org/10.1145/3793302.3793589), [official program](https://conf.researchr.org/track/msr-2026/msr-2026-mining-challenge). Publisher full-text equivalence was not checked. [Evidence brief](evidence/primary/2026-agarwal-agent-adoption.md) separates adoption-mode effects, static metrics and human-load hypotheses.

### P-2023-01 — Copilot productivity experiment

- Peng, Kalliamvakou, Cihon & Demirer. [*The Impact of AI on Developer Productivity: Evidence from GitHub Copilot*](https://arxiv.org/abs/2302.06590v1). arXiv v1, 13 February 2023.
- Status: preprint version reviewed. [Evidence brief](evidence/primary/2023-copilot-task-productivity.md) separates randomized participants, completers and conditional time reduction.

### P-2025-04 — GitClear code-change research

- William Harding, Alloy.dev Research / GitClear. *AI Copilot Code Quality: Evaluating 2024's Increased Defect Rate via Code Quality Metrics*. February 2025, footer v2025.2.5; Updates page states 4 February publication.
- [Full original PDF](https://gitclear-public.s3.us-west-2.amazonaws.com/GitClear-AI-Copilot-Code-Quality-2025.pdf), [publisher landing page](https://www.gitclear.com/ai_assistant_code_quality_2025_research), [evidence brief](evidence/primary/2025-gitclear-code-quality.md). Self-published commercial report; full PDF inspected 20 October 2026, with method/sampling, source-internal and landing/PDF discrepancies retained.

### P-2025-05 — GitClear developer-output research

- Bill Harding / GitClear. [*How much more productive are AI-powered developers? Large sample productivity data*](https://www.gitclear.com/research/ai_tool_impact_on_developer_productive_output_from_2022_to_2025). Publisher displays 1 October 2025; [full embedded original](https://public.amplenote.com/embed/w32ZX4GJ7ZwJasUQ1K7kqLqE), inspected 20 October 2026, contains later update text.
- Self-published commercial measurement report. [Evidence brief](evidence/primary/2025-gitclear-developer-output.md) records the four distinct methods/cohorts, positive/null findings, composite arithmetic and unresolved Method 1 mean discrepancy. It is not the quality study's dataset or a causal net-productivity estimate.

### P-2025-06 — Enterprise AI market estimates

- Tully, Redfern, Das & Xiao / Menlo Ventures. [*2025: The State of Generative AI in the Enterprise*](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/). 9 December 2025; [original PDF](https://menlovc.com/wp-content/uploads/2025/12/menlo_ventures_enterprise_ai_report-2025-123125.pdf).
- [Evidence brief](evidence/primary/2025-menlo-enterprise-ai-spend.md). Original commercial survey/market model, not audited maintenance cost or an identified causal delivery effect.

### P-2025-07 — AI spending reports and budget intentions

- CloudZero. [*The State of AI Costs in 2025*](https://www.cloudzero.com/state-of-ai-costs/). March 2025 survey; publication day not established; accessed 20 October 2026.
- [Evidence brief](evidence/primary/2025-cloudzero-ai-budget-intentions.md). Original commercial respondent survey, future plans and internal threshold discrepancy retained; not realized enterprise cost.

## Primary documentary sources

### D-2019-01 — Google engineering-system documentation

- Winters, Manshreck & Wright, eds. [*Software Engineering at Google*](https://abseil.io/resources/swe-book). O’Reilly / Google, **March 2020**; stable legacy ID retained.
- [Evidence brief](evidence/documentary/2020-google-engineering-practices.md), exact Chapters 9/19/20/23. Historical first-party practices, not a platform budget or AI outcome trial.

### D-2024-01 to D-2024-03 — Exact historical company filings

- Alphabet. [CY2024 Form 10-K, accession 0001652044-25-000014](https://www.sec.gov/Archives/edgar/data/1652044/000165204425000014/goog-20241231.htm); [accounting-line brief](evidence/documentary/2024-alphabet-financial-context.md).
- Meta. [CY2024 Form 10-K, accession 0001326801-25-000043](https://www.sec.gov/Archives/edgar/data/1326801/000132680125000043/meta-12312024x10kars.htm); [PPE/lease-principal brief](evidence/documentary/2024-meta-financial-context.md).
- Microsoft. [FY2024 Annual Report, ended 30 June 2024](https://www.microsoft.com/investor/reports/ar24/index.html); [fiscal-boundary brief](evidence/documentary/2024-microsoft-financial-context.md).
- Company-wide historical statements; neither AI-coding verification allocations nor customer transformation budgets. All accessed 20 October 2026.

### D-2025-05, D-2025-06, D-2026-04 — Terminology provenance

- Nick Vigier. [*“Subprime Code”: How Vibe Coding Could Trigger the Next Great Crash*](https://www.linkedin.com/pulse/subprime-code-how-vibe-coding-could-trigger-next-great-nick-vigier-yu5ve). 2025-09-16.
- Richard Ewing. [*The Subprime Code Crisis: What Happens When Unverified AI Code Floods the Enterprise*](https://careerwin.ai/research/the-subprime-code-crisis). Current syndication surface displays 2025-11-12; other current Ewing-controlled surfaces display or claim materially different provenance dates.
- Igor Światowski. *The Subprime Code Crisis Has Started*. Public LinkedIn profile listing dated 2025-12-16.
- Richard Ewing. [*The Subprime Code Crisis — Research Spec*](https://www.richardewing.io/concepts/subprime-code-crisis). Current page claims an April 2025 Built In / HackerNoon origin; that origin remains unverified in the repository review.
- Status: documentary provenance record under re-review and re-verification; see the [terminology provenance brief](evidence/documentary/terminology-provenance.md) for source-specific limitations and the unresolved chronology.

### D-2026-05 to D-2026-07 — Project-analysis provenance

- Vitalii Oborskyi. [*Ілюзія економії: чому заміна розробників на AI — це шлях до технічного дефолту*](https://dou.ua/forums/topic/57244/). DOU, 2026-01-05.
- GitHub REST repository record for [`UncertaintyArchitectureGroup/The-Subprime-Code-Crisis`](https://api.github.com/repos/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis), recording `created_at` as `2026-02-06T17:16:44Z`.
- Vitalii Oborskyi. [*Субпрайм-криза коду: чому AI-асистенти роблять нас повільнішими — і дані це доводять*](https://dou.ua/forums/topic/57846/). DOU, 2026-02-10.
- Status: reviewed documentary brief with integration audit in progress; these records establish the public development path of this project's own analysis, not phrase coinage or independent validation. See the [project provenance brief](evidence/documentary/project-provenance.md).

## Secondary evidence and industry context

### S-2025-01 — Deloitte enterprise survey

- Deloitte. [*State of Generative AI in the Enterprise*](https://www2.deloitte.com/us/en/pages/consulting/articles/state-of-generative-ai-in-enterprise.html). Q3 2025 edition cited by the report.
- Status: industry survey and analysis; brief pending.

### S-2025-02 — McKinsey adoption and impact reporting

- Current repository link: [third-party summary of a McKinsey 2025 report](https://www.banandre.com/blog/mckinsey-2025-ai-report-widespread-adoption-limited-impact).
- Status: secondary link only. Replace with and review the original McKinsey publication before using the figures as load-bearing evidence.

### S-2025-03 — Inference-cost commentary

- Artur Markus. [*The Inference Cost Paradox*](https://www.arturmarkus.com/the-inference-cost-paradox-why-generative-ai-spending-surged-320-in-2025-despite-per-token-costs-dropping-1000x-and-what-it-means-for-your-ai-budget-in-2026/). **2 January 2026**; stable legacy ID retained.
- [Secondary evidence brief](evidence/secondary/2026-inference-cost-commentary.md). Interpretive demand argument; market estimates and survey intentions are checked against separately registered originals; disputed headline/price claims are not adopted.

### S-2026-01 — Capability-curve commentary

- Andreas Horn. [*The Most Important Chart in AI*](https://www.linkedin.com/posts/andreashorn1_𝗧𝗵𝗲-𝗺𝗼𝘀𝘁-𝗶𝗺𝗽𝗼𝗿𝘁𝗮𝗻𝘁-𝗰𝗵𝗮𝗿𝘁-activity-7425435461994635264-IW2S/).
- Status: practitioner commentary; use for framing, not primary empirical support.

### S-2025-04 — Code-review bottleneck synthesis

- SoftwareSeni. [*Why AI Coding Speed Gains Disappear in Code Reviews*](https://www.softwareseni.com/why-ai-coding-speed-gains-disappear-in-code-reviews/).
- Status: practitioner synthesis; brief pending.

### S-2025-05 — Senior-developer bottleneck commentary

- TechnoDiaries. [*Post-Copilot Burnout: Are AI Assistants Making Senior Developers the New Bottleneck?*](https://technodiaries.medium.com/post-copilot-burnout-are-ai-assistants-making-senior-developers-the-new-bottleneck-1689e20364f1).
- Status: practitioner reporting; use for context and hypothesis generation.

## Theory and methodology

### M-1984-01 — Theory of Constraints

- Goldratt, Eliyahu M. *The Goal: A Process of Ongoing Improvement.* 1984.
- Status: methodology source used to interpret bottleneck migration, local optimization, and inventory. It is not direct evidence of AI-tool effects.

## Maintenance rule

When adding or updating a source:

1. select the applicable flow in [`AGENTS.md`](AGENTS.md);
2. register or update it in [`evidence/SOURCES.md`](evidence/SOURCES.md);
3. create or update the appropriate evidence brief and index;
4. complete the required repository-wide integration audit;
5. synchronize actual repository use and verification status in the canonical registry;
6. update this bibliography last.

Do not infer `Reviewed brief` or `Verified` from a citation appearing here. See [`AGENTS.md`](AGENTS.md) for the complete workflow and [`evidence/SOURCES.md`](evidence/SOURCES.md) for current status.
