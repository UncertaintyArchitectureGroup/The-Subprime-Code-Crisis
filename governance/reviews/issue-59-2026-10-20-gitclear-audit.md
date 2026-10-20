# Issue #59: GitClear original-source and integration audit

## Scope, authorization and checkpoint

Date: 2026-10-20. Primary agent: /root. Flow B for **P-2025-04** and **P-2025-05**; evidence review, all-use integration audit, content synchronization and separate independent review required. Initial issue/start comment 6298789501; pre-edit original-source findings, exact treatment and alternatives: issue comment 6298929074. The maintainer explicitly requested numeric/wording/placement corrections and neutral, testable mechanisms, one issue through separate review, acceptance and evidence/closure; latest instruction is to do the next issue. This is the existing authority for the scoped treatment, not approval inferred from silence.

Checked starting main `b753486243875bb75ce40464f842681b2b9e1d2e`, tree `af6861ea15335e5ae5ede85737c6cfad1f06369f`; clean starting tree. #58 closed/completed, PRs #68/#69 merged; final-main Main health 39476733113 succeeded. #59 remains open. Both GitClear records initially Registered / Not started / —. No nested AGENTS. Current root AGENTS, doctrine, glossary, mandatory B/review/synchronization/status/PR/issue playbooks and affected report/README/protocols/registry/index/bibliography were inspected.

**Decision:** separate the datasets and component measures; replace unsupported universal/causal conclusions with conditional mechanisms and disconfirming observations. Alternatives were retaining the blended claims, removing all useful descriptive evidence, or treating partial access as a complete review. All were rejected in favor of versioned original evidence with limitations. This changes bounded report interpretation, not source-state definitions, workflow, protocol logic or claim-confidence categories. Dependent R1 Ch2 and R3 Ch8 uses are included to prevent contradictory retellings; issue comment 6299079326 preserves the initial scope. Wider economics, secondary evidence, NBER/horizons and whole-report tone remain #60/#61/#63/#64.

## Original-source access and ground truth

### P-2025-04 — quality

[Full 34-page publisher-bucket PDF](https://gitclear-public.s3.us-west-2.amazonaws.com/GitClear-AI-Copilot-Code-Quality-2025.pdf), William Harding, *AI Copilot Code Quality: Evaluating 2024's Increased Defect Rate via Code Quality Metrics*. Cover February 2025; footer v2025.2.5; Updates p34 says publication 4 February and no updates. Accessed 2026-10-20, 2,396,766 bytes, SHA-256 `5c5291d96a25dbba88b6c14993261c969406ee5ac459846f62b82687baf992a5`. All pages including appendices inspected; rendered pp7/12/24/30 checked. Self-published commercial measurement, not established peer review. Landing requests contact details, but this full original is public; no form/login/payment/bypass. The old unprefixed URL returns redirect HTML, not the report. The earlier #53 access gap is historical, resolved for this edition.

Jan 2020–Dec 2024 descriptive selected corporate/OSS code changes, not an individually observed AI treatment/control study. A1 denominators sum to 211,087,305 changes (derived), not unique code stock or the productivity cohort. A0 pp23–24 defines operations and overlapping two-week churn; A2 pp26–27 explains roughly two-thirds private/one-third OSS mix and exclusions without establishing exact weighting. No confidence intervals for the adopted aggregate contrasts, raw-database rerun or independent replication.

A1 p24 count fractions (derived, percent rounded to two decimals): moved 9,275,559/37,635,351 = 24.65% (2021), 5,564,610/58,755,703 = 9.47% (2024); copied 2,431,654/27,433,911 = 8.86% (2020), 7,236,304/58,755,703 = 12.32% (2024); churn 837,906/27,433,911 = 3.05% (2020), 3,331,468/58,755,703 = 5.67% (2024). These explicitly derived appendix results do not adjudicate main-table differences.

P12 clone table: 139/19,805 scanned commits = 0.70% (2020), 3,764/56,495 = 6.66% (**2024**); at least one Type 1 block of five eligible contiguous lines. These are not the 9,227/63,566 total blocks. A8 p31 backfills largest 1,000 commits by Diff Delta per repository across 2020–23, not per repository-year; equivalent selection in 2024 is not established. A7's approximately 45M new-line two-/four-week revision subset is separate from all-line churn. Reuse/moved operations are not modularity/indexability/review accuracy.

**Unresolved source reporting limits, explicitly retained:** p7 versus A1 differences beyond rounding (e.g. 2020 copy 8.3% versus derived 8.86%); p10 moved baseline/decline differs from p7; eight-/ten-fold clone wording does not consistently reproduce table baselines. The current landing image has a different historical series and places 6.66% in a 2025 estimate. The report identifies the pinned PDF table rather than merging these versions; no authoritative reconciliation was located. A1 2025 values are projections, excluded from observed comparisons. A6 pp29–31 is a rough historical context estimate (3,750 tokens/file; assumed 8k gives 2.13, not three files), not a measured universal ten-file capability or current product specification.

Positive/limiting evidence: useful consistency tasks and beneficial early revision (pp9/19/21), no measured net maintenance loss, defects or review-agent intervention. CEO/product interest is disclosed (A3 p27); absent funding disclosure is not evidence of absent conflicts or misconduct. Secondary papers cited by GitClear are not independently reviewed findings of this dataset.

### P-2025-05 — developer output

[Publisher](https://www.gitclear.com/research/ai_tool_impact_on_developer_productive_output_from_2022_to_2025), Bill Harding, *How much more productive are AI-powered developers? Large sample productivity data*. [Full public embedded original](https://public.amplenote.com/embed/w32ZX4GJ7ZwJasUQ1K7kqLqE), inspected 2026-10-20 with all methods, appendix and figures. Acquired HTML includes publisher host/style parameters; 115,967 bytes, SHA-256 `8e33c8bfbc3df94a47c1c9fc450d0baeeccb8f4959f49c4092b221a2e8bb19aa`. Publisher displays 1 October 2025 but embedded later updates make that date unsuitable as an immutable edition timestamp. No actual AI-use treatment assignment, uncertainty intervals, downstream net benefit/cost or raw-query rerun.

- Method 1 aggregate commit distribution: same 17,341 contributors with at least 500 commits each year, bot-name exclusion; calendar 2022 versus trailing 365 days in Sep/Oct 2025. Median 1,162→1,241, +6.8%.
- Method 2: same people, each compared with their own 2022 count, then distribution of percentage changes: median +6.1%, mean +49.5%. A different estimand from the ratio of cohort medians.
- Method 3 proprietary Diff Delta: changing GitClear sample 132→286, annual output; median 40,140→45,799 (+14.1%), mean 49,319→52,318 (+6.1%). Appendix excludes insufficient January activity. Precise 2025 window is not established as identical to commit counts. 2023 median −12.6% is retained, not a uniformly positive trajectory.
- Method 4 monthly added lines, selected developer-month records with at least 50 commits and ten added lines. Mean 1,314→3,037 (+131.1%), median 921→1,624 (+76.3%). Table sample labels 655→3,162 do not establish unique persons; do not conflate with the balanced cohort or apply one common endpoint.
- Source median composite `(6.8+6.1+14.1)/3 = 9.0%`; old repository `(6.1+14.1)/2 = 10.1%`. A corrected average still mixes estimands/cohorts and counts two commit metrics from the same cohort. Prefer components; neither is net delivered productivity or an AI causal effect.
- **Unresolved:** Method 1 table/text mean +34.1% matches rounded 1,538→2,062 (+34.07% derived); later average-output summary uses +7.1%. Its +20.9% mean composite uses `(7.1+49.5+6.1)/3`. Both Method 1 mean and dependent composite withheld as headline results; no author correction inferred.

The positive descriptive activity findings remain visible. Survivor/high-activity selection, changing commercial cohorts, unobserved exposure/task mix/hours and proprietary metrics preclude universal staffing/maintenance claims. Approximate 75k developer-years is not 75k independent people. CEO/product interest is disclosed without motive attribution.

## Occurrence trace: wording, numbers and placement

R1/R2/R3 denote the three `report/` files in order. Each row identifies the original locator or explicitly unmeasured mechanism, relationship, wording/numeric action, current fit and better destination. The briefs hold granular arithmetic/limitations; report locations hold bounded results or conditional interpretation. No source-level row substitutes for the occurrence rows below.

| ID / occurrence | Original locator / relationship | Wording and numeric judgment / action | Current fit / better destination |
| --- | --- | --- | --- |
| Q01 R1 Ch1 quality opening | Cover, A1 p24, A2 pp26–27; direct/derived | 211M changed-line events, Jan2020–Dec2024; no AI causation or productivity cohort | Keep historical quality block; sample/filters in quality brief |
| Q02 R1 Ch1 moved row | A0 p23, A1 p24; derived | 24.65% 2021→9.47% 2024, explicit operation-count denominators; remove death-of-reuse inference | Keep bounded proxy; calculations in quality brief |
| Q03 R1 Ch1 copied row | A0 p23/A1 p24; derived | 8.86%→12.32%, 2020/2024 within-commit line metric, not clone commits | Keep distinct row; version conflict in brief |
| Q04 R1 Ch1 clone row | Table p12, A5/A8 pp28/31; direct/derived | Counts/fractions 0.70%→6.66% in 2024, not 2025; remove 8x/10x slogan and AI attribution | Keep counts near backfill limit; alternate landing series in brief |
| Q05 R1 Ch1 churn row | A0/A1 pp23–24; derived | 3.05%→5.67%, all-line two-week overlapping churn, not measured defect rate | Keep operational signal; separate new-line subset in brief |
| Q06 R1 Ch1 quality qualification | pp7/10/12 versus A1/A8 and landing; discrepancy | Expose differing tables, projections and selection; no silent reconciliation/interval/industry estimate | Limits adjacent; exact alternate values in brief |
| P01 R1 Ch1 output opening | Methods1/2, data-source footnote; direct | 17,341 matched contributors; baseline2022 and trailing365-day2025 commit window only | Separate output block; full cohort detail in output brief |
| P02 R1 Ch1 Method1 row | Method1 table; direct | +6.8% ratio of medians 1,162→1,241; not individual median change | Keep component; mean conflict withheld |
| P03 R1 Ch1 Method2 row | Method2 table; direct | +6.1% median of individual changes, same people | Keep separate from Method1; mean+49.5 in brief |
| P04 R1 Ch1 Method3 row | Method3/appendix; direct | +14.1% median weighted Diff Delta, N132→286; no literal-LOC or causal-value conversion | Keep component/selection; earlier negative/mean in brief |
| P05 R1 Ch1 Method4 row | Method4/appendix; direct | +131.1% mean/+76.3% median monthly added lines, selected records | Keep both statistics; no universal team doubling |
| P06 R1 Ch1 composite paragraph | Three-median summary; derived | Correct9.0 formula; old two-input result10.1; remove net productivity/value label | Keep error explanation once; headline findings are separate components |
| P07 R1 Ch1 mean-discrepancy warning | Method1 and average-output summary; unresolved | 34.1 versus7.1, dependent20.9 withheld; neither repaired nor headline-adopted | Warning near results; exact arithmetic/locators in brief |
| P08 former R1 Ch1 Pichai alignment | Neither GitClear dataset; unsupported cross-measure synthesis | Remove implied agreement between blended output and executive velocity | Remove here; Ch2 executive-claim audit belongs #60/#61 |
| P09 R1 Ch1 Work Intensity | Unmeasured; repository hypothesis | No assigned significant share, measured exhaustion or causal fear; hours/task mix/comparator and weakening observation stated | Keep explicit hypothesis; survey/practitioner source audit #61 |
| QP10 R1 Ch1 governance/economics/conclusion | Neither source measures intent/TCO; proposed practice/hypothesis | Remove vendor responsibility/motive inference, toxic-assets certainty and inevitable maintenance bankruptcy; preserve positive activity | Conditional downstream-work question fits synthesis; empirical TCO belongs #60 |
| P11 R1 Ch2 capacity/cost paragraph | Output Method4 does not measure staffing/cost; hypothesis | Remove universal2x volume/18-month burnout and implied fixed effect; capacity/verification conditions explicit | Bounded transition fits; separate cost tables remain #60 |
| QP12 R1 Ch4 source comparisons | Two separate original scopes; synthesis boundary | Replace pending59 with bounded quality/output measures, not jointly observed sequence or shared NBER/Agarwal effects | Keep cross-source boundary; no neighboring verified empirical-body edits |
| P13 R2 Ch5 title/opening/output paragraph | Method4 only; direct plus scenario | Mean/median selected months, no universal senior/junior ratio, ten-person load or permanent review failure | Conditional review-capacity chapter; source methods in output brief |
| P14 R2 Ch5 plausible-code/effort example | Unmeasured scenario | 10seconds/30+minutes explicitly illustrative, no prevalence or junior/senior error-visibility estimate | Retain labeled example; secondary doubled review and METR horizons explicitly separate #61/#63 |
| P15 R2 Ch5 responses/conclusion | Unmeasured scenario/proposed local measures | Two adverse responses not exhaustive/measured; no most-seniors-rubber-stamp or collapsed-mentorship conclusion | Conditional case with alternatives/local outcomes; wider tone remains #64 |
| Q16 R2 Ch6 context paragraph | A6 pp29–31; author rough estimate | Historical assumptions, not universal/current ten-file limit or proof entire-system/RAG requirement | Keep brief historical boundary; arithmetic assumptions relocated to quality brief |
| Q17 R2 Ch6 moved/indexability | A0/A1 pp23–24; proxy/unsupported extrapolation | Explicit24.65/9.47 appendix derivation; not modularity, indexability or review-agent accuracy | Keep proxy limitation; no measured automation claim |
| QP18 R2 Ch6 title/pilot/cost/conclusion | No tested review intervention; repository hypothesis | Positive benefit/comparator, possible burden or savings; quality/effort/cost and disconfirmation | Evaluation case replaces inevitable-worse claim; protocols unchanged |
| QP19 R2 Ch7 first transition | Dependent summary, not another source result | Qualifies Ch5–6 as conditional; NBER body/horizon empirical text unchanged | Transition only; whole mechanism #63 |
| QP20 R3 Ch8 local automation/rebalancing/conclusion | Retelling of Ch6, no measured net burden | Conditional benefit/mixed/burden, linked brief boundaries; no inevitable failed local solution or mandatory whole-SDLC redesign | Keep dependent summary with correct Ch6 anchor; Ch8 task-experiment opening and Ch9–10 unchanged |
| QP21 README Evidence Map | Two distinct reviewed briefs; navigation | Separate historical quality/output labels, no numerical net claim or changed confidence | Keep source-role navigation; arithmetic only report/briefs |
| QP22 R1/R2 reference lists; REFERENCES | Full original identities/editions/access | Split former combined citation; no pending-methodology assertion or shared sample | Keep full bibliography and local brief links |
| QP23 registry/index/brief current-use | Actual five paths each; synchronization | Preserve canonical source identity strings; distinct briefs; Reviewed brief/In progress/— pending separate review and merge | Registry owns state, index navigation; dated audit is review history |

## All-use search and unchanged surfaces

Searched source IDs, GitClear/Harding, titles, Diff Delta, moved/reuse/clone/duplication/churn, 211M,131.1,76.3,6.66,0.70,9.0/10.1, context/ten files, universal doubling and dependent uncited summaries. Inspected all three reports, README text/tables/confidence/Crisis Map, all four protocols and their index, references, registry and evidence indexes. Historical #53 audit and merged work records remain dated append-only history, not rewritten as current claims. No new corpus search acceptance or source is implied.

**Protocol outcome: No protocol change.** Protocol1 pattern/refactoring controls, Protocol2 local diagnostic/baseline, Protocol3 disclosure and Protocol4 capacity/governance scenarios do not use GitClear as an empirically validated threshold, staffing conversion, AI-review intervention or causal net effect. Their proposed/local scope survives these corrections. The README confidence/Crisis Map and protocol index contain no GitClear numeric threshold and do not require a source-specific change. No source result establishes all protocol effectiveness. Whole-report mechanism/secondary/future-tone issues remain explicitly pending.

Existing Peng/METR/Xu/Agarwal/NBER empirical sections are preserved; no changed relying metric/interpretation for those sources is certified by this issue. In particular, R2's METR horizon subsection and NBER Ch7 body, R1's empirical Peng/METR/Xu/Agarwal/NBER blocks, and R3's existing Ch8 task-result opening remain outside the GitClear correction. Their current canonical states are not promoted by this audit. No doctrine/glossary/canonical process/CI/tool implementation/attribution change is needed.

## Synchronization and acceptance

Updated: two briefs, canonical registry and primary index, R1–R3 dependent uses, README brief navigation, REFERENCES, CHANGELOG and dated memory; RI regenerated after represented inputs. Exactly one new work record per PR. Contributor guidance non-applicable: no contributor/process/authority change. All historical work records unchanged.

| Acceptance | Check / current result |
| --- | --- |
| AC-01 | Two complete separately identified original-source briefs, distinct datasets/citations/current use; candidate implemented and independently Confirmed; default-branch acceptance pending |
| AC-02 | Original tables plus count/level/percent arithmetic and uncertainty/discrepancy trace above; candidate implemented, independent numerical review Confirmed; default-branch acceptance pending |
| AC-03 | Net-output label and universal staffing/maintenance/automation inferences replaced by bounded findings or falsifiable hypotheses at all dependent uses; independent review Confirmed; default-branch acceptance pending |
| AC-04 | Full public quality PDF and full public output embed inspected; hashes/version/access and unresolved internal source conflicts explicit; no partial-access promotion |
| AC-05 | Independent all-original/all-occurrence/arithmetic/protocol review Confirmed at f278d6f/tree08f98726; merged-main/final-state acceptance pending |

## Validation and independent review

Initial candidate checkpoint: primary author /root; independent reviewer pending; **Review unavailable** recorded no completed separate review at that time. Subsequent actual review is recorded below. Both sources remain Reviewed brief / In progress / —. Primary candidate checks: repository contract, evidence-state integrity, RI freshness (101 represented files), all 119 tests and git diff whitespace check passed. Trusted-base gates, review/correction evidence, actual merge/main/CI and final checklist will be appended as observed; none inferred from source availability or a passing validator.


### Independent correction review — 2026-10-20

- Primary /root; independent /root/review_issue59; Flow B. Outcome **Confirmed**, no material discrepancy or additional human decision.
- Pinned local `f278d6f5be877bd2acb9d3ed91856ecc1f3db92d`, tree `08f98726e8773eba5131e5e99339875c0191831c`; independently checked remote PR #70 head `64797cc2182abfcf312f728f3653ef0fcffb0b42` has that identical tree.
- Independently reopened full quality original/read all34pages/rendered pp12/24; reopened output original via publisher iframe including methods/tables/appendix/later updates. Both local byte counts/hashes match the briefs.
- All eight quality fractions/211,087,305 sum, source-year/selection limits, output component calculations/units/windows, 9.0/10.1 arithmetic and mean discrepancy/composite reproduced. Full report/README/protocol/registry/index/reference/current-use/placement and dependent-summary review found no omission requiring correction.
- PDF/body/landing differences and mean34.1/7.1 are **documented source limitations**, not adjudicated data repairs or validation of proprietary measurement/causal AI effect. Positive, negative and uncertain findings preserved; No protocol change confirmed.
- Previously Verified source briefs and empirical report windows compared with b753486 and unchanged; no unwarranted state reset/promotion.
- Independent contract/state/RI (both contexts, five current-use paths each), all119tests, trusted-base Repository Gate/evidence transitions and whitespace passed. Exact-head PR CI: Repository Gate39482420475/Main health39482420483 success.
- Primary acceptance agrees with this evidence and AC-01–05 implementation; source states remain Reviewed brief/In progress/—/Confirmed. Resulting review metadata will be checked separately; actual merge/main/CI/final-state/closure are pending observations.


### Checked correction main and final-state acceptance — 2026-10-20

PR #70 merged at **`69c8a1b20ce2404ab6b2e65f6315669f08975cf7`**, tree **`2d1b471f9d642283c1650644746c8659d4022329`**, identical to separately Confirmed metadata candidate `62c80eafce7992838e2b3a5562633a75c2dc2eef` (review outcome Confirmed, no findings). Research/report/bibliography bytes remain those confirmed at f278d6f. Latest ready-for-review Repository Gate39483174628 and exact-head Main health39483075536 passed before merge. Actual merged-main [Main health39483238001](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/actions/runs/39483238001) succeeded at that exact SHA. Local checked-main119tests/contract/evidence-state/RI passed; both sources matched Reviewed brief/In progress/—/Confirmed with five actual current-use paths each. Main-health does not run trusted transitions: those separately passed from b753486 policy/base during correction/review.

This final-state candidate records matching Verified/2026-10-20 fields only after that completed correction state. It does not change research, interpretations, current-use paths, protocols or source identities. Final metadata review, resulting merge/main/CI and issue closure are subsequent live facts, not predicted here.

Integration-audit completion checklist, applied separately to P-2025-04 and P-2025-05:

- [x] Current AGENTS and mandatory playbooks read before work; independent reviewer did likewise.
- [x] Correct original versions, publication status and ground truth checked; complete originals reopened independently.
- [x] Two reviewed, indexed briefs exist, not a crossed dataset/citation.
- [x] Every mention/number/uncited dependent summary/diagram/caption/protocol dependency searched and inspected.
- [x] Q01–QP23 occurrence trace records wording, units, fit and better destination.
- [x] Numerators/denominators/units/populations/windows/uncertainty/derived arithmetic checked independently.
- [x] Claims and nearby conclusions bounded to descriptive samples or explicit testable hypotheses.
- [x] All report parts and README text/tables/maps/neighbors assessed; broader owners retained.
- [x] Exactly one protocol outcome: No protocol change, with per-protocol reasons above.
- [x] Existing explicit maintainer treatment/one-issue authorization recorded before edits, comments6298929074/6299079326.
- [x] Five actual Current use paths for each source match registry/brief and inspected uses.
- [x] Briefs/registry/index/REFERENCES/links/versions/removed claims synchronized; historical work records intact.
- [x] Research and resulting metadata review separately Confirmed by /root/review_issue59.
- [x] Brief/registry fields and dates match; correction main honestly In progress/—, final-state candidate Verified/2026-10-20 based on checked merged corrections.
- [x] No outstanding repository correction or human decision; unresolved original reporting conflicts remain disclosed limits and disputed estimates are withheld.

AC-01–05 content implementation and independent review are accepted on checked correction main. The issue stays open pending this final-state candidate's separate review and actual resulting main/CI/state acceptance. Confirmation concerns accurate bounded integration; it cannot establish raw-data validity, industry representativeness, causal AI benefit/harm or whole-report verification. Next owner after completed #59 is #60, not a new cost claim in this PR.


### Independent final-state review — 2026-10-20

/root/review_issue59 **Confirmed** final-state `35dc3a8e2acf02ea4aa6c90125da9edfb1aa67ca`, tree `34c734965d13e704d732e02ddaa66bef6a1ed9ef` (independently checked identical remote PR #71 head `b1a26ce7415097edfade1c2811dbc73745d69fff`). Reopened actual PR #70/main69c8a1b/CI39483238001 including successful steps; verified two precise final states/dates, all15completion gates, unchanged source research/identities/current-use/report/protocol/bibliography/index and conditional five-section memory. No material finding or additional decision. Independent119tests/contract/state/RI/whitespace/trusted correction-main Gate/transitions passed; both RI contexts matched final fields; exact initial final-head Repository Gate39483640797 passed. Primary agrees. The new work record now records this actual outcome; final resulting-head gates, merge/main/CI and closure remain subsequent live observations at #59/PR #71, not facts inferred from this review.
