# Issue #123 — README changed-use and report-route audit

Date: 2026-10-24. Base: `0aaccd7311af65727ddf0077f9ca605def967d22`. Active issue: [#123](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/123). Route decision: **Maintainer pending**.

## Scope and decision record

The maintainer selected #123 as the sole active implementation issue in [start comment 6384736791](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/123#issuecomment-6384736791). The exact reader-facing text is the corrected README V2 in #88: [V1 6383504860](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/88#issuecomment-6383504860) plus [six replacements and two implementation clarifications 6383542436](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/88#issuecomment-6383542436). Its proposal-level recheck is [Confirmed 6383555588](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/88#issuecomment-6383555588); implemented bytes still require separate review.

This change replaces only the README prefix before `## Repository Map`. The prior tail from that heading onward is preserved byte-for-byte. No report chapter prose, protocol, governance rule, source identity, source finding, hypothesis verdict, publisher implementation or deployed site changes in this candidate.

## README byte and navigation checks

- Exact V2 opening SHA-256: `dd69cb6aabdd849ecceba21666cb2b9040c4fcbf1cf0979807adbdd46852f1f2`.
- Exact complete candidate README SHA-256: `ed0f1c71add5ce858c0bbdb466181dce8b15aa981c286f1e59436bc6b70f8869`.
- The retained `## Repository Map` tail is compared with the selected base before replacement; a mismatch aborts the apply script.
- Existing `#the-research-thesis`, `#quick-start`, `#key-takeaways`, `#repository-map` and all destinations present in the corrected V2 remain available.
- Reader path now presents audience → thesis → two bounded empirical anchors → mechanism/alternatives → one first action → three principal routes.

## Flow D changed-use audit

Evidence review is reused; source identities and originals are unchanged. Integration is reset to **Needs re-verification / —** for the two materially changed condensed README uses. Final `Verified` restoration is forbidden until candidate corrections are merged, independent review is Confirmed, required checks pass and actual `main` is accepted.

### P-2026-01 — September 2026 NBER revision

| Audit item | Candidate treatment |
| --- | --- |
| Exact use | README says the pooled synchronous-agent weeks 21–30 estimates are **153.2% more commits** and **19.8% more repository releases**. |
| Source locator | Accepted September brief, Table 6, physical PDF 35 / printed 33. |
| Measurement boundary | Observational, per-developer normalized outcome estimates; commit and release regressions use different selected samples. Repository releases are repository/date events, not deployed feature value, customer benefit or a common-cohort conversion funnel. |
| Preserved positive result | Releases increase; the smaller release estimate is not labeled lost work. |
| Not established | Universal bottleneck, review overload, ownership loss, persistent debt, net negative value or remedy efficacy. |
| Alternatives kept visible | Effective existing capacity/substitutes, adaptation, experimentation/selection, changed task mix, release batching and positive net value. |
| Retained uses | Existing report, register, bibliography and Chen comparison remain unchanged and were checked for conflict with the new condensed opening. |

### P-2026-04 — Chen–Stratton, 4 August 2026

| Audit item | Candidate treatment |
| --- | --- |
| Exact use | README reports positive coding-activity estimates, a smaller uncertain tracked-completion estimate and about **49% longer PR submission-to-merge elapsed time** after agent adoption. |
| Source locator | Accepted brief, Figures 6–7 and 11–13; `3.45 / 7.03 ≈ 49.1%`. |
| Unit boundary | Coding and tracked-completion estimates are per active worker-month where applicable. The 49% result is elapsed days, not active review labor. |
| Identification boundary | Observational, non-random adoption; material pre-period movement limits causal interpretation. No formal between-outcome difference test establishes a production funnel or zero completion benefit. |
| Not established | Universal review saturation, actual reviewer hours, defect increase, lost ownership, downstream harm or remedy efficacy. |
| Retained uses | Existing report, register and bibliography uses remain unchanged and were checked for conflict with the new condensed opening. |

**Protocol outcome: No protocol change.** The opening links the existing team measurement/decision loop. Neither source establishes a universal control, role, threshold, staffing ratio or efficacy claim.

## Content synchronization assessment

| Surface | Disposition |
| --- | --- |
| README / reader navigation | **Updated.** Public landing-page order, condensed evidence and first action change. |
| Source registry and two briefs | **Updated.** Only P-2026-01 and P-2026-04 reset for changed use; identity/findings/Current use preserved. |
| Report / hypothesis register | **No text change.** Existing argument, alternatives and detailed evidence remain canonical; links are reused. |
| Protocols | **No protocol change.** Existing guides are destinations, not newly validated remedies. |
| References / evidence indexes | **No change required.** No new source object, identity, class or bibliography entry. |
| Doctrine / glossary / scope / artifact model | **No change required.** No claim class, term, scope, artifact relation or workflow changes. |
| Changelog | **Updated** for the public README reader-path change. |
| Publication inputs | Assessed below; no deployment or producer edit. |
| Memory / RI | Updated for the active task and regenerated after represented inputs changed. |

## Current heading/anchor inventory and future editorial owners

This is a bounded orientation map, not a claim-by-claim migration audit. Existing prose remains authoritative until its owning chapter replacement is independently accepted on `main`.

| New chapter | Sole editorial owner | Current authoritative heading/anchor area | Intended container under option A | Legacy treatment |
| --- | --- | --- | --- | --- |
| 1. Faster changes; what did the whole system gain? | #124 | `report/01_the_illusion.md` Ch1 and current README thesis | `report/01_the_illusion.md` | Retain useful old Ch1 anchors or add explicit compatibility anchors when changed. |
| 2. The SDLC produces more than code | #124 | README thesis; register node index; report cross-node synthesis | `report/01_the_illusion.md` | Preserve current lifecycle/register links. |
| 3. Intent | #125 | Part 1 Ch3/Ch4 material and INT register card | `report/01_the_illusion.md` | Detailed retain/move/retire decisions belong to #125. |
| 4. Requirements | #125 | Part 1 Ch4; Part 2 Ch7; REQ register card | `report/01_the_illusion.md` | Detailed dispositions belong to #125. |
| 5. Design | #133 | Part 2 Ch6/Ch7; DES register card | `report/01_the_illusion.md` | Detailed dispositions belong to #133. |
| 6. Code | #126 | Part 1 Ch1/Ch4; COD register card | `report/02_broken_mechanics.md` | Existing source anchors remain until #126 replacement. |
| 7. Review | #126 | Part 2 Ch5; REV/HUM cards | `report/02_broken_mechanics.md` | Preserve Ch5 links or explicit compatibility anchors. |
| 8. Test | #127 | Part 2 Ch7; TST card | `report/02_broken_mechanics.md` | Detailed dispositions belong to #127. |
| 9. Integration | #127 | Part 1 Ch4 / Part 2 Ch7; INTG card | `report/02_broken_mechanics.md` | Detailed dispositions belong to #127. |
| 10. Deployment | #128 | Part 3 Ch9/Ch10; DEP card | `report/03_the_aftermath.md` | Detailed dispositions belong to #128. |
| 11. Operation | #128 | Part 3 Ch9/Ch10; OPS card | `report/03_the_aftermath.md` | Detailed dispositions belong to #128. |
| 12. User outcomes | #129 | Part 3 Ch8/Ch9; VAL card and marketplace boundary | `report/03_the_aftermath.md` | Detailed dispositions belong to #129. |
| 13. Business economics | #129 | Part 1 Ch2/Ch3; Part 3 Ch10; ECO/cost appendices | `report/03_the_aftermath.md` | Detailed dispositions belong to #129. |
| 14. Management commitments | #130 | Part 1 Ch3, accepted #100 block | `report/03_the_aftermath.md` | Preserve the accepted management-record anchor or compatibility alias. |
| 15. Accumulated consequences | #130 | Part 3 Ch9; HUM/DEBT/BAL cards | `report/03_the_aftermath.md` | Scenarios remain bounded; detailed dispositions belong to #130. |
| 16. Runtime-model judgment boundary | #131 | No existing canonical Subprime chapter; bounded author/UA bridge inputs | `report/03_the_aftermath.md` | New heading only after #131 approval; no UA content duplication. |
| 17. Practical rebalancing | #131 | Part 3 Ch10 and existing protocols | `report/03_the_aftermath.md` | Preserve protocol destinations; no new universal control. |

## Publication input inspection

Live inspection by the coordinator is recorded in [#123 comment 6384820302](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/123#issuecomment-6384820302) against #74 and draft PR #75 head `219d974581fffb84b537302223217daf03d5d20f`.

| Input | Exact observed contract | #123 disposition |
| --- | --- | --- |
| Issue #74 content/URL contract | Canonical Markdown stays in present locations; three report files remain three pages initially. | **Unaffected now.** Supports option A unless a later migration is explicitly chosen. |
| PR #75 `tools/report_web/publication.json` | `README.md` → `/subprime/overview`; three report files → `/subprime/report/the-illusion`, `/subprime/report/broken-mechanics`, `/subprime/report/the-aftermath`. | **Affected by README content, not by route.** No manifest edit required for the existing source path. |
| PR #75 `tools/report_web/landing.md` | Current labels/counts 1–4 / 5–7 / 8–10. | **Deferred to #74 / a later selected editorial-publication synchronization unit.** It becomes textually stale as the 17-chapter edition is assembled. |
| PR #75 producer/link logic | Explicit source allowlist and stable slugs for the three report files. | **Unaffected by Phase A.** A later split is a producer-contract change. |
| Deployment/author mount | Separately owned by #74 and the linked author issue. | **Out of scope / not performed.** |

## Route decision

- **A — retain the three canonical report files and stable routes; use chapter headings/anchors.** Preserves current GitHub/Quartz URLs, avoids a compatibility migration during the rewrite and keeps one canonical text.
- **B — later create 17 chapter-sized canonical files.** Offers one page per chapter but requires new route mapping, compatibility handling, producer changes and broader synchronization.
- **C — hybrid.** No concrete need currently justifies mixed ownership; it risks duplicate canonical text.

**Recommendation: A. Maintainer decision pending.** No chapter file, directory, alias, compatibility stub or producer change is created by #123.

## Independent-review handoff and completion boundary

The reviewer must inspect exact README V2 bytes, tail preservation, both condensed source uses against accepted briefs, status resets, registry/brief synchronization, this occurrence audit, the #74/PR75 dispositions, the one work record, changelog, memory/RI and all applicable checks. Proposal review is not implemented-byte review.

This candidate is not complete or merge-ready until independent review is `Confirmed`, corrections are resolved and checked, the route decision is recorded, the content PR is merged and accepted on actual `main`, and a later narrow final-status step restores the two sources only after all verification gates pass.
