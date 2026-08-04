## Executable repository contract

[`repository-contract.toml`](repository-contract.toml) is a machine-readable projection of selected structural invariants already defined by `AGENTS.md` and the governance playbooks. It cannot create or override policy, source states, gates, contributor obligations, review outcomes, or exceptions.

The Python 3.11+ standard-library validator under [`tools/repository_validator/`](../tools/repository_validator/) checks:

- required files and required active Markdown headings;
- exact Evidence review and Integration audit enums across supported Markdown list markers, with exactly one active canonical heading for each status dimension;
- every configured Source Registry section and its table schema, including the zero-row dataset section, while allowing ordinary explanatory prose around the table;
- Source ID uniqueness, ASCII format, class placement, and `DS-YYYY-NN` dataset IDs;
- `Last verified` ASCII-date invariants; and
- local evidence-brief links for sources marked `Reviewed brief`, including the configured evidence class, exclusion of class-index `README.md` files, non-empty active content, and the exact Source ID.

Fenced code, multiline HTML comments, and indented code are treated as inactive Markdown and cannot satisfy required headings, status enums, Source Registry tables, or evidence-brief identity checks.

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
| B — Process legacy registered source | [status model](status-model.md), [evidence review](evidence-review.md), [integration audit](integration-audit.md), [independent review](independent-review.md), [templates](templates.md) |
| C — Re-review changed source | [status model](status-model.md), [evidence review](evidence-review.md), [integration audit](integration-audit.md), [independent review](independent-review.md), [templates](templates.md) |
| D — Re-verify changed repository use | [status model](status-model.md), [integration audit](integration-audit.md), [independent review](independent-review.md), [templates](templates.md) |
| E — Discover newer or missing evidence | [evidence discovery](evidence-discovery.md), [templates](templates.md) |

## Governance playbooks

- [Status model](status-model.md): allowed states, transitions, reset rules, and `Last verified`.
- [Evidence review](evidence-review.md): source review, evidence-brief standard, limitations, and source-level interpretation.
- [Integration audit](integration-audit.md): repository-wide use verification, claim tracing, corrections, and protocol assessment.
- [Evidence discovery](evidence-discovery.md): bounded search for newer, stronger, contradictory, positive, null, or replication evidence.
- [Independent review](independent-review.md): reviewer qualification, valid outcomes, correction handling, and review-unavailable behavior.
- [Templates](templates.md): mandatory records used by the applicable procedures.
- [Content synchronization](content-synchronization.md): affected-surface assessment, explicit non-applicability, and changelog decision for substantive changes.
- [Executable repository contract](repository-contract.toml): machine-readable structural invariants consumed by the repository validator.
