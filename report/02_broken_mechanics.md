# Part 2: Verification and Delivery Mechanisms

> **Navigation:** [🏠 Home](../README.md) | [🧭 Doctrine](../DOCTRINE.md) | [📖 Glossary](../GLOSSARY.md) | [📉 Part 1: Evidence and Delivery Outcomes](01_the_illusion.md) | **Part 2** | [🔥 Part 3: Scenarios and Adoption Decisions](03_the_aftermath.md) | [SDLC hypothesis register](appendices/mechanism-hypotheses.md) | [🛡️ Protocols](../protocols/README.md) | [📚 References](../REFERENCES.md)

**Table of Contents:**
*   [Chapter 5. Review Capacity and Verification Risk](#chapter-5-review-capacity-and-verification-risk)
*   [Chapter 6. A Thought Experiment: Operating an AI Review System](#chapter-6-a-thought-experiment-operating-an-ai-review-system)
*   [Chapter 7. Testing the Delivery Mechanism](#chapter-7-testing-the-delivery-mechanism)

---

## Chapter 5. Review Capacity and Verification Risk

Continue Chapter 4's conditional scenario: candidate work grows faster than a constrained review stage can process it. Reviewer load depends on change size/risk, familiarity, tooling and available capacity. The evidence reviewed here does not establish a universal senior-to-junior staffing ratio or that AI permanently breaks one.

[Chen–Stratton](../evidence/primary/2026-chen-stratton-firm-production.md) adds direct firm-level review-process evidence: agent adoption is associated with longer submission-to-merge elapsed time and more formal change requests and comments. This makes Review a concrete candidate constraint. It does not establish that active reviewer demand exceeded competent capacity, or that shared ownership deteriorated. [Chapter 1](01_the_illusion.md#firm-evidence-the-work-around-code-changes-too) gives the estimates and design limits; the [REV-1/REV-2 assessment](appendices/mechanism-hypotheses.md#review--rev-1-and-rev-2) separates the supported process component from those causal and capability questions.

### Activity Growth Does Not Set Staffing Ratios

[GitClear's developer-output report](../evidence/primary/2025-gitclear-developer-output.md) reports +131.1% mean and +76.3% median added-line output in selected developer-month records versus 2022. These are different statistics from a changing sample, without observed individual AI exposure. They do not establish that every team doubles its PR intake, or that one reviewer now handles the output of ten developers.

**Repository hypothesis:** Increased admitted work could grow review queues where capacity is constrained. Smaller changes, better verification or additional capacity could instead preserve flow. Direct local intake, review effort and delivered outcomes are required to distinguish these possibilities.

### Failure Mode to Test: Plausible but Incorrect Code

A plausible implementation could contain a logic, concurrency or security error that is expensive to detect. That possibility concerns generated and human-authored changes; the GitClear operation counts do not measure its prevalence or compare junior/senior error visibility.

The following **illustrative effort asymmetry** is an invented example, not a GitClear measurement, staffing prescription or general review-time ratio:

- **Candidate generation:** 10 seconds.
- **Verification:** 30 minutes.

A valid comparison also needs manual implementation/review effort and quality; those two times alone establish neither net loss nor net gain.

### Measurement Box: What METR Task Horizon Means

[METR's pinned March 2025 paper v1](../evidence/primary/2025-metr-task-horizon.md), §§3–4, defines a **50% task-completion horizon**: a fitted task length, in relevant human-baseline time, at which that agent/scaffold is predicted to succeed at the chosen benchmark threshold. It is not a claim that every software change succeeds half the time, that an agent runs for that duration, or that a human must spend the same duration reviewing its output.

The paper reports historical capability progress with a doubling estimate of about **seven months**; that is neither measured code-volume inflation nor exponential liability. Results depend on task distribution, scaffolding, baselining and success level. The March-dated blog now embeds later benchmark data, so later model points cannot be attributed to the original publication date. This report withdraws the unpinned GPT-5.2/6–7-hour threshold instead of treating it as current evidence.

**Bounded counterevidence:** In the paper's small internal-PR experiment, scoring each issue took less time than completing it. This is manual benchmark assessment, not comprehensive production verification, but it contradicts equating task duration with required review time.

**Hypothesis to test:** More autonomous task scope could increase verification demand, reduce it through better output/tools, or change the task mix. Measure verification/rework effort separately from total human effort, quality and delivered outcomes against a comparator. Implementation savings can yield net benefit even while verification demand rises. Benchmark horizon alone decides none of those outcomes; [H3 in the claim graph](appendices/mechanism-hypotheses.md) states the missing test.

### Possible Responses at a Constrained Review Stage

The [Techno Diaries public introduction](../evidence/secondary/2025-technodiaries-review-anecdote.md) contains one first-person report of doubled review time compared with the same period a year earlier. The logs, change mix and member-only remainder are unavailable. It also describes useful assistance on small tasks. This is an anecdote, not a measured senior-developer population effect or evidence of universally unsustainable cognitive load.

Two adverse scenarios are possible if review remains constrained:

1. **Keep the verification boundary:** A queue could delay feedback or displace other work if intake remains above capacity. The account does not measure that queue's effect on idle time, overtime or burnout.
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

**Repository inference:** learning is part of what the coding workflow supplies,
so a completion metric can miss a consequential outcome. This study measures
immediate individual performance; it does not establish durable skill loss,
expert system understanding or collective ownership. Its six observed prompting
patterns do not prove a remedy. [HUM-1](appendices/mechanism-hypotheses.md#hum-1--practice-understanding-and-collective-ownership)
keeps those questions separate, and the [Review inventory](appendices/mechanism-hypotheses.md#review--rev-1-and-rev-2)
retains both quality and competent ownership as outcomes to evaluate.

### Conclusion: Measure Review and Mentorship

The GitClear studies do not show that most senior engineers rubber-stamp changes, that code review ceases to function, or that mentorship necessarily collapses. Those would be additional outcomes to investigate, not consequences measured by commit/line proxies.

A team could gain useful output while preserving review and learning, or create a queue that displaces them. Track review effort, quality and knowledge transfer alongside delivery to test which outcome occurs. The task-horizon definition above does not calibrate review demand, and the practitioner account does not supply that missing comparison.

The skill-formation experiment adds a measured immediate individual-learning
outcome to that investigation. It makes learning an explicit part of the
comparison without establishing that team mentorship or ownership deteriorated.
Test whether the proposed workflow supplies the understanding needed for later
change and recovery, alongside completion, quality and total effort.

---

#### References

* **Shen and Tamkin (arXiv v2, 1 February 2026):** [How AI Impacts Skill Formation](https://arxiv.org/abs/2601.20245v2) and [source brief](../evidence/primary/2026-ai-impacts-skill-formation.md) — randomized unfamiliar-library tasks and immediate individual assessment; no delayed retention or collective-ownership result.
* **Chen and Stratton (August 2026):** [Firm evidence in Chapter 1](01_the_illusion.md#firm-evidence-the-work-around-code-changes-too) and [source brief](../evidence/primary/2026-chen-stratton-firm-production.md) — observed review-process measures, with identification and outcome limits; not measured review capacity or lost ownership.
*   **GitClear developer output:** [Evidence brief](../evidence/primary/2025-gitclear-developer-output.md) — selected output comparisons and aggregation/window limits; not a staffing or review-time estimate.
* **METR (March 2025):** [Pinned v1 definition and review boundary](../evidence/primary/2025-metr-task-horizon.md) — historical benchmark methods, limitations and bounded scoring evidence; no current-model threshold adopted.

---

## Chapter 6. A Thought Experiment: Operating an AI Review System

An AI review assistant could reduce some inspection work while adding setup and maintenance. This is a **thought experiment and proposed comparison**, not an observed deployment, collected pilot result or proof that automation necessarily shifts more work onto senior engineers. [Issue #54](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/54) owns pilot design and any later decision to collect data; [Chapter 5](#chapter-5-review-capacity-and-verification-risk) states the capacity question.

### Potential Benefit and Comparator

A bounded pilot could test whether an assistant finds defined error classes or relevant project conventions before human review. Compare the same change-risk classes with and without assistance, including false positives, missed defects, human effort, queue time and operating cost. These are evaluation objectives, not guaranteed capabilities.

### Context Is a Design Variable

[GitClear's quality report](../evidence/primary/2025-gitclear-code-quality.md), Appendix A6 pp29–31, gives a rough historical estimate about Copilot context in 2024. Its approximate ten-file statement rests on assumed file sizes/token budgets and informal sources, not a measured general limit for popular models or current tools. It does not establish that a review agent must read the entire system or always require a RAG pipeline.

The context needed depends on the change and its risk boundary. Targeted references, retrieval or a narrower automated check are possible designs to evaluate; missing relevant context is a risk to test rather than a universal fatal flaw.

### Reuse and Maintenance Hypotheses

The report's Appendix A1 counts imply a moved-line share of **24.65% in 2021 / 9.47% in 2024**. These relocation operations are a proxy, not a direct measure of modularity, indexability or AI-review accuracy. Body/appendix/landing differences and sample limits are recorded in the [brief](../evidence/primary/2025-gitclear-code-quality.md). The result does not prove that every codebase becomes harder to index or that a reviewer gets worse over time.

**Repository hypothesis:** Context/prompt/retrieval maintenance could consume some review savings. Possible alternatives include stable reference selection, a sufficiently narrow scope or improved verification. Measure total human effort and review quality over time; sustained savings with stable quality would weaken a claim of net extra burden.

### Conclusion: Evaluate the Whole Review Intervention

The relevant question is whether useful review savings exceed setup, supervision and maintenance costs at the required quality level. Either benefit or net burden is possible. Historical change-operation shares do not decide the answer, and neither GitClear report measures this intervention's net result.

---

## Chapter 7. Testing the Delivery Mechanism

The central empirical NBER synthesis belongs in [Chapter1](01_the_illusion.md#writing-code-vs-shipping-code). It preserves the September revision's positive releases, cumulative/incremental distinction, selected samples, estimation uncertainty and sensitivity, model assumptions and separate marketplace design. Attenuation does not establish overall decline, a universal review constraint or the full mechanism below. The [brief](../evidence/primary/2026-writing-code-vs-shipping-code.md) retains the supplied May version as history.

The [Chen–Stratton firm evidence](01_the_illusion.md#firm-evidence-the-work-around-code-changes-too) adds review-process observations to this investigation. Together, these sources motivate tests of complementary constraints; different populations, exposures and outcome definitions prevent a common conversion calculation or proof of the whole mechanism. The [source comparison](../evidence/primary/2026-chen-stratton-firm-production.md) and [hypothesis register](appendices/mechanism-hypotheses.md#e-chen-stratton) preserve those boundaries.

### Necessary Conditions and Alternatives

[Chapter 4](01_the_illusion.md#chapter-4-a-review-capacity-scenario-when-candidate-work-outruns-verification) defines the proposed capacity mechanism. It needs **admitted service demand**, effective capacity at required quality, utilization/variation and WIP/release policies. Higher generated volume alone is insufficient. No study reviewed here establishes one causal chain from AI generation through requirements, code review, QA and customer value.

The [SDLC hypothesis register](appendices/mechanism-hypotheses.md) is the single detailed home for the full function/outcome inventory, H0, node and cross-cutting hypotheses. Its [retained H1–H5 tests](appendices/mechanism-hypotheses.md#hypotheses-and-distinguishing-observations) cover demand and waits, context and rework, autonomous scope and verification, net review-automation burden, and requirements/test-oracle risks. Each has an endpoint, trigger, alternatives and observations capable of weakening the local relationship.

Distinguish **nonactivation/adaptation**, **disconfirmation when the trigger is present**, and **net delivery benefit**. A smaller queue after admission limits does not refute an overload mechanism; it shows a successful response. Lower total effort does not establish lower review effort. Conversely, independently measured exposure with no predicted endpoint change, estimated precisely enough to exclude a meaningful effect, weakens that proposed local link. These are repository hypotheses, not source-reported population effects.

### Adaptation and Budget Boundaries

Pull/WIP limits, smaller changes, risk-based task selection, useful tests/review assistance, training and adequate downstream capacity are plausible responses to evaluate. They are not an instruction to slow every adopter or require a new transformation programme. Existing capability may suffice. Chapter 2's [cost comparison](01_the_illusion.md#chapter-2-evaluating-the-cost-of-ai-assisted-delivery) asks whether benefits exceed additional work/cost at the required quality; market spending, budget intentions and company-wide filings do not establish an unfunded delivery gap.

### Evaluation Rather Than a Predetermined Crisis

The proposed design in [#54](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/54) should distinguish beneficial, neutral/mixed and adverse outcomes using a defined comparator, task/risk mix, review/rework effort, queue time, useful releases and quality. No pilot has been run for this chapter. Agree scope, outcome definitions and observation window before collection; resource and data-collection decisions remain with that issue's owner/maintainer.

If coding time falls and useful delivery improves at comparable or lower total effort with stable/improved quality, that supports benefit in that setting. It does not by itself refute a simultaneous increase in review demand; check the relevant endpoint and whether the proposed trigger occurred. If queues or defects rise, compare alternative explanations before attributing them to AI or a particular stage. No probability or industry prevalence is assigned to these scenarios. [Part 3](03_the_aftermath.md) develops conditional scenarios and decision responsibilities; these are repository interpretations, not further empirical results.

---

#### References

- **NBER September 2026 revision:** [Chapter 1 synthesis](01_the_illusion.md#writing-code-vs-shipping-code) and [evidence brief](../evidence/primary/2026-writing-code-vs-shipping-code.md); original, uncertainty and historical versions pinned in the brief.
- **Chen–Stratton August 2026:** [Firm-level findings and NBER comparison](../evidence/primary/2026-chen-stratton-firm-production.md); review-process observations do not identify the complete capacity mechanism or test a rebalancing remedy.
- **Goldratt and Cox:** [Methodology/access-gap record](../evidence/methodology/1984-the-goal.md); interpretive lens, not an empirically identified AI bottleneck or an edition-verified theorem.
- **Repository synthesis:** [Claim graph, alternatives and proposed tests](appendices/mechanism-hypotheses.md), coordinated with #54; no empirical results inferred from a diagram or protocol.

---

**Next:** [🔥 Part 3: Scenarios and Adoption Decisions](03_the_aftermath.md)
