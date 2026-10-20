+++
source_ids = ["D-2024-02"]
evidence_review = "Reviewed brief"
integration_audit = "In progress"
last_verified = "—"
independent_review = "Review unavailable"
current_use = ["README.md", "report/01_the_illusion.md", "report/appendices/cost-context.md", "REFERENCES.md"]
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

- Flow B for existing records; Flow A for the two explicitly registered original surveys/models. Audit owner /root, 2026-10-20; integration **In progress**, Last verified **—**.
- [Occurrence/placement trace and Astra handoff](../../governance/reviews/issue-60-2026-10-20-cost-audit.md) cover every material use, arithmetic, nearby conclusions, README and all protocols. Protocol outcome: **No protocol change**; no monetary threshold or validated ROI follows from this source.
- Corrections are a reviewable #60 candidate. Full economic/model-choice acceptance by Astra, merged corrections and checked main remain required; no Verified promotion.

## Independent review

- Primary agent: /root (Sol implementation). Separate execution/source/arithmetic review pending; outcome **Review unavailable** at this candidate checkpoint.
- Astra analytical acceptance remains an explicit separate handoff, not inferred from structural checks or a source brief.
