+++
source_ids = ["P-2023-01"]
evidence_review = "Reviewed brief"
integration_audit = "Needs re-verification"
last_verified = "—"
independent_review = "Corrections required"
current_use = ["README.md", "report/01_the_illusion.md", "report/03_the_aftermath.md", "REFERENCES.md", "evidence/primary/2025-metr-experienced-developer-productivity.md", "report/appendices/mechanism-hypotheses.md"]
+++

# Copilot and a standardized programming task

## Comparative-use reset — 2026-10-23, #110

The maintainer [approved T1–T4](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/110#issuecomment-6361681797) after the
[nine-source comparison and exact treatment proposal](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/110#issuecomment-6360324854).
The new [comparison C3](../../report/appendices/mechanism-hypotheses.md#comparison-c3)
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

- Integration status: Verified — independently Confirmed corrections merged in PR #66; main `21af254361dbd4f8d158516c1699fec7661e6312` checked on 2026-10-20. See the issue #57 trace for default-branch acceptance and remaining source limitations.
- Repository search: source IDs, names, titles, URLs, sample/effect figures and uncited summaries across all admitted text; trace records each material reader use.
- Report/numeric/README/map/bibliography/current-use checks: complete on merged main; exact research text matches the independently Confirmed candidate, with current-use paths and limits unchanged.
- Protocol outcome: No protocol change — none of the four protocols derives a role, gate or numerical threshold from this experiment; local outcome measurement remains proposed practice.
- Verification date: 2026-10-20.

## Independent review

- Primary agent: /root.
- Independent reviewer: /root/independent_evidence_review.
- Flow reviewed: B, alongside Flow A for P-2026-03.
- Materials independently checked: original v1, all uses, arithmetic, synchronized artifacts and AC-01–AC-05 in the issue #57 trace.
- Outcome: Confirmed — repeated independent review on 2026-10-20 at commit `91edb633d2d2f352a43c2333e80d5def9614b9f4`, tree `02fa53f8dfe0c23f1a2c62830d2716916da3aee9`; complete correction history and acceptance results in the issue #57 trace.
- Corrections completed: R1–R5 and precision/interval/tool boundaries independently rechecked; no unresolved correction or new human decision. Merged-main acceptance and final status review are recorded in the issue #57 trace.
- Review date: 2026-10-20.
