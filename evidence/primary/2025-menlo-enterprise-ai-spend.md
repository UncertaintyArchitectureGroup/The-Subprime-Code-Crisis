+++
source_ids = ["P-2025-06"]
evidence_review = "Reviewed brief"
integration_audit = "In progress"
last_verified = "—"
independent_review = "Confirmed"
current_use = ["README.md", "report/01_the_illusion.md", "report/appendices/cost-context.md", "evidence/secondary/2026-inference-cost-commentary.md", "REFERENCES.md"]
+++

# Menlo 2025: survey-informed market estimates, not maintenance costs

## Citation, version and access

Tim Tully, Joff Redfern, Deedy Das and Derek Xiao, Menlo Ventures. *2025: The State of Generative AI in the Enterprise*, **9 December 2025**. [Original HTML](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/), [publisher-linked 18-page PDF](https://menlovc.com/wp-content/uploads/2025/12/menlo_ventures_enterprise_ai_report-2025-123125.pdf). Self-published original survey/model report; peer review not established. Accessed2026-10-20; relevant findings/methods checked in both versions; PDF p2 rendered. HTML SHA-256 `c4038546188db38efd1624ae91e1c3eec60c83351aec11208ca3a15348216264`; PDF `188beb79a303f028869f86725f60830d14cbcd31b175e94f03075a5bfcf28290`. The later filename suffix is not silently substituted for the cover publication date.

## Question, design, population and units

Enterprise generative-AI adoption/spending and market composition. Methods p18/HTML “Data Sources and Methodology”: survey of **495 U.S. enterprise AI decision-makers**, with a research firm, **7–25 November 2025**; companies actively using AI. Market sizing also uses public information, industry analysis and a bottom-up revenue model. The market-dollar estimates are not simply audited invoices from495 companies, an identified causal effect or the whole global cost of AI.

## Findings and derived result

PDF p2 / “Follow the Money” reports estimated generative-AI spending **$37B in 2025 versus $11.5B in 2024**. Footnote4 revises the historical baseline to exclude inference, previously included in older reports. Scope excludes chips, inference/model serving and embedded AI features; includes foundation models, training/AI infrastructure and applications. Do not equate this market boundary with total infrastructure budgets.

Derived from rounded reported estimates: `(37 / 11.5 − 1) × 100 = 221.739…%`; level ratio `37 / 11.5 = 3.21739…`. **321.739% of baseline is not a 321.739% increase.** Display +221.7% or about 3.2 times the baseline; do not adopt Markus’s +320% headline. These are not confidence intervals or precise raw-data totals. PDF p12/HTML infrastructure section separates foundation-model APIs $12.5B from total infrastructure $18B; the secondary commentary conflates these. The report itself interprets adoption as valuable growth, not evidence of maintenance waste.

## Interpretations and limitations

**Source-author interpretation:** broad adoption, returns and demand; optimistic boom narrative, plus Jevons-style interpretation/predictions. **Repository interpretation:** market context only. A spending rise can reflect useful adoption, new applications, scale, mix or prices; it does not establish code debt, falling net ROI or more required verification work. No matched quality/time/model price index identifies the proposed rebound mechanism.

Methods limit survey coverage to U.S. enterprises; private-company revenues are estimates as of December 2025. Sampling frame, nonresponse, raw observations, detailed market weights and uncertainty intervals are insufficient for independent reconstruction. Menlo invests in the ecosystem and identifies portfolio companies; its commercial interest is explicit, not proof of bias or misconduct. Predictions and other cited studies are not independently accepted by this review.

## Repository use and placement

Ch2 provides a short qualified market-context pointer. The appendix holds the exact comparison and revised boundary; README/REFERENCES identify the original. The Markus brief compares its retelling against this original. No market total calibrates the hypothetical cost model.

## Repository integration audit

- Flow B for existing records; Flow A for the two explicitly registered original surveys/models. Audit owner /root, 2026-10-20; integration **In progress**, Last verified **—**.
- [Occurrence/placement trace and Astra handoff](../../governance/reviews/issue-60-2026-10-20-cost-audit.md) cover every material use, arithmetic, nearby conclusions, README and all protocols. Protocol outcome: **No protocol change**; no monetary threshold or validated ROI follows from this source.
- Corrections are a reviewable #60 candidate. Full economic/model-choice acceptance by Astra, merged corrections and checked main remain required; no Verified promotion.

## Independent review

- Primary /root; independent /root/review_issue60_implementation, 2026-10-20: **Confirmed**, bounded Sol implementation/source/arithmetic review of `9c5e12039b6a3895ae78c48157dd053b231faade`, tree `dca2170547449cd11df55e590dcb9c88b431e6cc` (remote PR #72 commit `8898ee0a9430079ba9a2c55f7c32cd5bf382aca4`, identical tree). Initial findings R1 (unsupported Ch3 quantified adverse costs) and R2 (index placement) independently confirmed resolved. Original-source values, all 24 model outputs, 126 tests and repository/RI/trusted-base checks passed. Full correction history and review limits are in the audit; this outcome does not approve the economic model, merge, Verified or closure.
- Astra analytical acceptance remains an explicit separate handoff, not inferred from structural checks or a source brief.
