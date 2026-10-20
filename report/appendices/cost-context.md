# Cost context: historical records, estimates and intentions

[Chapter 2](../01_the_illusion.md#chapter-2-evaluating-the-cost-of-ai-assisted-delivery) · [Sensitivity model](tco-sensitivity.md) · [Source Registry](../../evidence/SOURCES.md)

These records answer different questions. Corporate expenses and investment,
market-size estimates, survey intentions and a local delivery budget cannot be
combined into one observed cost of adopting an AI coding tool. None of the amounts
below calibrates the hypothetical sensitivity inputs.

## Company-wide 2024 records

Amounts below are **USD billions**, converted from original statement amounts in
USD millions by dividing by 1,000. Cash-flow outflows are shown as positive
spending magnitudes. These are historical actuals, not current budgets or guidance.

| Issuer / period | R&D expense | Cash-flow investment line | Original line and boundary |
| --- | --- | --- | --- |
| Alphabet, CY2024, ended 31 December | **49.326** | **52.535** | Research and development; purchases of property and equipment. [D-2024-01 brief](../../evidence/documentary/2024-alphabet-financial-context.md), Item 7 R&D and Item 8 income/cash-flow statements |
| Meta, CY2024, ended 31 December | **43.873** | **37.256** | Research and development; purchases of property and equipment. [D-2024-02 brief](../../evidence/documentary/2024-meta-financial-context.md), Item 8 statements and Item 7 FCF reconciliation, p77 |
| Microsoft, FY2024, 1 July 2023–30 June 2024 | **29.510** | **44.477** | Research and development; additions to property and equipment in cash-flow investing activities. [D-2024-03 brief](../../evidence/documentary/2024-microsoft-financial-context.md), FY2024 income/cash-flow statements |

Meta separately reports **1.969** of finance-lease principal payments.
**37.256 + 1.969 = 39.225**, rounded to the issuer's **39.23** measure of capital
expenditures including lease principal. The previous $39.2B label hid this
definition difference. It is not the cash-PPE line or noncash leased assets added.

Alphabet's former $45.4B R&D value belonged to 2023; Meta's former $44.4B was
incorrect. Microsoft retains its fiscal-year label. The table does not make the
periods or classifications identical. R&D expense and cash investment are not
additive categories on a common TCO basis: depreciation and other recognition
differences matter. There is no sum across these columns or companies.

These issuer-wide statements cover many products, businesses and shared assets.
They do not disclose the marginal cost of verifying AI-generated code or a budget
that another enterprise must reproduce. Former 2025 guidance, a Microsoft
calendar-year run-rate extrapolation and an aggregate news forecast are removed
from the comparison, rather than treated as comparable actual spending.

## A historical engineering example

Google's publisher identifies *Software Engineering at Google* as a **March 2020**
book. Chapter 23's TAP section describes **more than four billion individual test
cases daily**, not an exact 4.2 billion or a current rate. Chapters 9/19 describe
human review supported by Critique; Chapter 20 describes static analysis and its
tradeoffs. See [D-2019-01](../../evidence/documentary/2020-google-engineering-practices.md),
whose stable legacy ID does not determine the publication year.

This supports an example of surrounding engineering practices. The inspected
source does not establish the former $1B TAP budget, $1–3B platform budget,
10–15-year cost timeline, or that automated review removes human judgment. Those
claims are withdrawn. No mandatory platform, staffing ratio or adoption budget is
derived from the book.

## Menlo: a market estimate with a revised boundary

[P-2025-06](../../evidence/primary/2025-menlo-enterprise-ai-spend.md) reviews the
9 December 2025 original report and linked PDF. PDF p2 / “Follow the Money” gives
estimated generative-AI spending **$37B in 2025 versus $11.5B in 2024**.

The derived change is `(37 / 11.5 − 1) × 100 = 221.739…%`, or **+221.7%**;
the level ratio is **3.21739… times** the baseline. It is not a +320% increase.
These rounded model estimates are not precise invoice totals.

PDF p18 describes 495 U.S. enterprise AI decision-makers surveyed 7–25 November
2025 plus a bottom-up market model. The estimate covers selected model,
infrastructure and application markets; it excludes chips, inference/model
serving and embedded AI features. Footnote 4 revises the 2024 baseline to remove
inference previously included. It cannot be compared silently with an older
edition's boundary or relabeled total enterprise operating/maintenance cost.

The authors interpret the results optimistically as adoption and value creation.
Menlo's investments in this market and estimation/sampling limits are disclosed
in the brief. This repository does not infer poor ROI or code-debt growth from
market demand.

## CloudZero: retrospective reports and future intentions

[P-2025-07](../../evidence/primary/2025-cloudzero-ai-budget-intentions.md) reviews
the original March 2025 survey of 500 U.S. manager/senior respondents, stated
employer size 250–10,000. Respondents are not established as 500 unique firms.

Section 01 reports a 2024 mean monthly amount of **$62,964** and a planned/expected
2025 mean of **$85,521**. Their ratio implies **+35.825…%**, rounded 36%; it does
not demonstrate realized spending growth or individual-company growth rates.

The original chart titled **“Monthly AI budgets for 2024 vs 2025”**, and adjacent
body text, put **45%** in the planned 2025 **“Over $100,000”** bracket, versus
20% for 2024. Later Section 01 “Key takeaways” instead says **43% planning
$100,000 or more**. The different values and thresholds remain an **unresolved
source discrepancy**. The exact underlying question, record counts and weighting
are not available; neither percentage is selected as an industry headline.

The report mixes positive perceptions of AI with cost-visibility concerns. These
are self-reports from a commercial cost-tool publisher, not an experiment on
maintenance, verification controls or net delivery value. Its body also discusses
10,000-plus employers despite the stated methodology bound; subgroup coverage is
not silently repaired.

## Commentary and the price–volume question

[S-2025-03](../../evidence/secondary/2026-inference-cost-commentary.md) is Artur
Markus's **2 January 2026** practitioner commentary, despite the retained legacy
ID. Its Jevons-style interpretation is a possible demand mechanism, not a measured
causal result. The title's +320% retelling, realized-spend phrasing and $18B
API-only category do not match the reviewed originals. Its claimed same-period
1,000-fold cost decline lacks a matched model, capability, token type and price
window in the inspected analysis and is not adopted here.

Rising spend could reflect useful new applications, adoption, scope, model mix,
prices or rework. Testing a rebound effect requires matched unit prices,
capability, volumes and outcomes; testing code-debt cost additionally requires
software-maintenance observations. A larger bill alone establishes neither.
