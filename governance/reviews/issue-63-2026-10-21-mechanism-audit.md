# Issue #63 — Sol source checks, implementation and Astra handoff

## Scope and decisions

- Date: 21 October 2026, Europe/Warsaw. Primary implementer: Sol.
- Owner: [#63](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/63); base `ada19312045fd859631bc6e8f230f25582eec084`, tree `433c034ae15f334a02892adefb849ce49a700e74`.
- [Start declaration](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/63#issuecomment-6309339562), [changed-version scope note](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/63#issuecomment-6309440882), [pre-edit research-impact/treatment record](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/63#issuecomment-6309465344).
- Maintainer decision: original request authorizes precise numeric/inference/placement corrections, hypotheses and neutral criticism; #63 specifies conditional queues, source boundaries, adaptations/falsifiers and #54 coordination. Latest instruction: “Сол підхопи, в кінці звіт і статус і нагадай що передати Астра”. This stage prepares a reviewable draft and explicit analytical handoff. It does not infer Astra acceptance or authorize unreviewed September findings.
- Primary flow **C** after discovery of a new NBER revision; required changed-use audit retained. **B** source-review requirements apply to P-2025-02 and M-1984-01; their clarified registered identities also require **C** resets. Evidence review, integration audit, synchronization and independent review required. No governance change.
- Alternatives: unchanged text (retains demonstrated conflations); replace with latest abstract (not reviewed); remove NBER/positive results (loses relevant evidence); duplicate synthesis (poor placement). Selected: pinned May synthesis in Ch1, hypotheses elsewhere, explicit current-version/access gaps. Changes are reversible in a draft PR.
- Scope: P-2026-01, directly relying P-2025-02 definition and M-1984-01 interpretation; R1 Ch1/4, R2 Ch5–7, README map/navigation, protocols 2/3 clarifications, source records/indexes/bibliography, claim graph and continuity. Broader Part 3/vendor/macro rhetoric belongs to #64; final cross-repository sync to #65. No collection or completion claim for #54.

## Original-source checks

**NBER May original:** maintainer-supplied `w35275.pdf`, 97 pages, SHA256 `edf1a41a6e4e4cf562571b5fac79eac07693281f88d460a81ee9f8ce1a1c65bb`. Read abstract/introduction, relevant design/measurement/identification, Table 3/5, calibration, marketplace methods/discussion and appendices; Figure 1 and Table 5 rendered and visually inspected. This is a claim-relevant original-source audit, not a claim of reading all 97 pages or obtaining raw data. No copyrighted PDF is added to git.

- Abstract; Figure 1 p3 / PDF5: cumulative generation estimates and positive final release headline.
- §6.1 pp23–25 / PDF25–27; Table 3: matching, normalization, clustered uncertainty, different outcome samples and release-positive pre-period selection.
- Table 5 p33 / PDF35: exact incremental cells/standard errors; no async release estimate. §7.1 p32 says 20.2%; table 20.3%; both retained as a discrepancy.
- Appendix B.4.7 OA12–13 / PDF63–64: recently touched repositories releasing in a week, not an individual deployment/value outcome.
- §7.2/Figures 9–10 pp36–37 / PDF38–39: calibrated `theta=.75, sigma=.25`, not a raw measurement or review multiplier.
- §8.2 pp40–44 / PDF42–46, Figure 12 and Appendix B.6: entry/three-month proxy usage; three platforms' usage, SourceForge entry comparator; demand/discovery, selection, lag and imperfect value proxies.
- Cover: working paper not peer reviewed; Mack Institute/Wharton and Chicago AI Incubator support. Current [official disclosures](https://www.nber.org/papers/w35275) identify Demirer and Musolff's prior Microsoft postdocs/current paid consulting. Current disclosures are dated current observations, not proof of their precise May wording or misconduct. Public/tool telemetry and disclosed relationships are limitations to inspect, not reasons to discard positive results.
- **Revision discovery:** official page/search rendering lists September 2026 and different abstract estimates (>500,000; 30/180/240 cumulative commits, 80 projects, 30 releases, .23 calibration). Direct page opening returned 403; official search rendering was readable. These numbers record **discovery only**; no September original was reviewed or integrated. Before changing uses, P-2026-01 changed from Reviewed brief/Verified/2026-07-27 to Needs re-review/Needs re-verification/—. Preserved July brief body is verbatim history, not current verification. Full September Flow C remains open.

**METR original:** [arXiv v1 HTML](https://arxiv.org/html/2503.14499v1), 18 March 2025, §§3–4, 6–8 and baseline discussion; [March 19 author post](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/), accessed October 21, now embeds later TH1.0/1.1 data. Checked fitted success definition, human-time units, historical trend and external-validity limits. No unpinned current-model threshold accepted. The bounded brief records review work; the identity clarification resets it to **Needs re-review / Needs re-verification**, not a completed benchmark/funding/conflict audit.

**Methodology:** [North River Press notice](https://northriverpress.com/30th-anniversary-edition-of-the-goal-published/) confirms Goldratt/Cox, 1984 origin, manufacturing and later narrative changes. No original identified book edition/full text was read. Provisional methodology brief explicitly retains that gap; software assumptions are repository proposals. No search summary is treated as original-book evidence.

## Search and occurrence trace

Inspected report parts 1–3; all protocols/index; README takeaways/confidence/Evidence Map/Crisis Map; REFERENCES; registry/indexes and active briefs. Search terms include source IDs, NBER/35275/Demirer/Musolff/title, 180/50/30, 741/228.2/35.9/10.2/.25, Goldratt/1984/constraints, horizon/GPT-5.2/7-hour/7-month, queue/capacity/WIP, case study/thought experiment and uncited neighboring conclusions. Prior audit/work records and changelog history remain immutable historical observations, not active factual support. Cross-references in the old METR/Horn briefs correctly distinguish sources and are unchanged; they do not acquire this source's state.

Locators below refer to the **base** section and the exact proposed destination, avoiding unstable line numbers. Each row distinguishes inference, numeric/unit check and placement. The NBER brief's current numeric section has one audit table; its preserved historical body is not a second active integration claim.

| ID | Occurrence / source locator | Wording and numeric judgment | Placement / action / better destination |
| --- | --- | --- | --- |
| N63-01 | R1 Ch1 NBER opening; May abstract, §5–6 | Observational matched design; >100,000 May developers, not September's population | Keep central synthesis; add May/version boundary and source link |
| N63-02 | R1 Ch1 180% commits; abstract/Fig1 p3 | Accurate rounded cumulative stack; neither standalone async nor a fixed joint pipeline | Keep Ch1, explicitly cumulative; exact cells in brief |
| N63-03 | R1 Ch1 50% projects; same | Distinct repositories touched, not completed projects/customer outcomes | Qualify label; keep alongside same-version results |
| N63-04 | R1 Ch1 30% releases; Fig1/Table5/B4.7 | Positive cumulative headline; no separately measured async release cell; selected outcome sample | Preserve benefit; distinguish proxy/sample and incremental omission |
| N63-05 | R1 Ch1 ASCII funnel; Fig1 versus §8 | Implied joint activity→usage/value path stronger than separate designs | Remove; model graph/definitions in Ch4/appendix, empirical details remain Ch1 |
| N63-06 | R1 Ch1 marketplace sentence; §8.2/Fig12/B6 | Three entry changes, SourceForge no acceleration; three usage series with different proxies/windows | Correct locally; no all-four joint usage/causal claim |
| N63-07 | R1 Ch1 Architecture insight; §7.3/9 interpretation | Universal shifted bottleneck not identified; no measured capacity/quality/TCO effect | Replace with conditional hypothesis and alternatives; mechanism in Ch4 |
| N63-08 | R1 Ch1 conclusion/brief link and reference | Distinguish source estimates from repository systems inference and author interpretation | Keep brief link/reference; pin version and positive results |
| N63-09 | R2 Ch7 Production Attenuation 180% | Duplicate rounded cumulative commit finding | Remove duplicate retelling; Ch1 is better empirical home |
| N63-10 | R2 Ch7 same, 50% projects | Same unit/sample limit as N63-03 | Ch1 link plus conditional mechanism in Ch7 |
| N63-11 | R2 Ch7 same, 30% releases and funnel | Positive benefit must not disappear or become an async marginal effect/joint pipeline | Central Ch1 synthesis preserves it; remove duplicate funnel |
| N63-12 | R2 Ch7 Complementary Human Capital .25; §7.2/Fig9–10 | Model-calibrated under constant-layer assumptions, not observed review capacity | Central model note Ch1; exact calibration in brief; Ch7 references it |
| N63-13 | R2 Ch7 Verification Bottleneck/most organizations; §7–9 | Interpretation exceeds identified design; no review prevalence or all-stage harm estimate | Replace with necessary conditions/competing explanations, no probability |
| N63-14 | R2 Ch7 marketplace paragraph; §8.2 | Descriptive proxies not total value or same matched adopters; discovery/demand/lag remain | Relocate empirical explanation to Ch1; mechanism remains testable |
| N63-15 | R2 Ch7 conclusion/source reference | Categorical entire-chain failure exceeds findings | New chapter title/conclusion/hypotheses and version-pinned brief link |
| N63-16 | README Evidence Map NBER entry | Original research class valid; current review cannot imply latest revision accepted | Keep class, label supplied May/September pending |
| N63-17 | README Crisis Map empirical node | Higher upstream estimates observed in bounded May samples; not universal rate | Keep bounded node, pin version; add success branch/conditional edge |
| N63-18 | README map evidence boundary >100,000/four markets | May population accurate; release/usage designs differ and results include benefits | Correct local boundary; no confidence promotion; full graph review Astra |
| N63-19 | REFERENCES primary citation | Generic URL can resolve a revised paper | Pin May and flag September; exact source state stays in registry |
| N63-20 | Primary index/registry/Current use | Old Verified/date invalid after version discovery; bibliography was omitted from Current use | Reset before use edits; synchronize actual reader paths, index and appendix |
| N63-21 | Brief cumulative 40/140/180 and 180/50/30 | Fig1/abstract exact rounded reporting; commit sum178.6, repo52.9, release30.5 from table is a check, not new causality | Active exact-version findings plus full historical body retained separately |
| N63-22 | Brief autocomplete228.2LOC/35.9commits/10.2releases | Table5: percentage effects; SE17.6/2.9/4.1; weeks21–30/normalized, differing samples | Keep exact table/units in brief, not duplicate report detail |
| N63-23 | Brief sync741LOC/65PR/20releases | Exact table741.3/65.5/20.3 (SE19.2/2.3/2.6); prose20.2 differs | Keep exact table, note discrepancy; report about20 avoids false precision |
| N63-24 | Brief/appendix .25 and marketplace interpretation | Separate calibration/empirical/descriptive/repository classes; no fixed capacity, motives or total-value claim | Brief houses source/model; appendix graph exposes missing empirical edges |
| N63-25 | Preserved July brief audit/Verified/date | Actual historical review/completion; does not prove October/current version | Verbatim dated details with explicit supersession; no edit to past audit history |
| H63-01 | R2 Ch5 Exponential Liability heading and 7-month trend; METR v1 §4.2 | Horizon trend about7 months; not observed volume/complexity/liability doubling | Replace heading with measurement box; exact212 days/171–249 CI in brief |
| H63-02 | R2 Ch5 GPT-5.2/6–7hours/March19 attribution | Later chart/current-model conflation; old blog now embeds updated suites/models | Withdraw threshold; new pinned-v1 source record; no replacement ranking |
| H63-03 | R2 Ch5 50/50/forensic7hours/fixed capacity | 50% fitted benchmark level is not universal defect probability or required review duration | Remove roulette/liability inference; H3 proposed local scope/effort comparison |
| H63-04 | R2 Ch5 conclusion/reference | Previously repeated wrong threshold and pending audit placeholder | Correct definition/version reference, retain incomplete full-source review |
| H63-05 | README/REFERENCES/primary index/registry/METR brief/appendix D1/H3 | Definition versus deployment inference kept distinct; no new model numerical claim | Link bounded definition record; all actual Current use paths recorded |
| M63-01 | README methodology row; publisher notice | Goldratt/Cox/1984 bibliographic record; no full original-book evidence | Link access-gap brief, no implied completed review |
| M63-02 | R1 Ch4 lens/initial constraint/reference | Original claim non-bottleneck optimization always increases inventory too categorical; no edition/page source | Repository assumptions/coding and non-coding cases; book gap explicit |
| M63-03 | R2 Ch7 opening/conclusion; appendix A1–A3 | Single fixed slowest stage/universal harm not established by unread book or NBER | Conditional multi-stage/policy model; no quoted queue theorem |
| M63-04 | REFERENCES/methodology index/registry/brief | Add missing coauthor and exact access boundary, preserve stable ID | Legacy review and identity reset/Needs re-verification; no verification date |

### Uncited mechanism, diagram and protocol occurrences

| ID | Occurrence / relationship | Numeric/inference check | Placement/action |
| --- | --- | --- | --- |
| Q63-01 | R1 Ch4 initial coding constraint versus useless typing optimization | Contradiction resolved by distinguishing initial/downstream constraints and effort savings | Conditions before mechanism diagram; no measured general SDLC history |
| Q63-02 | R1 Ch4 diagram and queue prose | Generated≠admitted work; comparable demand/capacity units, risk mix, variation and policies required | Replace two-choice diagram with admission, beneficial/adverse and adaptation branches |
| Q63-03 | R1 Ch4 inventory/response section | Xu p=.086 and Agarwal34.85/42.87 unchanged; not WIP/review hours or human-load calibration | Keep bounded source context; no status/brief change to these verified sources |
| Q63-04 | R1 Ch4 Safe Adoption loop/final conclusion | Fixed capacity, exploding costs and burnout are conditional unmeasured edges | Replace feedback with edge conditions, alternatives and H1/H2 weakening outcomes |
| Q63-05 | R2 Ch5 10-second/30+minute example | Invented effort asymmetry, no net effect without manual comparator; no junior/senior population claim | Label invented, use30minutes plainly, add comparator/quality boundary |
| Q63-06 | R2 Ch5 queue, mentorship and responses | No fixed staffing ratio; positive output/anecdote limits unchanged | Existing success/adaptation branch retained, link definition/H3 test |
| Q63-07 | R2 Ch6 evaluation case/conclusion | Thought experiment, no deployment/pilot results; both saved effort and upkeep/errors count | Explicit label; Ch5 and #54 design links; no actual case data fabricated |
| Q63-08 | R2 Ch7 Product/BA and QA claims | Universal low-value requirements/shared-error tests unsupported | Conditional H5 and independent-check alternatives; no empirical effect sizes |
| Q63-09 | R2 Ch7 sponsor/cost paragraph | Already bounded #60 cash/capacity comparison; not proof of new transformation requirement | Preserve meaning/link in Adaptation and Budget Boundaries; no old cost-source brief/row edits |
| Q63-10 | README takeaways/confidence/Crisis Map | Existing confidence labels not probabilistic estimates; bottleneck prevalence unresolved | Success branch and conditions; confidence ranking/Part3 audit remains Astra/#64 |
| Q63-11 | Protocol2 §2 Step2/3 example | Wait/rework/failure alone cannot establish falling throughput; no actual pilot | Clarify existing capacity measures and hypothetical comparable completion rate, quality/confounders |
| Q63-12 | Protocol3 §4/7 disclosure templates | Fictional eight-week card/patterns may otherwise look like collected evidence | Explicit fictional label covering card and response patterns; controls unchanged |
| Q63-13 | Protocol1/4/index, R3 Ch8 | Existing adaptation/comparator/quality boundaries and no direct NBER/METR/Goldratt result | No dependent #63 edit; protocol names/strong broad rhetoric remain #64/#65 findings |
| Q63-14 | R3 Ch9–10 and README warning confidence | Wider probabilities, macro/legal/motive rhetoric not justified by this mechanism | Explicitly unresolved #64 scope; #63 draft must not claim whole-report neutrality/completion |
| Q63-15 | New appendix class table/graph/H1–5/S1–3/measurement note | Findings, source model, definition, repository assumptions, hypotheses and scenarios separated; no assigned probabilities | Analytical review artifact available to readers; not empirical evidence or a protocol authority |

## Status and synchronization assessment

- Canonical decision: implement the bounded #63 treatment; changed-version discovery and book access remain open.
- Source state: P-2026-01 Needs re-review / Needs re-verification / —; P-2025-02 and M-1984-01 Needs re-review / Needs re-verification / — after identity clarification. No promotion. The other 26 Verified rows/brief bytes must be checked unchanged. The initial trusted transition check rejected progressing the two clarified legacy identities without resets; corrected to its required reset states, with no rule/gate change.
- Reader/report/maps: R1 central May synthesis; R2 corrected benchmark and short Ch7 evidence link; source detail in briefs, conditional tests in appendix; README adds success path and version/access navigation. No new confidence rating.
- Evidence: exact Current use includes bibliography and appendix; primary/methodology indexes and REFERENCES synchronized. Older audit/work records untouched; full old NBER body preserved.
- Protocol outcome: **Protocol clarification**. Only existing measurement/example disclosure meaning clarified in protocols2/3. No new control, role, threshold, gate or escalation. Protocols1/4/index need no #63-dependent change; broader style/navigation findings remain separate.
- Doctrine/Glossary/Scope/Artifact Model: existing finding/inference/scenario/protocol boundaries already apply; no new canonical term or content model. No symmetry edit.
- Attribution/CITATION/LICENSE: no source-term priority, repository identity, reuse or authorship change; not applicable.
- Governance/CONTRIBUTING/tooling: existing source flows/approval/review/issue rules suffice; only dated work/review/memory/RI projection records change. No new obligations, tests or gate behavior.
- **Changelog: Updated** for material reader-facing mechanism/source/version corrections and protocol example meaning.
- Validation/independent review recorded below when performed. Assessment of applicable surfaces completed; analytical acceptance/current-version source review/merge verification remain open.

## Acceptance mapping and Astra work

| AC | Sol contribution / evidence | Remaining whole-criterion condition |
| --- | --- | --- |
| AC-01 | Claim classes/edges and tests in mechanism appendix, source/occurrence trace above | Astra independently accepts or corrects final analytical graph; **open** |
| AC-02 | Supplied May PDF/table/figure checks, single synthesis, positive releases and reset/version history | September Flow C version decision and accepted all-use integration/final checks; **open** |
| AC-03 | Admission/risk mix/capacity/variation/policy conditions, competing explanations and beneficial adaptation | Independent analytical approval of sufficiency and map/protocol implications; **open** |
| AC-04 | H1–H5 weakening outcomes, no calibrated scenario probabilities in the scoped mechanism | Astra reviews falsifiability and remaining cross-report dependencies; #64 still owns wider rhetoric; **open** |
| AC-05 | Independent Sol source/implementation review Confirmed at1c0d338/tree1a8aa6; explicit README/protocol assessment | Full independent final argument review, accepted merge/default-branch verification and exact current state; **open** |

**Передати Астрі, у цьому порядку:**

1. Перечитати current AGENTS/issue/PR/main/CI; не повторювати закрите #62. Перевірити exact head і цей audit, а не лише RI/memory.
2. Отримати точний оригінал **September2026 NBER**, зафіксувати hash/версію, провести повне Flow C review + every-use audit. Не змішувати травневі цифри з новими. Вирішити з maintainer, чи зберігати травневий ретроспективний блок поряд з новою версією, чи оновити центральний синтез; новий зміст спочатку подати на потрібне приймання.
3. Аналітично перевірити A1–A3, H1–H5, причинні ребра/альтернативи, достатність weakening tests, beneficial/null/adverse branches і відсутність прихованої тези про неминучий крах. Перевірити load-bearing confidence/map wording; Sol не змінив confidence ranking.
4. Закінчити/явно вирішити повний review METR і access/edition gap Goldratt. Коректна дефініція або чесний access gap не дорівнюють Reviewed brief/Verified. Не приписувати queueing theorem непрочитаному виданню.
5. Оцінити placement Ch1/Ch4/Ch5–7/appendix і Protocol clarification. Перевірити #54 як дизайн порівняння з належним baseline/quality/effort; дані не збиралися, його AC не закриваються тут.
6. Провести незалежне рев’ю після своїх виправлень, accepted merge, exact-main gates і окреме final-verification state, коли виконані source gates. Оновити цілі AC доказами та закрити #63 лише після виконання. Далі #64, потім #65.

## Independent review and validation

- Primary reviewer: Sol. Independent reviewer: `/root/sol_review_issue63`, separate Sol agent, no implementation or GitHub mutations.
- Flow reviewed: bounded C/B/D Sol preparation; not full September/original-book/benchmark completion or Astra analytical acceptance.
- Actual outcome: **Confirmed** on candidate `1c0d33806824add200e5b215dd1f8194955ec441`, tree `1a8aa6b26b24b9e0901cbb8684443c3c7abd60a7`, 21 October 2026. No material discrepancy found.
- Independently checked original May hash and visual Figure1/Table5, active numeric cells/SEs, positive releases/missing async cell/internal discrepancy, methods/selection/proxy/calibration/marketplace alternatives; pinned METR definition/trend and publisher-only book boundary; all relying report/map/protocol uses, trace/placement, actual source states and authorization.
- Independently verified 26 other Verified rows, 24 unique brief byte sequences, full historical May body and 19 prior work records unchanged. Trusted validator/state/transition and RI verification passed.
- Initial pre-record Repository Gate failed solely because the new work record did not yet exist; that run is **not** a pass. The actual result is now recorded in exactly one new record. Final candidate checks/final faithful-recording review follow.
- Two predeclared small follow-up edits: active brief's cover funding/current-dated relationship disclosure, and quoted plain-text README labels preserving map meaning. No source finding, hypothesis, control or source status promoted.
- Author targeted check: 262 local links/anchors, zero unresolved; numeric table sums178.6/52.9/30.5; historical body and other26rows/briefs unchanged. Repository contract/state/RI144 and trusted transition checks passed before review.
- Live checkpoint: #62 closed/completed; #63 open/all ACs unticked; main `ada19312045fd859631bc6e8f230f25582eec084`, Main health [39549672929](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/actions/runs/39549672929) success at that exact SHA. This is base evidence, not candidate CI.
- Astra analytical acceptance, accepted publication/merge, current-version/full-source processing and source verification remain separate future observations.
