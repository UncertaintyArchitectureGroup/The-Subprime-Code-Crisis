# Governance playbooks

[`AGENTS.md`](../AGENTS.md) is the canonical operating specification and has precedence over every file in this directory. Read `AGENTS.md` in full before any repository work. These playbooks are mandatory procedural extensions when the selected flow requires them; they cannot override `AGENTS.md`. Resolve conflicts in favor of `AGENTS.md` and escalate unresolved ambiguity.

The repository also maintains four cross-cutting content references:

- [`DOCTRINE.md`](../DOCTRINE.md) defines research philosophy, evidence and interpretation principles, protocol principles, claim boundaries, and artifact principles.
- [`SCOPE.md`](../SCOPE.md) expands the repository's in-scope, out-of-scope, and adjacent-topic boundaries.
- [`ARTIFACT_MODEL.md`](../ARTIFACT_MODEL.md) expands the reader-facing map of repository artifacts and relationships.
- [`GLOSSARY.md`](../GLOSSARY.md) defines canonical repository vocabulary.

These documents do not create a workflow, source status, verification outcome, contributor obligation, or exception to `AGENTS.md`. Doctrine remains the canonical content authority for artifact and interpretation principles; Scope and Artifact Model are dedicated supporting references. When terminology is ambiguous, use the Glossary unless an original source explicitly uses the term differently.

After selecting a flow under `AGENTS.md`, read only its required playbooks plus the repository materials required by the start-of-work gate. For every substantive repository change, also use the [content synchronization](content-synchronization.md) playbook to assess affected surfaces and make an explicit changelog decision.

## Executable repository contract

[`repository-contract.toml`](repository-contract.toml) is a machine-readable projection of selected structural invariants already defined by `AGENTS.md` and the governance playbooks. It cannot create or override policy, source states, gates, contributor obligations, review outcomes, or exceptions.

The Python 3.11+ standard-library validator under [`tools/repository_validator/`](../tools/repository_validator/) checks:

- required files and required Markdown headings;
- exact Evidence review and Integration audit enums;
- every configured Source Registry section and its table schema;
- Source ID uniqueness and format;
- `Last verified` invariants; and
- local evidence-brief links for sources marked `Reviewed brief`, including the configured evidence class and exclusion of class-index `README.md` files.

Run it from the repository root:

```bash
python3 -m tools.repository_validator
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

The [`Main health`](../.github/workflows/main-health.yml) workflow runs these checks on pull requests, pushes to `main`, and manual dispatch. In this baseline phase it is diagnostic and non-blocking: it is not a required status check and does not establish governance completion, independent review, or source verification.

On a pull request, Main health executes the validator version proposed by that pull request. It is therefore a validator self-test, not tamper-resistant enforcement. On `main`, it checks the merged canonical version. A trusted base-branch validator and required status check belong to the later enforcement layer.

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
- [Executable repository contract](repository-contract.toml): machine-readable structural invariants consumed by the repository validator.
