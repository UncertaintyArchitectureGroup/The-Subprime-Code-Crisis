# Issue #57: bounded productivity experiments

## Start and decision record

- Owner: [#57](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/57), child of #53. Primary implementer: /root. Base: `86060ebc08bf03a05a974f826792c5a4e6b9126e`.
- Primary Flow B for P-2023-01 and P-2025-01; companion Flow A for the separate follow-up P-2026-03. Evidence review, complete integration audit, content synchronization and separate independent review are required.
- The maintainer requested one issue at a time, implementation, independent review, acceptance, default-branch evidence and closure; the current “Роби” authorizes the explicit #57 treatment. The start/impact comment on #57 records the scope before editing. No new workflow or source-state rule is introduced.
- Trigger: the inherited audit C01–C02 identified an incorrect Peng sample, a time/rate conflation, an unsupported universal seniority narrative and a missing temporal update.
- Approved treatment: three separate briefs; correct every relying use; centralize positive and negative results; qualify adjacent task-to-delivery/seniority inferences; synchronize source metadata and navigation. Retain uncertainty and contradictory evidence.
- Alternatives: no change preserves known errors; fixing only reference numbers leaves misleading titles/conclusions; pooling studies conceals design differences. A bounded comparison with explicit limits was selected. All edits are reversible through Git; lack of a participant-level reanalysis remains explicit.
- #58 owns Xu/Agarwal's remaining metrics/design; #59 owns GitClear; #60–61 economics/surveys; #63 owns NBER and METR task horizons; #64 owns the remaining report-wide tone; #65 final synchronization. None inherits verification from #57.

## Originals and acquisition

All originals were opened as full text on 2026-10-20; methods, results, limitations and version metadata were inspected. An abstract was not used as the entire method. No underlying dataset was independently reused or reanalyzed, so no new dataset object is created.

| Source | Reviewed version and exact original | Load-bearing locators |
| --- | --- | --- |
| P-2023-01 | [Peng v1, 13 February 2023](https://arxiv.org/html/2302.06590v1) | Study Design; Results first paragraph; Figure 6 results paragraph; Table 1; Discussion |
| P-2025-01 | [METR paper v2, 25 July 2025](https://arxiv.org/html/2507.09089v2), [author report, 10 July](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) | §§2.1–2.3, 3, 4.1; Figure 1; Table 2; Appendices C.2.7, D.1–D.3, G.7; the update below explicitly restates the +2 to +39% interval |
| P-2026-03 | [METR update, 24 February 2026](https://metr.org/blog/2026-02-24-uplift-update/), public body accessed 20 October | Opening results/limitations; “Wider adoption of AI has made it more difficult to measure task-level productivity”, numbered problems 1–6; “Details of the productivity study” |

Full source-oriented reviews are [Peng](../../evidence/primary/2023-copilot-task-productivity.md), [METR 2025](../../evidence/primary/2025-metr-experienced-developer-productivity.md) and [METR 2026](../../evidence/primary/2026-metr-productivity-design-update.md). Their analytical limits and publication status apply to every use below. The update links public early/follow-up datasets and regression code. No independent raw-data/code reanalysis was performed; no inaccessibility is inferred.

## Search coverage and occurrence trace

Searches covered tracked and newly added text: IDs, Peng/Copilot, METR, titles, canonical URLs, 196, 55/55.8%, 19%, 24%, 20%, 80–90%, seniority and uncited slowdown/task-to-delivery paraphrases. All three report files, README/maps, bibliography, evidence records/indexes, all four protocols, foundation documents, attribution, governance and generated RI were inspected. Exact search commands: `rg -n -i 'Peng|METR|55[.,]8|196|19%|24%|20%|80.?90'` and `rg -n -i 'copilot|experienced.develop|task.time|great.illusion|data.shows.we|55%.productivity'`, followed by source IDs/titles/URLs and surrounding paragraphs. Historical records are classified below; they are not current research uses.

The “before” locations refer to the base SHA above. Section names locate the current occurrence after edits; stable IDs survive line shifts. Each row separates wording/inference, numbers/units, fit and destination. “Keep” means the same section remains the best destination; it does not mean unchanged text.

| ID / current location | Before → after; wording/inference | Numbers/units and original locator | Fit / action | Better destination |
| --- | --- | --- | --- | --- |
| O01 — R1 Ch1 title, TOC and opening | Universal feeling-faster/data-slower claim → heterogeneous task outcomes and open delivery question | Removed unmeasured “10x”; three source scopes above | Correct title and opening so they do not overrule caveats | Keep Ch1 entry |
| O02 — R1 “Bounded Experiments”, Peng row | Defensive positive aside → positive result in central comparison | 196 → 95 randomized (45/50), 70 completers (35/35); 55.8% speedup → conditional time reduction; 71.17/160.89 min and CI 21–89%; Peng Results/Figure 6 | Correct and relocate; equal visibility with negative finding | Opening comparison rather than later concession |
| O03 — R1 comparison, METR 2025 row | Generic experienced-developer slowdown → early-tool familiar-OSS task-time finding | 16 developers/246 completed tasks analyzed; +19% time, CI +2 to +39%; 24% forecast/20% retrospective less time; METR §3/Fig1, update opening | Keep with tool/date and uncertainty adjacent | Central comparison |
| O04 — R1 comparison, METR 2026 row | Missing → separate update with unreliable current magnitude | No raw percentage promoted as a current effect; update opening/problems 1–6 | Add temporal boundary beside historical finding | Central comparison, not replacement citation |
| O05 — R1 comparison interpretation | “Senior Penalty confirmed at scale” → no identified junior/senior or greenfield/brownfield causal contrast | Peng Table1; METR Table2/§4.1; no cross-study pooled rate | Remove unsupported synthesis; preserve both results | Immediately below comparison |
| O06 — R1 Xu heading/intro | Xu called METR scale validation → distinct design/outcome requiring own audit | Removed unsupported 10,000-enterprise wording from this joint argument; remaining Xu figures belong to #58 | Separate sources; do not certify Xu | Separate observational subsection |
| O07 — R1 mechanism paragraph | Seniors shifted author→reviewer stated as fact → conditional review-capacity hypothesis with alternatives and disconfirmation | Neither RCT measures team-wide redistribution; METR C.2.7 does not establish lower-quality PRs | Qualify adjacent inference | After separate activity evidence |
| O08 — R1 “From Task Results…” | Repeated n=196/55.8% “speedup”, junior universality and inevitable loss of local gains → refer back to bounded comparison | Remove duplicate wrong count/rate, unsupported 80–90% task mix and asserted Xu aggregate disappearance | Replace dismissal with open delivery question | Keep transition to downstream-outcome study |
| O09 — R1 “Match Productivity Claims…” | “No vendor data”, “Placebo Analytics”, generalized subjective error and “55% faster development” → outcome-specific measurement criteria | No universal survey or brownfield percentage retained; Peng Fig6, METR Fig1 support narrower points | Qualify nearby synthesis without claiming a completed literature search | Keep measurement boundary |
| O10 — R1 Ch1 conclusion | Unavoidable engineering slowdown/accelerated debt → bounded task results and conditional queue hypothesis | Does not turn task-time percentages or other proxy metrics into observed lifecycle costs | Correct relying conclusion | Keep Ch1 conclusion |
| O11 — R1 Ch1 METR reference | “Copilots make experienced developers 19% slower” → tool/date/population/task-time statement, v2 and brief | +19% time, CI +2 to +39%, 16/246 completed; same locators as O03 | Correct duplicate summary | Keep chapter bibliography |
| O12 — R1 Ch1 Peng reference | n=196, 55.8% speedup, universal experience implication → denominators/time/CI and exploratory heterogeneity | Same locators and numbers as O02; Table1 p=0.0629 in brief | Correct duplicate summary | Keep chapter bibliography |
| O13 — R1 Ch1 follow-up reference | Absent → separate dated update and brief | No present-day effect claimed; update opening | Add separate identity | Alongside 2025 reference |
| O14 — R1 Ch3 opening | Ch1 generalized as senior slowdown → explicitly reject that extrapolation | No new number; O02–O05 scope | Correct uncited repetition | Keep Ch3 transition |
| O15 — R1 Ch3 “Execution Mandate” opening | Unattributed “55% productivity gains” used to explain investor pressure → adoption-pressure hypothesis | Task result does not measure market decisions; remove untraceable generic percentage | Qualify causal bridge; economic/tone audit remains open | Keep as hypothesis, not empirical finding |
| O16 — R1 Ch4 reference summary | METR listed as support for volume/complexity/review/rework → task-time boundary and removal from that attribution list | METR §2.3; other source metrics remain #58/#59 | Correct mismatched source attribution | Keep cross-reference with correct source set |
| O17 — R3 Ch8 opening | “Everyone” feels faster while industry slows → bounded comparison and conditional system hypothesis | No industry-wide rate; all three source scopes | Synchronize relying conclusion | Keep opening, link Ch1 comparison |
| O18 — README Takeaway1/confidence row | Existential task acceleration claim retained | Peng Fig6 supports “can”; no numeric constant or junior/senior universality | Keep High for bounded existence claim; no reclassification | Keep reader map |
| O19 — README Evidence Map | Unlinked developer RCT / Peng and ambiguous METR coverage → three brief links, separate long-task source | No quantitative synthesis added | Synchronize coverage/navigation | Keep Evidence Map |
| O20 — REFERENCES P-2023-01/P-2025-01 | Unversioned citations/brief pending → pinned v1/v2, full authors, brief links | Version dates verified on arXiv; no peer-review claim inferred | Correct metadata | Keep bibliography |
| O21 — REFERENCES P-2026-03 | Absent → separate first-party original update with publication/access dates | Update title/date/contributors | Add, do not overwrite 2025 object | Keep bibliography |
| O22 — SOURCES three rows | Legacy Registered; follow-up absent → reviewed briefs, In progress, —; explicit actual paths | Source identities preserved for legacy rows; new object registered before use | Synchronize, no premature Verified | Canonical registry |
| O23 — primary index three entries | Only NBER brief indexed → three additional bounded descriptions | No stronger result than briefs | Add concise source navigation | Keep primary index |
| O24 — Peng brief design/results | New source-oriented record | Each table row has Study Design/Results/Fig6/Table1 locator; count versus completion and time versus rate explicit | Keep source findings separate from inference | Primary brief rather than report detail |
| O25 — Peng brief arithmetic/heterogeneity/conflicts | New calculation and boundaries | Reproduced 55.7648…% from means; Table1 p=0.0629; title/ethics statement for interests | Keep inspectable derivation; no new population result | Primary brief |
| O26 — METR 2025 brief design/results | New source-oriented record | §2.1–2.3/§3/Fig1/G.7; C.3.3–C.3.4/G.6 completion, exclusions and imputation; D.1–D.3 regression/HC3/time convention; update opening for interval, data/code README variance explicitly disclosed | Keep estimate, perceptions, outcome boundary and method distinct | Primary brief |
| O27 — METR 2025 brief limits/interests | New analysis of generalization | §4.1/Table2, C.2.7, acknowledgments, author-report FAQ; no inferred vendor grant | Keep hypotheses separate from measured mechanisms | Primary brief |
| O28 — METR 2026 brief design/raw estimates | New source-oriented record; raw estimates kept out of headline comparison | Update opening: returning −18% [−38,+9], new −4% [−15,+9]; study details: 57=10+47, 143 repos, 800+ tasks | Both intervals cross zero; no reliable causal reversal asserted | Detail in brief, limits in report |
| O29 — METR 2026 brief selection/measurement/interests | New source limitations and interpretation | Update problems 1–6 and study details, $50 versus $150/hour; no separate funding disclosure supplied | Identification problem stated alongside results | Primary brief plus immediate report caveat |


### Cross-brief material uses (correction R5)

These are synthesis/limitation uses, not merely links, and their destination paths are included in the supplying source's registry/front matter. Each brief's own findings remain in its source-oriented table O24–O29.

| ID / location | Wording and inference | Numbers/locator | Fit/action | Better destination |
| --- | --- | --- | --- | --- |
| X01 — METR2025 brief, Repository interpretation | Peng contrast is bounded; does not isolate experience/task/tool causes | Peng Results/Fig6; METR §4.1/Table2; no pooled value | Keep comparison; add path to P-2023-01 Current use | Keep in interpretation, not source findings |
| X02 — Peng brief, Not established | Historical METR comparison does not invalidate Peng benefit | METR Table2/§4.1; no new metric | Keep boundary and explicit 2025 link; add path to P-2025-01 | Keep source boundary |
| X03 — METR2026 brief, Repository interpretation | +19% historical finding remains separate from later estimates | METR2025 §3/Fig1 | Keep dated result; add path to P-2025-01 | Keep temporal interpretation |
| X04 — METR2025 brief, estimate/interval provenance | Exact interval attributed to later author restatement; data/code README output differs slightly | February 2026 update opening +2..+39; early data/code README HC3 0.013..0.394, estimate 0.188; no reanalysis to adjudicate | Keep both attributed outputs visible; add path to P-2026-03 | Detailed provenance in brief, attributed restatement in report |
| X05 — METR2025 brief, Not established | Follow-up limits current magnitude without retracting original trial | February 2026 update opening/problems 1–6 | Keep temporal boundary; add same material-use path to P-2026-03 | Keep next to temporal limit |

## Exclusions and unchanged evidence

- METR long-task/horizon occurrences in R1 Chapters 3/references and R2 Chapter 5/references belong to **P-2025-02**, not the productivity RCT. Their model/date/reliability problems remain for #63; their status is still Registered/Not started.
- Xu's source title and remaining +43.5/−19/+6.5/+2.4 figures and Agarwal's quality proxies remain owned by #58. O06/O08 remove only their misuse as a replication or dismissal of Peng. No completion is asserted for those studies.
- NBER P-2026-01's specific findings, existing brief, current-use paths and README Crisis Map numerical boundary are unchanged. This task does not renew or inherit its historical verification; #63 still owns its identified corrections.
- Historical issue-53 audit/remediation instructions preserve the base errors as before-state evidence. Historical work records are immutable. Author-publication titles in documentary provenance remain exact quoted titles, not current empirical endorsements. RI is a generated projection of current files/statuses, rebuilt after edits, never an independent source.
- Remaining vendor rhetoric, economics, GitClear and universal risk scenarios outside these relying passages remain open in their owning issues. Verification of these three source integrations will not mean that the entire report is corrected.

## Protocol and synchronization assessment

**Protocol outcome: No protocol change.** All four protocol bodies and the index were inspected. Protocol 1's containment/verification patterns do not derive thresholds from these experiments. Protocol 2 §§1–2 and §6 already separates output, active effort, lead time, local comparators and universal claims. Protocol 3 §3 requires metric definitions, comparators and limitations; it is consistent with the selection warning. Protocol 4 §§6–7 requires multiple local outcomes and adoption gates as proposed practice. None specifies a control based on 55.8%, +19% or the later raw estimates. This review does not empirically validate any control.

| Surface | Disposition |
| --- | --- |
| Evidence/source registry/indexes | Three briefs and exact current-use paths synchronized; existing identities retained; follow-up distinct |
| Report and reader navigation | O01–O17; heading/TOC anchors synchronized; README Evidence Map linked |
| README confidence/Crisis Map | Assessed: bounded “can accelerate” retained; maps already identify systems inferences and P-2026-01 boundaries; no new confidence or diagram claim |
| References | Three pinned/separate objects and brief links |
| Scope/Doctrine/Glossary/Artifact Model | Assessed, no boundary/term/artifact change; no edit required |
| Protocols | No protocol change, rationale above |
| Attribution/CITATION | No project-author, title, licensing or provenance finding changed |
| Governance/contributor guidance | Audit/work/handoff records updated; AGENTS, playbooks and contributor obligations unchanged |
| History/RI | CHANGELOG Updated; projection rebuilt, freshness and trusted gates required |

## Initial candidate acceptance record

These are candidate checks, not completed issue checkboxes or final source verification.

| Criterion | Primary implementation result | Remaining gate |
| --- | --- | --- |
| AC-01 | Three source-oriented briefs with full-original locators, versions, publication/access boundaries | Independent source check |
| AC-02 | O01–O29 before/after trace; Peng arithmetic reproduced; remaining METR horizon numbers explicitly excluded by identity | Independent occurrence/numeric check |
| AC-03 | Peng in opening comparison; unsupported brownfield percentage and universal junior/senior contrast removed | Independent balance/placement check |
| AC-04 | Registry/index/bibliography/reader uses synchronized at Reviewed brief + In progress + — | Checks, merge and default-branch verification before final state |
| AC-05 | Separate reviewer available, not yet performed | Confirmation and primary acceptance; unresolved items stay open |

## Initial review request (superseded by outcomes below)

- Primary: /root. Independent reviewer: pending.
- Flow: B plus companion A. Materials: originals, all changes/uses, source lifecycle, synchronization and AC-01–AC-05.
- Outcome: Review unavailable — interim, pending the required separate review.
- Discrepancies/corrections: pending. No new maintainer decision identified beyond the authorized treatment.
- Review date: —. No readiness or Verified claim is made.
- Implementation checks, reviewed tree and subsequent default-branch evidence will be appended after they occur.


## First independent review and correction loop — 2026-10-20

- Reviewer: /root/independent_evidence_review; did not author the implementation or edit files.
- Inspected commit `5236936075426eff2084d3ea3c7ee7ac1f894fb4`, content tree `2d8d839ce3ce1532a48c7e77a48644e01ab28f03`, base `86060ebc08bf03a05a974f826792c5a4e6b9126e`. Remote PR #66 head `1ced4dca9a71851bf6e62c0b02281e48302cf57c` has the identical content tree.
- Originals independently reopened: Peng full v1; METR full v2 and July author report; February 2026 full update and public data/code links. Repository uses, source states, synchronization and every AC were independently checked.
- Outcome: **Corrections required**. AC-01 required R1–R3; AC-02 partial for R3–R4; AC-03 passed within this scope; AC-04 required R5; AC-05 remained open for repeated review.
- Independently passed: 119 tests, contract, evidence-state integrity, RI freshness, diff check, trusted-base Repository Gate and transition/integrity gates using the exact base checkout.

| Finding | Implemented correction | Recheck required |
| --- | --- | --- |
| R1 wrong AppendixA tools/time locators | Replace with §§2.2.1–2.3/C.3.4; AppendixA is author contributions | Exact original locators |
| R2 unsupported inaccessible/unpublished data wording | State public data/code links and no independent reanalysis; no inaccessible subset asserted | Update/data links and all access wording |
| R3 missing METR completion/imputation rules | 246 completed (136/110); 13 unfinished, 24 intentionally dropped, 3 excluded developers; 27 post-review times imputed; retain author sensitivity checks and concise report caveat | §§2.3/C.3.3–4/G.6–7; every new number and report summary |
| R4 incorrect intermediate decimal | 55.7648…% rounds to 55.8%; headline result unchanged; also found independently by implementer | Reproduce arithmetic |
| R5 cross-brief uses omitted | Add X01–X05 and actual paths to supplying sources' Current use and front matter | Exact registry/brief path sets and interpretation boundaries |

A supplementary primary check found that the linked early-study code README displays slightly different interval bounds from the 2026 author restatement. Both are explicitly attributed in the METR brief; the report labels its interval as the dated restatement. No cause is inferred and no raw-data reanalysis is claimed. This does not change the bounded positive/negative interpretation; repeat review must check the treatment.

All three integrations were set to Corrections required / — while these findings remained unresolved. Corrections are now implemented but not self-confirmed; repeated independent review is pending. No new substantive maintainer decision was identified by either reviewer for R1–R5.

### Repeated-review precision correction

The repeated review confirmed R1/R2/R4/R5 and the substantive completion/imputation treatment in R3, then caught an imprecise shorthand: G.6 counts two excluded developers affected by paused repository development, not two distinct repositories. The brief now preserves the developer unit. The follow-up brief also explicitly names the article's agentic-tool examples and states that exact model/build versions are not supplied. No result or count is inferred from this additional tool description. Final repeated-review confirmation is still pending; states remain Corrections required/—.


## Final implementation review and primary acceptance — 2026-10-20

Independent reviewer /root/independent_evidence_review returned **Confirmed** at commit `91edb633d2d2f352a43c2333e80d5def9614b9f4`, tree `02fa53f8dfe0c23f1a2c62830d2716916da3aee9`; remote head `734856de9b4eebcbaf1196b8ba0688d7495f0ff1` has identical content. R1–R5, the G.6 precision correction and interval/tool-version supplements were independently rechecked. No material discrepancy, unresolved source correction or new human decision remains within #57. The reviewer did not edit files.

Primary acceptance checked actual implementation against the original issue after this independent outcome:

| AC | Observable check and exact evidence | Result |
| --- | --- | --- |
| AC-01 | Three full-original briefs, source/version/design/uncertainty/public-data boundaries; independent source checks above | Pass |
| AC-02 | O01–O29 and X01–X05; corrected n/completer/issue denominators, time units, source-attributed intervals and exact Peng calculation | Pass |
| AC-03 | Ch1 opening comparison includes Peng first; no unsupported brownfield dismissal or identified universal seniority effect | Pass |
| AC-04 | Current-use path sets 5/6/5, actual cross-brief uses, bibliography/index/reader synchronization; all three Reviewed brief/In progress/— | Candidate pass; merge/default-branch and final-state synchronization pending |
| AC-05 | Separate repeated review Confirmed; primary acceptance performed; no unresolved source issue within scope | Implementation pass; lifecycle completion pending |

Independent final checks: contract, trusted evidence integrity/transitions, RI freshness, diff check and trusted Repository Gate passed. 119 tests passed at correction commit `e821c39`; subsequent edits only clarified text/history/RI. CI on exact remote implementation head 734856de passed [Main health 39465305694](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/actions/runs/39465305694) and [Repository Gate 39465300432](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/actions/runs/39465300432).

Only actual confirmation/acceptance metadata and derived RI follow the reviewed content. Integration remains In progress/— until this confirmed correction set is merged and checked on main. The existing CI/source limitations are retained, not unresolved corrections. This acceptance does not extend to sibling source audits or the whole report.


## Default-branch verification and final-state proposal — 2026-10-20

PR [#66](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/pull/66) merged with correction head `897c792ee78999c747ffe353f9fadde2f37cdc97` into main `21af254361dbd4f8d158516c1699fec7661e6312`, tree `b711f3ab97fc35610c146e5e4f4b3cbf1eaa7a05`. Exact-head implementation checks passed: [Main health 39465590241](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/actions/runs/39465590241), latest [Repository Gate 39465663351](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/actions/runs/39465663351). Merged-main [Main health 39465753207](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/actions/runs/39465753207) completed successfully for the push SHA.

Primary merged-state checks on that exact SHA: 119 tests passed; contract, evidence-state integrity/transitions, RI freshness and diff checks passed. Reader-facing report/README/bibliography/index files were byte-compared with independently Confirmed commit `91edb633`; each brief's research body before the integration-audit section was also byte-compared. They are identical; only actual confirmation/acceptance metadata follows the reviewed content. A separate clean worktree pins the merged main for the final trusted-policy checks.

Integration completion checklist for P-2023-01/P-2025-01/P-2026-03:

- [x] Current AGENTS/applicable procedures, exact originals/versions and source-ground-truth fields inspected.
- [x] Three reviewed indexed briefs; source findings, calculations, author interpretation, repository inference and limitations separated.
- [x] Every material use searched/traced (O01–O29, X01–X05), including uncited report conclusions and cross-brief uses.
- [x] Numerical units, denominators, populations, dates and uncertainty checked; published interval outputs separately attributed; no raw-data reanalysis claimed.
- [x] Argument fit, positive/negative visibility, adjacent summaries, maps and source boundaries checked.
- [x] Protocol outcome: No protocol change, with all four assessed and rationale recorded.
- [x] Exact treatment authorized by the maintainer; no new decision unresolved.
- [x] Current-use paths 5/6/5, source identity, bibliography/index and removed/replaced claims synchronized.
- [x] Repeated independent source/integration review Confirmed; all required research corrections merged into main and checked.
- [x] Registry and briefs now propose matching Reviewed brief / Verified / 2026-10-20 for this checked default-branch content.

| AC | Merged evidence | Finalization condition |
| --- | --- | --- |
| AC-01 | Original locators and three complete briefs, independent Confirmed review | Satisfied on merged main |
| AC-02 | O01–O29/X01–X05, exact units/arithmetic/completion and time boundaries | Satisfied on merged main |
| AC-03 | Positive Peng result central; unsupported dismissal removed | Satisfied on merged main |
| AC-04 | Uses and metadata synchronized for the checked content; matching final fields proposed here | Final-state PR must be reviewed, merged and checked |
| AC-05 | Separate source/integration review Confirmed; primary merged-state acceptance performed | Separate final-state review pending, then issue proof/closure |

This final-state change does not modify research claims, source identities/current-use sets, protocols or confidence. Its new work record is separate; the merged implementation work record is immutable. Final-state independent review is pending, so this PR is not yet ready for merge or issue closure. These lifecycle values concern only the three scoped source integrations; other source audits and whole-report corrections remain open.


## Final-state independent review and primary acceptance — 2026-10-20

Independent reviewer /root/independent_evidence_review returned **Confirmed** for final-state candidate `5e48af1d8d6fa629ee7b38c772c921e549cba75e`, tree `538b0c05d3dc0b6ff4be3c129b6f56dbd928c465`, against checked main `21af254361dbd4f8d158516c1699fec7661e6312`. Remote PR [#67](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/pull/67) head `8147d0cbafb4e6dc21d34e74de6fd616fc2d1157` has identical content. The reviewer did not author or edit the candidate.

The reviewer independently checked live GitHub merge/main/CI, 16 unchanged report/navigation/rule files and the three unchanged research bodies, all completion gates, exactly three status/date transitions, unchanged Current use sets 5/6/5, and immutable existing work records. No material discrepancy, new interpretation or unresolved maintainer decision remains. The transition to Reviewed brief / Verified / 2026-10-20 is permitted for the checked default-branch research content.

Independent checks: main 119 tests, contract, evidence integrity and RI passed; candidate contract, trusted integrity/transitions, RI, diff and trusted Repository Gate passed. Primary acceptance after this outcome confirms AC-01/02/03 on merged main and AC-04/05 for the final-state proposal. Only actual confirmation metadata/handoff and derived RI follow the inspected candidate. Latest exact-head CI, merge and resulting-main verification remain the final publication/closure conditions; they will be linked in #57 and both PR completion comments, not inferred from this record.

Known source limitations, the separately attributed interval difference without reanalysis, and sibling source/tone audits remain explicit. This completes only the three scoped source integrations once the final-state change is published and checked.
