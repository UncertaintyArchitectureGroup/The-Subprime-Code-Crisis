# Issue workflow

This is a mandatory procedural extension of [AGENTS](../AGENTS.md#issue-intake-and-task-lifecycle), which remains canonical. Source flows and completion/independent-review gates retain precedence.

## Issue intake and durable intent

Use an issue as the durable record for each substantive research, publication,
repository-management or tooling task. Reuse an existing issue when it already
owns the input. Strictly mechanical fixes may proceed without a new issue; state
the narrow exception in the PR. Incoming contributor issues may be incomplete:
triage them with a comment rather than requiring a duplicate or rewriting the
contributor's original message.

Before implementation, record:

- **Original intent:** the question/problem, why it matters, initial request and
  public source or maintainer decision.
- **Owner and type:** research input, publication or repository task; exact owning
  paths, current ref, source/research IDs where applicable.
- **Scope:** expected outcome, exclusions, dependencies, unresolved choices.
- **Acceptance:** observable checks and required editorial, independent or human
  decisions.
- **Plan:** next step and linked PRs; use full issue URLs for other repositories.

Preserve the original intent. Append scope changes with date, reason and decision
reference; never silently rewrite the goal to fit the result. An issue is a task
record, not a replacement for a canonical source registry, research register,
provenance note or framework decision.

### Research-input report before integration

For a new report, expert discussion, hypothesis, test data, changed source or
material critique, first inspect the original input and all plausibly affected
existing research and source uses. Produce a bounded report in an issue comment
or linked review artifact **before substantive claim, protocol or framework
edits**. Safe source acquisition, inventory and provisional review work may
proceed to prepare that report.

The report must contain:

1. exact input/version, access limitations and public/private provenance;
2. source methods/findings/limitations, separated from repository interpretation;
3. existing source/research IDs, conflicting or corroborating evidence and the
   complete searched use/impact scope (including a reasoned no-change result);
4. affected claims, numbers, diagrams, maps, protocols, publications or framework
   owners, with paths and proposed treatment;
5. recommendation: include, exclude, narrow, defer, or request more evidence;
6. proposed acceptance checks, open decisions and maintainer-review request.

Wait for the required maintainer decision on substantive integration. An existing
explicit authorization covering that exact treatment may be referenced instead
of asking again. Silence or elapsed time is not approval. Preserve private
correspondence boundaries; link public evidence or a bounded authorized summary.

### Implementation, review and closure

1. Link the owning issue in the PR body using `Refs #N` or a full issue URL.
   Prefer a non-closing reference while review, deployment, publication or sibling
   work remains. Do not use `Closes`/`Fixes` merely because some code is merged.
2. Implement the accepted scope under the repository's existing review,
   synchronization, validation and source/research procedures.
3. Independently check the result where required, return corrections to the
   applicable flow, and record unresolved disagreement or missing review.
4. Add a completion summary to **both PR and issue**: original intent versus
   actual outcome, exact merged ref/edition, acceptance evidence, review and
   decision references, deviations, remaining work and cross-repository results.
5. Close as completed only when the accepted outcome is merged and checked and
   all applicable decisions/acceptance checks are satisfied. Rejection,
   duplication, supersession or deferral needs an explicit disposition and links
   to surviving work; it must not be reported as implementation completion.

Draft, merged, reviewed, published and deployed are separate observations.
An umbrella issue remains open until its required dependencies are complete.
Issue closure and green CI do not change scientific or source-verification state.
