# Issue #74 — standalone browser-report producer

Owner: [#74](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/74).
Consumer: [author #116](https://github.com/oborskyivitalii/oborskyivitalii/issues/116).

## Start-of-work declaration

- Selected procedure: maintainer-approved publication/tooling implementation.
  Source Flows A–E do not apply to a read-only rendition of existing research.
- Files in scope: `tools/report_web/`, its bounded tests/workflow, this record,
  one new work record, changelog and RI/memory synchronization.
- Source IDs: none added or reclassified. Existing canonical source bytes and
  all research/source states remain unchanged.
- Evidence review / integration audit: not required; no source interpretation,
  material use, claim, protocol or canonical Current use changes.
- Content synchronization: required for the new publication navigation/interface.
- Independent reviewer: `/root/review_report_architecture`, separate from implementer;
  implementation review requested, outcome pending at this initial checkpoint.
- Substantive-change discussion: already covered by the inspected #74 plan and
  the maintainer's explicit instruction “Сол починай”. No AGENTS/status/rule edits.
- Read current root AGENTS, applicable mandatory playbooks, doctrine/glossary,
  repository/evidence entry points and registry, report/protocol inputs and
  contribution/ownership/PR contracts. This is not a fresh scientific source audit.

## Live baseline and human decision

Checked 21 October 2026, Europe/Warsaw:

- Subprime main `2b0f6528f86fc28eaf6d759d283dcd3e098c9127`; isolated branch
  `work/issue-74-quartz-report`. #74 open, no prior implementation PR found.
- Existing PR #46 remains a separate draft, head `9f1f255ee4d886d036b489490a08296256fed5f0`.
  Reuse only its inspected immutable UA/Quartz engine selection, not its draft
  article, restricted transport, PDF workflow or governance edits.
- Author main `ca70a66f340a8e804e4263c02aa9abe79a062765`; PR #79 still Draft,
  head `283b32f65f0589e85c0aa914d0990704dcf8ac38`. Its admitted content-release
  contract remains the consumer prerequisite; no forced merge or second publisher.
- Approved direction: separate Quartz HTML generation, mounted under `/subprime/`
  by the existing whole-site author publisher. Alternatives retained in the plan:
  leaving repository links, a separate subdomain, or a proxy-hosting change.
  The maintainer explicitly chose the path and then authorized implementation.
- This changes rendition/navigation and producer tooling. It changes no evidence,
  report logic, protocol, source state or general contributor workflow. Output is
  reversible and isolated; consumer admission, staging and production remain open.

## Implementation and design decisions

The source/route manifest selects 43 complete documents. Existing Markdown stays
in place. The stage projection parses TOML metadata and applies AST-position link
edits without reserializing research prose or code fences. Included links use
the route map, excluded existing support sources have immutable GitHub links,
and missing targets/anchors fail. Publication drafts are not confused with
research-review statuses. The browser pages retain state/context/source links.

Quartz is pinned to the same UA commit `989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3`
(4.5.2). A small plugin emits only selected directory indexes because standard
ContentPage skips them and FolderPage would synthesize extra pages. Config,
layout, CSS and local components are explicit cache overlays; no upstream
implementation fork or Quartz-major migration. Text/nav require no JavaScript;
search/theme/Mermaid are enhancements with documented limits.

The palette is selected from author main's warm paper/ink/accent tokens and
system typography. This does not import the author's scene/article runtime.
CSS/scripts/search and source images have content-addressed URLs. The consumer
still must retain prior resources and establish actual host cache/reader and
rollback behavior. Same-origin report scripts are admitted trusted site code,
not sandboxed by their URL path. Analytics remains disabled for this candidate.

The package records source commit/tree/actual input hashes, dirty state,
engine/config/adapter identity, source state and route/link map, files/digests/MIME,
runtime/rights and optional Actions run identity. A local manifest is not trusted
admission: #116 must authenticate its origin and actual CI evidence.

Read-only candidate CI uses the exact PR head, full Git history and immutable
Actions pins. It caches npm downloads by immutable engine selection, installs no
browser/PDF toolchain and uploads artifacts without deployment. Public candidate
generation on main requires a clean source checkout. Fourteen-day review artifact
retention is explicitly not a production recovery guarantee.

## Validation checkpoint — initial producer candidate

- Full existing unittest discovery: **133 tests passed** (including 7 new bounded
  producer tests); source contract and evidence-state integrity passed.
- Actual pinned Quartz render: **43 complete pages**, **2,859 local links**,
  **43 search documents**. Every expected output page, canonical, indexing mode,
  local fragment/resource target and search membership is checked.
- Observed local warm HTML producer samples: **3.763s / 3.497s**. These are local
  generation measurements, not end-to-end release timing, three delivered text
  updates, author-generation reuse or an accepted production SLA.
- Canonical `report/`, `evidence/`, `protocols/` and foundation/source Markdown
  compare unchanged to the inspected base. The adapter also checks its selected
  source, asset and adapter hashes after generation.
- Browser/visual gate: **pending**. The available local Playwright browser binary
  is absent; its official headless-shell download returned an invalid archive.
  The cloud browser reports `ERR_BLOCKED_BY_CLIENT` for localhost. No desktop,
  tablet, mobile, physical-device, no-JS runtime or Mermaid visual pass is claimed.
  Do not convert these environment failures into product defects or fake passes.
- No source status reset, source/attachment integration, PDF, author build,
  publication dispatch, merge, DNS change or deployment performed.

## Content synchronization assessment

- Canonical approved change: add a derived report website package, preserving
  canonical research authority and existing source/argument boundaries.
- Surfaces assessed: all source/entry/index/reference/report/protocol/foundation
  owners selected by the route manifest, contributor/governance owners and history.
- Updated: publication tool/config/docs, validation/CI, this work record/review,
  changelog and RI/memory. User-facing author links are left to #116; no premature
  live-page link is added to canonical reader entry points.
- Non-applicable research surfaces: source bodies, registry/brief states, Current
  use, bibliography identity, report/protocol content, doctrine/glossary and scope
  retain their bytes/meaning. The new rendition is not a new empirical claim.
- Changelog: Updated — new publication/navigation structure and producer interface.
- Outstanding delivery dependency and visual/device/release gates are explicit;
  no issue-level completion or merge readiness is inferred from this assessment.

## Independent review

- Primary implementer: `/root` (Sol).
- Separate reviewer: `/root/review_report_architecture`.
- Reviewed scope: current S0–S3 standalone producer candidate, not scientific
  verification or author integration/production acceptance.
- Current outcome: **Confirmed**, bounded to corrected standalone producer code
  and checks. The initial `Corrections required` findings and repeat evidence
  are preserved below; remaining visual/rights/consumer gates are not confirmed.
- Human decisions still required: whole reader/editorial/rights/device acceptance
  and existing merge/publication decisions; not a repeated permission request for
  the already-authorized implementation work.

## Acceptance reconciliation

All whole-issue checkboxes remain unchecked. This candidate implements independent
preparation and rendering; it does not discharge the cross-repository delivery
criteria. Planned selectors below map to current commands/evidence, not a copied
per-issue acceptance engine.

| AC | Check / evidence | Candidate disposition | Remaining gate |
| --- | --- | --- | --- |
| AC01 | `report_web.py check`, input/source digest check | implemented, structurally checked | independent scope review |
| AC02 | AST graph + complete rendered-output links/anchors | 43 pages / 2,859 links pass | actual host deep-link/slash compatibility |
| AC03 | real 43-document render, TOML/fence projection | structurally checked | visual/editorial/diagram fidelity |
| AC04 | source metadata/snapshot and date projection | implemented | independent context-presentation review |
| AC05 | output/search inventory and negative cases | producer checks pass | consumer cached-reader/runtime proof |
| AC06 | immutable interface/manifest | producer implemented | authenticated consumer round trip/rejection |
| AC07 | minimal responsive Quartz layout | code implemented | browser/keyboard/visual/device review |
| AC08 | HTML-only workflow and local generation timings | producer implemented | three actual text updates + author reuse/timing |
| AC09 | bounded producer tests + existing repository checks | current local checks pass | exact-source remote CI / hosted receipts |
| AC10 | author entry and real canonical delivery | pending | author #116 |
| AC11 | pinned owned adapter and separate review | review in progress | confirmed current-source review |
| AC12 | producer runbook and consumer recovery contract | partial | demonstrated rollback / authorized delivery |

At the next checkpoint append the actual PR/head/tree, remote runs and independent
review result. Preserve historical failed builds; do not rewrite partial work into
whole-issue completion. #74/#116 remain open until their full acceptance.

## Correction loop — independent implementation review

The separate reviewer returned **Corrections required** for the initial producer
candidate. Its own real build passed43pages/2859links/43search in3.889s and hashes
of49 canonical source/assets files stayed unchanged. Four P2 findings remained:

1. Package-root extras were not included in `verify_package`'s check. Corrected
   exact-root inventory and file types/symlink rejection. Negative tests now start
   from an actually valid package and add/mutate actual files or links.
2. Slug equality missed static clean-URL file/directory collisions. Corrected
   directory-prefix and reserved resource-root validation with evidence/report/media cases.
3. Reference image definitions bypassed the image allowlist. Corrected reference
   usage resolution; added actual pinned-AST regression cases, including allowed
   and rejected reference images and preserved code/diagram fences.
4. Dirty-engine rejection occurred after npm installation. Corrected source-tree
   verification before any install, with dependency-presence verification after;
   a mocked-order regression proves npm is never called on a rejected cache.

Current local suite: **134 tests passed**, including8producer tests; six actual
AST projection cases passed. A corrected build before the subsequent mobile-nav
adjustment produced43pages/2902links/43search in3.504s; `verify` passed. These are
separate observed versions, not an invented final exact-source result.

Additional review limitations addressed/prepared: the mobile contents is now a
native collapsed disclosure before the long article (desktop enhancement opens
it); actual responsive/keyboard/visual acceptance remains pending. The payload
now includes the exact original Quartz MIT notice (upstream baseline4923affa)
and pinned UA Apache-2.0 license with an explicit runtime/source notice map.
Final rights inventory is explicitly pending, not inferred from copying licenses.

Independent repeat review was requested on the corrected code/config/tests/docs.
The work record retains the actual non-confirming initial outcome until the
separate reviewer supplies its repeat disposition. No merge/readiness, hosted
cache, author reuse, device or production acceptance is claimed.

## Independent repeat outcome — Confirmed

Separate reviewer `/root/review_report_architecture` independently rechecked the
four corrections and the repaired collision regression fixture. The fixture now
preserves the mandatory index and asserts the actual collision/reserved-route
error, rather than passing because an unrelated index check fails.

- Outcome: **Confirmed** for corrected standalone producer code/checks only.
- Inspected local base: `2b0f6528f86fc28eaf6d759d283dcd3e098c9127`, dirty worktree.
- Effective production input digest:
  `b20c312bbc4a2c7eba4a90382379820889e1da0e52f9df341b0d6eb243208d39`.
- Preview payload digest:
  `06904061f3cd2972afc213974280259846a4084844de07f05ce758ef4dfdcd14`.
- Independent real build/package verification: **43 pages / 2,902 links /
  43 search entries / 3.677 seconds**. Eight producer tests and six actual
  Markdown-AST cases passed. All49 canonical source/assets hashes unchanged.
- Independent added-root-file and URL-collision fixtures reproduce rejection.
- No blocking producer-code finding remains. Browser/visual/accessibility/device,
  editorial/rights, exact-source remote CI, authenticated consumer, actual-host
  route/cache compatibility, rollback and production delivery remain pending.

The work record records this actual bounded outcome. Recording its receipt and
regenerating RI/memory does not change reviewed renderer inputs. A published
commit must still get source-qualified CI and rendering: its source URL identity
will legitimately differ from this dirty local preview. Do not reuse the local
payload hash as if it were the eventual clean hosted edition.
