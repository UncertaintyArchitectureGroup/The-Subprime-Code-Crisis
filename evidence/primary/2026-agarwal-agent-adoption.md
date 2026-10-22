+++
source_ids = ["P-2026-02"]
evidence_review = "Reviewed brief"
integration_audit = "Verified"
last_verified = "2026-10-22"
independent_review = "Confirmed"
current_use = ["README.md", "report/01_the_illusion.md", "REFERENCES.md", "report/appendices/mechanism-hypotheses.md"]
+++

# Agarwal: agent adoption, activity and code structure

## Final integration checkpoint — 2026-10-22, #86

Changed-use integration is **Verified / 2026-10-22** for accepted correction main
`c67eb5787838735ab670a3788db4714d5ae45ff2`. Separate content, faithful-recording
and actual-main eligibility reviews are **Confirmed**. The
[final verification record](../../governance/reviews/issue-86-2026-10-22-final-verification.md)
records the reviewed trees, actual-main checks and exact source boundary.

The source's identity, findings, limitations and Current use paths are unchanged.
Verification covers the audited repository use; it does not validate every linked
hypothesis or proposed protocol remedy. This checkpoint supersedes the reset
history below. The live #86 issue records later acceptance of the final metadata PR.

## Changed-use reset history — 2026-10-22, #86

The full SDLC register adds or materially reframes this source's bounded evidence
coverage. Flow D retains **Reviewed brief** and resets integration to
**Needs re-verification / —** until the changed use is independently confirmed,
merged and checked on main. The source findings/version below are unchanged.
The earlier review and verification records remain historical. A separate
reviewer **Confirmed** the corrected #86 content on 2026-10-22, after I86-01’s
Design-test correction. The current review field records that actual outcome;
correction merge, actual-main acceptance and final integration verification
remain separate gates. See the dated audit for the exact reviewed commit/tree.

Current use includes `report/appendices/mechanism-hypotheses.md`, in addition to
the prior paths. The [#86 audit and occurrence trace](../../governance/reviews/issue-86-2026-10-22-register-audit.md)
record original locators, scope, outcome omissions, all-use checks and placement.
**Protocol outcome for #86: No protocol change.** Existing controls do not acquire
empirical efficacy from a new hypothesis map. This checkpoint supersedes earlier
integration-state prose for the new use; it does not rewrite prior acceptance.


## Citation, version and acquisition

Shyam Agarwal, Hao He and Bogdan Vasilescu. *AI IDEs or Autonomous Agents? Measuring the Impact of Coding Agents on Software Development*. Reviewed text: [arXiv:2601.13597v2](https://arxiv.org/abs/2601.13597v2), 27 January 2026 (v1: 20 January). **P-2026-02; primary empirical research.** MSR 2026 Mining Challenge conference paper, Rio de Janeiro, 13–14 April 2026; [ACM DOI 10.1145/3793302.3793589](https://doi.org/10.1145/3793302.3793589). Title/authors are listed in the [official accepted-paper/program record](https://conf.researchr.org/track/msr-2026/msr-2026-mining-challenge).

Full five-page [v2 PDF](https://arxiv.org/pdf/2601.13597v2), including Table 2/Figure 2, inspected 2026-10-20. SHA-256: `b6a59f6989710c6ed67e4b0bf8c69eac1bed600aa481d246789a426d00c9819a`. Publisher full text returned access denial; byte/content equivalence to the final proceedings edition was not established. The conference record does not upgrade the inspected v2 to an independently checked final edition. No replication code or raw data was rerun.

## Design and measured findings

| Item | Source-reported detail | Locator (PDF) |
| --- | --- | --- |
| Population/window | AIDev v3 OSS activity, January 2024–November 2025; ≥10 stars, ≥10 agent-attributed PRs per treated repository | §3.1, pp2–3 |
| Exposure | First observable agent PR, inferred from branch/login/commit/text signals. Agent-first (AF): no detected AI-IDE configuration traces during collection; IDE-first (IF): traces before first agent PR. Absence of traces is not absence of AI use | §3.1, pp2–3 |
| Matched samples | AF: 401 treated/606 controls; IF: 117/73. These are separate matched panels, not developer counts | §3.1, p3 |
| Unit/outcomes | Repository-month commits, lines added and SonarQube warnings, cognitive complexity, duplication/comment density; LOC and other time-varying covariates included | §3.2, p3 |
| Identification | Propensity/language matching, staggered imputation DiD with later/never-adopter comparisons, repository-clustered SEs and event-study diagnostics; conditional counterfactual-trend assumptions remain | §3.3, p3 |

Table 2 (p3) reports the following log-scale coefficients, SEs and percentage changes. Percentages below are the table's reported values (unrounded inputs unavailable), not a pooled effect or an independently recomputed estimate.

| Repository-month outcome | AF: β (SE); reported change | IF: β (SE); reported change | Table significance |
| --- | --- | --- | --- |
| Commits | .309 (.051); +36.25% | .030 (.092); +3.06% | AF p<.001; IF inconclusive |
| Lines added | .569 (.103); +76.59% | −.066 (.189); −6.34% | AF p<.001; IF inconclusive |
| Static-analysis warnings | .163 (.048); +17.73% | .174 (.114); +19.00% | AF p<.001; IF inconclusive |
| Cognitive/code complexity | .299 (.059); +34.85% | .357 (.114); +42.87% | AF p<.001; IF p<.01 |
| Duplicate-line density | .076 (.044); +7.92% | −.009 (.056); −.94% | Neither p<.05 |
| Comment-line density | .042 (.028); +4.34% | .201 (.055); +22.30% | IF p<.001; AF inconclusive |

“Inconclusive” means not significant at the table's 5% threshold, not evidence of exactly zero. The abstract's approximate +18%/+39% shorthand hides mode-specific effects and the IF-warning uncertainty; do not use it as one universal or per-feature rate. LOC adjustment does not turn a repository-month aggregate into a per-feature outcome.

## Interpretations, limitations and conflicts

**Source-author interpretation:** Increased structural metrics signal agent-induced complexity debt; prior AI exposure may moderate gains through coordination/review costs. **Repository interpretation:** Positive AF activity and higher complexity can coexist. These estimates motivate a maintainability investigation without measuring its human cost or proving the coordination mechanism.

Selection, imperfect PR/configuration attribution, unknown actual exposure/intensity and time-varying confounding restrict causal/general scope. In Figure 2/§4 (p4), IF complexity is already significantly elevated at t=−2; the authors acknowledge isolated pre-treatment warning/complexity coefficients as a design/data concern. Do not declare the parallel-trends assumption established. Short follow-up cannot settle lifecycle effects. Outcomes are not review hours, cognitive load, defect rates, functional correctness or TCO. No comparison labels entire codebases as purely AI- versus human-authored. Authors are affiliated with Carnegie Mellon University; no study-specific funding/conflict declaration was identified in the inspected text, which does not establish absence of conflicts.

**Not established:** +39% debt per feature, universal harm from agents, a measured senior-review bottleneck, or that AF/IF class membership proves actual first AI use. The study's positive gains and inconclusive outcomes remain central, rather than being dismissed because they do not fit a single crisis narrative.

## Repository use and placement

- `report/01_the_illusion.md`: Ch1 adoption-mode table and limitations, transition/conclusion/references; Ch4 structural-risk hypothesis and bounded cross-reference.
- `README.md`: Evidence Map brief navigation.
- `REFERENCES.md`: versioned citation, conference metadata/access boundary and brief link.

Detailed coefficients stay in this brief; the report retains the heterogeneous activity/structure result without repeating a false per-unit rate. The [#58 trace](../../governance/reviews/issue-58-2026-10-20-xu-agarwal-audit.md) records all-use and placement checks. **No protocol change:** local complexity/review/quality controls remain diagnostic proposed practices, not validated thresholds from this study.

## Repository integration audit and independent review

- Integration: Verified; Last verified: 2026-10-20. Independently Confirmed corrections merged in PR #68; default branch `bc0e4621d87e28137215573f963ae66b9a78da2b` checked on that date. The #58 trace records every completion gate, exact CI and source-state acceptance; this does not resolve the original study's stated limitations.
- Primary agent: /root; flow: B; reviewer: /root/review_issue58; date: 2026-10-20.
- Outcome: Confirmed on corrected candidate `48f9292881ce9d9df5f7277dfce5a91cb6741eb5`, tree `e25e689db69a2f7a675e4e9c84a0602b4ee1538a`. Reviewer independently reopened both full originals, checked methods/tables/uncertainty, every relying occurrence, positive/null findings, synchronization, source states and live-status evidence; ran 119 tests and trusted checks in a separate worktree.
- Initial review required R1–R3: unsupported Xu placebo assertion, CI-step attribution and missed Ch4 relying framing. All independently rechecked and resolved; no new human decision. The #58 trace preserves the correction loop and later main acceptance.
