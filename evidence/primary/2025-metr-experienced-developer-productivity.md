+++
source_ids = ["P-2025-01"]
evidence_review = "Reviewed brief"
integration_audit = "Corrections required"
last_verified = "—"
independent_review = "Corrections required"
current_use = ["README.md", "report/01_the_illusion.md", "report/03_the_aftermath.md", "REFERENCES.md", "evidence/primary/2023-copilot-task-productivity.md", "evidence/primary/2026-metr-productivity-design-update.md"]
+++

# METR: familiar open-source tasks with early-2025 tools

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

**Completion and imputation boundary:** The 246 analyzed completed issues are not all assigned issues. Appendix C.3.3 reports 13 unfinished issues (7 disallowed, 6 allowed) and separately 24 intentionally dropped issues; G.6 excludes all issues from three developers whose participation stopped (two repositories paused, one participant repeatedly violated assignment). Section 2.3/C.3.4 imputes post-review time for 27 issues using each condition's mean. The authors report sensitivity checks under completion restrictions, extreme imputation and screen-recorded rather than self-reported time; these retain a slowdown. They reduce particular concerns without establishing absence of selection or measurement bias.

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

- Integration status: Corrections required; first-review corrections implemented, repeated review and default-branch verification pending.
- Search: source identity, distinctive percentages, uncited repetitions and adjacent conclusions; see issue #57 trace.
- Report/numeric/README/map/bibliography/current-use checks: candidate recorded; independent review and merged-state acceptance pending.
- Protocol outcome: No protocol change — all four protocols retain locally bounded measures and proposed controls; no threshold comes from +19% or the perception estimates.
- Verification date: —.

## Independent review

- Primary agent: /root.
- Independent reviewer: /root/independent_evidence_review.
- Flow reviewed: B; companion Flow A for P-2026-03.
- Materials to check: full v2, author report/update, uncertainty, all occurrences, synchronization and AC-01–AC-05.
- Outcome: Corrections required — first review at tree `2d8d839ce3ce1532a48c7e77a48644e01ab28f03`; exact findings and dispositions in the issue #57 trace.
- Corrections implemented: locators, completion/exclusion/imputation boundary, public-data wording and cross-brief uses. Repeat review pending; no new human decision required.
- Review date: 2026-10-20.
