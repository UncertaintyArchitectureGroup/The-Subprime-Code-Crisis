+++
source_ids = ["P-2026-05"]
evidence_review = "Reviewed brief"
integration_audit = "Needs re-verification"
last_verified = "—"
independent_review = "Confirmed"
current_use = ["README.md", "report/02_broken_mechanics.md", "report/appendices/mechanism-hypotheses.md", "REFERENCES.md"]
+++

# Shen–Tamkin: AI assistance and learning a new programming library

## Comparison acceptance — 2026-10-23, #110

The [independent acceptance report](../../governance/reviews/issue-110-2026-10-23-independent-acceptance.md)
confirms the comparison and integration correction at `22c4f589d7d9eb6adfa1b50138dc17e4471acd8f`.
It states which accepted original-source checks were reused and which fresh
access attempts were unavailable; it does not claim a fresh reading of every PDF.
The factual findings, accepted version, uncertainty and Current use are unchanged.

Evidence review remains **Reviewed brief**. Integration remains
**Needs re-verification / —** until the accepted content is merged and actual-main
checks pass. Independent review is **Confirmed** for the report’s stated content
scope, not for a future merge or a final Verified state. The dated notes below
are history and do not replace this current checkpoint.

## Comparative-use reset history — 2026-10-23, #110

The maintainer [approved T1–T4](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/110#issuecomment-6361681797) after the
[nine-source comparison and exact treatment proposal](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/110#issuecomment-6360324854).
The new [comparison C9](../../report/appendices/mechanism-hypotheses.md#comparison-c9)
uses this same accepted source object. Its findings, version and historical
reviews below are preserved. Flow D retains **Reviewed brief** and resets
integration to **Needs re-verification / —** for the changed use.

Independent review of this new comparison is **Corrections required**. The
[separate review](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/pull/115#discussion_r4359943405) inspected all nine comparisons, their accepted
briefs and prior source checks, the synthesis and retained-use trace. It found
the reused factual premises of C3–C9 adequately covered by accepted original
checks and required synchronization of the stale review outcomes. This note
records that review, not final acceptance of this correction. Earlier
Confirmed reviews retain their dated scope; they do not certify the new
comparison by themselves. The
[primary integration record](../../governance/reviews/issue-110-2026-10-23-integration.md) identifies the inspected
surfaces, exact locators and remaining acceptance. No final verification, merge
or confidence promotion is claimed. This checkpoint supersedes older current-
state wording only for the new use; it does not erase earlier acceptance.


## Review checkpoint — 2026-10-22, #4

This is the source assessment for [#4](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/4).
The [impact and treatment proposal](../../governance/reviews/issue-4-2026-10-22-source-impact.md)
contains the exact report, hypothesis-register and README treatment, approved
by the maintainer on 2026-10-22 ([decision receipt](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/4#issuecomment-6339806018)).
The accepted additions were merged through PR #108 and independently accepted
on actual main `66f3d8ac65432275c8745654a47b693cb8d9ed0e`; the
[integration audit](../../governance/reviews/issue-4-2026-10-22-integration.md)
records their actual uses. The [final-verification receipt](../../governance/reviews/issue-4-2026-10-22-final-verification.md)
records independent acceptance of that exact default-branch state and its checks.
Source verification concerns accurate repository use; it does not resolve the
paper's reporting limitations or establish the full SDLC thesis.

## Identity, exact version and access

**P-2026-05** — Judy Hanwen Shen and Alex Tamkin, *How AI Impacts Skill Formation*.
Reviewed original: [arXiv:2601.20245v2](https://arxiv.org/abs/2601.20245v2),
submitted **1 February 2026**; v1 submitted 28 January. The version record says
v2 corrects the balance table and preregistration link. This review pins the
[31-page v2 PDF](https://arxiv.org/pdf/2601.20245v2) and its
[HTML rendering](https://arxiv.org/html/2601.20245v2); section/table/figure
locators below refer to that version, not an unversioned future revision.

The original was inspected through web PDF/text and HTML access. Local download
failed at the unavailable browser proxy, so **no local PDF checksum or byte-level
archive is claimed**. The PDF displays 3 February; the HTML rendering displays
24 August. Neither display date supersedes arXiv's version/submission record.
The reviewed object is a preprint. An [official OpenReview lead](https://openreview.net/forum?id=WpL9rAd0K7)
also exists, but accepted venue/publication and text equivalence have not been
independently established; do not label this edition peer reviewed.

The first author identifies work within the Anthropic Fellows Program; the
second lists Anthropic. Acknowledgments name the Anthropic Safety Fellows
Program; Appendix A.1 describes internal Anthropic ethics review. These are
disclosures, not evidence of improper influence. The tested assistant used
**GPT-4o**, not an Anthropic model. The paper does not identify an exact model
snapshot or a fieldwork calendar interval sufficient to reproduce that exposure.

The authors identify [OSF w49e7](https://osf.io/w49e7) as their preregistration.
Access returned HTTP 403 in both reviews. Statements about preregistration,
grading-rubric timing and preregistered exclusion are therefore **attributed to
the paper**, not independently authenticated against the registration.

## Question, design and scope

The experiment asks whether assistance changes completion and skill acquisition
while learning unfamiliar programming concepts. Sections 4–5 describe a
between-subject randomized study on an online coding-interview platform.

| Dimension | Original observation | Boundary for interpretation |
| --- | --- | --- |
| Main analysis | 58 invited, 53 completed all three stages, one excluded; 52 analyzed, 26 per arm (§5.2.1; Table 1) | Exclusion followed incomplete quiz submission, attributed to preregistered criteria; this is not an analysis of all invited workers |
| Population | Python users with prior AI experience and no prior Trio use (§4.3) | New to the library does not mean new to programming; corrected Table 1 has 48 of 52 with at least four years' coding experience |
| Treatment | Access to, and encouragement to use, GPT-4o chat with current-code context (§4.1; Appendix D) | An offer/encouragement to use assistance, not random assignment to a specific prompting style or uniform full delegation |
| Comparator | Instructions, examples and permitted web search, without AI (§4.3; Appendix D) | No comparison with a human mentor, pair programming or a learning-oriented AI intervention |
| Tasks | Two Trio exercises under a 35-minute cap; unassisted warm-up first (§§4.1, 4.3) | One short session with unfamiliar-library tasks, not an operating software team's lifecycle |
| Learning endpoint | Immediate unassisted quiz: 14 questions, 27 points, seven concepts; conceptual, reading and debugging items (§4.2) | Direct evidence of immediate test performance; no delayed retention, independent code-writing test or production maintenance endpoint |
| Incentives | Both groups told to work quickly; flat participation payment (§4.3) | Results need not match a workflow explicitly optimized for long-term learning |

The study-specific control is observed; the actual previous workflow in any
adopting team remains **unmeasured**. Neither the control condition nor a
repository baseline inventory establishes that old workflows reliably produced
all the competence, ownership or coordination they were expected to provide.

## Findings, units and uncertainty

| Outcome | Published result and locator | Permitted reading |
| --- | --- | --- |
| Overall immediate quiz | Lower AI-group score, Cohen's d = 0.738, p = .010 (§5.2.2; Figure 6) | Randomized evidence for this immediate independent assessment in the analyzed sample |
| Warm-up adjustment | d = 0.725, p = .016 (§5.2.2) | Reported robustness to that adjustment, not an independent study |
| Task time | No statistically significant mean difference; p = .391 (Figure 6) | Uncertain time effect; no equivalence or demonstrated absence of benefit |
| Second-task completion | All 26 AI participants completed; four of 26 controls did not, within the cap (§5.2.2) | Favorable descriptive completion result: 26/26 versus 22/26; no reported inferential test for this contrast |
| Encountered runtime errors | Median 1 (IQR 0–3) with AI versus 3 (2–5) without (Table 4, §6.2) | Fewer errors encountered during exercises, not measured escaped defects or deployed-code quality |

The paper's plotted intervals are not numerically tabulated with these results;
this review does not invent their endpoints or reconstruct regressions. No
minimum practically important learning difference was specified by this
repository before observing the result. Statistical significance is not a
decision about an organization's acceptable competence floor.

### Numerical discrepancy: do not adopt “17% less skill”

Section 5.2.2 reports a **4.15-point** difference on a **27-point** quiz, then
describes it as **17%** and approximately two grades. Arithmetic gives
`100 × 4.15 / 27 = 15.37037` **percentage points of the full scale**.
It does not give 17 percentage points or a relative percentage reduction from
the control mean. The inputs themselves cannot be reconciled from the published
text and inspected public files. The [numeric/access record](../../governance/reviews/issue-4-2026-10-22-numeric-checks.json)
preserves this discrepancy without silently choosing which input is wrong.

Use the reported direction, standardized effect and p-value for the accepted
headline. Do not substitute the arithmetic result as a newly verified observed
effect, or present any quiz percentage as a percentage loss of general skill.
The reporting discrepancy limits precision; it does not by itself demonstrate
that the entire experiment is invalid.

### Exploratory findings and pilots

The domain breakdown is explicitly exploratory and not preregistered (§5.2.2).
The overall test does not establish a separately significant effect for every
quiz domain. Six retrospectively identified interaction patterns (§6) associate
different AI-use behaviors with different scores. Small, self-selected clusters
cannot establish that explanations, conceptual questions or any other proposed
learning practice cause recovery of learning. High-scoring assisted participants
remain visible: assistance does not mechanically imply poor learning for every
user. The observational copying comparison (§6.1) gives no demonstrated benefit
from manually typing rather than pasting generated code.

Four pilots changed platforms, tasks, compliance controls and quiz design
(Table 2). Pilot D reported faster completion with AI (d = 1.11, p = .03) and
lower quiz scores (d = 1.7, p = .003; Figure 5), before the main study added
syntax hints. These are development-stage observations from the same research
program, not independent replications to pool into a stronger verdict. Earlier
pilots' noncompliance also explains design changes; it is not automatically a
measured violation rate in the final study.

## Supplementary access and unresolved reporting issues

The [author repository](https://github.com/safety-research/how-ai-impacts-skill-formation/tree/bae6eab7b80ab652d612ff9a9ee2d72dddd754aa)
was inspected at commit `bae6eab7b80ab652d612ff9a9ee2d72dddd754aa`.
All 52 transcript JSON files were read; their labels are 25 AI and 27 No AI.
The files contain participant ID, condition, task times, observations and
summary, but no participant quiz-score or analysis-exclusion fields. The
`final_task/post-survey.ipynb` notebook contains question/task material, not the
missing participant-level quiz outcomes. No raw outcome replication is claimed.
These inspected supplementary materials are described as part of this source;
they are not republished as a new repository dataset or counted independently.

| Issue | Source locations | Review disposition |
| --- | --- | --- |
| Main sample versus recordings | §6 says 51 recordings, with one AI recording missing; Appendix B.1 says 51/52 and then 25 AI + 25 controls | Preserve the inconsistent counts. They cannot all identify the same recorded sample as written |
| Public-file labels | Pinned repository contains 25 AI + 27 No AI, rather than the main 26 + 26 | Without exclusions/linkage, do not infer which records enter the main estimates or reconstruct an analysis set |
| Pattern counts | Six group sizes in §6 sum to 24, below the reported 25 AI recordings | Do not impute the unclassified/missing case or overstate the qualitative denominators |
| Copying counts | §6.1 lists groups totaling 26, despite 25 reported AI recordings | Treat the typing/pasting comparison as exploratory with an unresolved denominator |
| Quiz caption | Figure 20 mentions code writing; §4.2 explicitly excludes it and Appendix C names debugging | Follow the detailed evaluation definition; flag the caption discrepancy rather than claim an independent writing assessment |
| Secondary summary | Anthropic's [29 January summary](https://www.anthropic.com/research/AI-assistance-coding-skills) uses a novice/junior framing and repeats the percentage headline | Use corrected v2 population and the qualified numeric record. This is the same research family, not corroborating independent evidence |

These issues are limits on interpretation and reproducibility, not silently
resolved errors. A corrected paper or inspectable outcomes/registration would
trigger reassessment under the existing changed-source procedure.

## Source-author interpretation

The authors attribute better learning without assistance to cognitive engagement
and independently resolving errors, and discuss preserving supervisory skills
(§§6–7). They suggest more agentic tools could produce greater learning losses.
Those are mechanisms and extrapolations offered by the authors. The experiment
does not randomize error exposure, engagement, prompting pattern or an agentic
tool, and it does not identify a causal mediator. Its support for an overall
immediate quiz difference is stronger than its support for those explanations.

## Repository interpretation and complete outcomes

**Accepted treatment, 2026-10-22:** completing a task and acquiring the capability to
understand it independently are separate outputs of Code. A favorable completion
observation can coexist with weaker immediate learning. This directly motivates
including human capability in an improvement assessment; it does not establish
that this tradeoff occurs in every team or persists over time.

The [impact proposal](../../governance/reviews/issue-4-2026-10-22-source-impact.md#complete-node-outcomes)
maps **all four Code and all four Review functions**, including each baseline,
direct/proxy/missing coverage and downstream uncertainty. It also separates
HUM-1's durable learning, shared system model, knowledge distribution and capability
when the tool or author is absent. The study provides immediate individual
learning evidence adjacent to the Review learning function; it contains no actual
team code-review intervention. Individual quiz scores cannot stand in for
competent shared ownership.

The accepted HUM-1 successor is **Provisional support for the immediate
individual-learning component**, with the specified displacement mechanism,
durable learning, collective ownership and remedy still **Open**. Existing
COD-1/COD-2 and REV-1/REV-2 verdicts are unchanged; added coverage does not
establish their separate mechanisms or remedies. One study may support its scoped result without establishing all
downstream links. Macro output and micro learning observations cannot be joined
into one measured causal chain by counting citations.

### What would weaken the mechanism or remedy?

For the broader adverse hypothesis, test whether actual AI-assisted practice,
including existing compensating learning, preserves meaningful independent
explanation, diagnosis and modification on delayed/unfamiliar tasks, across
contributors, within agreed competence floors. A well-powered result meeting
those floors without additional burden would weaken the alleged capability
loss in that setting. A nonsignificant underpowered result would not prove
preservation. The mechanism further needs independent evidence about displaced
practice and knowledge transfer, rather than inferring displacement from the
same lower score it is used to explain.

For a remedy, compare a specified learning/review intervention against actual
practice, account for all learning, mentoring and context cost, and set meaningful
effect/floor criteria before observing results. No competence gain, unacceptable
delay or a greater total burden without compensating benefit would weaken that
remedy. Manual work may be replaced by an adequate alternative; retaining typing
or adding a ceremony is not the objective. Teams and accountable owners must
accept the relevant tradeoff; the paper supplies no universal threshold.

The proposed business mechanism runs through capability to reliable change and
recovery, then useful user outcomes and lifecycle economics. None of those later
effects is measured here. No claim of debt growth, cognitive overload, burnout,
TCO increase, competitive advantage or ROI follows from this quiz result alone.

## Limitations and what is not established

- Small, selected participant sample; unfamiliar-library tasks and one assistant
  interface. Coding experience does not make this a representative industry
  sample, while library novelty does not make it a novice-programmer sample.
- Immediate assessment is not long-term retention or deterioration of previously
  acquired skill. A learning-acquisition result should not be renamed deskilling.
- Task completion, encountered errors, quiz performance and self-report are
  different outcomes. No composite net-productivity or overall-harm score is
  computed from them.
- Post-assignment exclusion, inaccessible preregistration, missing quiz outcomes
  and inconsistent supplementary counts constrain independent reconstruction.
  Random assignment does not remove these reporting limits.
- No measured team review, mentorship comparator, shared ownership, later
  maintenance/recovery, production quality, workload exhaustion, user benefit
  or economics; no causal test of a proposed learning safeguard.
- Tool capability, UI, task pressure and engagement may change results. This
  experiment cannot establish what every current or future coding agent does.

## Known repository uses

The source is used in this brief, the primary index, the bibliographic entry in
`REFERENCES.md`, canonical registration and dated review/calculation records.
Accepted substantive uses implemented for #4:

- `report/02_broken_mechanics.md`: Chapter 5 learning/understanding subsection,
  bounded conclusion addition and reference.
- `report/appendices/mechanism-hypotheses.md`: evidence card and dated Code,
  Review and HUM-1 coverage/assessment; preserved earlier history and remaining
  missing links.
- `README.md`: a compact skill/understanding evidence row with source, brief and
  register routes, preserving the already accepted entry-point structure.

**No protocol change.** Existing professional-development and
independent-understanding practices remain proposals with local cost/benefit
requirements. This paper tests neither the protocol stack nor a universal gate.
No AGENTS/workflow, causal diagram or global confidence change is implemented
by this source treatment. The maintainer's later competing-hypothesis direction
is separately owned planning work under #84.

## Repository integration audit

**Verified; Last verified 2026-10-22.** The [occurrence-level audit](../../governance/reviews/issue-4-2026-10-22-integration.md)
records every material source use, exact original locators, numeric/inference
boundaries, placement and neighboring argument; full Code/Review/HUM-1 coverage;
README/maps and all four protocols; and synchronized registry/index/bibliography.
The approved treatment preserves favorable completion, inconclusive mean time,
the percentage-reporting discrepancy and unmeasured durable/shared capability.
Independent implementation and faithful-recording reviews are Confirmed for the
exact candidates recorded in the audit. Published-head checks passed, PR #108
merged, and independent actual-main acceptance Confirmed the identical tree
`6cc46c399294ae6777ffdae9f7167ab30c4b191a` at `66f3d8ac65432275c8745654a47b693cb8d9ed0e`.
The [final receipt](../../governance/reviews/issue-4-2026-10-22-final-verification.md)
records the completed prerequisites and separately tracks acceptance of this
verification metadata. No material implementation correction remains.

## Independent review

**Confirmed**, 2026-10-22, for the source assessment, numeric/access record and
concrete treatment proposal. Primary source reviewer: `/root`; proposal drafter:
`/root/issue4_existing_fit`; separate reviewer: `/root/issue4_independent_review`,
who did not author or edit them. The [review receipt](../../governance/reviews/issue-4-2026-10-22-review.md)
records exact inspected hashes, originals, corrections I4-01/I4-02 and scope.
No material discrepancy remains in this preparation. Source reporting/access
limitations remain unresolved and correctly represented. This outcome does not
confirm later integration, merge or actual main.

**Implementation review: Confirmed**, 2026-10-22, by the same independent reviewer
for local `ecd53d3670aaa115c2722c7db9bd035929dbfea6`, tree
`9456a9a6d48fae44bf1fd0a88954b4d4bc43fa74`. The
[integration receipt](../../governance/reviews/issue-4-2026-10-22-integration.md#completed-candidate-review--2026-10-22)
records actual P1–P5 uses, complete outcomes, I4-03 locator correction, source
states, synchronization and approval checks. No material implementation correction
remains; source limitations are preserved. This confirms the pre-merge candidate,
not its future published head, merge or accepted main.

**Actual-main acceptance: Confirmed**, 2026-10-22, by
`/root/issue4_independent_review`, after independently fetching the merge/ref/tree,
PR #108 state, exact hosted runs and job steps, and source brief/registry bytes.
Accepted main `66f3d8ac65432275c8745654a47b693cb8d9ed0e` has the same reviewed tree;
[main health 39774666155](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/actions/runs/39774666155)
passed tests, contract, evidence integrity and RI freshness. This completed review
permits final source-verification metadata; the final PR and issue acceptance
remain separately traceable in the [final receipt](../../governance/reviews/issue-4-2026-10-22-final-verification.md)
and live #4. Scientific findings and unmeasured outcomes are unchanged.
