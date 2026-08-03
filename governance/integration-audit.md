# Integration audit playbook

This playbook is a mandatory procedural extension of [`AGENTS.md`](../AGENTS.md) for integration audits in Flows A–D. `AGENTS.md` is canonical and has precedence; resolve conflicts in its favor. Read it in full before this playbook. Evidence review and integration audit remain separate.

## Integration-audit procedure

### 1. Start the audit

Set in both the registry and brief:

```text
Integration audit = In progress
Last verified = —
```

### 2. Establish source ground truth

Confirm:

- title, authors, date, exact version, and publication status;
- official URL;
- research entity, affiliations, and funding when relevant;
- design, dataset, population, period, and comparator;
- exact metric definitions;
- exact numbers and uncertainty;
- whether results are observed, derived, model-calibrated, self-reported, or interpreted;
- limitations and conflicts.

### 3. Locate every repository use

Search for:

- source ID;
- author and organization names;
- title fragments;
- distinctive metric names;
- every attributed number;
- uncited paraphrases;
- diagrams, captions, summaries, and protocol language implicitly depending on the source.

Inspect at minimum:

- all files under `report/`;
- `README.md`, including tables, captions, diagrams, and claim-confidence entries;
- all files under `protocols/`;
- `REFERENCES.md`;
- `evidence/SOURCES.md`;
- evidence-directory indexes.

Do not trust `Current use` without confirming actual usage.

### 4. Build a claim-to-source trace

For every material use, record:

| Repository claim | Location | Exact source result | Relationship | Action |
| --- | --- | --- | --- | --- |
| Claim or paraphrase | File and section | Finding or record | Direct, derived, synthesis, scenario, or unsupported | Keep, qualify, correct, relocate, or remove |

The trace must be inspectable and its location recorded in the brief.

### 5. Verify numbers and units

For every number:

- confirm numerator, denominator, unit, population, and time window;
- distinguish percentages from percentage points;
- distinguish cumulative, average, median, short-run, and long-run effects;
- preserve material uncertainty;
- reproduce simple derived calculations where practical;
- do not combine different studies, samples, tools, or periods into one observed sequence without explicit labeling;
- remove obsolete or untraceable numbers.

A number in a table, caption, or diagram is a claim.

### 6. Verify argument fit

Check whether:

- observational evidence is presented as causal;
- bounded tasks are generalized to teams, enterprises, industries, or the economy;
- different developer populations are treated as interchangeable;
- activity is described as productivity, quality, shipped value, or business impact without justification;
- source-author interpretation is presented as an observed result;
- repository synthesis is clearly identified;
- positive, null, mixed, contradictory, and unfavorable findings are treated fairly.

When this check reveals a possible need to change report logic, a major conclusion, claim confidence, protocol logic, or a load-bearing repository map, do not edit that substantive artifact yet. Trigger the human-curated substantive-change discussion defined above, then follow [escalation](../AGENTS.md#escalation-and-conflict-handling) and [human approval gate](../AGENTS.md#human-approval-and-substantive-change-gate).

### 7. Verify report integration

For every report use:

- explain what the source measured;
- link to the evidence brief;
- separate findings from repository inference;
- expose material limitations near the claim;
- remove inconsistent duplicate retellings;
- identify neighboring paragraphs and chapter conclusions that may require change.

A corrected citation is insufficient if the surrounding argument remains misleading.

Substantive report changes require explicit human approval before implementation.

### 8. Verify README and repository maps

Reassess:

- Key Takeaways;
- claim-confidence map;
- Evidence Map;
- Crisis Map and other diagrams;
- repository-level numeric claims;
- source coverage descriptions.

Multi-source diagrams must label source boundaries and must not present unrelated numbers as one measured causal chain.

Changes to load-bearing synthesis or claim confidence require explicit human approval before implementation.

### 9. Verify protocol implications

Inspect every protocol for explicit or implicit reliance on the source. Document exactly one outcome:

- `No protocol change`
- `Protocol clarification`
- `Protocol change proposed`

Do not change a protocol merely for symmetry with a report change.

A proposed protocol clarification or protocol change must follow [escalation](../AGENTS.md#escalation-and-conflict-handling) and [human approval gate](../AGENTS.md#human-approval-and-substantive-change-gate), and must be discussed with and approved by the human user before implementation.

### 10. Synchronize records

After approved corrections:

- update the brief;
- update actual `Current use` locations in `evidence/SOURCES.md`;
- update the relevant evidence index;
- update `REFERENCES.md`;
- verify links;
- record superseded versions and removed claims.

## Correction handling and verification completion

When any defect remains, set `Integration audit = Corrections required` and `Last verified = —`, document the defect and affected locations, complete approved corrections, repeat all affected checks, and repeat independent review. Do not infer correction from a changed citation or plausible text.

Only after all corrections are merged, the independent-review outcome is `Confirmed`, and the checklist below passes may the registry and brief be synchronized to `Integration audit = Verified` with the same `Last verified = YYYY-MM-DD`. Verification must describe the completed default-branch state.

## Completion checklist

- [ ] Current `AGENTS.md` and mandatory playbooks were read before work.
- [ ] Correct source version and source-ground-truth fields were checked.
- [ ] Reviewed, indexed evidence brief exists.
- [ ] Every repository mention, attributed number, uncited paraphrase, diagram, caption, summary, and implicit protocol dependency was searched and inspected.
- [ ] Inspectable claim-to-source trace exists for every material use.
- [ ] Numerators, denominators, units, populations, periods, uncertainty, and derived calculations were checked.
- [ ] Claim strength and nearby argument fit match source design and scope.
- [ ] Report, README claims/tables/diagrams/maps, and neighboring conclusions were assessed.
- [ ] Protocol implications record exactly one allowed outcome.
- [ ] Any substantive change received explicit human approval before implementation.
- [ ] `Current use` records actual locations.
- [ ] Brief, registry, relevant index, `REFERENCES.md`, links, versions, and removed claims are synchronized.
- [ ] Independent review is `Confirmed`.
- [ ] Brief and registry have matching status and date.
- [ ] No unresolved correction or human decision remains.
