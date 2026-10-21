+++
source_ids = ["P-2025-02"]
evidence_review = "Needs re-review"
integration_audit = "Needs re-verification"
last_verified = "—"
independent_review = "Confirmed"
current_use = ["README.md", "report/02_broken_mechanics.md", "REFERENCES.md", "report/appendices/mechanism-hypotheses.md"]
+++

# METR: task horizon is a benchmark definition

## Identity, version and access

Thomas Kwa, Ben West, Joel Becker et al. / METR, *Measuring AI Ability to Complete Long Tasks*, [arXiv:2503.14499v1](https://arxiv.org/abs/2503.14499v1), 18 March 2025; [original HTML](https://arxiv.org/html/2503.14499v1). Preprint; peer review not established here. The [19 March author post](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/), accessed 21 October 2026, now embeds later TH1.0/TH1.1 data. Its date does not date every plotted model result.

## Method and bounded findings

V1 §§3–4 fits success against task length measured using relevant human expertise, with suite-specific baselining. The 50% horizon is the fitted length at that success level, **not** the success rate of every task or deployed change. V1 §4.2 reports a historical doubling estimate of 212 days (95% bootstrap interval 171–249), approximately seven months. This is positive benchmark capability progress, not measured doubling of code volume, review demand or liability.

## Interpretation and limits

Authors discuss external validity, messier tasks, human-baseline selection/noise and scaffold/elicitation dependence (§§6–8). This brief checks the definition and the withdrawn report inference, not all benchmark results or current model rankings. Funding/conflict inventory and a full source review remain open; no current frontier-model threshold is adopted. Repository inference: longer autonomous tasks may change verification needs, which require local effort/quality measurement. Neither a universal coin-flip defect rate nor a one-for-one human review duration follows.

## Repository integration audit

H63-01–05 in the [dated occurrence trace](../../governance/reviews/issue-63-2026-10-21-mechanism-audit.md) cover the former heading, numbers, reasoning, reference and README navigation. Removed GPT-5.2/6–7-hour claims rather than dating later chart values to March 2025. [Hypothesis H3](../../report/appendices/mechanism-hypotheses.md) states the missing verification comparison. Full source review/accepted integration remain pending; no verification date.

## Independent review

Independent reviewer `/root/sol_review_issue63` (separate Sol agent) returned **Confirmed** on 21 October 2026 at `1c0d33806824add200e5b215dd1f8194955ec441`, tree `1a8aa6b26b24b9e0901cbb8684443c3c7abd60a7`, for the bounded definition/limitation-disposition and implementation check. See the [dated audit](../../governance/reviews/issue-63-2026-10-21-mechanism-audit.md). This does not complete the full source review, establish original-book access, accept current model results, or replace Astra analytical acceptance. Both canonical source dimensions remain reset and no verification date is proposed.
