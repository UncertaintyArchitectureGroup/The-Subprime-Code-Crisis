+++
source_ids = ["D-2024-03"]
evidence_review = "Reviewed brief"
integration_audit = "In progress"
last_verified = "—"
independent_review = "Confirmed"
current_use = ["README.md", "report/01_the_illusion.md", "report/02_broken_mechanics.md", "report/03_the_aftermath.md", "report/appendices/cost-context.md", "REFERENCES.md"]
+++

# Microsoft FY2024: preserve the fiscal-year boundary

## Citation, version and documentary purpose

[Microsoft 2024 Annual Report / FY2024 financial statements](https://www.microsoft.com/investor/reports/ar24/index.html). Primary documentary source; issuer’s historical consolidated financial record, accessed **2026-10-20**. Publisher HTML and financial tables inspected through public retrieval; direct local download returned403. No local-byte hash or unavailable file access is claimed.

The review checks the listed original statement lines and adjacent definitions, not every claim in the annual report. The financial statements’ audit does not independently validate this repository’s AI interpretation.

## Scope, units and documented figures

Period: **FY2024 (1 July 2023–30 June 2024)**. All adopted input amounts are **USD millions**; display billions divide by1,000. Cash-flow parentheses denote outflows; the table shows positive spending magnitudes, not gains. The comparator is the specified issuer period, not an AI/no-AI counterfactual.

| Accounting line | Exact original locator | Reported USD millions | Converted USD billions |
| --- | --- | --- | --- |
| Research and development | Operating Expenses; Income Statements, year ended June 30 | 29,510 | $29.510B |
| Additions to property and equipment | Cash Flows Statements, investing activities, year ended June 30 | 44,477 | $44.477B |

## Reconciliation and removed uses

The amounts belong to FY2024 ending June 30, not the other companies’ CY2024. The cash-flow additions line is not a complete measure of all cash and noncash capital investment. The former ~$64B CY run-rate extrapolation and ~$80B 2025 plan are withdrawn from this comparison rather than presented as like-for-like actuals. R&D covers broad product engineering; cash PPE investment does not identify an AI-coding verification budget. Expense/cash-flow measures are not added into a TCO total.

## Interpretation, limitations and incentives

**Source-author position:** issuer-reported results and management’s discussion. **Repository interpretation:** contextual scale and an accounting caution; none of these totals enters the scenario model. The statements do not establish enterprise AI ROI, minimum transformation spend, causation, senior review needs or marginal customer costs. Different companies, fiscal periods, classifications, depreciation/leases and shared assets limit comparability. Public issuer reporting and management incentives remain distinct from independent AI-effects research; no misconduct is inferred.

## Repository use and placement

The exact table belongs in the **cost-context appendix**, not as a budget needed to reproduce an AI productivity result. Ch2 links that boundary. README/REFERENCES provide navigation. The hypothetical sensitivity model uses no corporate totals or allocation inferred from these statements.

## Repository integration audit

- Flow B for existing records; Flow A for the two explicitly registered original surveys/models. Sol checkpoint 2026-10-20 was In progress; the initial Astra review required corrections. Current audit owner /root, 2026-10-21: integration **In progress**, Last verified **—**; the corrected argument is independently Confirmed, pending accepted merge and checked default-branch verification.
- [Occurrence/placement trace and Astra handoff](../../governance/reviews/issue-60-2026-10-20-cost-audit.md) record the Sol occurrence review, arithmetic, nearby conclusions, README and protocols; the subsequent Astra review below identifies an omitted dependent conclusion. Protocol outcome: **No protocol change**; no monetary threshold or validated ROI follows from this source.
- The bounded economic/model-choice/source-placement correction is independently Confirmed at the latest checkpoint below. Merged corrections and checked main remain required; no Verified promotion.

## Independent review

- Primary /root; independent /root/review_issue60_implementation, 2026-10-20: **Confirmed**, bounded Sol implementation/source/arithmetic review of `9c5e12039b6a3895ae78c48157dd053b231faade`, tree `dca2170547449cd11df55e590dcb9c88b431e6cc` (remote PR #72 commit `8898ee0a9430079ba9a2c55f7c32cd5bf382aca4`, identical tree). Initial findings R1 (unsupported Ch3 quantified adverse costs) and R2 (index placement) independently confirmed resolved. Original-source values, all 24 model outputs, 126 tests and repository/RI/trusted-base checks passed. Full correction history and review limits are in the audit; this outcome does not approve the economic model, merge, Verified or closure.
- Astra analytical review, 2026-10-21: **Corrections required**, primary /root; independent /root/astra_cost_economics and /root/astra_cost_sources. [Pinned review, original checks and Sol correction task](../../governance/reviews/issue-60-2026-10-21-astra-review.md): A60-01 requires a conditional Ch3 conclusion; A60-02 corrects the quality comparator; A60-03 is a nonblocking cash-boundary clarification. Retained source values/placement are supported, but the shared cost argument remains inconsistent. This is an integration defect, not a finding that this source is numerically wrong. Prior bounded Sol confirmation is preserved; no merge, Verified or closure.

## First Sol correction checkpoint — 2026-10-21

At candidate514d014, [the correction trace](../../governance/reviews/issue-60-2026-10-21-sol-corrections.md) addressed A60-01/02 and nonblocking A60-03; source findings, limitations and Current use were then unchanged. Independent re-review returned Corrections required for the omitted A60-04 downstream uses. That historical outcome remains intact; the added uses and later acceptance follow below.

A60-04 correction also covers the R2 sponsor-cost paragraph and R3 budget/resource reprises, now listed in Current use as **indirect synthesis of the shared Chapter2 cost comparison** (trace H15/H16). No new finding or corporate/market calibration is attributed to this source. Other R2/R3 claims remain outside this bounded acceptance.

## Current correction re-review — 2026-10-21

Primary /root (Sol); independent /root/astra_cost_economics and /root/astra_cost_sources: **Confirmed**, bounded economics/inference, source integration and placement, for local `59324326c2135860f332a820bf956eb7ec1f7e69`, tree `b844181d7db07e5b4a35d2d9f37caca2ce3a5e79`. A60-01/02/03/04 are resolved. [Actual findings, correction loop and checks](../../governance/reviews/issue-60-2026-10-21-sol-corrections.md) preserve the earlier Corrections required reviews. Broader #61/#63/#64 claims are not accepted. Integration stays In progress / — until accepted corrections are merged and the default branch and final source states are checked.
