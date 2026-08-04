# PR process and synchronization contract

## Status and precedence

`AGENTS.md` remains canonical. This document explains the executable PR process approved for PR 2 and cannot override source states, approval gates, independent review, or completion rules.

## Pull request records

Every governed pull request uses both:

- `.github/pull_request_template.md` for the human-readable review record; and
- one new `governance/work-records/*.toml` file for machine validation.

## Changed-path classification

`governance/synchronization-matrix.toml` maps repository paths to synchronization surfaces. Repository Gate fails closed when a changed path is not classified or when the work record omits a required surface.

## Changelog decision

The work record must declare exactly one decision:

- `Updated`, in which case `CHANGELOG.md` must change; or
- `Not required`, with a specific reason, in which case `CHANGELOG.md` must not change.

## Critical deletion protection

Critical paths listed in the synchronization matrix cannot be deleted or renamed by an ordinary pull request. Changing that protected set is itself a substantive governance change.

## Repository Gate

`.github/workflows/repository-gate.yml` uses `pull_request_target`, read-only permissions, immutable checkout actions, and the gate implementation from the trusted base branch. Candidate content is checked as data; candidate scripts are not executed by the trusted workflow.

After this PR is merged, repository branch rules must require the status check named `Repository Gate`. The workflow cannot be made a required check before it exists on the default branch.
