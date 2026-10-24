# GitHub enforcement desired state

## Status and precedence

This playbook records the approved GitHub enforcement desired state. `AGENTS.md` remains canonical. The machine-readable contract is `governance/github-enforcement.toml`. Neither this file nor the TOML activation flags prove that external GitHub settings are active.

## Protected branch

The protected branch is `main`. The desired state requires changes to arrive through pull requests and prohibits force pushes and branch deletion.

## Required checks and freshness

The desired state requires the status check named `Repository Gate`. Strict branch freshness requires that check to pass against the current base branch before merge.

## Pull request requirements

Conversation resolution is required from initial activation.

While no independent reviewer pool exists, the desired state does not require an approving review, code-owner approval, or last-push approval. `.github/CODEOWNERS` remains useful for routing and accountability, but it is not a merge gate when the only listed owner is the pull-request author.

After at least one independent reviewer or reviewer team has repository access, enable one approving review, code-owner review, stale-review dismissal, and approval of the most recent push. When a team is used, configure its slug in `governance/github-enforcement.toml`.

A green check or GitHub approval does not replace the repository's human approval, evidence review, integration audit, or independent-review rules.

## Merge strategy

The desired state permits squash merge only. Merge commits and rebase merges are disabled, and linear history is required.

## CODEOWNERS

`.github/CODEOWNERS` assigns default ownership to the repository maintainer and explicitly covers governance, workflows, tooling, tests, and the Source Registry.

When an independent reviewer team exists and has repository access, supplement or replace individual ownership for the relevant surfaces and activate the reviewer requirements in the TOML contract.

## Activation boundary

Files in a pull request cannot themselves activate repository settings or an organization ruleset. This PR establishes a tracked desired-state baseline. It does not complete PR 4's external enforcement activation.

After merge, a repository administrator must apply the declared settings in GitHub and verify that:

1. `Repository Gate` is listed as required.
2. strict status-check freshness is enabled.
3. conversation resolution is required.
4. squash merge is the only enabled merge method.
5. linear history is required.
6. force pushes and branch deletion are blocked.
7. review requirements remain disabled while no independent reviewer pool exists.
8. review, code-owner, stale-review, and last-push requirements are enabled only after an independent reviewer pool exists.

Activation is complete only after live settings match the TOML contract and a follow-up audited change sets the activation flags to `true`.
