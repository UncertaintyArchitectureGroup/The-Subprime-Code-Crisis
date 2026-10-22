# Issue #88: plain-language pass — 2026-10-22

## Request and scope

The maintainer asked whether the ALT families were all counterhypotheses to the
central thesis, then requested clearer wording and simpler language across the
repository. The existing editorial owner is [#88](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/88).
The [approved start](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/88#issuecomment-6349668620)
records the request, scope and PL-1–5 acceptance before implementation.
[Master plan #84, amendment 14](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/84#14-plain-language-pass-selected--2026-10-22)
brings this pass forward before the proposed #110 comparison.

Base: `5a55c6fc8b8d85eb761f0d22a2f030c2c0fb532f`, tree
`bf45b556cdce66e30e5dde2db537d95c324ae8a7`.
Primary procedure: the authorized editorial change, issue workflow, content
synchronization, independent review and PR contract under current AGENTS.

The pass changes language and explanations. It does not reassess sources, select
a new scientific conclusion, change a source status or introduce a new obligation.
A material change to a source interpretation would require its existing source
flow and is outside this pass. Original #88 AC-1–6 stay open; PL-1–5 assess this
limited request without redefining the broader edition as complete.

## What changed

| Reader problem | Treatment |
| --- | --- |
| The main idea was hidden behind delivery terminology | README and register explain the thesis, whole process and useful outcomes before technical IDs. |
| “Six rivals” sounded like six denials of the whole thesis | A plain role table distinguishes challenges to a capacity gap or its duration, other explanations of data, overall benefit and a remedy's added value. Several can hold together. |
| Method instructions required decoding research shorthand | The evaluation guide asks which explanations apply, what each predicts, what was observed, what else may explain it and what remains to be tested. Existing requirements remain. |
| Readers had to translate dense report prose themselves | The three chapters unpack introductions, causal arguments, costs, scenarios and decision implications. Exact empirical tables and source boundaries remain. |
| The same jargon returned in forms and definitions | Assessment/comparison prompts, contribution guidance and selected glossary definitions use the same ordinary-language explanations. |

H0 remains the main-thesis identifier, not a statistical null. ALT-1 addresses
adequate existing capability or a working substitute. ALT-2 asks whether teams
adapt after an initial mismatch. ALT-3 concerns work scope, experiments and
measurement. ALT-4 concerns demand and uptake after delivery. ALT-5 concerns
selection, context and other changes. ALT-6a tests benefits after all costs;
ALT-6b separately tests a specified remedy's added value.

The comparison still distinguishes an absent cause from a prediction that fails
when its independently measured condition is present. A remedy that adds too
little value can fail even if the original problem is real. Positive net value
does not erase local harm or excuse an unacceptable loss in a critical outcome.

## Content synchronization assessment

| Surface | Inspection and result |
| --- | --- |
| Reader navigation | README and explanations change; existing chapter/register paths and heading anchors are retained. |
| Report | All three chapters and register explanations are edited. Detailed evidence cards, full node inventories, dated verdicts and H1–H5 remain. |
| Governance and contributor guidance | Evaluation guide, relevant template prompts and CONTRIBUTING explain the same procedure more clearly. AGENTS and other workflows retain their rules. |
| Doctrine and terms | Selected GLOSSARY definitions are clarified. DOCTRINE's claim classes and principles remain unchanged. |
| Repository architecture | Not applicable to edits: SCOPE and ARTIFACT_MODEL inspected; no subject boundary, artifact type, file ownership or relationship changes. |
| Source Registry | Not applicable to edits: source identity, factual Current use, statuses and verification dates remain unchanged. Meaning-preserving prose does not claim a new audit. |
| Evidence | Not applicable to edits: no brief, original finding, estimate, source interpretation or evidence assessment changes. #110 still owns the nine-entry comparison. |
| Evidence indexes | Not applicable to edits: no source or brief is added, removed or relocated; classification, navigation and processing descriptions remain accurate. |
| References and attribution | Not applicable to edits: citations and link destinations are preserved. No author, source version, bibliography or provenance changes. |
| Protocols | Not applicable to edits: the four guides and their roles, controls, thresholds, decision rights and adaptation requirements remain unchanged. |
| History and handoff | CHANGELOG records the language pass. Memory records its actual baseline and conditional next actions; RI is rebuilt from the resulting files. Historical audits and existing TOML work records stay untouched. |

Changelog: **Updated**. No new style policy or approval layer is added.

## Checks that matter for this change

The preservation checks compare against the exact base above. They help catch
accidental omissions; independent reading is still needed to check meaning.

- Register: preserve headings/link targets, all dated verdict blocks and the
  complete suffix beginning with “Existing evidence and its exact coverage.”
- Report: preserve headings, links, numeric tokens, tables, quotations, formulas,
  diagrams and reference sections; compare changed arguments in context.
- Repository: check unchanged source records/status fields and governance rules,
  local links/anchors, contract, evidence integrity, RI and trusted-base PR gates.
- Independent reading: identify the thesis and the different ALT roles without
  relying on the codes; check against the first-reader concerns recorded in #1.

Implementation checks on the corrected candidate passed: 126 tests, repository
contract, evidence-state integrity, RI freshness and whitespace checks. Root
checked 401 local Markdown links/anchors without failures. The independent
reviewer reran the tests and repository checks and separately checked links.
All nine edited content files retain existing headings and link targets. The
three chapters retain their numeric tokens, tables, quotes, formulas and diagrams;
register evidence and detailed node/test sections remain byte-identical.

The final trusted-base gates, hosted checks and exact-main acceptance are recorded
in the live PR/#88 when performed. This implementation receipt does not assert a
future merge or default-branch result.

## Independent review

- Authors: `/root`, `/root/plain_register`, `/root/plain_report`.
- Independent reviewer: `/root/readability_review`.
- Review scope: base-to-candidate language and meaning, current AGENTS/playbooks,
  live #88/#84 authorization, source-use boundaries, navigation and synchronization.
- Initial review required corrections to preserve thesis strength, the range of
  possible outcomes, remedy falsifiers, accepted tradeoffs, Review's full quality
  function, economic benefits as well as costs, and the meaning of technical debt.
  It also checked that “AI use” did not replace a study's actual exposure measure.
- Corrections completed: all findings above resolved; the reviewer independently
  checked the corrected prose in context, including all three report chapters.
- Outcome: **Confirmed**, 2026-10-22, for implementation candidate
  `7b23af7cb3567ed489fd158a84ea76fff0bf3cde`, tree
  `6e37fdc7544cc0bc6dc636b7c5e06403f56fbe16`.
- No remaining material discrepancy found. This confirms the language change,
  its preserved meaning and synchronization. The final work record and published
  tree still receive a faithful-record check; hosted checks, merge and actual-main
  acceptance are separate observations recorded in the PR and live #88.

## Completion boundary and next work

After the corrected pass is independently confirmed, merge and verify its exact
main commit, then reread #84. Record PL-1–5 against that evidence. Keep #88 open
for the remaining first-edition work and its original AC-1–6. Proposed #110
compares the nine accepted source entries; it still needs explicit selection.
#111's search, #100's marketing/decision analysis and later publication remain
separate work. Clearer wording supplies no new empirical result.
