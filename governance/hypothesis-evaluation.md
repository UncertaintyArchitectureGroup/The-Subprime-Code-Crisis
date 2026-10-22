# SDLC hypothesis and outcome evaluation

This guide explains how to test a claim about AI and software delivery: state the
idea, consider other explanations, compare it with the evidence and say what
remains unknown. A **node** means a part of the software development lifecycle
(SDLC), such as coding, review or operation.

Follow this guide when adding or materially changing a hypothesis about a delivery
activity, a claim that AI improves it, or a proposed control. It is a mandatory
extension of [AGENTS](../AGENTS.md#sdlc-hypotheses-and-complete-node-outcomes). Its
[comparison method](#compare-explanations) also implements the
[canonical comparison rule](../AGENTS.md#competing-explanations-and-diagnostic-evidence)
for relevant source assessments/searches. It runs inside the existing source and
governance procedures, not as a new source flow.
The [hypothesis register](../report/appendices/mechanism-hypotheses.md) owns the
research content; [master plan #84](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/84)
records the order of work. This is a method for testing the thesis and proposed
controls; adopting the method does not establish that either is correct.

## Start with a thesis and a discriminating question

Start with the explanation in ordinary words. Then split it into claims that
could receive different answers. Faster coding, different rates of improvement
across delivery activities, lost team understanding, checking and maintenance
obligations that remain unresolved, and higher total cost are separate claims.
Evidence for one does not establish the rest.

For each hypothesis, say who and what it concerns, what condition or change is
being tested, what it is compared with, what result it predicts and over what
period. Give plausible other explanations and results that would weaken the
hypothesis. Preserve existing IDs and links when revising the register. If an
earlier hypothesis is renamed or replaced, record where it went and why. A clear
thesis can make a strong argument while saying where it applies and which links
have yet to be measured.

## Compare explanations

Ask **“What else could produce this result, and what evidence would tell the
explanations apart?”** The register's
[ALT questions](../report/appendices/mechanism-hypotheses.md#competing-explanations)
help identify the strongest relevant alternatives. They cover different parts of
the argument and can sometimes be true together. They are a starting list, not
every possible explanation. `H0` is simply the ID of our main thesis; it is not the
statistical term “null hypothesis.”

Some ALT questions challenge the proposed mismatch or its persistence. Others
ask whether the work, measurement or user demand explains a particular result.
Two questions concern the decision to act: whether benefits exceed all costs
(ALT-6a), and whether a specified remedy adds enough benefit to justify its extra
costs (ALT-6b). Those two answers do not decide whether every individual harm
occurred. Keep the comparison in the existing source brief, register or task's
review record, using the [comparison template](templates.md#source-hypothesis-comparison).

1. **Choose the relevant questions.** For every source in the selected scope,
   identify the exact claim, delivery activity and relevant hypothesis/ALT IDs.
   Record who was studied, the condition or change, the comparison, the outcomes
   and the period measured. Explain why any important comparison does not apply.
   Say which explanations compete for the same result, which can coexist and
   which address different questions: coding speed, mismatch, duration, harm or
   value.
2. **Say what each explanation predicts.** Record the expected result and what
   would weaken that explanation. Describe evidence that could tell them apart:
   which way the result should change, how large a change would matter and over
   what period. Set those margins before testing; disclose choices made after
   seeing results. Distinguish “the proposed cause was absent” from “the proposed
   cause was present but the predicted harm did not follow.” Successful adaptation
   under the stated conditions can challenge a prediction of harm.
3. **Compare predictions with the original finding.** Give the exact source
   location, measure and unit, direction and size of the result, scope and
   uncertainty. Explain whether it supports, weakens or contradicts an account
   within that scope, or cannot tell the accounts apart. Say whether a missing
   answer comes from no measurement, an imprecise estimate or a study of a
   different question. A precise result can weaken a prediction of a meaningful
   effect. A statistically nonsignificant result alone does not show that two
   outcomes are equivalent. A result that fits several explanations may favor
   one if that explanation predicts its pattern more specifically. Explain why,
   and retain the study's design limits. Fitting the same result is not enough;
   do not invent probabilities or likelihood ratios to manufacture a distinction.
4. **Check other causes and all relevant outcomes.** Keep limits due to who chose
   the tool, which tasks they did, other simultaneous changes, measurement and
   the settings to which results can apply. Check for shared data, versions or
   analyses before counting evidence as independent. Use the full inventory below,
   including Review quality (such as fit, assumptions and security) and the team's
   ability to understand and take care of the system. Assess overall benefit
   (ALT-6a) separately from the added value of
   the specified remedy (ALT-6b). Benefits and harms can coexist; an overall gain
   cannot hide a loss in a critical outcome. An unchanged process that already
   works well can weaken the need for a remedy without disproving every proposed
   cause of harm.
5. **Record what follows and what is still needed.** Link the comparison to the
   hypothesis and the record of where the source is used. State unresolved
   outcomes and name the issue responsible for the next comparison or search.
   Source review checks the original finding; integration audit checks every
   material use; independent review looks for omitted alternatives and claims
   that the evidence tells them apart when it does not. These descriptions of
   support are not new source statuses or replacements for the hypothesis verdicts
   below. During a search (Flow E), judgments remain provisional. Before searching,
   record the question that could separate explanations and the search's scope
   and stopping point. Include evidence favorable to alternatives and against
   the proposed remedy.

**Example of the reasoning, not a study result:** if coding activity grows more
than releases, both a delivery constraint and a change in the type of work may
fit that pattern. The difference between the counts alone cannot decide which
explanation is better. The comparison must say what additional observation would
help, such as evidence about the work being done or the suspected constraint.

**Applying the method:** [#109](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/109)
introduced the method. [#110](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/110)
owns its application to the nine accepted evidence entries, and
[#111](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/111)
owns the limited search for evidence that can tell explanations apart. Adopting
the method did not compare the older source cards or change their status. Actual
changes to a source or its material use still trigger the applicable Flow A–D.

## Inventory the whole node

Use the [node assessment template](templates.md#sdlc-node-assessment) for Intent,
requirements, design, code, review, test, integration, deployment and operation.
Include the post-operation boundaries of realized user outcomes and business
economics, with feedback to Intent. The categories may overlap or recur; they are
not mandatory sequential departments or an instruction to equalize staffing.

List what the previous process actually contributed, including every function
or result that materially matters:

- product or technical output and assurance;
- decisions, constraints and acceptance criteria;
- team understanding, learning and knowledge transfer;
- responsibility, decision rights and competent ownership;
- coordination, handoff and dependencies;
- feedback, correction and future ability to change or recover the system.

The list helps check for omissions. It does not assume that every team or part of
the old process performed all these functions well. Add results that matter in the
particular setting and explain exclusions. Separate what the process was meant
to do from what evidence shows it did: demonstrated, weak, absent or unmeasured.
These descriptions are not new source statuses. Include existing automation,
known defects and costs; compare AI with the real previous process.

Describe what the intervention adds, removes or moves. If another node, person,
tool or procedure supplies the function, name that mechanism, owner and cost.
Do not count displaced work as eliminated or count the same benefit twice.

## Compare outcomes, including unknowns

For every result that materially matters, say how it is measured, whether the
measure is direct or an indirect indicator, its unit or denominator, what it is
compared with and for how long. Record the evidence and uncertainty. Keep benefits,
losses, work shifted to someone else and missing measurements separate. Time spent
working differs from time spent waiting. Completing a task, shipping a change,
helping a user and earning a business return are also different results.

A source does not need to measure the entire inventory. Its brief states which
outcomes it measures and which remain outside its scope. The node synthesis then
shows the combined coverage and gaps. Missing measurement establishes neither
preservation nor deterioration. A result about one outcome remains useful as a
bounded result, even when no overall verdict is possible.

Before calling a change an overall improvement, say how that judgment will be
made, which critical outcomes must meet a minimum standard, what tradeoffs are
acceptable and who decides. Include effects on users and the wider system. Every
metric need not improve. A new tool or practice can replace an old one when it
demonstrably performs the needed function; keeping the same manual steps,
document count or staffing level is not the goal. A critical loss needs an
explicit remedy or decision and must not disappear inside an average score.
Justify acceptable margins for the setting; this method sets no universal number.

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
