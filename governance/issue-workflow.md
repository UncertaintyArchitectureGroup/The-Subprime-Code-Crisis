# Issue workflow

This is a mandatory procedural extension of [AGENTS](../AGENTS.md#issue-intake-and-task-lifecycle), which remains canonical. Source flows and completion/independent-review gates retain precedence.

## Issue intake and durable intent

Use an issue as the durable record for each substantive research, publication,
repository-management or tooling task. Reuse an existing issue when it already
owns the input. Strictly mechanical fixes may proceed without a new issue; state
the narrow exception in the PR. Incoming contributor issues may be incomplete:
triage them with a comment rather than requiring a duplicate or rewriting the
contributor's original message.

The issue records the intent; PRs and their commits record its execution. When
asked to create an issue, recover the request and clarify the intended outcome,
reason, boundaries and acceptance with the maintainer. If a material choice is
unclear, ask focused questions before presenting an agreed intent or starting
dependent implementation. An intake issue may preserve the original request with
clearly marked open questions; assumptions are provisional, not decisions.
Continue independent inspection or reversible preparation where useful. Do not
ask again about decisions or routine work already authorized.

Compare each implementation scope with the owning issue before editing, during
PR review and before closure. Explain which acceptance checks the PR/commits
satisfy and which remain open. If execution diverges, correct it or record the
maintainer's dated intent change; do not rewrite the issue to excuse the result.

Before implementation, record:

- **Original intent:** the question/problem, why it matters, initial request and
  public source or maintainer decision.
- **Owner and type:** research input, publication or repository task; exact owning
  paths, current ref, source/research IDs where applicable.
- **Scope:** expected outcome, exclusions, dependencies, unresolved choices.
- **Acceptance:** observable checks and required editorial, independent or human
  decisions.
- **Plan:** next step and linked PRs; use full issue URLs for other repositories.

Use stable acceptance IDs such as `AC-1`. Record a compact table of
`AC ID | observable pass condition | check/review | exact source/run | result`.
Automated checks, source interpretation, independent review and maintainer
decisions remain distinct. Tick only an entire satisfied criterion; clear a tick
when its evidence is invalidated. A stale run or unchecked manual condition stays
open. Link implementation commits with `Refs #N` and refresh links after rebases.
Keep detailed analysis/review in a dated `governance/reviews/issue-N-YYYY-MM-DD-kind.md`
owned by the same task; an issue comment supplies the outcome and exact link.

Preserve the original intent. Append scope changes with date, reason and decision
reference; never silently rewrite the goal to fit the result. An issue is a task
record, not a replacement for a canonical source registry, research register,
provenance note or framework decision.

## One-issue execution and plan checkpoint

The canonical cycle is in
[AGENTS](../AGENTS.md#one-issue-then-a-plan-and-approval-checkpoint). The live
[master plan #84](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/84)
owns sequence and dependencies; dated audits and memory are navigation snapshots.

Before substantive work, record the selected issue, scope/acceptance and explicit
maintainer approval. A queued item or approved roadmap is not approval to start
each item. Work only that implementation issue through corrections, independent
review, required checks, merge and accepted default-branch verification. Several
PRs may belong to it, including a final source-verification PR. Preserve existing
authorization for routine steps inside that scope; do not repeatedly ask for it.

After completion, use the [plan checkpoint](templates.md#post-merge-plan-checkpoint):

1. Fetch the actual issue/PR/main/check state and reread the live master plan.
2. Compare the result with the thesis, process, dependencies and proposed order.
   Append a dated change with its reason, or record why no change is needed.
   Do not rewrite original intent or imply a dependent issue is complete.
3. Present the maintainer with the completed outcome, current ordered plan and
   **one proposed next issue**, its concrete scope/acceptance and open decisions.
4. Wait for explicit approval before starting that next issue. Record the approval
   in its intake/start record. Silence, elapsed time and passing checks do not count.

The checkpoint is part of closing the current cycle. It can be recorded in the
owning issue and live plan after merge; a speculative future merge must not be
written as a fact in a PR. Memory can point conditionally to those live records,
without requiring a recursive PR merely to predict its own completion.

If blocked, show the blocker and proposed replan and request a decision before
switching implementation issues. Read-only planning, issue intake and independent
review within the active scope may run in parallel. Multiple implementation issues
require an explicit maintainer exception. A materially different treatment within
the active issue still uses the existing substantive-change gate.

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
6. proposed acceptance checks, open decisions and maintainer-review request;
7. for an SDLC hypothesis or improvement claim, the affected node's full outcome
   inventory, source coverage/omissions, tradeoffs and symmetric tests under the
   [hypothesis evaluation method](hypothesis-evaluation.md);
8. for a relevant hypothesis, improvement claim, control or source assessment,
   the [applicable rival comparison](templates.md#source-hypothesis-comparison),
   its diagnostic limits and the owner of pending application/search. A proposed
   Flow E search states the discriminating question and bounded scope; screening
   judgments remain provisional and do not authorize integration.

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
After completion, finish the master-plan and next-issue approval checkpoint above.

## Handoff and proportional checks

Update [memory](memory.md) at meaningful interruption or handoff, retaining its
five sections and 120-line bound. It records dated refs, decisions, evidence,
remaining acceptance and next action, not an alternative source registry.
Revalidate live state when resuming. Do not copy the site's deployment, browser,
release-controller or per-task acceptance machinery into this research repository.
Use existing repository tests/gates, targeted RI regressions when RI changes and
human source/argument review. Green structural validation cannot prove a number,
causal conclusion or optimal placement.

### Live-status checkpoint

This checklist makes the existing AGENTS start/handoff/closure checks explicit;
it does not add a flow, approval or source-state definition. At resumption and
final acceptance, inspect the live owning issue (state, full ACs, latest evidence),
linked PRs (head/base, merged SHA and review outcome), default-branch SHA and CI
runs for that exact SHA. Compare canonical registry/brief fields and dates at
that ref with the dated handoff. Record inspected URLs, refs, run conclusions,
unavailable facts and the as-of checkpoint in the issue/review record.

Refresh memory when the checkpoint changes. A merge awaiting verification is not
completion; an old pending action must not be repeated unconditionally after its
issue closes. Point to the live owner for subsequent status and use conditional
next actions where a PR cannot record its own future merge. Rebuild/verify RI
after memory changes. RI verifies local bytes and reproduces source fields; it
does not fetch GitHub or decide whether an issue, review or scientific audit is
complete. Missing live access stays unresolved.
