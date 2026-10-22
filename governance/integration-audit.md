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
For each material occurrence, add a stable claim ID and source page/table/figure
or exact section. Distinguish four judgments: wording/inference, numbers/units,
fit at the current location, and a better destination if one is proposed. Include
uncited repetitions and neighboring conclusions; a source-level row alone cannot
establish occurrence-level completeness.

### 5. Verify numbers and units

For every number:

- confirm numerator, denominator, unit, population, and time window;
- distinguish percentages from percentage points;
- distinguish cumulative, average, median, short-run, and long-run effects;
- preserve material uncertainty;
- reproduce simple derived calculations where practical;
- do not combine different studies, samples, tools, or periods into one observed sequence without explicit labeling;
- remove obsolete or untraceable numbers.
- distinguish participant counts from completer counts, activity counts from
  elapsed time, repository role from professional seniority, and stock from flow;
- preserve version and observation dates; a live chart embedded in an old post
  is not evidence that its current model results existed on the post's date;
- do not average unrelated metrics into a claimed net-productivity estimate or
  turn a proxy complexity measure into a measured cognitive-load percentage.

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
- an SDLC improvement claim covers the node's full function/outcome inventory,
  including understanding/ownership, or explicitly remains a bounded result;
- the actual baseline, substitutions, missing measures, tradeoffs and downstream
  user-value/full-cost implications follow the
  [hypothesis evaluation method](hypothesis-evaluation.md);
- hypothesis support reflects independent evidence, scope fit and counterevidence,
  and adverse mechanisms and proposed remedies both remain falsifiable;
- the [source hypothesis comparison](templates.md#source-hypothesis-comparison)
  covers applicable rivals and matches original direction, magnitude, scope and
  uncertainty at every material use; it distinguishes missing measurement,
  imprecision and irrelevant scope, and justifies any claimed discrimination
  rather than inferring it from shared compatibility alone;
- net value and the specified remedy's incremental value remain separate, with
  adverse endpoints and critical-outcome losses visible alongside benefits.

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
Critique named claims with evidence and scope, not presumed vendor intent.
For an unmeasured mechanism, state the conditions, plausible alternatives,
observable consequences and possible disconfirming evidence. Scenarios need
explicit uncertainty; do not assign relative probabilities without a method.

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

For a proposed SDLC control, map the functions/outcomes it supplies, shifts or
risks losing; inspect Review ownership as well as quality where affected. State
the comparator, cost/tradeoffs, expected benefit and observation that could weaken
the remedy. Do not infer a control's effectiveness from support for the risk alone.

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
- [ ] Applicable source hypothesis comparisons and their diagnostic limits match the original results and every material use.
- [ ] Report, README claims/tables/diagrams/maps, and neighboring conclusions were assessed.
- [ ] Protocol implications record exactly one allowed outcome.
- [ ] Any substantive change received explicit human approval before implementation.
- [ ] `Current use` records actual locations.
- [ ] Brief, registry, relevant index, `REFERENCES.md`, links, versions, and removed claims are synchronized.
- [ ] Independent review is `Confirmed`.
- [ ] Brief and registry have matching status and date.
- [ ] No unresolved correction or human decision remains.
