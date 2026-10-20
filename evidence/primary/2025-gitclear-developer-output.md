+++
source_ids = ["P-2025-05"]
evidence_review = "Reviewed brief"
integration_audit = "In progress"
last_verified = "—"
independent_review = "Review unavailable"
current_use = ["README.md", "report/01_the_illusion.md", "report/02_broken_mechanics.md", "report/03_the_aftermath.md", "REFERENCES.md"]
+++

# GitClear: separate developer-output measures

## Citation, version and access

Bill Harding, CEO/Programmer, GitClear. *How much more productive are AI-powered developers? Large sample productivity data*. **P-2025-05; primary empirical research; self-published commercial measurement report**, not established as peer reviewed. [Publisher](https://www.gitclear.com/research/ai_tool_impact_on_developer_productive_output_from_2022_to_2025) displays last updated **1 October 2025**. Its [full public embedded original](https://public.amplenote.com/embed/w32ZX4GJ7ZwJasUQ1K7kqLqE) also contains later update text; the page date does not establish an immutable historical version.

Full embedded report, original tables and figures inspected **2026-10-20**. Acquired embed URL also included publisher-host/style parameters; HTML snapshot SHA-256 `8e33c8bfbc3df94a47c1c9fc450d0baeeccb8f4959f49c4092b221a2e8bb19aa`. No raw GitHub/GitClear database, spreadsheet or analysis-code rerun; simple aggregate arithmetic is identified below. This is a different source/sample from GitClear's quality report.

## Research question, design and sample

Descriptive comparisons of output against 2022, concurrent with widespread AI adoption, **not** an individually observed AI-use treatment/control experiment. The original says actual AI use is not directly measured in this analysis. Popularity/adoption surveys cited by the author do not assign exposure to these records.

| Method / exact original section | Population, unit and window | Reported 2025 contrast versus 2022 |
| --- | --- | --- |
| Method 1: aggregate commit distribution | Same 17,341 GitHub contributors with ≥500 commits in each studied year, excluding usernames ending in “bot.” Annual counts; 2025 is trailing 365 days in September/October 2025, not completed calendar 2025 | Median 1,162→1,241: +6.8%. Mean has unresolved reporting discrepancy below |
| Method 2: individual baseline ratios | Same cohort; calculate each contributor's percent change against their own 2022 count, then summarize ratios | Median +6.1%; mean +49.5%. This is not the ratio of cohort medians/means |
| Method 3: proprietary Diff Delta | GitClear sample varies: 132 in 2022, 286 in 2025. Annual metric; method appendix excludes contributors without sufficient January activity; the trailing-window footnote specifically describes commit counts, not all four methods | Median 40,140→45,799: +14.1%; mean 49,319→52,318: +6.1% |
| Method 4: added-line output | Selected developer-month records: ≥50 commits/month and ≥10 added lines; monthly lines added grouped by year. Table labels sample size 655→3,162, but does not establish these as unique contributors; sample composition changes | Mean 1,314→3,037: +131.1%; median 921→1,624: +76.3% |

Methods 3/4 use opted-in commercial/OSS GitClear data, not Method 1/2's matched-person cohort. The report does not provide an equally precise 2025 endpoint for every measure; do not silently apply the commit-count 365-day window to all metrics. Its approximately 75,000 developer-years headline is not a count of independent developers; Methods 1/2 reuse the same people. The table values are reported descriptive contrasts; uncertainty intervals/causal identification are absent. Earlier Diff Delta results include a negative median contrast in 2023 (−12.6%), so the trajectory is not uniformly positive.

## Calculations and source reporting discrepancy

- **Derived reproduction of source's median composite:** `(6.8 + 6.1 + 14.1) / 3 = 9.0%`, using Methods 1–3. The repository's former two-input formula `(6.1 + 14.1) / 2 = 10.1%` could not yield 9.0%. Even the corrected composite mixes different estimands/cohorts and twice weights commit-based metrics from the same cohort. It is not net delivery productivity, an AI causal effect or a cost-adjusted outcome; the report presents the component measures separately instead.
- **Unresolved Method 1 mean:** its method table/text gives +34.1%, consistent with `(2062 / 1538 − 1) × 100 = 34.07%` from rounded printed means. The later average-output summary gives **+7.1%**. The source's displayed mean composite +20.9% uses `(7.1+49.5+6.1)/3`, rather than the method section's mean. No authoritative correction was located. Both locators remain documented; neither Method 1 mean nor the dependent mean composite is adopted as a headline estimate.
- Method 4's reported +131.1%/+76.3% reproduce, after rounding, the mean and median level ratios above. They are changes in selected monthly added-line output, not a measured doubling in every team's review intake or a throughput multiplier.

## Interpretation, limits and conflicts

**Source-author interpretation:** increased output plausibly reflects AI's spread, with maintenance risks and concentrated gains among high-output developers. **Repository interpretation:** the positive activity changes are useful descriptive evidence, and their differing size shows why measurement choice matters. A larger code count does not itself establish more value, more defects or higher maintenance cost. There is no observed senior/junior conversion ratio or tested review-agent performance in this dataset.

Confounders include survival/high-activity selection, task/project and employment changes, time trends, unobserved exposure and differing cohorts/windows. Diff Delta is a proprietary weighted code-change measure, not literal lines or validated shipped value; code, commits and time are different units. Raw data/queries were not independently reproduced here. No downstream review-time, release, defect, total-cost or human cognitive-load outcome establishes net benefit/harm. Commercial interest is explicit: the author leads GitClear, whose product calculates the metric and supplies some of the data; separate study-funding information was not identified. No misconduct is inferred.

## Repository use and placement

- `report/01_the_illusion.md`: distinct Ch1 output comparison, arithmetic/boundary, relying hypothesis/references; Ch2/Ch4 remove universal volume extrapolation.
- `report/02_broken_mechanics.md`: Ch5 conditional review-intake scenario instead of a universal staffing multiplier.
- `report/03_the_aftermath.md`: Ch8 separates the conditional automation case from observed output metrics.
- `README.md`: Evidence Map brief navigation; `REFERENCES.md`: full source/edition/access citation.
- [Issue #59 trace](../../governance/reviews/issue-59-2026-10-20-gitclear-audit.md) records all-use, numerical and placement checks; **No protocol change**, since local diagnostic/proposed controls do not derive thresholds from these estimates.

## Repository integration audit

- Integration audit: In progress; Last verified: —. All-use search, numeric/placement trace and synchronization are recorded in #59. Corrections require separate confirmation, merge and checked main before final verification.
- Protocol outcome: No protocol change — existing local diagnostic/proposed controls do not derive a validated threshold from this source.

## Independent review

- Primary agent: /root; flow B; date: 2026-10-20.
- Separate candidate review pending; outcome: Review unavailable. No readiness, completed review or verification inferred.
