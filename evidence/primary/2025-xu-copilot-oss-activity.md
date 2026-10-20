+++
source_ids = ["P-2025-03"]
evidence_review = "Reviewed brief"
integration_audit = "In progress"
last_verified = "—"
independent_review = "Confirmed"
current_use = ["README.md", "report/01_the_illusion.md", "REFERENCES.md"]
+++

# Xu: Copilot availability and open-source activity

## Citation, version and acquisition

Feiyang (Amber) Xu, Poonacha K. Medappa, Murat M. Tunc, Martijn Vroegindeweij and Jan C. Fransoo. *AI-Assisted Programming Decreases the Productivity of Experienced Developers by Increasing the Technical Debt and Maintenance Burden*. [arXiv:2510.10165v3](https://arxiv.org/abs/2510.10165v3), 28 January 2026 (v1: 11 October 2025; v2: 24 October). **P-2025-03; primary empirical research; reviewed edition is a preprint.** Conference presentations do not establish peer review.

Full [PDF v3](https://arxiv.org/pdf/2510.10165v3), including Appendix Tables 11–14 absent from the HTML rendering, inspected on 2026-10-20. SHA-256: `446bd9154be2f77e77b2a316f0681573433515876aef58cdd491a9ec0f81594e`. PDF page numbers below. No raw-data or analysis-code reproduction was performed.

## Design and measured findings

| Item | Source-reported detail | Locator |
| --- | --- | --- |
| Population | 2,755 Microsoft-owned OSS repositories: 1,660 treatment, 1,095 control; separately filtered panel of 1,699 contributors: 1,186/513 | §§3.1–3.2, pp10–12; footnote 14 |
| Exposure/comparator | Copilot's 2021 technical-preview language support: Python, JavaScript, Ruby, TypeScript and Go versus non-endorsed languages. Individual Copilot use is unobserved | §3.1, pp10–11 |
| Period/unit | July 2020–July 2022, described as 12 months before/after introduction; repository-month and contributor-month outcomes | §§3.1–3.3, pp11–12 |
| Identification | Difference-in-differences, unit/month effects, unit-clustered standard errors; relies on comparable counterfactual trends and no confounding language-specific shock | §3.4, pp15–16 |
| Outcomes | Counts transformed as log(1+count). Rework: follow-up commits after initial PR submission. Reviews: formal PR reviews, not time. Core: top 25% of pre-treatment commit activity; peripheral: other 75%, not job grades | Table 2/§3.3, pp12–14 |
| Project activity | Reported +17.7% lines added (β=.163, SE=.060), +4.1% commits (.040, .022), +4.3% PRs (.042, .015). Commits meet only p<.10; other two p<.01 | Table 5, p16 |
| Project rework | +2.4% follow-up-commit activity (.024, .010, p<.05), with PR count controlled; not a per-PR defect rate | Table 5, p16 |

### Subgroup results and calculations

Use the appendix subgroup regressions for subgroup effects; Table 6's core-by-treatment interaction is a different quantity. The following percentages and intervals are **derived** as `100*(exp(x)-1)` from printed coefficients/95% bounds, rounded to one decimal. With log(1+counts), these are transformed-count contrasts, not time or value ratios.

| Outcome/subgroup | β; SE; p | Derived estimate and 95% interval | Locator |
| --- | --- | --- | --- |
| Commits, bottom activity quartile | .3614; .0447; <.001 | +43.5%; +31.5 to +56.7% | Table 13, p29 |
| Commits, top/core quartile | −.2149; .0551; <.001 | −19.3%; −27.6 to −10.1% | Table 13, p29 |
| PRs, bottom quartile | .1630; .0317; <.001 | +17.7%; +10.6 to +25.3% | Table 14, p29 |
| Reviews, top/core quartile | .0628; .0366; .086 | +6.5%; −0.9 to +14.4%, includes zero | Table 11, p29 |

Table 13's middle quartiles differ (+.1115 and −.0381 coefficients); bottom-quartile +43.5% cannot describe all peripheral contributors. Top-quartile PR change is inconclusive (Table 14, p=.147). Reviewed-repository count rises for the top quartile (Table 12, β=.0530, p=.006); that also measures activity, not review hours.

## Interpretations, limitations and conflicts

**Source-author interpretation:** Activity redistribution and PR rework indicate maintenance burden/technical debt. **Repository interpretation:** The pattern motivates testing displacement of development work by review, while preserving positive project activity. It does not identify review work as the cause of reduced commits or establish net project productivity loss.

Exposure is language availability in a selected OSS setting, not randomized or individually observed use. Language trends, selection, spillovers, proxy validity and early tool vintage limit causal/general scope. The PR-rework event study/lead-lag analysis, matching and omitted-variable sensitivity (§5, pp18–20; Appendix pp28–29) address particular concerns without eliminating them. Counts do not measure hours, defects, functional correctness, enterprise throughput or lifecycle cost. Affiliation: Tilburg University. No study-specific funding/conflict declaration was identified in the inspected paper; this is not evidence of no conflicts.

**Source-internal reporting uncertainty:** Table 6 (p18) prints β=.142 with SE=.408 and significance stars that do not agree on their face; §4.2 (p17) describes a −.357 interaction using the positive `exp(.357)-1` calculation. Neither is used as the subgroup estimate. Table 5's 66,120/66,168 observations and Table 6's 51,408 cannot be fully reconciled here with the stated samples/window; footnote 14's contributor-filter wording is also ambiguous. Preserve the reported sample and table-specific estimates without claiming an independently reconstructed panel or silently repairing the original. These limits qualify the study, rather than being resolved by repository validation.

## Repository use and placement

- `report/01_the_illusion.md`: Ch1 observational comparison, source summary/conclusion/references; Ch4 bounded activity/WIP hypothesis and cross-reference. Detailed tables stay here rather than becoming a measured SDLC chain.
- `README.md`: Evidence Map brief navigation, no general seniority finding.
- `REFERENCES.md`: full title, pinned edition and brief link.

The [#58 occurrence trace](../../governance/reviews/issue-58-2026-10-20-xu-agarwal-audit.md) records numbers, interpretation and placement separately. **No protocol change:** existing local controls do not derive a threshold or validated review-capacity rule from these estimates.

## Repository integration audit and independent review

- Integration: In progress; Last verified: —. Independently Confirmed corrections await merge and checked default-branch acceptance before final verification.
- Primary agent: /root; flow: B; reviewer: /root/review_issue58; date: 2026-10-20.
- Outcome: Confirmed on corrected candidate `48f9292881ce9d9df5f7277dfce5a91cb6741eb5`, tree `e25e689db69a2f7a675e4e9c84a0602b4ee1538a`. Reviewer independently reopened both full originals, checked methods/tables/uncertainty, every relying occurrence, positive/null findings, synchronization, source states and live-status evidence; ran 119 tests and trusted checks in a separate worktree.
- Initial review required R1–R3: unsupported Xu placebo assertion, CI-step attribution and missed Ch4 relying framing. All independently rechecked and resolved; no new human decision. The #58 trace preserves the correction loop and later main acceptance.
