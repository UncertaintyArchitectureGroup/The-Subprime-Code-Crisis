+++
source_ids = ["P-2025-01"]
evidence_review = "Reviewed brief"
integration_audit = "Needs re-verification"
last_verified = "—"
independent_review = "Corrections required"
current_use = ["README.md", "report/01_the_illusion.md", "report/03_the_aftermath.md", "REFERENCES.md", "evidence/primary/2023-copilot-task-productivity.md", "evidence/primary/2026-metr-productivity-design-update.md", "report/appendices/mechanism-hypotheses.md"]
+++

# METR: familiar open-source tasks with early-2025 tools

## Comparative-use reset — 2026-10-23, #110

The maintainer [approved T1–T4](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/110#issuecomment-6361681797) after the
[nine-source comparison and exact treatment proposal](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/110#issuecomment-6360324854).
The new [comparison C4](../../report/appendices/mechanism-hypotheses.md#comparison-c4)
uses this same accepted source object. Its findings, version and historical
reviews below are preserved. Flow D retains **Reviewed brief** and resets
integration to **Needs re-verification / —** for the changed use.

Independent review of this new comparison is **Corrections required**. The
[separate review](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/pull/115#discussion_r4359943405) inspected all nine comparisons, their accepted
briefs and prior source checks, the synthesis and retained-use trace. It found
the reused factual premises of C3–C9 adequately covered by accepted original
checks and required synchronization of the stale review outcomes. This note
records that review, not final acceptance of this correction. Earlier
Confirmed reviews retain their dated scope; they do not certify the new
comparison by themselves. The
[primary integration record](../../governance/reviews/issue-110-2026-10-23-integration.md) identifies the inspected
surfaces, exact locators and remaining acceptance. No final verification, merge
or confidence promotion is claimed. This checkpoint supersedes older current-
state wording only for the new use; it does not erase earlier acceptance.


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

Joel Becker, Nate Rush, Beth Barnes and David Rein. *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*. [arXiv:2507.09089v2](https://arxiv.org/abs/2507.09089v2), 25 July 2025 (v1: 12 July); [full paper](https://arxiv.org/html/2507.09089v2). Companion [author report](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), 10 July 2025.

**P-2025-01; primary empirical research; preprint and first-party report.** Peer review is not established by these publication surfaces. Full paper, appendices and author report were accessible on 2026-10-20. The v2 paper governs methods where the evolving blog FAQ differs. No raw-data or analysis-code reanalysis was performed.

## Research question, design and observed findings

| Item | Source-reported detail | Exact locator |
| --- | --- | --- |
| Population and period | 16 experienced developers; 246 completed issues (136 AI allowed, 110 disallowed) in familiar mature open-source repositories; February–June 2025 | Paper §§2.1–2.2, 3; Appendix G.7, Table 7 |
| Treatment | Issue-level randomization, AI allowed versus disallowed; mainly Cursor Pro with Claude 3.5/3.7 Sonnet | §2.2, especially §2.2.1 |
| Outcome | Active implementation time before/after review, primarily self-reported, with some post-review time imputed; not team lead time or other reviewers' hours | §§2.2.2–2.3; Appendix C.3.4 |
| Estimate | Adjusted +19% task time with AI allowed; 95% CI +2 to +39% | Figure 1; Appendix D.2; interval restated in the February 2026 author update |
| Perceptions | Forecast 24% less time; retrospective estimate 20% less time | §3, Figure 1 |

The estimand concerns permission to use AI, not mandatory use on every task. The paper uses log-linear adjustment for predicted difficulty/time; Appendix D.2 describes default HC3 intervals and alternative uncertainty calculations. Tasks within developers are not 246 independent people.

**Completion and imputation boundary:** The 246 analyzed completed issues are not all assigned issues. Appendix C.3.3 reports 13 unfinished issues (7 disallowed, 6 allowed) and separately 24 intentionally dropped issues; G.6 excludes all issues from three developers whose participation stopped (two developers following a pause in repository development; one participant repeatedly violated assignment). Section 2.3/C.3.4 imputes post-review time for 27 issues using each condition's mean. The authors report sensitivity checks under completion restrictions, extreme imputation and screen-recorded rather than self-reported time; these retain a slowdown. They reduce particular concerns without establishing absence of selection or measurement bias.

**Interval provenance:** The report uses the +2 to +39% interval explicitly restated in the dated February 2026 update. The linked [early-study data/code README](https://github.com/METR/Measuring-Early-2025-AI-on-Exp-OSS-Devs/blob/7ff2d7670235f531dff77eff58355bd77392f396/README.md) displays HC3 output 0.013–0.394 for a 0.188 estimate. Those displayed bounds differ slightly; no independent code/data reanalysis was performed to adjudicate the difference or its cause. Both displayed intervals exclude zero, but they should not be silently treated as identical numerical outputs.

## Calculations and interpretations

**Derived:** The paper reports `S = exp(beta) − 1` from its log-time regression (Appendix D.1–D.3); positive means more time. Its interpretation as a conditional mean-time ratio requires the disturbance assumptions stated in D.3. “19% slower” is replaced with “19% longer task time” to avoid confusing time and inverse rates. No conversion to delivered throughput or pooled estimate with Peng is justified.

**Source-author interpretation:** High repository familiarity, quality requirements and limitations of early tools may explain the result (§4.1); the authors explicitly restrict generalization (Table 2). These explanations are not separately randomized mechanisms.

**Repository interpretation:** The result challenges a presumption of automatic acceleration in this setting. Together with Peng it shows different measured effects across different tasks, populations and tool vintages; it does not identify which difference caused the contrast. The perception result motivates objective measurement, not a claim that all users' reports are wrong.

## Limitations, conflicts and claims not established

Selection was nonrandom; developers knew their repositories well; the sample was small, paid and restricted to early-2025 tooling. Self-reported time, task clustering and incomplete lifecycle coverage matter. Compensation was $150/hour (§2). METR describes itself as a donation-funded nonprofit with an AI-R&D measurement mission (author report FAQ). The paper's acknowledgments identify assistance, not a specific vendor grant; this review does not infer undisclosed funding.

**Not established:** a universal senior penalty, enterprise-wide slowdown, review-load redistribution, production defects, TCO, or the current effect of later agents. The separately registered [2026 follow-up](2026-metr-productivity-design-update.md) changes the temporal context without retracting this historical result.

## Repository use and placement

- `report/01_the_illusion.md`, Chapter 1: central comparison, perception boundary, temporal update, conclusion and references.
- `report/03_the_aftermath.md`, Chapter 8 opening: bounded summary of heterogeneous results.
- `README.md`: Evidence Map and task-versus-delivery boundary.
- `REFERENCES.md`: versioned citation and brief link.
- `evidence/primary/2023-copilot-task-productivity.md`: comparison boundary does not invalidate Peng's positive finding.
- `evidence/primary/2026-metr-productivity-design-update.md`: historical +19% result remains distinct from the later uncertain estimates.

The [issue #57 trace](../../governance/reviews/issue-57-2026-10-20-productivity-audit.md) records every reader occurrence. METR's long-task horizon study is **P-2025-02**, a different source outside this audit; it cannot inherit this brief's status.

## Repository integration audit

- Integration status: Verified — independently Confirmed corrections merged in PR #66; main `21af254361dbd4f8d158516c1699fec7661e6312` checked on 2026-10-20. See the issue #57 trace for default-branch acceptance and remaining source limitations.
- Search: source identity, distinctive percentages, uncited repetitions and adjacent conclusions; see issue #57 trace.
- Report/numeric/README/map/bibliography/current-use checks: complete on merged main; exact research text matches the independently Confirmed candidate, with current-use paths and limits unchanged.
- Protocol outcome: No protocol change — all four protocols retain locally bounded measures and proposed controls; no threshold comes from +19% or the perception estimates.
- Verification date: 2026-10-20.

## Independent review

- Primary agent: /root.
- Independent reviewer: /root/independent_evidence_review.
- Flow reviewed: B; companion Flow A for P-2026-03.
- Materials independently checked: full v2, author report/update, uncertainty, all occurrences, synchronization and AC-01–AC-05.
- Outcome: Confirmed — repeated independent review on 2026-10-20 at commit `91edb633d2d2f352a43c2333e80d5def9614b9f4`, tree `02fa53f8dfe0c23f1a2c62830d2716916da3aee9`; complete correction history and acceptance results in the issue #57 trace.
- Corrections completed: R1–R5 and precision/interval/tool boundaries independently rechecked; no unresolved correction or new human decision. Merged-main acceptance and final status review are recorded in the issue #57 trace.
- Review date: 2026-10-20.
