+++
source_ids = ["P-2025-02"]
evidence_review = "Reviewed brief"
integration_audit = "Needs re-verification"
last_verified = "—"
independent_review = "Corrections required"
current_use = ["README.md", "report/02_broken_mechanics.md", "REFERENCES.md", "report/appendices/mechanism-hypotheses.md"]
+++

# METR: long-task capability, measurement and verification boundaries

## Current integration checkpoint — 2026-10-22, #86

The full SDLC register adds or materially reframes this source's bounded evidence
coverage. Flow D retains **Reviewed brief** and resets integration to
**Needs re-verification / —** until the changed use is independently confirmed,
merged and checked on main. The source findings/version below are unchanged.
The earlier Confirmed review and verification records remain historical. Initial
#86 content review returned **Corrections required** for the Design card’s I86-01
test direction, with no source-fit defect found. That narrow correction is made;
repeat independent review remains pending. The current front matter records the
actual received outcome, not a promised confirmation.

Current use includes `report/appendices/mechanism-hypotheses.md`, in addition to
the prior paths. The [#86 audit and occurrence trace](../../governance/reviews/issue-86-2026-10-22-register-audit.md)
record original locators, scope, outcome omissions, all-use checks and placement.
**Protocol outcome for #86: No protocol change.** Existing controls do not acquire
empirical efficacy from a new hypothesis map. This checkpoint supersedes earlier
integration-state prose for the new use; it does not rewrite prior acceptance.


## Identity, original and publication status

Thomas Kwa, Ben West, Joel Becker et al. / METR, *Measuring AI Ability to Complete Long Tasks*, [arXiv:2503.14499v1](https://arxiv.org/abs/2503.14499v1), **18 March 2025**; [original PDF](https://arxiv.org/pdf/2503.14499v1), [HTML](https://arxiv.org/html/2503.14499v1). Retrieved 21 October2026: **45 pages**, SHA256 `a630a66414b2e7651c7c7473de0aecf2c2161fca88c7d7d2f16e92c5ae0864c5`. Preprint; peer-reviewed publication not established. Locators use PDF pages, matching printed numbering.

This is a historical v1 assessment, not current frontier performance. The [19 March author post](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) now includes later TH1.0/TH1.1 data; its date does not date every chart point. No GPT-5.2/6–7-hour threshold is adopted.

## Design, baselines and reporting discrepancies

Sections3–4 fit model/agent success to log human-baseline task duration using logistic regression. Tasks come from HCAST, SWAA and RE-Bench, with task-family weighting and suite-specific pass criteria. Runs generally repeat about eight times per model/task, with some infrastructure failures; scaffold/elicitation effort differs between models. GPT-2 long-task failures are partly imputed. This measures an elicited system on a selected suite, not a model in every deployment.

V1 has unresolved internal count differences: Section3.1 says **170 tasks (97 HCAST, 7 RE-Bench, 66 SWAA)**; Table2/p8 says **169 (97, 6, 66)**, with **148 baselined / 21 estimated**. Appendix B1/p28 instead states **149 total / 133 baselined**. Introduction says thirteen models, summary/Appendix D says eleven, while Table7/p32 lists twelve. These are source-internal discrepancies, not numbers reconciled by guessing a single total. They limit exact cohort reconstruction; no repository claim depends on a chosen total.

Human times are noisy and suite-specific: successful HCAST completions use geometric means; some times are estimates; RE-Bench thresholds reflect roughly eight-hour expert performance and those human baseliners **had AI access**. SWAA timing excludes some instruction/context overhead. Successful-only baselines and encouragement to stop unpromising attempts can select durations (§8.2/p21). Skill and context vary. These lengths do not represent a universal employee's unaided time.

## Findings, uncertainty and positive evidence

The **50% horizon** is a fitted human-baseline task length at a chosen benchmark success level. It is not a 50% defect rate for every task, agent elapsed time, or an amount of necessary human review. Section4.2/p10 reports a **212-day doubling estimate**, 95% hierarchical bootstrap interval **171–249 days** from 10,000 resamples, about seven months. Capability improves in the studied period. The chosen success level matters: 80% horizons are substantially shorter while the historical trend is similar (p12). Neither curve supplies a production reliability threshold.

Sections5–6 describe improved tool use/recovery and lower performance on messier tasks, without clearly slower improvement trends in that split. SWE-bench comparisons have different task-time estimation and trend sensitivity. These are bounded positive and mixed findings, not evidence that capability progress is irrelevant.

**Contrary evidence for an inevitable verification burden:** Section6.4/Appendix B2 (pp16/29–31) tests five internal repository issues, split into six tasks. Maintainers and contractors differ sharply in implementation speed and context; scores also differ. Appendix B2’s “Time to score” prose (p31, following Table6) reports mean manual scoring times of **3.5 minutes for maintainers and 8 minutes for contractors**; all issues took less time to score than to complete. This small manual evaluation is a real counterexample to equating verification time with task duration. It is not a representative estimate of production security, maintenance, comprehensive review or net benefit of long autonomous work.

## External validity and forecasts

Sections6–8/Appendices B–D discuss task selection, success-only baselines, elicitation, weighting and extrapolation sensitivity. The suite is largely automatically scored, static, comparatively tolerant of mistakes and limited in interaction/coordination. Longer realistic tasks and very high reliability require additional measurement. Context differences in the internal PR experiment caution against treating low-context contractor hours as employee labor replaced.

The authors extrapolate future horizons, but their statistical bands omit important trend-change and external-validity uncertainty. This repository adopts no forecast date, job-automation prediction or current vendor ranking. The historical trend cannot calibrate code volume, review demand or liability. Full-source assessment here means review of methods, findings, limits and actual uses, not reproduction of benchmark runs or resolution of every internal reporting discrepancy.

## Funding and relationships

The paper's affiliation notes include Daniel Ziegler (Anthropic) and Luke Harold Miles (Ohm Chip), with work performed while at METR; acknowledgments thank draft reviewers, graphic design and scoring-method contributors; they do not establish project funding or token/access support. A complete project-specific funding/conflict allocation is **not established from v1**, not assumed absent. METR's [current About page](https://metr.org/about), inspected 21 October2026, says it is donation-funded with a small EU AI Office contract, receives no AI-company funding, and receives substantial free tokens/access from AI companies. This current organizational disclosure must not be backdated into proof of v1 project funding. Relationships imply no misconduct.

## Repository interpretation, placement and state

R2 Chapter5 uses the definition and bounded scoring counterexample beside the proposed verification-demand test; it does not use the paper to support exponential liability. [H3](../../report/appendices/mechanism-hypotheses.md) measures verification/rework separately from total human effort. Implementation savings can yield net benefit even when review demand grows. README, bibliography and the primary index route to this bounded source assessment.

The [Astra audit](../../governance/reviews/issue-63-2026-10-21-astra-review.md) supersedes the earlier pending-full-review disposition. Initial independent analytical outcome **Corrections required** on ef5b228/tree809141fe; corrected-candidate review **Confirmed**, 21 October 2026, at `317bc1a3103840866f7d353c29b55ec001cfebd0`, tree `b45614fcee03100bc58d643c5626229250755d43`, for source/argument/all-use scope. The two precise locator/disclosure corrections and actual outcome are recorded there. PR80 retained both reset states during identity correction. Following accepted merge `1233ea3663f3166d20918565565a3e970ab9afb8`, exact-main checks and actual independent source/all-use confirmation, the [final verification record](../../governance/reviews/issue-63-2026-10-21-final-verification.md) records **Reviewed brief / Verified / 2026-10-21** for this historical v1 integration. Internal reporting and project-funding gaps remain explicit; no current-model threshold or raw benchmark replication is certified.

## Preserved Sol review history

The following record describes the earlier bounded definition check, not the subsequent full source assessment or its final outcome.

<details>
<summary>Sol preparation review, 21 October2026</summary>

## Independent review

Independent reviewer `/root/sol_review_issue63` (separate Sol agent) returned **Confirmed** on 21 October 2026 at `1c0d33806824add200e5b215dd1f8194955ec441`, tree `1a8aa6b26b24b9e0901cbb8684443c3c7abd60a7`, for the bounded definition/limitation-disposition and implementation check. See the [dated audit](../../governance/reviews/issue-63-2026-10-21-mechanism-audit.md). This does not complete the full source review, establish original-book access, accept current model results, or replace Astra analytical acceptance. Both canonical source dimensions remain reset and no verification date is proposed.

</details>
