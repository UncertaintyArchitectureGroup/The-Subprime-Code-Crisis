# Governance playbooks

[`AGENTS.md`](../AGENTS.md) is the canonical operating specification and has precedence over every file in this directory. Read `AGENTS.md` in full before any repository work. These playbooks are mandatory procedural extensions when the selected flow requires them; they cannot override `AGENTS.md`. Resolve conflicts in favor of `AGENTS.md` and escalate unresolved ambiguity.

The repository also maintains four cross-cutting content references:

- [`DOCTRINE.md`](../DOCTRINE.md) defines research philosophy, evidence and interpretation principles, protocol principles, claim boundaries, and artifact principles.
- [`SCOPE.md`](../SCOPE.md) expands the repository's in-scope, out-of-scope, and adjacent-topic boundaries.
- [`ARTIFACT_MODEL.md`](../ARTIFACT_MODEL.md) expands the reader-facing map of repository artifacts and relationships.
- [`GLOSSARY.md`](../GLOSSARY.md) defines canonical repository vocabulary.

These documents do not create a workflow, source status, verification outcome, contributor obligation, or exception to `AGENTS.md`. Doctrine remains the canonical content authority for artifact and interpretation principles; Scope and Artifact Model are dedicated supporting references. When terminology is ambiguous, use the Glossary unless an original source explicitly uses the term differently.

After selecting a flow under `AGENTS.md`, read only its required playbooks plus the repository materials required by the start-of-work gate. For every substantive repository change, also use the [content synchronization](content-synchronization.md) playbook to assess affected surfaces and make an explicit changelog decision.

| Flow | Required playbooks |
| --- | --- |
| A — Add source | [status model](status-model.md), [evidence review](evidence-review.md), [integration audit](integration-audit.md), [independent review](independent-review.md), [templates](templates.md) |
| B — Legacy source | [status model](status-model.md), [evidence review](evidence-review.md) when needed, [integration audit](integration-audit.md), [independent review](independent-review.md), [templates](templates.md) |
| C — Changed source | [status model](status-model.md), [evidence review](evidence-review.md), [integration audit](integration-audit.md), [independent review](independent-review.md), [templates](templates.md) |
| D — Changed repository use | [status model](status-model.md), [integration audit](integration-audit.md), [independent review](independent-review.md), [templates](templates.md) |
| E — Evidence discovery | [evidence discovery](evidence-discovery.md), [independent review](independent-review.md), [templates](templates.md) |

## Navigation

- [Evidence review](evidence-review.md): registration, source acquisition and assessment, evidence brief, and completion.
- [Integration audit](integration-audit.md): repository-wide use search, trace, numeric and argument checks, corrections, synchronization, and verification completion.
- [Evidence discovery](evidence-discovery.md): complete Flow E methodology and Independent Search Review.
- [Independent review](independent-review.md): reviewer independence, allowed outcomes, correction loop, escalation, and verification gate.
- [Content synchronization](content-synchronization.md): affected-surface assessment, explicit non-applicability, and changelog decision for substantive changes.
- [Status model](status-model.md): allowed states, transitions, resets, and `Last verified`.
- [Templates](templates.md): mandatory records used by the applicable procedures.
