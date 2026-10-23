+++
source_ids = ["P-2026-03"]
evidence_review = "Reviewed brief"
integration_audit = "Needs re-verification"
last_verified = "—"
independent_review = "Corrections required"
current_use = ["README.md", "report/01_the_illusion.md", "report/03_the_aftermath.md", "REFERENCES.md", "evidence/primary/2025-metr-experienced-developer-productivity.md", "report/appendices/mechanism-hypotheses.md"]
+++

# METR: follow-up selection and measurement limits

## Comparative-use reset — 2026-10-23, #110

The maintainer [approved T1–T4](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/110#issuecomment-6361681797) after the
[nine-source comparison and exact treatment proposal](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/110#issuecomment-6360324854).
The new [comparison C5](../../report/appendices/mechanism-hypotheses.md#comparison-c5)
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

Joel Becker, Nate Rush, Tom Cunningham, David Rein and Khalid Mahamud. [*We are Changing our Developer Productivity Experiment Design*](https://metr.org/blog/2026-02-24-uplift-update/). METR, 24 February 2026; accessed 2026-10-20.

**P-2026-03; primary empirical research update.** This is a first-party research blog with original experimental results and design discussion, not an established peer-reviewed paper. The full public article was accessible and links public [early-study](https://github.com/METR/Measuring-Early-2025-AI-on-Exp-OSS-Devs/blob/7ff2d7670235f531dff77eff58355bd77392f396/README.md) and [follow-up data/code](https://github.com/METR/Measuring-Late-2025-AI-on-OSS-Devs/blob/55f007216a26493f0a9b7650ab3191cad7fb9e7f/README.md). No independent raw-data/code reanalysis was performed; no claim of data inaccessibility is made. This review does not establish a reliable current causal magnitude.

## Research question, design and observed findings

| Item | Source-reported detail | Exact locator in article |
| --- | --- | --- |
| Follow-up | Started August 2025; 57 developers: 10 returning and 47 new; 143 repositories, 800+ tasks | “Details of the productivity study” |
| Comparator and tools | Randomized AI-allowed/disallowed work; later agentic workflows, with Claude Code and Codex named as adoption examples; exact model/build versions not supplied | Study details; “Wider adoption of AI has made it more difficult to measure task-level productivity” |
| Raw time estimates | Returning: −18%, 95% CI −38 to +9%; new: −4%, CI −15 to +9% | Opening results paragraphs |
| Selection | Reluctance to work without AI, task withholding and differential participation; lower pay than earlier trial | “Wider adoption of AI tools…”; study details |
| Measurement | Concurrent agents complicate time attribution | Opening summary; “Wider adoption of AI has made it more difficult to measure task-level productivity”, numbered problem 6 |

Both intervals cross zero. Negative signed time changes mean less estimated task time; the article's “speedup” terminology must not be converted into an equally sized throughput gain.

## Calculations and interpretations

**Derived:** No pooled effect, reweighted population effect or current productivity percentage is calculated here. The two cohort estimates are kept separate.

**Source-author interpretation:** AI probably helps more than in early 2025, but selection and measurement problems make this experiment an unreliable measure of the present magnitude (opening summary and design discussion).

**Repository interpretation:** Put this update immediately beside the historical METR result. It prevents a time-stamped +19% finding from becoming a claim about current tools. It also prevents the opposite error: presenting the later raw estimates as proof of a general speedup or a causal reversal of the earlier experiment.

## Limitations, conflicts and claims not established

Selection into participation and submitted tasks, changed compensation ($50/hour versus $150 earlier), task mix and concurrent work limit interpretation (study details). These are substantive identification concerns, not merely wider confidence intervals. The author organization is the same METR research team; the article does not supply a separate funding declaration. Do not infer independence from the original team or unreported vendor sponsorship.

**Not established:** reliable current magnitude, an industry trend, universal acceleration, or invalidity of the original randomized result. The update does not measure end-to-end enterprise delivery or TCO.

## Repository use and placement

- `report/01_the_illusion.md`, Chapter 1: separate dated row next to the 2025 result, interpretation boundary, conclusion and references.
- `report/03_the_aftermath.md`, Chapter 8 opening: time-bounded summary of the comparison.
- `README.md`: Evidence Map navigation.
- `REFERENCES.md`: separate citation, not a replacement for P-2025-01.
- `evidence/primary/2025-metr-experienced-developer-productivity.md`: author's retrospective interval for the original trial and separate temporal update.

See the [issue #57 trace](../../governance/reviews/issue-57-2026-10-20-productivity-audit.md). The original study and follow-up remain distinct source objects; this entry was registered before adding any report use.

## Repository integration audit

- Integration status: Verified — independently Confirmed corrections merged in PR #66; main `21af254361dbd4f8d158516c1699fec7661e6312` checked on 2026-10-20. See the issue #57 trace for default-branch acceptance and remaining source limitations.
- Search/report/numeric/README/bibliography/current-use checks: candidate and exact locators in the issue #57 trace.
- Protocol outcome: No protocol change — none of the four protocols treats these raw estimates as a threshold or validated control.
- Corrections: add the temporal boundary without substituting an unreliable present-day estimate.
- Verification date: 2026-10-20.

## Independent review

- Primary agent: /root.
- Independent reviewer: /root/independent_evidence_review.
- Flow reviewed: A, alongside Flow B for P-2023-01/P-2025-01.
- Materials independently checked: full original update, selection/measurement warnings, placement, source separation and AC-01–AC-05.
- Outcome: Confirmed — repeated independent review on 2026-10-20 at commit `91edb633d2d2f352a43c2333e80d5def9614b9f4`, tree `02fa53f8dfe0c23f1a2c62830d2716916da3aee9`; complete correction history and acceptance results in the issue #57 trace.
- Corrections completed: R1–R5 and precision/interval/tool boundaries independently rechecked; no unresolved correction or new human decision. Merged-main acceptance and final status review are recorded in the issue #57 trace.
- Review date: 2026-10-20.
