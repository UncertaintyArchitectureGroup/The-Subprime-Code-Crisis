# Part 2: Verification and Delivery Mechanisms

> **Navigation:** [🏠 Home](../README.md) | [🧭 Doctrine](../DOCTRINE.md) | [📖 Glossary](../GLOSSARY.md) | [📉 Part 1: Evidence and Delivery Outcomes](01_the_illusion.md) | **Part 2** | [🔥 Part 3: Scenarios and Adoption Decisions](03_the_aftermath.md) | [SDLC hypothesis register](appendices/mechanism-hypotheses.md) | [🛡️ Protocols](../protocols/README.md) | [📚 References](../REFERENCES.md)

**Table of Contents:**
*   [Chapter 5. Review Capacity and Verification Risk](#chapter-5-review-capacity-and-verification-risk)
*   [Chapter 6. A Thought Experiment: Operating an AI Review System](#chapter-6-a-thought-experiment-operating-an-ai-review-system)
*   [Chapter 7. Testing the Delivery Mechanism](#chapter-7-testing-the-delivery-mechanism)

---

## Chapter 5. Review Capacity and Verification Risk

Continue Chapter 4's conditional scenario: more proposed work reaches review than the stage can handle. The workload depends on the size and risk of changes, reviewers' familiarity with them, available tools and capacity. The evidence reviewed here establishes neither a universal senior-to-junior staffing ratio nor a permanent disruption of one by AI.

[Chen–Stratton](../evidence/primary/2026-chen-stratton-firm-production.md) adds direct firm-level review-process evidence: agent adoption is associated with longer submission-to-merge elapsed time and more formal change requests and comments. This makes Review a concrete candidate constraint. It does not establish that active reviewer demand exceeded competent capacity, or that shared ownership deteriorated. [Chapter 1](01_the_illusion.md#firm-evidence-the-work-around-code-changes-too) gives the estimates and design limits; the [REV-1/REV-2 assessment](appendices/mechanism-hypotheses.md#review--rev-1-and-rev-2) separates the supported process component from those causal and capability questions.

### Activity Growth Does Not Set Staffing Ratios

[GitClear's developer-output report](../evidence/primary/2025-gitclear-developer-output.md) reports +131.1% mean and +76.3% median added-line output in selected developer-month records versus 2022. These are different statistics from a changing sample, without observed individual AI exposure. They do not establish that every team doubles its PR intake, or that one reviewer now handles the output of ten developers.

**Repository hypothesis:** Accepting more work for review could lengthen the queue if review capacity is constrained. Smaller changes, better checking or added capacity could keep work moving. To distinguish these possibilities, measure what enters the local review process, the effort it takes to review, and what is delivered.

### Failure Mode to Test: Plausible but Incorrect Code

Code that looks plausible could contain an error in its logic, handling of concurrent operations or security that is expensive to detect. That possibility applies to both generated and human-written changes. GitClear's operation counts do not measure how often it occurs or whether errors made by junior or senior developers are easier to spot.

The following **illustrative effort asymmetry** is an invented example, not a GitClear measurement, staffing prescription or general review-time ratio:

- **Candidate generation:** 10 seconds.
- **Verification:** 30 minutes.

A valid comparison also needs the effort and quality of manual implementation and review. Those two times alone cannot show whether the benefits exceed the costs.

### Measurement Box: What METR Task Horizon Means

[METR's pinned March 2025 paper v1](../evidence/primary/2025-metr-task-horizon.md), §§3–4, defines a **50% task-completion horizon**: a fitted task length, in relevant human-baseline time, at which that agent/scaffold is predicted to succeed at the chosen benchmark threshold. It is not a claim that every software change succeeds half the time, that an agent runs for that duration, or that a human must spend the same duration reviewing its output.

The paper reports historical capability progress with a doubling estimate of about **seven months**; that is neither measured code-volume inflation nor exponential liability. Results depend on task distribution, scaffolding, baselining and success level. The March-dated blog now embeds later benchmark data, so later model points cannot be attributed to the original publication date. This report withdraws the unpinned GPT-5.2/6–7-hour threshold instead of treating it as current evidence.

**Bounded counterevidence:** In the paper's small internal-PR experiment, scoring each issue took less time than completing it. This is manual benchmark assessment, not comprehensive production verification, but it contradicts equating task duration with required review time.

**Hypothesis to test:** Expanding what an agent does autonomously could require more checking, require less because its output or tools improve, or change which tasks are attempted. Against a suitable comparison workflow, measure checking and rework separately from total human effort, quality and delivered outcomes. Implementation savings can outweigh added checking even when the need for checking rises. The benchmark horizon alone cannot tell us which result occurs; [H3 in the claim graph](appendices/mechanism-hypotheses.md) states the missing test.

### Possible Responses at a Constrained Review Stage

The [Techno Diaries public introduction](../evidence/secondary/2025-technodiaries-review-anecdote.md) contains one first-person report of doubled review time compared with the same period a year earlier. The logs, change mix and member-only remainder are unavailable. It also describes useful assistance on small tasks. This is an anecdote, not a measured senior-developer population effect or evidence of universally unsustainable cognitive load.

Two adverse scenarios are possible if review remains constrained:

1. **Keep the required checks:** A queue could delay feedback or displace other work if intake remains above capacity. The account does not measure that queue's effect on idle time, overtime or burnout.
2. **Shorten checks without adequate verification:** Defects might escape into production. No observed frequency or six-month failure horizon is established here.

Other responses include limiting intake, reducing change size, changing scope or improving verification. Useful delivery gains with stable review effort and quality would weaken the adverse scenario.

### Skill Formation Is a Separate Outcome

Completing a task and learning enough to work independently afterward are
different outcomes. In [Shen and Tamkin's randomized study](../evidence/primary/2026-ai-impacts-skill-formation.md),
52 analyzed developers learned the unfamiliar Python library Trio, with GPT-4o
chat assistance or a comparison workflow using instructions, examples and web
resources. Most had substantial coding experience: 48 reported at least four
years. All were new to this library.

The AI arm scored lower on an immediate unassisted 14-question assessment
(reported Cohen's d = .738, p = .010; adjusted analysis retained the result).
The mean completion-time comparison was inconclusive (p = .391), while all 26
AI-arm participants and 22 of 26 controls finished the second task within the
study's 35-minute programming limit. This preserves a useful completion result alongside the
learning difference. The brief documents exclusions, the paper's inconsistent
percentage summary and the limits of its exploratory interaction patterns.

**Repository inference:** people can learn while they code, so counting completed tasks can miss an important result. This study measures immediate individual performance. It does not establish lasting skill loss, expert understanding of a system or a team's shared ability to take responsibility for it. Its six observed prompting patterns do not prove that any proposed remedy works. [HUM-1](appendices/mechanism-hypotheses.md#hum-1--practice-understanding-and-collective-ownership) keeps those questions separate. The [Review inventory](appendices/mechanism-hypotheses.md#review--rev-1-and-rev-2) includes both quality and competent ownership: whether the team understands the system well enough to take responsibility for it.

### Conclusion: Measure Review and Mentorship

The GitClear studies do not show that most senior engineers rubber-stamp changes, that code review ceases to function, or that mentorship necessarily collapses. Those would be additional outcomes to investigate, not consequences measured by commit/line proxies.

A team could deliver more useful output while preserving review and learning, or create a queue that leaves less time for them. Track review effort, quality and knowledge transfer alongside delivery to find out which occurs. The task-horizon definition above does not tell us how much review is needed, and the practitioner account does not supply the missing comparison.

The skill-formation experiment adds a measured immediate individual-learning
outcome to that investigation. It makes learning an explicit part of the
comparison without establishing that team mentorship or ownership deteriorated.
Alongside completion, quality and total effort, test whether the proposed workflow gives people the understanding needed to make later changes and recover the system when something goes wrong.

---

#### References

* **Shen and Tamkin (arXiv v2, 1 February 2026):** [How AI Impacts Skill Formation](https://arxiv.org/abs/2601.20245v2) and [source brief](../evidence/primary/2026-ai-impacts-skill-formation.md) — randomized unfamiliar-library tasks and immediate individual assessment; no delayed retention or collective-ownership result.
* **Chen and Stratton (August 2026):** [Firm evidence in Chapter 1](01_the_illusion.md#firm-evidence-the-work-around-code-changes-too) and [source brief](../evidence/primary/2026-chen-stratton-firm-production.md) — observed review-process measures, with identification and outcome limits; not measured review capacity or lost ownership.
*   **GitClear developer output:** [Evidence brief](../evidence/primary/2025-gitclear-developer-output.md) — selected output comparisons and aggregation/window limits; not a staffing or review-time estimate.
* **METR (March 2025):** [Pinned v1 definition and review boundary](../evidence/primary/2025-metr-task-horizon.md) — historical benchmark methods, limitations and bounded scoring evidence; no current-model threshold adopted.

---

## Chapter 6. A Thought Experiment: Operating an AI Review System

An AI review assistant could save some inspection work while adding setup and maintenance work. This chapter is a **thought experiment and proposed comparison**. It reports no deployment or pilot result and does not establish that automation necessarily gives senior engineers more work. [Issue #54](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/54) owns pilot design and any later decision to collect data; [Chapter 5](#chapter-5-review-capacity-and-verification-risk) explains the capacity question.

### Potential Benefit and Comparator

A pilot with a defined scope could test whether an assistant spots specified kinds of errors or identifies relevant project conventions before human review. Compare changes of the same risk class with and without assistance. Include false alarms, missed defects, human effort, time in queues and operating cost. These are things to test; the assistant is not assumed to do them successfully.

### Context Is a Design Variable

[GitClear's quality report](../evidence/primary/2025-gitclear-code-quality.md), Appendix A6 pp29–31, gives a rough historical estimate about Copilot context in 2024. Its approximate ten-file statement rests on assumed file sizes/token budgets and informal sources, not a measured general limit for popular models or current tools. It does not establish that a review agent must read the entire system or always require a RAG pipeline.

The context needed depends on the change and the risks being checked. Possible designs include supplying selected references, retrieving relevant material or narrowing what the automated check attempts. Test whether missing context causes problems; do not assume it makes every design fail.

### Reuse and Maintenance Hypotheses

The report's Appendix A1 counts imply a moved-line share of **24.65% in 2021 / 9.47% in 2024**. These relocation operations are a proxy, not a direct measure of modularity, indexability or AI-review accuracy. Body/appendix/landing differences and sample limits are recorded in the [brief](../evidence/primary/2025-gitclear-code-quality.md). The result does not prove that every codebase becomes harder to index or that a reviewer gets worse over time.

**Repository hypothesis:** Maintaining context, prompts and retrieval could use up some of the review savings. Stable reference selection, a sufficiently narrow scope or better checking could avoid that burden. Measure total human effort and review quality over time. Sustained savings at stable quality would weaken a claim that the assistant adds more work than it saves.

### Conclusion: Evaluate the Whole Review Intervention

The relevant question is whether useful review savings exceed setup, supervision and maintenance costs while meeting the required quality. The assistant could provide a benefit after those costs, or add more burden than benefit. Historical shares of code-change operations cannot decide the answer, and neither GitClear report measures the overall result of this intervention.

---

## Chapter 7. Testing the Delivery Mechanism

The central empirical NBER synthesis belongs in [Chapter1](01_the_illusion.md#writing-code-vs-shipping-code). It preserves the September revision's positive releases, cumulative/incremental distinction, selected samples, estimation uncertainty and sensitivity, model assumptions and separate marketplace design. Attenuation does not establish overall decline, a universal review constraint or the full mechanism below. The [brief](../evidence/primary/2026-writing-code-vs-shipping-code.md) retains the supplied May version as history.

The [Chen–Stratton firm evidence](01_the_illusion.md#firm-evidence-the-work-around-code-changes-too) adds review-process observations to this investigation. Together, these sources motivate tests of complementary constraints; different populations, exposures and outcome definitions prevent a common conversion calculation or proof of the whole mechanism. The [source comparison](../evidence/primary/2026-chen-stratton-firm-production.md) and [hypothesis register](appendices/mechanism-hypotheses.md#e-chen-stratton) preserve those boundaries.

### Necessary Conditions and Alternatives

[Chapter 4](01_the_illusion.md#chapter-4-a-review-capacity-scenario-when-candidate-work-outruns-verification) defines the proposed capacity mechanism. To test it, establish how much work is **actually accepted into the process**, what checking that work needs, and what the team can handle at the required quality. Also measure how busy the stage is, how demand varies, and how work-in-progress and release rules affect it. More generated code alone is insufficient. No study reviewed here establishes one causal chain from AI generation through requirements, code review, QA and customer value.

The [SDLC hypothesis register](appendices/mechanism-hypotheses.md) holds the detailed account of what each function contributes and which outcomes to assess, along with H0 and the hypotheses for individual functions and the whole process. Its [retained H1–H5 tests](appendices/mechanism-hypotheses.md#hypotheses-and-distinguishing-observations) cover work demand and waiting, context and rework, autonomous task scope and checking, review automation's costs and savings, and risks in requirements and tests' criteria for correct behavior. Each test states the condition that would start the proposed mechanism, the result to look for, alternative explanations and observations that could weaken it.

Keep three questions separate: **Did the condition for harm arise? Did the predicted harm follow? Did the deployment still provide a benefit after costs?** A smaller queue after limits on intake shows a successful response; it does not refute the proposed effect of overload. Lower total effort also does not establish lower review effort.

A proposed link is weakened when the triggering condition is measured independently but the predicted change is absent, with enough precision to rule out an effect large enough to matter. These are ways to test the repository's hypotheses. They are not effects measured across a population by the cited sources.

### Adaptation and Budget Boundaries

Possible responses include limits on how much work starts or stays in progress, smaller changes, task selection based on risk, useful test or review assistance, training and enough capacity in later stages. Evaluate these options against the local problem. They do not require every adopter to slow down or start a transformation programme; existing capability may suffice. Chapter 2's [cost comparison](01_the_illusion.md#chapter-2-evaluating-the-cost-of-ai-assisted-delivery) asks whether benefits exceed added work and cost at the required quality. Market spending, budget intentions and company-wide filings do not show that a particular delivery need has gone unfunded.

### Evaluation Rather Than a Predetermined Crisis

The proposed design in [#54](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/54) should be able to find beneficial, neutral/mixed or adverse outcomes. It needs a defined comparison workflow, task and risk mix, review and rework effort, queue time, useful releases and quality. No pilot has been run for this chapter. Agree the scope, what each outcome means and how long to observe it before collecting data. Resource and data-collection decisions remain with that issue's owner/maintainer.

If coding takes less time and useful delivery improves at comparable or lower total effort, with stable or improved quality, that supports a benefit in that setting. Review demand could still have increased at the same time. Check that result separately and establish whether the condition that was supposed to cause it occurred. If queues or defects rise, compare alternative explanations before attributing them to AI or a particular stage. These scenarios have no assigned probability or estimated industry prevalence. [Part 3](03_the_aftermath.md) develops conditional scenarios and decision responsibilities as repository interpretations; it adds no empirical results.

---

#### References

- **NBER September 2026 revision:** [Chapter 1 synthesis](01_the_illusion.md#writing-code-vs-shipping-code) and [evidence brief](../evidence/primary/2026-writing-code-vs-shipping-code.md); original, uncertainty and historical versions pinned in the brief.
- **Chen–Stratton August 2026:** [Firm-level findings and NBER comparison](../evidence/primary/2026-chen-stratton-firm-production.md); review-process observations do not identify the complete capacity mechanism or test a rebalancing remedy.
- **Goldratt and Cox:** [Methodology/access-gap record](../evidence/methodology/1984-the-goal.md); interpretive lens, not an empirically identified AI bottleneck or an edition-verified theorem.
- **Repository synthesis:** [Claim graph, alternatives and proposed tests](appendices/mechanism-hypotheses.md), coordinated with #54; no empirical results inferred from a diagram or protocol.

---

**Next:** [🔥 Part 3: Scenarios and Adoption Decisions](03_the_aftermath.md)
