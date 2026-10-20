+++
source_ids = ["S-2025-03"]
evidence_review = "Reviewed brief"
integration_audit = "In progress"
last_verified = "—"
independent_review = "Confirmed"
current_use = ["report/01_the_illusion.md", "report/02_broken_mechanics.md", "report/03_the_aftermath.md", "report/appendices/cost-context.md", "REFERENCES.md"]
+++

# Markus inference-cost commentary: interpretation and corrected source boundaries

## Citation, publication and access

Artur Markus, *The Inference Cost Paradox: Why Generative AI Spending Surged 320% in 2025 Despite Per-Token Costs Dropping 1,000x—And What It Means for Your AI Budget in 2026*. [Original post](https://www.arturmarkus.com/the-inference-cost-paradox-why-generative-ai-spending-surged-320-in-2025-despite-per-token-costs-dropping-1000x-and-what-it-means-for-your-ai-budget-in-2026/), displays **2 January 2026**; stable legacy ID **S-2025-03** retained, not treated as publication year. Secondary practitioner commentary, no established peer review. [Full author-generated 14-page PDF](https://www.arturmarkus.com/the-inference-cost-paradox-why-generative-ai-spending-surged-320-in-2025-despite-per-token-costs-dropping-1000x-and-what-it-means-for-your-ai-budget-in-2026/?pdf=3401) inspected 2026-10-20. Acquired PDF SHA-256 `2c3fc73227af810521aa1fa90d8c2bfdac66c8ad7717a06461da7dd81c80b221`; it is dynamically generated on access, not an immutable January artifact. Public HTML retrieved through browsing; direct local HTML download timed out.

## Purpose, approach and underlying originals

Practitioner explanation of a Jevons-style demand rebound and budget planning. It combines external market estimates/surveys, anonymous case archetypes and scenario multipliers; no reproducible original cost dataset or causal design. Independently inspected underlying originals are separately registered: [Menlo P-2025-06](../primary/2025-menlo-enterprise-ai-spend.md), [CloudZero P-2025-07](../primary/2025-cloudzero-ai-budget-intentions.md). Other cited surveys, price trends and anonymous cases were not separately accepted as research evidence here.

## Retelling checked against originals

- Opening “$25.5 Billion Question” / PDF pp1–2: $11.5B→$37B is **+221.7%**, not the title’s +320%; `37/11.5` is 3.217×. Menlo’s revised market boundary excludes inference/model serving; this is not all-enterprise audited cost or maintenance expense.
- “Understanding Jevons” / PDF p3 calls $18B foundation-model APIs; Menlo’s infrastructure section says total infrastructure 18B, including APIs 12.5B and training 4B. Do not adopt the secondary category assignment.
- Opening CloudZero retelling converts planned2025 $85,521/45% into realized spending. Original mean comparison is retrospective2024 versus intended2025; original body/chart45%>$100k conflicts with later43%≥$100k. Neither is an audited current market share.
- “1,000× cheaper” lacks a matched model/capability/token-type/price/date series for the same year comparison. The article also cites a different 280-fold capability-level figure. Neither is independently validated by this review; remove the 1000× same-period cost assertion rather than assume a comparison.

## Author interpretation, repository interpretation and boundaries

**Author:** cheaper capability can expand useful demand; proposes cost visibility, multiple scenarios and governance, acknowledges alternative future trajectories, and presents the spending rise as value creation rather than waste. **Repository:** a possible price/volume/mix interaction worth testing. It is not proof that AI-generated code caused technical debt, budgets rose for verification, all adopters lose ROI, or every organization needs one platform/ratio.

Unattributed deployment examples, scenario ranges and timing forecasts are not adopted as empirical benchmarks or calibrated probabilities. General inference cost is different from AI-assisted software-delivery TCO. The author promotes practitioner/consulting expertise; funding, case-data provenance and independent verification are not established. No dishonesty or motive is inferred from transcription or scope errors.

## Repository use and placement

Ch2 retains an attributed interpretive link; exact quantitative context belongs to separately reviewed originals and the cost-context appendix. REFERENCES corrects the publication date. The hypothetical sensitivity model is authored by the repository and does not inherit Markus’s forecast multiples or anonymous cases.

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
