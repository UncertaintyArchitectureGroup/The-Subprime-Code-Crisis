# Dated repository handoff

## Snapshot

- Observed 2026-10-20; main `06fdd63b332fd4efe27462dbbd648119c3f96ce8`.
- Issue #52 completion starts from PR #56 candidate
  `8fc0a4877b7036068c058072dd8121ad1663ead1`; live acceptance/merge evidence is in #52.
- Author-site reference `82b57b8948c6c30143213b846ee2848d06f8d200`.
- Revalidate refs, issues and checks live; this file cannot establish current status.

## Active owners

- #47: issue-led work; #52: local RI; implementation remains PR #56.
- #53: evidence backlog; #4: skill-formation input. Do not duplicate these owners.
- #57–62: bounded source corrections; #63: mechanism; #64: tone; #65: final sync.
- Older PRs #40/#41/#42/#46 remain separate scope; this handoff does not adopt them.

## Decisions

- 2026-10-20 request authorizes useful site-rule/RI adaptation and an evidence,
  placement and neutral-tone audit with detailed Sol issues.
- Keep Subprime's source-state gates, original-source authority and independent review.
- Do not transplant site hosting/release tooling or treat a report as source verification.
- Complete one issue at a time: #52 implementation, independent review, acceptance,
  merged/main verification, evidence and closure; report the next issue before starting it.

## Evidence

- Baseline: 113 tests, repository contract, evidence-state check and RI verify passed.
- Current review/check outcomes belong in PR #56 and its dated review artifact.
- Governance/RI independently Confirmed: `reviews/issue-52-2026-10-20-ri-review.md`.
- Fresh #52 review found and corrected a historical Verified test invariant.
  Corrective review Confirmed at tree `047f455eed71f6ce45c96bd48bc113a429a3758d`;
  reviewer ran 119 tests and independently reproduced the old failure/new pass.
- All 25 sources and report/protocol claims assessed in
  `reviews/issue-53-2026-10-20-evidence-audit.md`; remediation is not verification.
- Audit/remediation plan independently Confirmed; current research integration
  still requires corrections. Source tasks remain open.
- Source status remains exclusively in `evidence/SOURCES.md`; findings can require
  correction even where an older audit had recorded Verified.

## Next actions

- Complete #52 corrective review, final acceptance and PR #56 main integration.
- Close only #52 after merged-state evidence; next assess #47's own acceptance.
- Execute the source-audit follow-ups in bounded PRs with original-source locators.
- Retain partial/blocked acceptance and missing source access explicitly.
- Merge/canonical adoption requires its own maintainer decision.
