+++
source_ids = ["P-2025-04"]
evidence_review = "Reviewed brief"
integration_audit = "In progress"
last_verified = "—"
independent_review = "Review unavailable"
current_use = ["README.md", "report/01_the_illusion.md", "report/02_broken_mechanics.md", "report/03_the_aftermath.md", "REFERENCES.md"]
+++

# GitClear: historical code-change and clone signals

## Citation, edition and access

William Harding, Lead Researcher/CEO, Alloy.dev Research / GitClear. *AI Copilot Code Quality: Evaluating 2024's Increased Defect Rate via Code Quality Metrics*. **P-2025-04; primary empirical research; self-published commercial report**, February 2025. Peer review is not established. Footer edition **v2025.2.5**; Updates (PDF p34) states publication on 4 February and no subsequent updates, so the footer is not silently converted into a publication date.

Full [34-page original PDF](https://gitclear-public.s3.us-west-2.amazonaws.com/GitClear-AI-Copilot-Code-Quality-2025.pdf) and [publisher landing page](https://www.gitclear.com/ai_assistant_code_quality_2025_research) inspected 2026-10-20, including appendices and rendered tables. PDF SHA-256: `5c5291d96a25dbba88b6c14993261c969406ee5ac459846f62b82687baf992a5`.

The landing page requests contact details and the older unprefixed PDF URL returns redirect HTML. The accessible original above is on the publisher's public bucket; no form, login, payment or private access was used. The earlier #53 access gap is dated history, resolved for this edition. No raw-database or analysis-code reanalysis was performed; the arithmetic below reproduces published aggregates only.

## Design, population and metric boundaries

Descriptive historical trends, **January 2020–December 2024**, in vendor-selected commercial and open-source repositories. The paper describes the data mix as roughly two-thirds opted-in private corporations and one-third OSS (A2, pp26–27). It does not identify actual AI exposure for each contributor, commit or line, randomize use, or provide an identified AI/no-AI counterfactual. Changing customers and project/task mix can affect year comparisons (A1, p24).

The main operation sample is approximately **211 million meaningful changed lines**; summing A1's 2020–24 denominators gives **211,087,305** (derived). This counts changes, not a stock of unique source lines, developers, or the productivity study's cohort. No-op and other excluded/generated-file changes are omitted (A0/A2, pp23,26). Six operation categories describe change composition; churn overlaps those categories rather than forming a seventh disjoint share.

| Measure | Definition and original locator |
| --- | --- |
| Moved lines | Content relocated to another file/function, allowing leading whitespace changes; a refactoring/reuse proxy, not all refactoring or modularity. A0 p23 |
| Copy/pasted lines | Matching non-keyword contents committed to multiple functions/files within a commit; distinct from commits containing a clone. A0 p23; explanation p11 |
| All-line churn | Authored/pushed code reverted or substantially revised within two weeks, overlapping operations. A0 pp23–24; not measured defects |
| Clone-containing commits | Scanned commits with at least one Type 1 repeated block of ≥5 contiguous nonblank/non-keyword lines. Table p12, A5/A8 pp28,31; not total blocks or all clone types |

## Findings and reproduced arithmetic

For operation shares below, **derived = 100 × A1 operation count / that year's changed-line denominator**, rounded to two decimals. The count table (p24) supplies an inspectable numerator and denominator; this choice does not adjudicate conflicting source versions.

| Metric / year | Numerator / denominator | Derived share |
| --- | --- | --- |
| Moved, 2021 | 9,275,559 / 37,635,351 | 24.65% |
| Moved, 2024 | 5,564,610 / 58,755,703 | 9.47% |
| Copy/pasted, 2020 | 2,431,654 / 27,433,911 | 8.86% |
| Copy/pasted, 2024 | 7,236,304 / 58,755,703 | 12.32% |
| All-line two-week churn, 2020 | 837,906 / 27,433,911 | 3.05% |
| All-line two-week churn, 2024 | 3,331,468 / 58,755,703 | 5.67% |
| Clone-containing commits, 2020 | 139 / 19,805 scanned commits | 0.70% |
| Clone-containing commits, 2024 | 3,764 / 56,495 scanned commits | 6.66% |

The last two fractions reproduce p12; **6.66% is 2024**, not 2025. The block table also counts 9,227/63,566 total detected blocks in those years; those are different numerators. A8 p31 backfilled the largest 1,000 commits by Diff Delta per repository across 2020–23, rather than establishing identical sampling in every year. Treat the contrast as descriptive in those scanned sets, not a representative causal industry effect. Confidence intervals are not reported for these aggregate comparisons.

The new-line revision analysis (pp19–20/A7 p31) uses a separate approximately 45-million-new-line subset and two-/four-week windows. It must not be substituted for the all-line churn series. The authors also acknowledge useful AI-assisted consistency work and that some early revision is beneficial (pp9,19,21); higher counts alone cannot establish waste.

## Internal discrepancies and interpretations

- The main p7 table reports moved 24.8% (2021)/9.5% (2024), and copy/paste 8.3% (2020)/12.3% (2024). Some main-table values differ from A1's counts/shares beyond rounding. Page 10 also uses 16.9%/44% for a decline whose main table has 15.8%/39.9%. Preserve these as source reporting discrepancies, not repaired data.
- The main text's eight-fold/approximately ten-fold clone language (pp5,12) does not consistently specify or reproduce the p12 endpoints; the report uses counts/shares instead. The current landing graphic has a different historical series and labels 6.66% as a 2025 estimate. No authoritative reconciliation was found; the pinned PDF table governs the explicitly identified PDF result, without treating the landing graphic as equivalent.
- A1's 2025 rows are projections in a February 2025 report, not observed full-year outcomes. They are excluded from the observed comparison.
- A6 pp29–31 is the author's rough historical Copilot-context estimate. It assumes file sizes and characters/token and admits no documented limit; “ten files” is not a measured general model capability. Its own 3,750 tokens/file and 8,000-token assumption yield about 2.13 files (derived), rather than its prose's roughly three. No current product specification is established here.

**Source-author interpretation:** these patterns threaten maintainability and may reflect growing AI use. **Repository interpretation:** they motivate local measurement of duplication/rework and review effort; they do not prove causation, universal loss of reuse, indexability decline, review-agent failure or lifecycle TCO. The paper's cited DORA/clone studies and generated literature synopsis are not independently reviewed empirical findings of this dataset and are not adopted as such.

Limitations include selection, unbalanced/changing samples, proprietary classification and clone backfill, no direct exposure or downstream outcome identification, no independent replication, and internal reporting differences. The author leads a company selling the analytics/review products described in A3 (p27), a documented commercial interest; no separate study-funding declaration was identified. This is a conflict to disclose, not evidence of misconduct.

## Repository use and placement

- `report/01_the_illusion.md`: Ch1 separate quality block/references and bounded relying interpretation; Ch4 source boundary.
- `report/02_broken_mechanics.md`: Ch6 context/reuse/agent scenario, with observed proxies separated from proposed mechanisms.
- `report/03_the_aftermath.md`: Ch8 dependent summary bounds the review-automation scenario without a measured net-burden claim.
- `README.md`: separate Evidence Map navigation; `REFERENCES.md`: pinned full citation/access.
- [Issue #59 trace](../../governance/reviews/issue-59-2026-10-20-gitclear-audit.md): every occurrence, numbers/units, interpretation and placement; protocol outcome **No protocol change**.

## Repository integration audit

- Integration audit: In progress; Last verified: —. All-use search, numeric/placement trace and synchronization are recorded in #59. Corrections require separate confirmation, merge and checked main before final verification.
- Protocol outcome: No protocol change — existing local diagnostic/proposed controls do not derive a validated threshold from this source.

## Independent review

- Primary agent: /root; flow B; date: 2026-10-20.
- Separate candidate review pending; outcome: Review unavailable. No readiness, completed review or verification inferred.
