# Writing Code vs. Shipping Code

## Citation

Demirer, Mert, Leon Musolff, and Liyuan Yang. **“Writing Code vs. Shipping Code: Productivity Effects Across Generations of AI Coding Tools.”** NBER Working Paper No. 35275, May 2026.

- Official paper page: https://www.nber.org/papers/w35275
- Official PDF: https://www.nber.org/system/files/working_papers/w35275/w35275.pdf

The repository links to the publisher-hosted PDF rather than redistributing the copyrighted full paper.

## Publication status

**Working paper; not peer reviewed.** The paper is circulated by the National Bureau of Economic Research for discussion and comment. It has not undergone the peer-review process or the NBER Board of Directors review associated with official NBER publications.

## Research question and scope

The paper asks two related questions:

1. How do measured productivity effects change across successive generations of AI coding tools?
2. How much of the increase in upstream coding activity propagates into higher-level outputs such as pull requests, projects, releases, new applications, and application usage?

The study focuses on software development from 2022 through 2026 and distinguishes among:

- AI autocomplete;
- synchronous or interactive coding agents;
- asynchronous or autonomous coding agents.

## Dataset and methodology

The authors combine several data sources:

- public GitHub activity for more than 100,000 developers;
- internal Microsoft telemetry on GitHub Copilot adoption and usage;
- observable adoption signals for tools from multiple vendors;
- limited internal evidence for private-repository activity;
- monthly panels from the Apple App Store, Google Play Store, Chrome Web Store, and SourceForge.

The main developer-level analysis uses a matched event-study design. Each treated developer is matched to a control developer observed in the same calendar week one year earlier. Matching uses recent activity, and the authors report pre-trend checks, placebo tests with non-AI tools, and comparisons with earlier experimental evidence.

This remains an observational design. Matching and validation reduce some sources of bias but do not make every estimate equivalent to a randomized controlled trial.

## Directly observed findings

### Coding activity rises substantially

**Observed:** The paper reports significant increases in commit activity after adoption of successive tool generations:

- autocomplete: approximately **40%** cumulative increase in commits;
- autocomplete plus synchronous agents: approximately **140%** cumulative increase;
- autocomplete, synchronous agents, and asynchronous agents: approximately **180%** cumulative increase.

These are cumulative effects because newer tools are generally adopted on top of earlier tool generations.

### Effects attenuate across the production hierarchy

**Observed:** The increase becomes smaller as measurement moves from code production toward shipped software.

For the cumulative asynchronous-agent generation, the reported effect falls from approximately:

- **180%** for commits;
- to **50%** for distinct projects or repositories touched;
- to **30%** for releases.

The paper reports similar attenuation for earlier generations. Examples include:

- autocomplete: **228.2%** increase in lines of code, **35.9%** in commits, and **10.2%** in releases;
- synchronous agents: **741%** increase in lines of code, **65%** in pull requests, and **20%** in releases.

The exact percentages refer to specific samples, outcomes, and event-study specifications. They should not be treated as universal productivity constants.

### New application supply increases, but measured usage does not

**Observed:** Across four application marketplaces, the authors find a broad increase in the number of new applications beginning around mid-2025.

**Observed:** They do not find an increase in total application usage during the first three months after launch. The supply-side increase is concentrated largely among applications with little or no user base.

This result concerns marketplace-level usage as measured in the study. It does not establish that no individual AI-assisted application creates value.

## Model-calibrated findings

**Model-calibrated:** The authors estimate an elasticity of substitution of approximately **0.25** between upstream AI-augmented output and downstream human effort.

In their production model, a value well below one indicates strong complementarity: more upstream output cannot readily substitute for human work in review, integration, release management, and other downstream stages.

This number is produced by the paper’s fitted hierarchical production model. It is not a directly observed ratio and should not be presented as a universal property of software engineering organizations.

## Repository interpretation

**Repository interpretation:** The paper provides unusually direct evidence for a central Subprime Code Crisis claim: increasing the rate at which code is produced does not automatically increase shipped, adopted, or valuable software at the same rate.

The relevant production chain is not simply:

```text
more generated code → more productivity
```

It is closer to:

```text
generated code
    ↓
integration and commits
    ↓
pull requests and review
    ↓
projects and releases
    ↓
usage and realized value
```

Capacity constraints at later stages can absorb much of the upstream gain. This makes local measures such as lines of code, generated tasks, or commits incomplete indicators of system-level productivity.

The paper strengthens the case for measuring production attenuation and complementary human capacity. It does not, by itself, prove every broader claim made in this repository about code quality, technical debt, organizational risk, or a future systemic crisis.

## What the source does not establish

**Not established:** The paper does not demonstrate that:

- AI-generated code is generally lower quality than human-written code;
- AI adoption reduces total software productivity in every organization;
- all additional commits or releases are waste;
- review is the only downstream bottleneck;
- AI coding tools cause technical debt or security vulnerabilities;
- application usage is the only valid measure of customer value;
- the observed marketplace changes were caused solely by AI adoption;
- the estimated effects will remain stable as tools, workflows, and organizations adapt.

Those claims require separate evidence.

## Limitations and external-validity risks

The paper’s main limitations include:

1. **Working-paper status.** The analysis has not yet been peer reviewed.
2. **Observational adoption design.** Tool adopters may differ from matched non-adopters in ways that are not fully observed.
3. **Public-repository emphasis.** Much of the GitHub analysis relies on public activity, although the authors provide a limited private-repository validation.
4. **Rare release outcome.** Release analysis uses a smaller selected sample because releases are infrequent and require pre-period release activity.
5. **Measurement hierarchy.** Commits, repositories, and releases are useful proxies but do not capture quality, revenue, reliability, security, or customer outcomes completely.
6. **Marketplace scope.** Four marketplaces cover a meaningful but incomplete portion of the software industry.
7. **Rapid technological change.** Estimates from tools and workflows observed between 2022 and 2026 may not generalize to later systems.
8. **Cumulative tool generations.** Estimates for newer generations often represent adoption of a stack of tools rather than the isolated causal effect of one tool.
9. **Usage interpretation.** Flat aggregate usage can coexist with redistribution, consumer-surplus gains, or value not captured by the study’s metrics.

## Use in this repository

This source is suitable for claims about:

- increased upstream coding activity after AI-tool adoption;
- attenuation between coding activity and shipped output;
- complementarity between AI-generated upstream work and downstream human effort;
- the need to measure releases and usage rather than relying only on code-production metrics.

It should be paired with separate research when making claims about code quality, defects, review burden, maintainability, security, or long-term organizational outcomes.

## Repository integration audit

### Claim-to-source trace

| Repository claim | Location | Exact source result | Relationship | Action |
| --- | --- | --- | --- | --- |
| Higher upstream coding activity in studied settings | `README.md`, Crisis Map | P-2026-01 reports increased upstream coding activity after AI-tool adoption in its studied samples and specifications | Direct, bounded empirical support | Keep as the only Crisis Map node directly supported by P-2026-01 |
| Lower cost of producing code-like output | `README.md`, Crisis Map | P-2026-01 does not directly measure a general reduction in the cost of producing code-like output | Repository synthesis, not an evidence-backed inference | Reclassify as repository synthesis |
| Higher upstream activity can contribute to downstream verification bottlenecks and wider delivery-system risk | `README.md`, Crisis Map and evidence-boundary text | P-2026-01 reports attenuation from upstream activity toward downstream outcomes; it does not measure the map's full bottleneck-and-risk mechanism | Repository synthesis connecting the bounded empirical finding to the wider model | Keep the empirical node independent and label downstream connections as repository synthesis |

- **Integration status:** Corrections required
- **Repository search completed:** Yes
- **Report mentions checked:** Yes
- **Numeric claims checked:** Yes; no numeric claim is added by this correction
- **README claims and diagrams checked:** Yes; the Crisis Map now limits P-2026-01 to the upstream-activity node and labels the wider mechanism as repository synthesis
- **Protocol outcome:** No protocol change
- **Corrections made:** Reclassified “Lower cost of producing code-like output” as repository synthesis; separated the P-2026-01 finding from the proposed downstream mechanism; added an explicit evidence boundary and claim-to-source trace
- **Current-use locations confirmed:** `README.md`; `report/01_the_illusion.md`; `report/02_broken_mechanics.md`
- **Verification date:** —

The source remains `Integration audit = Corrections required`. These corrections do not establish verified integration, and the source must not be marked `Verified` without a `Confirmed` independent review after all corrections are merged.

## Independent review

- **Primary agent or reviewer:** Repository agent implementing the approved PR #28 corrections
- **Independent reviewer:** Not available
- **Flow reviewed:** Flow D — changed repository content relying on P-2026-01
- **Materials independently checked:** None independently checked
- **Outcome:** Review unavailable
- **Discrepancies found:** Independent review was not available
- **Corrections completed:** The two requested Crisis Map corrections were implemented; confirmation remains outstanding
- **Human decision required:** Keep PR #28 in draft and retain `Corrections required` until independent review is available
- **Review date:** 2026-07-27
