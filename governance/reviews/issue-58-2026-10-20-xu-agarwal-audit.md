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
| Exact-main CI | [39466705409](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/actions/runs/39466705409) | Success; 119 tests/contract/state/RI/transitions |
| Source fields at baseline | SOURCES/briefs at that SHA | #57's three sources Verified/2026-10-20; Xu/Agarwal Registered/Not started/— |
| Active owner | #58 body + dated AC-06 addition; start comment | Open, no implementation PR at start |

Memory now records this dated checkpoint and conditional resumption via the live owner; it no longer unconditionally tells a later agent to merge/close already completed #57. RI local-byte freshness cannot establish any live state. Final issue/PR/main/CI and source-state acceptance will be recorded after actual merge, not forecast here.

## Acceptance matrix — candidate stage

| AC | Check/evidence | Result |
| --- | --- | --- |
| AC-01 | Both complete versioned briefs; original pages/tables/figure and calculations above | Implemented; independent check pending |
| AC-02 | X01–XA16; repeated numeric/implicit-use search | Implemented; independent check pending |
| AC-03 | Ch1 hypotheses/Ch4 scenario and source boundaries | Implemented; independent check pending |
| AC-04 | Xu project gains and AF/IF table in central Ch1/conclusion | Implemented; independent check pending |
| AC-05 | Separate reviewer, registry/front matter, main integration | Pending review/merge/final fields |
| AC-06 | Live-start table, memory, discoverable existing status checklist; final checkpoint | Start passed; final pending |

## Independent review

- Primary agent: /root; flow B for both sources.
- Independent reviewer: pending separate agent after pinned candidate.
- Outcome: Review unavailable — review not yet performed; no readiness/verification claimed.
- Materials to check: full originals, publication/access boundaries, all occurrence rows, calculations/units/uncertainty, positive/null findings, neighboring arguments, protocol/sync/current-use, authorization, status/handoff and AC-01–06.
- Corrections, validation, merged-main checklist and final acceptance: append actual outcomes below as they occur.
