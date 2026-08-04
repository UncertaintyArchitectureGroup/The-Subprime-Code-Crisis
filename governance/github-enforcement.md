# GitHub enforcement

## Status and precedence

This playbook implements the approved GitHub enforcement baseline. `AGENTS.md` remains canonical. The machine-readable desired state is `governance/github-enforcement.toml`.

## Protected branch

The protected branch is `main`. Changes must arrive through pull requests. Force pushes and branch deletion are prohibited.

## Required checks and freshness

`Repository Gate` is the required status check. Strict branch freshness is enabled, so the check must pass against the current base branch before merge.

## Pull request requirements

Pull requests require one approving review, code-owner review, dismissal of stale approvals after new pushes, approval of the most recent push, and resolution of all review conversations.

A green check does not replace the repository's human approval, evidence review, integration audit, or independent-review rules.

## Merge strategy

Squash merge is the only permitted merge method. Merge commits and rebase merges are disabled. Linear history is required.

## CODEOWNERS

`.github/CODEOWNERS` assigns default ownership to the repository maintainer and explicitly covers governance, workflows, tooling, tests, and the Source Registry.

When an independent reviewer team exists and has repository access, replace or supplement individual ownership with that team and set the reviewer-team requirement in `governance/github-enforcement.toml`.

## Activation boundary

Files in a pull request cannot themselves activate repository settings or an organization ruleset. After this PR is merged, an administrator must apply the declared settings in GitHub and verify that:

1. `Repository Gate` is listed as required.
2. strict status-check freshness is enabled.
3. conversation resolution is required.
4. squash merge is the only enabled merge method.
5. linear history is required.
6. code-owner review is required.
7. stale approvals and last-push approval protections are enabled.
8. force pushes and branch deletion are blocked.

Activation is complete only after the external settings match the TOML contract and the activation flags are updated in a follow-up audited change.
