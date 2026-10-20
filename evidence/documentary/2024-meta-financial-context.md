+++
source_ids = ["D-2024-02"]
evidence_review = "Reviewed brief"
integration_audit = "Verified"
last_verified = "2026-10-21"
independent_review = "Confirmed"
current_use = ["README.md", "report/01_the_illusion.md", "report/02_broken_mechanics.md", "report/03_the_aftermath.md", "report/appendices/cost-context.md", "REFERENCES.md"]
+++

# Meta CY2024: distinguish PPE purchases from lease-principal capex

## Citation, version and documentary purpose

[Form 10-K, year ended 31 December 2024, accession 0001326801-25-000043, signatures dated 29 January 2025](https://www.sec.gov/Archives/edgar/data/1326801/000132680125000043/meta-12312024x10kars.htm). Primary documentary source; issuer’s historical consolidated financial record, accessed **2026-10-20**. Full original HTML retrieved, SHA-256 `3cb2ccff9ed5e28f310162401177fb29e1d5ba06e0c35b8ae7cdfde536cc2852`.

The review checks the listed original statement lines and adjacent definitions, not every claim in the annual report. The financial statements’ audit does not independently validate this repository’s AI interpretation.

## Scope, units and documented figures

Period: **CY2024 (1 January–31 December)**. All adopted input amounts are **USD millions**; display billions divide by1,000. Cash-flow parentheses denote outflows; the table shows positive spending magnitudes, not gains. The comparator is the specified issuer period, not an AI/no-AI counterfactual.

| Accounting line | Exact original locator | Reported USD millions | Converted USD billions |
| --- | --- | --- | --- |
| Research and development | Item 8, Consolidated Statements of Income; Item 7, R&D | 43,873 | $43.873B |
| Purchases of property and equipment | Item 8, Consolidated Statements of Cash Flows, investing; Item 7, FCF reconciliation p77 | 37,256 | $37.256B |
| Principal payments on finance leases | Item 8, cash flows, financing; Item 7, FCF reconciliation p77 | 1,969 | $1.969B |

## Reconciliation and removed uses

Derived: 37,256 + 1,969 = **39,225M = $39.225B**, which rounds to the issuer’s **$39.23B** capital-expenditure measure including finance-lease principal (Item 7, Executive Overview/FCF). This is not the same line as cash PPE purchases and is not a measure of noncash leased assets added. Display the cash-PPE line in the main comparative appendix and lease-principal reconciliation separately. The previous $44.4B R&D was incorrect. The filing’s then-forward-looking $60–65B 2025 guidance is not retained as actual spending. Broad data-center/core-business/generative-AI investment is not a review-infrastructure allocation; R&D and capex are not additive cost categories on one accounting basis.

## Interpretation, limitations and incentives

**Source-author position:** issuer-reported results and management’s discussion. **Repository interpretation:** contextual scale and an accounting caution; none of these totals enters the scenario model. The statements do not establish enterprise AI ROI, minimum transformation spend, causation, senior review needs or marginal customer costs. Different companies, fiscal periods, classifications, depreciation/leases and shared assets limit comparability. Public issuer reporting and management incentives remain distinct from independent AI-effects research; no misconduct is inferred.

## Repository use and placement

The exact table belongs in the **cost-context appendix**, not as a budget needed to reproduce an AI productivity result. Ch2 links that boundary. README/REFERENCES provide navigation. The hypothetical sensitivity model uses no corporate totals or allocation inferred from these statements.

## Repository integration audit

- Flow B for existing records; Flow A for the two explicitly registered original surveys/models. Sol checkpoint 2026-10-20 was In progress; the initial Astra review required corrections. Current audit owner /root, 2026-10-21: integration **Verified**, Last verified **2026-10-21**; the independently Confirmed correction is merged and its exact default-branch tree/checks verified below.
- [Occurrence/placement trace and Astra handoff](../../governance/reviews/issue-60-2026-10-20-cost-audit.md) record the Sol occurrence review, arithmetic, nearby conclusions, README and protocols; the subsequent Astra review below identifies an omitted dependent conclusion. Protocol outcome: **No protocol change**; no monetary threshold or validated ROI follows from this source.
- The bounded economic/model-choice/source-placement correction is independently Confirmed at the latest checkpoint below. The correction merged in PR72 and exact main99df797 was checked; final state verification is recorded below.

## Independent review

- Primary /root; independent /root/review_issue60_implementation, 2026-10-20: **Confirmed**, bounded Sol implementation/source/arithmetic review of `9c5e12039b6a3895ae78c48157dd053b231faade`, tree `dca2170547449cd11df55e590dcb9c88b431e6cc` (remote PR #72 commit `8898ee0a9430079ba9a2c55f7c32cd5bf382aca4`, identical tree). Initial findings R1 (unsupported Ch3 quantified adverse costs) and R2 (index placement) independently confirmed resolved. Original-source values, all 24 model outputs, 126 tests and repository/RI/trusted-base checks passed. Full correction history and review limits are in the audit; this outcome does not approve the economic model, merge, Verified or closure.
- Astra analytical review, 2026-10-21: **Corrections required**, primary /root; independent /root/astra_cost_economics and /root/astra_cost_sources. [Pinned review, original checks and Sol correction task](../../governance/reviews/issue-60-2026-10-21-astra-review.md): A60-01 requires a conditional Ch3 conclusion; A60-02 corrects the quality comparator; A60-03 is a nonblocking cash-boundary clarification. Retained source values/placement are supported, but the shared cost argument remains inconsistent. This is an integration defect, not a finding that this source is numerically wrong. Prior bounded Sol confirmation is preserved; no merge, Verified or closure.

## First Sol correction checkpoint — 2026-10-21

At candidate514d014, [the correction trace](../../governance/reviews/issue-60-2026-10-21-sol-corrections.md) addressed A60-01/02 and nonblocking A60-03; source findings, limitations and Current use were then unchanged. Independent re-review returned Corrections required for the omitted A60-04 downstream uses. That historical outcome remains intact; the added uses and later acceptance follow below.

A60-04 correction also covers the R2 sponsor-cost paragraph and R3 budget/resource reprises, now listed in Current use as **indirect synthesis of the shared Chapter2 cost comparison** (trace H15/H16). No new finding or corporate/market calibration is attributed to this source. Other R2/R3 claims remain outside this bounded acceptance.

## Correction re-review before merge — 2026-10-21

Primary /root (Sol); independent /root/astra_cost_economics and /root/astra_cost_sources: **Confirmed**, bounded economics/inference, source integration and placement, for local `59324326c2135860f332a820bf956eb7ec1f7e69`, tree `b844181d7db07e5b4a35d2d9f37caca2ce3a5e79`. A60-01/02/03/04 are resolved. [Actual findings, correction loop and checks](../../governance/reviews/issue-60-2026-10-21-sol-corrections.md) preserve the earlier Corrections required reviews. Broader #61/#63/#64 claims are not accepted. At that checkpoint integration remained In progress / — pending accepted merge and checked default-branch state; the later verification follows below.

## Final default-branch verification — 2026-10-21

[Final verification record](../../governance/reviews/issue-60-2026-10-21-final-verification.md) checks merged PR72 at default-branch `99df79758e29357a40cf862b77b6afe9c5407796`, tree `a67205adc909286f425e041d8dfc352c9293c517`, identical to the independently accepted content/recording. Exact-main Main health39511925110 succeeded. A60-01–04 are resolved; source findings, limits, use paths and protocol outcome are synchronized. Integration **Verified**, Last verified **2026-10-21**, independent_review **Confirmed**. The status-update candidate itself still requires independent recording review and checked integration before #60 closure; see live PR/issue evidence. This verifies this source's bounded uses, not every other assertion in its report files.
