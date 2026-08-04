# Changelog

This changelog records selected material changes to the repository's reader-facing argument, evidence model, protocols, content architecture, attribution, citation identity, and governance.

It is not a complete commit ledger. Git history and pull requests remain authoritative for implementation details. [`evidence/SOURCES.md`](evidence/SOURCES.md) remains canonical for source identity and status, and evidence briefs remain canonical for source-oriented review records.

## Unreleased

### Added

- Added this repository changelog and a dedicated content-synchronization playbook.

### Changed

- Restructured the README around Quick Start, Key Takeaways, and a repository map; reduced duplicate navigation and artifact-flow explanation while preserving the Claim confidence map, Evidence Map, Crisis Map boundaries, operational control stack, and the bounded `P-2026-01` evidence summary.
- Expanded the Doctrine's map principles so reader summaries and visualizations preserve claim class, scope, uncertainty, attribution, and source boundaries.

### Governance

- Added a mandatory content-synchronization assessment and explicit changelog decision for substantive repository changes.
- Added a non-blocking executable repository contract, standard-library validator and tests, five-class Source Registry parser including the canonical dataset section, inactive-Markdown filtering, and diagnostic Main health workflow.
- Added the governed PR template, machine-readable work records, changed-path classification and synchronization matrix, critical-deletion protection, and trusted Repository Gate workflow.

## 2026-08-03

### Added

- Added the [Repository Scope](SCOPE.md) and [Repository Artifact Model](ARTIFACT_MODEL.md), with synchronized reader and contributor entry points ([PR #34](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/pull/34)).
- Added the [Repository Doctrine](DOCTRINE.md) and canonical [Glossary](GLOSSARY.md), clarifying claim classes, evidence boundaries, protocol principles, and recurring terminology ([PR #33](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/pull/33)).

### Changed

- Added bounded terminology-provenance records, clarified attribution boundaries, and corrected repository citation metadata ([PR #32](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/pull/32)).

## 2026-07-27

### Evidence

- Established the Evidence Library taxonomy and evidence-brief standard, added the canonical Source Registry, and separated evidence review from repository-wide integration verification ([PR #5](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/pull/5), [PR #15](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/pull/15), [PR #16](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/pull/16)).
- Added and integrated the *Writing Code vs. Shipping Code* evidence brief, then rebuilt and independently verified its bounded use in the Crisis Map and repository argument ([PR #6](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/pull/6), [PR #7](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/pull/7), [PR #28](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/pull/28), [PR #30](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/pull/30)).

### Added

- Reworked the four operational protocols into an engineer boundary, team control loop, public evidence and disclosure protocol, and organizational control model, then integrated them as one control stack ([PR #10](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/pull/10) through [PR #14](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/pull/14)).

### Changed

- Added and refined the Evidence Map, separating evidence classification from the Claim confidence map and from repository synthesis ([PR #8](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/pull/8), [PR #9](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/pull/9)).

### Governance

- Established explicit source workflows, independent review, human escalation, workflow evolution, evidence discovery, source-state governance, and the compact `AGENTS.md` router with mandatory playbooks ([PR #18](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/pull/18), [PR #20](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/pull/20) through [PR #25](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/pull/25), and [PR #31](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/pull/31)).

## Maintenance rule

Every substantive pull request must make an explicit changelog decision:

- **Updated** — when the change materially affects readers, contributors, evidence interpretation, major claims or maps, protocols, repository architecture, attribution, citation identity, or governance.
- **Not required — reason** — when the change is mechanical or does not materially alter repository behavior or reader understanding.

Do not add entries merely for spelling, formatting, final-newline fixes, broken-link repair, navigation-only maintenance, or internal refactoring with no material reader or contributor effect.

Use [`governance/content-synchronization.md`](governance/content-synchronization.md) for the complete assessment procedure.
