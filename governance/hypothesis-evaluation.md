# SDLC hypothesis and outcome evaluation

This is a mandatory procedural extension of
[AGENTS](../AGENTS.md#sdlc-hypotheses-and-complete-node-outcomes) for new or materially
revised SDLC-node hypotheses, AI-improvement claims and proposed controls. It runs
inside the existing source and governance procedures, not as a new source flow.
The [hypothesis register](../report/appendices/mechanism-hypotheses.md) owns the
research content; [master plan #84](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/84)
owns its implementation sequence. This playbook defines the method, not a finding
that the thesis or a control is already validated.

## Start with a thesis and a discriminating question

State the proposed systems mechanism plainly, then decompose it into claims that
could receive different answers. A local coding gain, an uneven change in stage
capacity, a loss of team understanding, persistent debt and higher lifecycle cost
are separate claims. Evidence for one does not automatically establish the others.

For each hypothesis identify population/context, exposure or intervention,
comparator, predicted outcome, observation horizon, plausible alternatives and
observations that would weaken it. Preserve existing IDs and links when revising
the register. Record explicit aliases or dispositions instead of silently replacing
earlier hypotheses. A precise bounded thesis can be forceful without claiming a
universal effect or an already measured complete causal chain.

## Inventory the whole node

Use the [node assessment template](templates.md#sdlc-node-assessment) for Intent,
requirements, design, code, review, test, integration, deployment and operation.
Include the post-operation boundaries of realized user outcomes and business
economics, with feedback to Intent. The categories may overlap or recur; they are
not mandatory sequential departments or an instruction to equalize staffing.

For the actual previous workflow, inventory all material functions/outcomes:

- product or technical output and assurance;
- decisions, constraints and acceptance criteria;
- team understanding, learning and knowledge transfer;
- responsibility, decision rights and competent ownership;
- coordination, handoff and dependencies;
- feedback, correction and future ability to change or recover the system.

This is a coverage checklist, not an assertion that every node or historical team
delivered every function. Add context-specific outcomes and explain exclusions.
For each relevant outcome distinguish its intended function from evidence of its
actual delivery: demonstrated, weak, absent or unmeasured. These descriptions are
not additional source states. Include existing automation, known defects and
baseline costs; do not compare AI with an idealized manual process.

Describe what the intervention adds, removes or moves. If another node, person,
tool or procedure supplies the function, name that mechanism, owner and cost.
Do not count displaced work as eliminated or count the same benefit twice.

## Compare outcomes, including unknowns

For each material outcome record its observable, direct measure or proxy,
denominator/unit, comparator, follow-up period, evidence and uncertainty. Record
benefits, losses, transferred burdens and missing observations separately. Active
work and elapsed waiting are different; task completion, shipped change, user
benefit and business return are different boundaries.

A source does not need to measure the entire inventory. Its brief states which
outcomes it measures and which remain outside its scope. The node synthesis then
shows the combined coverage and gaps. Missing measurement establishes neither
preservation nor deterioration. A result about one outcome remains useful as a
bounded result, even when no overall verdict is possible.

For an overall-improvement claim, state the decision rule, critical outcome floors,
acceptable tradeoffs, decision owner and relevant user/system effects. A useful
change need not improve every metric. Functional replacement is permitted when
its claimed outcomes are demonstrated; manual ceremony, document volume and
headcount are not success criteria. Critical losses require an explicit remedy or
decision, not concealment inside an average score. Proposed margins must be
justified for the local context; this method sets no universal numerical threshold.

Assess the path to useful user outcomes and sustainable economics. Preserve service
quality, reduced user burden, avoided harm and useful learning as possible benefits;
an experiment that correctly stops unnecessary work can succeed without a release.
Separate realized user benefit, competitive advantage and ROI. Specify how benefits
and lifecycle costs connect in the given setting, including delayed maintenance,
support, failure and opportunity costs, rather than assuming those concepts coincide.

### Review has two gates

**Quality:** challenge assumptions, identify defects and assess fit, security,
maintainability and risk.

**Ownership:** the team knowingly takes responsibility and acquires or demonstrates
enough shared understanding to explain consequential behavior, diagnose failures,
make changes and contain or recover the system. Include knowledge transfer beyond
the original producer and the distribution of competent ownership.

Approval clicks, assigned names and generated explanations do not alone demonstrate
that capability. Possible observations include explanation of held-out behavior,
diagnosis/change/recovery tasks and dependence on a single author or preferred tool.
These are candidate measurements to justify in context, not universal mandatory
production gates. AI assistance can supply an effective replacement for manual
line inspection; the comparison concerns outcomes and total burden.

For example, faster merge and better defect detection with unmeasured understanding
support those two bounded gains. They do not yet establish improvement across the
whole Review node. Likewise, less manual reading is not evidence of lost ownership
when the proposed substitute demonstrably supplies it.

## Test harms and remedies symmetrically

State an adverse prediction and a separate intervention prediction. Define exposure
and intervention independently of the outcome: do not infer overload from a queue
and then use that queue as confirmation, or define lost ownership by the recovery
failure that is supposed to test it.

Specify the comparator, meaningful effect and quality/capability margins before
evaluating the result. For retrospective synthesis, say what was specified before
the search and what was learned afterward; do not claim preregistration after
seeing the findings. A nonsignificant difference does not establish equivalence.

Distinguish absence of the trigger, successful adaptation, disconfirmation under
the trigger and net benefit. Successful unchanged practice limits a claim that
rebalancing is necessary. A prespecified remedy that adds cost without sufficient
benefit weakens that remedy; do not rescue it by redefining "proper rebalancing"
afterward. An adverse local result does not demonstrate industry-wide prevalence.

## Judge evidence by fit and independence

One macro study and one micro study can provide useful triangulation when they
address the same scoped claim or complementary links in its stated mechanism.
For this purpose, "macro" means evidence across a broader delivery population or
organizational system; "micro" means direct investigation of the local task,
team behavior or mechanism. Record the actual unit and design: sample size alone
does not determine either category or its strength.

Before assigning a triangulated verdict:

1. Map each result to the exact hypothesis, outcome and scope it bears on.
2. Assess methods, selection, comparator, uncertainty and plausible alternatives.
3. Check independence of underlying data/analysis. Versions, summaries, the same
   dataset reused, and the author's own essays are not independent replications.
4. Search for relevant positive, null, contradictory and successful-adaptation
   evidence, including evidence against the proposed remedy.
5. Explain what remains unsupported and what observation would change the verdict.

Two independent, relevant empirical evidence families with convergent results can
justify **Plausible — triangulated** when methodological adequacy, metric fit and
material contrary evidence have been addressed. A macro/micro pair is one route,
not a rigid quota. Convergence on separate links does not itself identify the full
causal chain. A serious unresolved contradiction requires a narrower or mixed
verdict. Institution reputation and source counts do not substitute for this work.

A single rigorous study can support its own bounded finding. Do not downgrade that
finding solely because no macro/micro pair exists, or require a census of the
industry before a clearly labeled systems hypothesis can be investigated.

### Hypothesis verdict vocabulary

| Verdict | Meaning |
| --- | --- |
| **Open** | The scoped proposition has not been adequately assessed or material evidence is missing. |
| **Provisional support** | Relevant evidence supports part of the proposition; important gaps remain. |
| **Plausible — triangulated** | Independent, scope-compatible empirical families converge under the assessment above; the broader mechanism remains an inference where not directly identified. |
| **Supported within scope** | Evidence adequately establishes the stated bounded proposition, with design, uncertainty and limits explicit. This may describe one rigorous study's finding. |
| **Mixed / context-dependent** | Relevant results differ, conditions matter materially or the balance cannot be resolved at the proposed scope. |
| **Weakened / rejected within scope** | Relevant observations materially weaken or contradict the stated proposition within the tested setting. |

Record the rationale, source IDs/versions, outcome coverage, counterevidence and
date next to the verdict. These are claim-level assessments, not probabilities or
a compulsory ladder. They do not replace claim classes, `Evidence review`,
`Integration audit`, `Last verified` or independent-review outcomes. No existing
hypothesis receives a new verdict merely because this method was adopted.

## Integrate and hand off through existing flows

Use Flow E for a defined search; route accepted new or changed sources through A
or C. Use B/D when their existing triggers apply. Discovery notes cannot change
report claims or source status. Source impact reports, substantive approval,
integration audits, synchronization and independent review remain required.

When a node assessment changes report wording or a protocol, inspect all relying
claims and the consequences for other outcomes. Keep the four protocol layers;
map a proposed control to the function it supplies and the outcome it should
improve. Completing a research issue may legitimately leave a hypothesis open,
mixed or rejected. Complete all applicable procedural acceptance, then follow the
[one-issue plan checkpoint](issue-workflow.md#one-issue-execution-and-plan-checkpoint).
No requirement to prove every hypothesis or finish every node blocks an otherwise
accepted first readable edition; the master plan records the selected release scope.
