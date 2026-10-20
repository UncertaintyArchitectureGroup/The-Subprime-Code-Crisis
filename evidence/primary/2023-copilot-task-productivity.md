+++
source_ids = ["P-2023-01"]
evidence_review = "Reviewed brief"
integration_audit = "Corrections required"
last_verified = "—"
independent_review = "Corrections required"
current_use = ["README.md", "report/01_the_illusion.md", "report/03_the_aftermath.md", "REFERENCES.md", "evidence/primary/2025-metr-experienced-developer-productivity.md"]
+++

# Copilot and a standardized programming task

## Citation, version and acquisition

Sida Peng, Eirini Kalliamvakou, Peter Cihon and Mert Demirer. *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot*. [arXiv:2302.06590v1](https://arxiv.org/abs/2302.06590v1), 13 February 2023; [full original](https://arxiv.org/html/2302.06590v1).

**P-2023-01; primary empirical research; preprint version reviewed.** An arXiv deposit does not establish peer review. Full text, methods, results, Table 1 and figure descriptions were accessible on 2026-10-20. This review does not reproduce participant-level data or independently validate the authors' statistical code.

## Research question, design and observed findings

| Item | Source-reported detail | Exact locator |
| --- | --- | --- |
| Setting | Upwork recruitment; May 15–June 20, 2022; GitHub Copilot access versus no access, other resources allowed | Study Design |
| Assignment | 95 randomized: 45 treatment, 50 control; 70 task-and-survey completers: 35 per arm; five assigned treatment did not finish tool setup | Study Design; Results, first paragraph |
| Task and endpoint | JavaScript HTTP server from a skeleton; repository creation to first commit passing all 12 tests | Study Design, Classroom paragraphs |
| Conditional completion time | Treatment 71.17 minutes; control 160.89; 55.8% reduction; 95% CI 21–89%; p=0.0017 | Results, Figure 6 paragraph |
| Other results | Reported success-rate difference +7 percentage points, CI −11 to +25; experience interaction p=0.0629 | Results after Figure 6; Table 1 |

The time estimate conditions on completion; assignment and completer counts are different denominators. The success result is inconclusive. Do not substitute the completer counts for the authors' separate success-rate analysis without its underlying eligibility data.

## Calculations and interpretations

**Derived:** `(160.89 − 71.17) / 160.89 × 100 = 55.7648…%`, rounding to 55.8% less time. This is not a 55.8% increase in an inverse time rate or in delivered throughput. No repository model is fitted here.

**Source-author interpretation:** Copilot improved performance in this experiment; exploratory heterogeneity suggests potential benefits for less experienced programmers (Results, Table 1; Discussion).

**Repository interpretation:** This is positive evidence for bounded task acceleration and belongs in the central comparison. The experience analysis does not warrant a universal junior-versus-senior rule. Successful testing is not a measurement of lifecycle quality.

## Limitations, conflicts and claims not established

Completion conditioning, a single standardized task, freelancer selection, early tool vintage and limited follow-up constrain generalization. The source lists GitHub/Microsoft affiliations and Microsoft ethics approval; this is vendor-linked research, not evidence of misconduct (title block; Study Design). Discussion explicitly leaves code quality unexamined.

**Not established:** enterprise delivery speed, production defects, maintenance cost, review bottlenecks, industry task mix, or universal benefits for any experience group. Neither these omissions nor the [METR 2025 comparison](2025-metr-experienced-developer-productivity.md) demonstrate that the positive result disappears elsewhere.

## Repository use and placement

- `report/01_the_illusion.md`, Chapter 1: central comparison, outcome boundary, conclusion and references.
- `report/03_the_aftermath.md`, Chapter 8 opening: synchronized bounded summary of the comparison.
- `README.md`: existential task-acceleration claim and Evidence Map navigation.
- `REFERENCES.md`: versioned citation and brief link.
- `evidence/primary/2025-metr-experienced-developer-productivity.md`: cross-study interpretation contrasts the bounded effects without identifying their cause.

See the occurrence-level [issue #57 trace](../../governance/reviews/issue-57-2026-10-20-productivity-audit.md) for wording, numbers, placement and excluded sources. The positive finding was moved from a defensive aside to the opening comparison; duplicate descriptions now point back to that comparison.

## Repository integration audit

- Integration status: Corrections required; first-review corrections implemented, repeat independent review and default-branch verification pending.
- Repository search: source IDs, names, titles, URLs, sample/effect figures and uncited summaries across all admitted text; trace records each material reader use.
- Report, numeric, README/map, bibliography and current-use checks: recorded in the issue #57 trace; final acceptance pending independent review and merge.
- Protocol outcome: No protocol change — none of the four protocols derives a role, gate or numerical threshold from this experiment; local outcome measurement remains proposed practice.
- Verification date: —.

## Independent review

- Primary agent: /root.
- Independent reviewer: /root/independent_evidence_review.
- Flow reviewed: B, alongside Flow A for P-2026-03.
- Materials to check: original v1, all uses, arithmetic, synchronized artifacts and AC-01–AC-05 in the issue #57 trace.
- Outcome: Corrections required — first review at tree `2d8d839ce3ce1532a48c7e77a48644e01ab28f03`; see the issue #57 trace for five findings and correction disposition.
- Corrections implemented: exact intermediate arithmetic and cross-brief dependencies; repeat independent review pending. No new human decision required.
- Review date: 2026-10-20.
