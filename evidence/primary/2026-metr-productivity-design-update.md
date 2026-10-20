+++
source_ids = ["P-2026-03"]
evidence_review = "Reviewed brief"
integration_audit = "In progress"
last_verified = "—"
independent_review = "Review unavailable"
current_use = ["README.md", "report/01_the_illusion.md", "report/03_the_aftermath.md", "REFERENCES.md"]
+++

# METR: follow-up selection and measurement limits

## Citation, version and acquisition

Joel Becker, Nate Rush, Tom Cunningham, David Rein and Khalid Mahamud. [*We are Changing our Developer Productivity Experiment Design*](https://metr.org/blog/2026-02-24-uplift-update/). METR, 24 February 2026; accessed 2026-10-20.

**P-2026-03; primary empirical research update.** This is a first-party research blog with original experimental results and design discussion, not an established peer-reviewed paper. The full public article was accessible. This review does not analyze unpublished participant/task records or establish a reliable current causal magnitude.

## Research question, design and observed findings

| Item | Source-reported detail | Exact locator in article |
| --- | --- | --- |
| Follow-up | Started August 2025; 57 developers: 10 returning and 47 new; 143 repositories, 800+ tasks | “Details of the productivity study” |
| Comparator | Randomized AI-allowed/disallowed work; later tools and selected tasks | Same section; opening summary |
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

See the [issue #57 trace](../../governance/reviews/issue-57-2026-10-20-productivity-audit.md). The original study and follow-up remain distinct source objects; this entry was registered before adding any report use.

## Repository integration audit

- Integration status: In progress; default-branch verification pending.
- Search/report/numeric/README/bibliography/current-use checks: candidate and exact locators in the issue #57 trace.
- Protocol outcome: No protocol change — none of the four protocols treats these raw estimates as a threshold or validated control.
- Corrections: add the temporal boundary without substituting an unreliable present-day estimate.
- Verification date: —.

## Independent review

- Primary agent: /root.
- Independent reviewer: pending separate review.
- Flow reviewed: A, alongside Flow B for P-2023-01/P-2025-01.
- Materials to check: full original update, selection/measurement warnings, placement, source separation and AC-01–AC-05.
- Outcome: Review unavailable — interim pending review, not completion.
- Discrepancies/corrections/human decision: pending review; authorized treatment in issue #57 and its trace.
- Review date: —.
