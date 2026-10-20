# Issue #58: Xu/Agarwal source, occurrence and placement audit

## Intent, authorization and start

Owner: [#58](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/58), child of #53. Primary agent: /root. Primary flow B for P-2025-03/P-2026-02; full evidence review and every-use integration audit, synchronization and separate review required. Current AGENTS and mandatory playbooks read before work; no nested AGENTS. Start base/main `384929717ff8d3129b7e90990c11132f161194ba`, tree `5a75b50e7137ba410e3badc42d7d58ea8ef00f16`; clean before branch `work/issue-58-xu-agarwal`.

Maintainer decision, 2026-10-20: correct evidence, numbers, placement and unsupported/vendor-accusing claims, one issue at a time, then independent review, acceptance, evidence and closure. The current instruction adds status checking and authorizes the next planned issue. [Start declaration](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/58#issuecomment-6297782350) and [pre-edit impact/decision report](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/58#issuecomment-6297923181) preserve the exact treatment before substantive editing. This is existing explicit approval, not approval inferred from silence.

Previously, R1 called core/peripheral activity senior/junior productivity, attributed hours/displacement to review counts, treated bottom-quartile gains as all peripheral gains, and combined aggregate static metrics into per-feature debt and a measured SDLC chain. Approved treatment: retain and bound both studies, preserve positive/null results, correct each use and distinguish the proposed mechanism. No-change would preserve factual defects; removal would discard useful mixed evidence. Both alternatives rejected within the approved correction scope. No protocol logic, confidence classification, source-state definition, canonical workflow or contributor obligation changes. Source/internal-data uncertainty remains disclosed; all edits are reviewable/reversible.

## Original acquisition and numerical check

- [Xu v3](https://arxiv.org/abs/2510.10165v3), dated 2026-01-28: full 29-page PDF and HTML inspected, especially PDF-only p29 Tables 11–14; brief records SHA-256, history, methods, sample, metrics and unresolved internal reporting discrepancies. Preprint edition; presentations are not peer-review proof.
- [Agarwal v2](https://arxiv.org/abs/2601.13597v2), dated 2026-01-27: full five-page PDF/HTML, Table 2 p3 and Figure 2 p4 inspected. Official MSR 2026 Mining Challenge program confirms conference listing, title/authors and linked ACM DOI; publisher full text inaccessible, final-edition equivalence unresolved. No claim to have compared that edition.
- Original PDFs were rendered and key tables/figure visually inspected, not just extracted text. No dataset/replication code rerun. Described datasets are not independently reused repository assets.
- Xu Table 13: `100*(exp(.3614)-1)=43.53`; core `exp(-.2149)-1=-19.34%`; Table 11 `exp(.0628)-1=6.48%`. Transforming its printed 95% endpoints yields −0.89 to +14.40%, consistent with p=.086. These are derived transformed-count effects, not hours/throughput. Table 5 commits are only p<.10; rework controls PR count rather than defining a per-PR outcome.
- Agarwal Table 2's printed percentages retained rather than rederived from rounded coefficients. AF/IF results and SE/significance reproduced separately in the brief. IF warnings and both IF activity estimates are inconclusive at 5%; complexity estimates have pre-treatment diagnostic concerns. Positive AF activity cannot be omitted.

## Search scope and occurrence trace

Searched all tracked text for IDs, names, title/URL fragments, `10,000`, `43.5`, `6.5`, `2.4%`, `39%`, `18%`, `19%`, core/peripheral, senior/junior, review/rework, cognitive complexity/load, per-feature/per-unit and uncited labor-redistribution claims. Inspected every report part, all four protocols and index, README claims/maps/diagrams, source registry, bibliography, evidence briefs/indexes and governance/task history. Checked adjacent paragraphs and conclusions, not only named citations.

Locators below identify stable sections/paragraphs rather than line numbers that drift. Each row separately records interpretation, numbers/units and placement. “Keep” means retain the bounded corrected use, not endorse the source's causal interpretation.

| ID | Material use and current location | Original locator / metric | Wording/inference and numerical action | Placement / better destination |
| --- | --- | --- | --- | --- |
| X01 | R1 Ch1 Xu introduction | §§3.1–3.3 pp10–14 | Replace unspecified pending/enterprise frame with 2,755 OSS repos/1,699 contributors, availability proxy and DiD assumptions | Keep separate observational block after experiments; detailed filters in Xu brief |
| X02 | R1 Ch1 Xu activity bullets | Table 5 p16; Table 13 p29 | Retain positive project +17.7/+4.3/+4.1 with p thresholds; bottom +43.5/core −19.3 are activity quartiles, not juniors/seniors or all peripheral contributors | Keep central mixed finding; coefficients/derived CIs in brief |
| X03 | R1 Ch1 review/rework bullet and final source paragraph | Tables 11/13 p29; Table 5 p16 | +6.5 review counts has p=.086/CI crossing zero; +2.4 repository-month follow-up commits controls PR count. Remove forced displacement, per-PR defects and disappearing aggregate gains | Keep uncertainty next to claim; internal table discrepancies in brief |
| X04 | R1 Ch1 mechanism hypothesis following Xu | §4.2/§6 pp17–22; activity proxies only | Review-capacity mechanism is explicitly repository hypothesis with alternatives and weakening observations; no measured cross-team labor displacement | Keep as hypothesis after findings, not inside empirical bullets |
| A01 | R1 Ch1 Agarwal introduction/table | §§3.1–3.3 pp2–3; Table 2 p3 | Replace AI-codebase versus human-codebase comparison with repository-month AF401/606 and IF117/73; exposure traces are proxies | Keep dedicated observational section; design detail in brief |
| A02 | R1 Ch1 Agarwal activity/structure/warning results | Table 2 p3; Figure 2/§4 p4 | Show AF +36.25/+76.59 activity, IF inconclusive +3.06/−6.34; complexity +34.85/+42.87; warnings +17.73/+19.00 significant only AF. No uniform +39/+18 claim | Keep mode-specific table central; all six outcomes/SEs in brief |
| A03 | R1 Ch1 Agarwal implication/limitations | §3.2 p3; §4/Figure 2 p4 | Remove functional-correctness, measured cognitive-load and +39% per-feature debt inferences. Keep pre-treatment signals/causal limits near findings; proposed review-cost mechanism distinguished | Keep bounded hypothesis after results; further lifecycle/mechanism work #63/#64 |
| A04 | R1 Ch1 GitClear transition | No jointly observed source result | Remove “overlay completes picture”; mark source/sample independence and pending GitClear audit | Keep transition/boundary; GitClear numbers/methods owned by #59 |
| XA05 | R1 Ch1 conclusion, added observational paragraph | Xu Table 5/p29; Agarwal Table 2 | Retain positive Xu/AF activity and uncertain IF results. No aggregate-loss, per-feature or one-chain inference | Keep conclusion beside existing task-time conclusion; no changes to Peng/METR findings |
| X06 | R1 Ch1 Xu reference item | v3; §§3.1–3.3, Tables 5/11/13 | Remove 10,000+ developers, seniors/hours and all-peripheral +43.5; pin v3/brief and bounded sample/outcomes | Keep concise reference; full title/history in bibliography/brief |
| A07 | R1 Ch1 Agarwal reference item | v2 Table 2; official venue | Replace uniform quality harm with separate panels, IF uncertainty, static-metric boundary and publisher-edition access gap | Keep concise reference; full publication metadata in bibliography/brief |
| XA08 | R1 Ch4 post-diagram pipeline paragraph | Xu Table 5; Agarwal Table 2 | Remove jointly measured doubled-volume/+39/+18 and universal junior-speedup chain; preserve positive/uncertain outcomes and independent samples | Keep systems-scenario setup; empirical figures remain in Ch1/briefs |
| X09 | R1 Ch4 Inventory Problem / WIP bullet | Xu Tables 11/13 p29 | Remove measured WIP/senior triage; fewer core commits and uncertain review-count change do not measure queues or hours | Keep conditional WIP question with brief link; direct WIP evidence requires further study |
| A10 | R1 Ch4 Inventory Problem / Cognitive Load bullet | Agarwal Table 2, §3.2 p3 | Replace +39% mental effort per review with +34.85/+42.87 aggregate complexity and explicit absence of human-load/time measure | Keep risk hypothesis; human effort must be locally measured |
| XA11 | R1 Ch4 “Safe Adoption” introduction and numbered loop | Neither source measures whole SDLC loop | Remove factual senior bottleneck and fixed cross-study numeric inputs; label conditional scenario, no per-unit complexity rate; give weakening observations | Keep as systems scenario, with exact measurements in Ch1; wider mechanism/tone review #63/#64 remains |
| XA12 | R1 Ch4 cross-reference item | Both briefs' metric boundaries | Remove one numerical causal-chain shorthand; distinguish activity/proxies/static metrics, positive/null results and pending GitClear/secondary audits | Keep brief navigation; no new source support |
| XA13 | README Evidence Map row | Both originals, described in briefs | Add brief links and bounded activity/structure descriptions; no causal/role claim added | Keep map navigation; detail in briefs/Ch1 |
| X14 | REFERENCES P-2025-03 | arXiv v3 metadata | Full title/authors/version/date; preprint boundary and positive/uncertain findings | Keep bibliography; states exclusively registry/front matter |
| A15 | REFERENCES P-2026-02 | arXiv v2; official program/DOI | Full title/date and conference metadata; no checked publisher-equivalence claim | Keep bibliography; access limitation in brief |
| XA16 | SOURCES and primary index | Existing IDs, both complete briefs | Preserve existing source identity strings; actual three current-use paths each; Reviewed brief/In progress/— until final gates | Keep canonical states in SOURCES/briefs; index is navigation |
| XA17 | R1 Ch4 title/TOC, opening and adoption-intro superlative | Neither original identifies a universal quality decline or ranked adoption catastrophe | Replace categorical failure/established mechanism with bounded positive/mixed findings and a conditional capacity scenario | Keep title/intro consistent with findings; full-report tone work remains #64 |
| XA18 | R1 Ch4 capacity setup, diagram and post-diagram interpretation | Neither original measures a universal senior constraint or unlimited inflow | Identify illustrative assumptions and conditional arrows; remove professional-role and universal typing-only bottleneck labels | Keep uncalibrated scenario diagram; no percentages or empirical-source endorsement |
| XA19 | R1 Ch4 conclusion | Xu Table 5; Agarwal Table 2 and missing downstream measures | Preserve positive activity, state alternative successful-delivery outcome, require local review/production measures; remove categorical inevitable traffic jam | Keep conditional conclusion aligned with chapter title; source details remain Ch1/briefs |

### Assessed non-applicable surfaces and remaining owners

- README Key Takeaways/claim-confidence map/Crisis Map: no Xu/Agarwal-specific number, role or unit; high-level possibility of downstream constraints remains a bounded inference. Crisis Map's NBER estimates and its current verification state are not adopted/reverified by #58. No confidence or diagram change.
- R2/R3 have no additional attributed Xu/Agarwal number or distinct empirical result. Their general review/automation/cognitive-load rhetoric is a scenario/tone concern, not evidence newly validated here; #63/#64 own that full audit. Secondary doubled/2–3x review-time claims are #61, not Xu review counts. Chapter 2 economic estimates and `2.4x/year` are not Xu's 2.4% rework (#60).
- R1's remaining GitClear numbers, 2–3x review-time claim, vendor/economic rhetoric, capability/horizon and NBER sections remain separately assigned #59–64. #58 does not certify them or claim whole-report neutrality/verification. No material Peng/METR empirical-use rewrite or new use path; their #57 findings and fields remain unchanged.
- Protocol 1: containment/reference patterns are proposed practices, no quartile/complexity percentage or validated effect. Protocol 2: local baselines, diagnostic complexity, separate waiting/effort and no universal threshold. Protocol 3: explicit association/causal/metric and disclosure boundaries. Protocol 4: locally assessed capacity/governance scenario, not measured by these studies. Index: protocols are adaptable patterns. **No protocol change**, for both sources.
- Doctrine/glossary/scope/artifact-model/contributor entry points/citation identity/attribution: no changed term, artifact boundary, source identity/class or rule. Existing normative distinctions cover the corrected findings. Historical #53/#57 audits and merged work records remain dated history, not new current-use endorsements; no historical TOML mutation.

## Synchronization and live-status check

Updated: two briefs; registry; primary index; R1 occurrences/neighboring synthesis; README Evidence Map; bibliography; changelog; dated memory; existing issue-workflow checklist/RI explanation and navigation aliases/manual check route; regenerated RI. All evidence/report/reader-navigation/references/governance/history surfaces assessed. Contributor guidance only clarifies already required checks; AGENTS, flows, gates, approvals, statuses and obligations unchanged. **Changelog: Updated.**

Start live observations, 2026-10-20:

| Check | Exact inspected source | Result |
| --- | --- | --- |
| Previous issue | #57 live state; completion comment 6297061565 | Closed/completed; five ACs satisfied |
| Previous PR/main | #67 merged; main `384929717ff8d3129b7e90990c11132f161194ba` | Actual merged final-state baseline |
| Exact-main CI | [39466705409](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/actions/runs/39466705409) | Success; 119 tests/contract/state/RI; transitions are a separate Repository Gate check |
| Source fields at baseline | SOURCES/briefs at that SHA | #57's three sources Verified/2026-10-20; Xu/Agarwal Registered/Not started/— |
| Active owner | #58 body + dated AC-06 addition; start comment | Open, no implementation PR at start |

Memory now records this dated checkpoint and conditional resumption via the live owner; it no longer unconditionally tells a later agent to merge/close already completed #57. RI local-byte freshness cannot establish any live state. Final issue/PR/main/CI and source-state acceptance will be recorded after actual merge, not forecast here.

## Acceptance matrix — candidate stage

| AC | Check/evidence | Result |
| --- | --- | --- |
| AC-01 | Both complete versioned briefs; original pages/tables/figure and calculations above | Passed on independently Confirmed correction candidate; merged-main check pending |
| AC-02 | X01–XA19; repeated numeric/implicit-use search | Passed on independently Confirmed correction candidate; merged-main check pending |
| AC-03 | Ch1 hypotheses/Ch4 scenario and source boundaries | Passed on independently Confirmed correction candidate; merged-main check pending |
| AC-04 | Xu project gains and AF/IF table in central Ch1/conclusion | Passed on independently Confirmed correction candidate; merged-main check pending |
| AC-05 | Separate reviewer, registry/front matter, main integration | Pending review/merge/final fields |
| AC-06 | Live-start table, memory, discoverable existing status checklist; final checkpoint | Start passed; final pending |

## Independent review

- Primary agent: /root; flow B for both sources.
- Independent reviewer: /root/review_issue58; date: 2026-10-20.
- Initial outcome: Corrections required at `ff1fe9403c08738d0775a9f6b2831ccf73d82b55`, tree `e634bceddcb132b2961148b743017653b2c492fd`. R1–R3 below; no new human decision required.
- Materials independently checked: full originals, publication/access boundaries, all occurrence rows, calculations/units/uncertainty, positive/null findings, neighboring arguments, protocol/sync/current-use, authorization, status/handoff and AC-01–06.
- Corrections, validation, merged-main checklist and final acceptance: append actual outcomes below as they occur.


## Validation before independent review

At candidate `ff1fe9403c08738d0775a9f6b2831ccf73d82b55`, tree
`e634bceddcb132b2961148b743017653b2c492fd`: 119 tests, contract, evidence-state,
RI build/verify, status-query owner and source task-context passed. Trusted-base
Repository Gate and evidence-transition module passed against base `3849297`.
An initial direct-script invocation failed on module import path; rerunning the
trusted module from its policy checkout passed. This was not a source finding.
Remote PR #68 initial head `abe9410e251ef5ea421636c0b0cbb02b434b55fc` has the same
tree; Main health run 39474382291 and Repository Gate run 39474382332 passed.
Those structural passes did not establish independent confirmation or readiness.

### Review correction log

- R1: independent reviewer found an unsupported placebo-test assertion in the Xu
  brief. Original v3 has a PR-rework event study/lead-lag analysis, CEM and Oster
  sensitivity; no placebo test was located. Removed the unsupported assertion.
- R2: independent reviewer found that memory/start table over-attributed transition
  checks to Main health run 39466705409. Corrected: Main health runs 119 tests,
  contract/state/RI; trusted transition validation is a separate Repository Gate
  check. Source/main check conclusions themselves remain as observed.
- Primary corrections are not self-confirmed; the reviewer must recheck them at
  the new pinned candidate before an outcome is recorded as Confirmed.

- R3: independent reviewer found the Ch4 opening/title and adoption-intro still
  asserted established quality degradation/failure despite later qualifications.
  Narrowed title/TOC and opening; labeled capacity setup/diagram as conditional;
  removed the “most dangerous” ranking; aligned the chapter conclusion with
  positive activity and unmeasured downstream outcomes. Added XA17–XA19. This is
  correction of the relying Xu/Agarwal argument, not a claim to finish #64.


The initial reviewer independently reopened both originals (matching PDF hashes),
checked Xu methods/Tables 5–6/11–14 and Agarwal methods/Table 2/Figure 2,
publication/access limitations and the full repository use/synchronization scope.
Their separate-worktree 119 tests, contract/state/RI/status query and trusted-base
Repository Gate/transitions passed. No additional numerical/material synchronization
defect was found. Primary implemented R1–R3; source/work-record outcomes remain
Corrections required until independently rechecked. No readiness or Verified claim.


### Repeated independent review — Confirmed

Reviewer /root/review_issue58, 2026-10-20, independently rechecked corrected
`48f9292881ce9d9df5f7277dfce5a91cb6741eb5`, tree
`e25e689db69a2f7a675e4e9c84a0602b4ee1538a`: **Confirmed**. R1–R3 resolved;
full correction diff and relying context checked, including title/TOC, conditional
diagram/setup/conclusion and the retained METR boundary. No material discrepancy
or new maintainer decision remains within the approved correction scope.
Independent 119 tests, contract/state/RI, status query/task context and trusted-base
Repository Gate/evidence transitions passed in a separate worktree. Reviewer
also independently fetched initial successful PR runs 39474382291/39474382332.

The subsequent metadata update records this actual outcome, restores both source
integrations to In progress/— and rebuilds RI; no research text changes after the
Confirmed candidate. This confirms the corrections, not merged-main verification.
AC-01–04 pass at correction-candidate scope; AC-05/final AC-06 await actual merge,
main checks and final state acceptance. The remaining completion steps stay open.


## Checked default-branch acceptance — 2026-10-20

Correction PR [#68](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/pull/68)
merged at **bc0e4621d87e28137215573f963ae66b9a78da2b**, tree
**af3c1ce73304e6f2c4e9d8c0e1b65144e8d6b7ff**. Live main matches that merge;
its entire tree is identical to remote reviewed head d356251c671d4df59bf909641ac6581bb72c1f1e.
Metadata-only independent check also Confirmed that exact tree at local a5050e1;
report/empirical brief bodies match the Confirmed correction candidate 48f9292.
Primary 119 tests, repository contract, state integrity, RI freshness and status
query passed from a separate checkout of the actual merged main.
[Main health 39475740670](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/actions/runs/39475740670)
succeeded at the exact merge SHA (tests/contract/state/RI). Before merge, exact-head
[Main health 39475471984](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/actions/runs/39475471984)
and latest [Repository Gate 39475603480](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/actions/runs/39475603480)
succeeded; trusted Gate/state/transitions also passed locally against base 3849297.
Source fields on that checked main were Reviewed brief/In progress/—/Confirmed,
three current-use paths each; no final verification was inferred from the PR/CI.

### Integration completion checklist — both sources

- [x] Current AGENTS and mandatory Flow B/cross-cutting playbooks read first.
- [x] Exact versions, original ground-truth fields and access/publication bounds checked.
- [x] Both complete reviewed evidence briefs exist and are indexed.
- [x] Every named/numeric/uncited/diagram/neighboring/protocol use searched and inspected.
- [x] X01–XA19 give each material use, exact result/unit, inference and placement decision.
- [x] Samples, denominators, periods, transformed counts, uncertainty and calculations checked.
- [x] Claim strength and nearby argument corrected under original design/scope limits.
- [x] Report, README claims/maps/diagrams and neighboring conclusions assessed.
- [x] Exactly one protocol outcome: No protocol change, for both sources.
- [x] Exact substantive treatment approved before implementation; decision links above.
- [x] Current use is actual README/R1/REFERENCES, three paths per source.
- [x] Brief/registry/index/bibliography/links/version and removed claims synchronized.
- [x] Separate review Confirmed; R1–R3 and metadata independently rechecked.
- [x] Registry/brief fields and dates agree; final candidate uses Verified/2026-10-20.
- [x] No unresolved correction or new human decision in accepted #58 scope.

This checklist records completed research corrections on the checked default
branch, not a claim that source-internal uncertainty disappeared. The final-state
PR changes only matched fields/verification records, changelog, dated memory,
new append-only work record and derived RI. Final independent review and its
actual resulting main/CI/closure evidence will be appended to #58/PR completion
comments after they occur; this candidate does not forecast those future events.

| AC | Default-branch evidence | Status at final-state preparation |
| --- | --- | --- |
| AC-01 | Both full pinned briefs, locators and original/render checks on bc0e462 | Passed |
| AC-02 | X01–XA19; matched checked tree; source/body numeric review | Passed |
| AC-03 | Conditional Ch1/Ch4 findings/scenario distinction on bc0e462 | Passed |
| AC-04 | Positive Xu/AF and uncertain IF results central in Ch1/conclusion | Passed |
| AC-05 | Correction/metadata review Confirmed; all corrections on checked main | Final matched-state review/merge pending |
| AC-06 | Start/live merged checkpoint, actual main/CI/source fields and conditional memory | Final resulting main/CI/issue checkpoint pending |
