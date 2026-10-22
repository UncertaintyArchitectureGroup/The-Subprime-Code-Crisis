+++
source_ids = ["P-2026-01"]
evidence_review = "Reviewed brief"
integration_audit = "Needs re-verification"
last_verified = "—"
independent_review = "Confirmed"
current_use = ["README.md", "report/01_the_illusion.md", "report/02_broken_mechanics.md", "REFERENCES.md", "report/appendices/mechanism-hypotheses.md"]
+++

# Writing Code vs. Shipping Code — September 2026 revision

## Current integration checkpoint — 2026-10-22, #86

The full SDLC register adds or materially reframes this source's bounded evidence
coverage. Flow D retains **Reviewed brief** and resets integration to
**Needs re-verification / —** until the changed use is independently confirmed,
merged and checked on main. The source findings/version below are unchanged.
The earlier review and verification records remain historical. A separate
reviewer **Confirmed** the corrected #86 content on 2026-10-22, after I86-01’s
Design-test correction. The current review field records that actual outcome;
correction merge, actual-main acceptance and final integration verification
remain separate gates. See the dated audit for the exact reviewed commit/tree.

Current use includes `report/appendices/mechanism-hypotheses.md`, in addition to
the prior paths. The [#86 audit and occurrence trace](../../governance/reviews/issue-86-2026-10-22-register-audit.md)
record original locators, scope, outcome omissions, all-use checks and placement.
**Protocol outcome for #86: No protocol change.** Existing controls do not acquire
empirical efficacy from a new hypothesis map. This checkpoint supersedes earlier
integration-state prose for the new use; it does not rewrite prior acceptance.


## Identity, access and disclosures

Mert Demirer, Leon Musolff and Liyuan Yang, *Writing Code vs. Shipping Code: Productivity Effects Across Generations of AI Coding Tools*, NBER Working Paper 35275, May 2026, **revised September 2026**, DOI 10.3386/w35275. [Official page](https://www.nber.org/papers/w35275); [publisher PDF](https://www.nber.org/system/files/working_papers/w35275/w35275.pdf). Retrieved 21 October 2026: **134 pages**, SHA256 `a11c3c7442a4299b54654ba303e791c92166e807d2b6e4f12af50087ee713711`. Locators below use physical PDF pages, with printed pages where helpful. No original PDF is redistributed.

This is a working paper. The cover says it has not undergone the NBER publication review process; the authors' current research pages list a QJE revise-and-resubmit, not an accepted journal publication. Cover funding: Mack Institute at Wharton and Chicago AI Incubator. The current official page discloses Demirer and Musolff's prior Microsoft postdoctoral positions and paid consulting. Microsoft supplied internal tool-use information. These are relevant relationships, not evidence of motive or misconduct.

The supplied **97-page May PDF**, SHA256 `edf1a41a6e4e4cf562571b5fac79eac07693281f88d460a81ee9f8ce1a1c65bb`, and the July integration record remain verbatim history below. Their numbers and verification dates do not describe the September revision. A mutable publisher URL alone does not pin a version.

## Research question, population and design

The paper compares coding activity with higher-level repository outcomes after adoption of autocomplete, synchronous and asynchronous coding tools. The abstract describes more than 500,000 developers. Section 4.3 and Table OA4 (PDF22/76) give **521,329 pre-match records across tool samples**; repeat adopters can occur in more than one sample. This is neither an established unique-person count nor the regression sample for every outcome. Public GitHub histories run from January 2020 to May 2026; tool cohorts and post-adoption windows differ.

Table2/PDF20 distinguishes Copilot subscriptions, Microsoft-recorded agent usage, first CLAUDE.md commits, bot PRs and codex-branch PRs. These signals differ in completeness and meaning. Async users also use sync tools; estimated human and agent-authored activity is not a randomized vendor comparison.

Sections 5 and Appendix D (PDF24–30/95–97) use one-to-one pre-activity matching without replacement, generally eleven pre-weeks and **controls one calendar year earlier**. Outcomes are weekly activity normalized by an individual's pre-period mean. Estimates therefore average proportional individual changes, not ratios of population totals. The **agent-authored async estimates use interrupted time series**: agent outcomes are zero before adoption and for controls by definition, normalized to the corresponding pre-period total outcome. They must not all be described as matched difference-in-differences estimates.

Activity-span restrictions, a final six-calendar-week trim, pre-period positive-outcome requirements, week-minus-one observation and unbalanced follow-up change the eligible population. Baseline normalized differences are winsorized at the 1st/99th percentiles; async positive post-period outcomes use an upper-tail rule. Standard errors cluster by developer; pooled estimates use developer-by-tool units, with some repeat adopters treated as independent units. Outcome samples differ substantially: Table OA6/PDF98 lists commit matched-pair units of **14,279 / 140,118 / 114,104** for autocomplete/sync/async, versus **1,609 / 8,912 / no async estimate** for releases. These are not the abstract's population.

**Identification limits:** adoption/trace selection, changing tools, calendar shocks, noisy pre-period normalization, rare outcomes and public-activity coverage remain material. Matching, pre-trends, placebos and sensitivity checks help, but neither design randomizes adoption. They do not identify effects in a representative enterprise population or hold human labor constant.

## Numeric findings and uncertainty

Figure1 (PDF4, printed p2) reports cumulative adoption-generation headlines: approximately **30%, 180%, 240% more commits** for autocomplete, +sync and +async; the final display reaches about **80% more distinct repositories** and **30% more releases**. Downstream gains remain positive. This is not a fixed set of commits tracked through a funnel or a measured percent of work lost.

Table6 (PDF35, printed p33) gives incremental weeks21–30 estimates; parentheses are source-reported standard errors in the same percentage units:

| Incremental generation | Lines changed | Files | Commits | PRs | Distinct repos | Releases |
| --- | --- | --- | --- | --- | --- | --- |
| Autocomplete | 234.3 (17.9) | 50.0 (4.2) | 30.2 (2.7) | 18.3 (2.2) | 11.9 (1.5) | 9.0 (5.0) |
| Pooled sync | 957.5 (23.2) | 265.0 (4.7) | 153.2 (2.7) | 86.0 (2.1) | 47.3 (0.9) | 19.8 (2.9) |
| Pooled async | 1254.9 (75.3) | 83.3 (3.5) | 60.7 (2.4) | 68.5 (3.4) | 19.2 (0.3) | **Not reported** |

Transcription checks: commits `30.2+153.2+60.7=244.1%`; repos `11.9+47.3+19.2=78.4%`; reported releases `9.0+19.8=28.8%`. These sums follow the authors' cumulative presentation; they are not compounded effects on one jointly observed adoption stack. There is **no marginal async release estimate** because releases cannot be separated into agent and human authorship; missing is not zero. Async PR growth exceeds commit growth, so attenuation is not strict monotonicity in every row.

The autocomplete release estimate is uncertain: a **derived normal 95% approximation**, `9.0 ± 1.96×5.0`, is **−0.8 to 18.8%**; pooled sync similarly gives **14.1 to 25.5%**. These intervals are calculations, not reported confidence intervals. No cumulative interval is calculated without covariance. The pooled positive release headline must not imply every tool-specific release effect is significant.

Appendix C4 (PDF82–83): lines changed count additions plus deletions; repositories are distinct weekly contributions. A release outcome counts recently contributed-to repositories with at least one GitHub release created that week, using a trailing twelve-week contribution window and counting each repository once per week. The construction uses repository/date, not a verified deployment, individual feature authorship, quality or consumer value.

**Sensitivity matters:** Table OA7/PDF128 removes activity-span restrictions and lowers pooled sync commits to **97.2%**, versus 153.2% baseline. Contemporaneous controls give **85.5%** (OA11/PDF132); possible unobserved control adoption is one explanation, not proof that the baseline magnitude is correct. Matching variants cover commits/PRs only (PDF103), so cannot validate releases by association. The common-six-outcome sample still shows broad attenuation and positive releases (OA8/PDF129: sync releases **35.0%, SE6.1**), but PRs **112.4%** exceed commits **103.0%**. Preserve both sign evidence and magnitude/sample sensitivity.

## Additional observations and authors' interpretation

Section6.2/Table7 (PDF37–39) examines added/deleted lines, branch creation/deletion and repository abandonment. Larger release contents and more experimentation/selection can contribute to the activity pattern. Descriptive abandonment rises from **60.0% in 2021 to 69.0% in 2026** (nine percentage points); this is not an identified AI-caused defect rate. Selecting useful alternatives and abandoning others can create value. A subject-keyword bug-fix proxy changes by about **+1pp autocomplete / −1pp sync** (Figure OA16/PDF126), not evidence of uniform quality deterioration. None of these proxies measures review hours, maintainability or escaped defects directly.

## Model result, assumptions and alternatives

Sections3/6.3 and Appendix D8 (PDF11–18/40–42/101–102) represent production as nested layers combining upstream output with effective human/AI input. Review is part of the assumed effective-input technology; the baseline fixes human allocation, with extensions for reallocation. Layer weights and substitution elasticity are assumed common for calibration.

The **autocomplete-only calibration** fits gross-output gains across six layers, giving approximately **theta0.76 and sigma0.23**. Applying those parameters to later tools is a counterfactual under the model, not a direct estimate of review staffing, review hours, replacement ratios or net productivity loss. Alternatives including Cobb–Douglas, decreasing returns and reallocation are explored within a limited model class; their comparative fit does not identify actual organizations' production technology or prove they cannot adapt. The authors favor complementarity and experimentation/selection; repository interpretation keeps these distinct from an observed capacity bottleneck.

## Marketplace analysis: separate descriptive design

Section7.2/Figure11 and Appendix C7/D7 (PDF45–49/89–92/101) use four catalogs, with **usage series for only three**. iOS entry rises; Android's decline reverses; Chrome growth starts before the agentic period. SourceForge has a **slight entry increase**, but insufficient downloads for an equivalent usage analysis (footnote30/PDF47).

For new non-incumbent cohorts over three months, iOS rating totals are roughly stable, **Android download totals rise modestly**, and Chrome's usage proxy declines on a trend predating the agentic period. These specifics qualify the broader abstract/conclusion wording. iOS uses ratings, Android lower-bound install buckets, and Chrome a running maximum of observed **current-user counts**, not directly measured cumulative installs. Centered three-month smoothing, cohort exclusions and follow-up affect timing. Marketplace raw data extend to August2026, later than the GitHub estimation panel; the two designs are not matched developer-to-product outcomes.

Demand, discovery/attention, entry selection, lag and changes in app scope/value are competing explanations. The proxies omit much enterprise software and consumer surplus. Neither flat ratings nor lower Chrome usage identifies a causal AI-to-value loss, and the Android increase must remain visible.

## Repository use and non-findings

One empirical synthesis belongs in R1 Chapter1; R2 Chapter7 links there and develops conditional tests. README summarizes the source boundary; the [mechanism appendix](../../report/appendices/mechanism-hypotheses.md) separates estimates, model results and repository assumptions. Exact cells/sensitivity belong here, not in repeated chapter narratives. The [Astra occurrence audit](../../governance/reviews/issue-63-2026-10-21-astra-review.md) maps every active use and the older historical statements.

The source does not establish universal review overload, fixed verification capacity, declining quality, security harm, vendor intent, industry collapse or net enterprise TCO loss. Useful release gains, efficient selection and successful review/intake adaptation are compatible with the evidence. No raw-data replication was performed; numerical checks verify published cells, units and calculations.

## Review and integration state

Flow C, with pre-edit treatment [6310154890](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/63#issuecomment-6310154890), following the maintainer's authorized correction/hypothesis scope. Primary Astra; independent reviewer `/root/astra_review_issue63` inspected originals and all dependent surfaces without implementing. Initial outcome **Corrections required** on Sol candidate ef5b228/tree809141fe. Corrected-candidate outcome **Confirmed**, 21 October 2026, on `317bc1a3103840866f7d353c29b55ec001cfebd0`, tree `b45614fcee03100bc58d643c5626229250755d43`, for source, argument and all-use integration scope. The dated audit preserves the correction trail. Acceptance does not establish merge or final source verification.

Identity-changing PR80 retained both reset states. Following its accepted merge at `1233ea3663f3166d20918565565a3e970ab9afb8`, exact-main checks and actual independent source/all-use confirmation, the [final verification record](../../governance/reviews/issue-63-2026-10-21-final-verification.md) records **Reviewed brief / Verified / 2026-10-21** for this bounded September integration. This does not validate raw data, universal causal claims or later revisions. Protocol disposition: **Protocol clarification**, no new control or threshold.

## Preserved May and July review history

Historical bodies below are retained verbatim, including their then-pending and then-Verified statements. The current version, source states and dated Astra audit above supersede those statements for present use.

<details>
<summary>Historical Sol audit of the supplied May PDF, before September integration</summary>

# Writing Code vs. Shipping Code — pinned May audit; revision pending

## Identity, version and publication status

Mert Demirer, Leon Musolff and Liyuan Yang, *Writing Code vs. Shipping Code: Productivity Effects Across Generations of AI Coding Tools*, NBER Working Paper 35275, **May 2026**. [Official page](https://www.nber.org/papers/w35275); [publisher PDF URL](https://www.nber.org/system/files/working_papers/w35275/w35275.pdf). Working paper, not peer reviewed according to the supplied cover.

**Version boundary (21 October 2026):** the maintainer supplied a 97-page May PDF, SHA256 `edf1a41a6e4e4cf562571b5fac79eac07693281f88d460a81ee9f8ce1a1c65bb`. All findings below refer to those bytes. Page locators give printed page, then physical PDF page where useful. The live publisher page now lists a **September 2026 revision** with a changed abstract. It is not reviewed or integrated here. The current PDF URL must not be assumed to return the supplied May bytes. Exact-version acquisition/full re-review of September remains open under Flow C; the old July verification is historical, not current.

The May cover credits Mack Institute for Innovation Management at Wharton and Chicago AI Incubator funding. The official page inspected on 21 October 2026 discloses Demirer and Musolff’s prior Microsoft postdocs and current paid consulting. These are dated disclosures to consider with tool/data support; their exact May wording is not established here, and they imply no misconduct.

## Scope, design and measurement

The May abstract describes more than 100,000 GitHub developers combined with AI-use telemetry. §§5–6 use public adoption/activity traces, Microsoft Copilot telemetry and matched observational event studies, with controls' outcomes measured one calendar year earlier. Matching, pre-trends, placebos and limited private-usage checks address some confounding; adoption is not randomized. Public trace selection, cohort/tool differences, changing models and residual adoption/calendar confounding limit causal and enterprise generalization.

Table 5 reports **weeks 21–30**, 1% winsorized outcome coefficients normalized by each developer's pre-period mean; these are average individual proportional changes, not the ratio of aggregate output totals (§6.1, pp23–25 / PDF25–27). Standard errors are clustered by developer. Outcome samples differ: developers with no pre-period releases are excluded, removing most developers from that regression. Table 3 gives outcome-specific treated counts; this is not one identical sample tracked through every layer.

Releases are a proxy: Appendix B.4.7, OA12–13 / PDF63–64, counts recently touched repositories with at least one release in a week, using a trailing twelve-week touched-repository set. It is not the developer's own deployed value, customer benefit or a full quality/cost measure.

## Direct May findings and numeric checks

Figure 1 (p3 / PDF5) explicitly combines adoption up to each generation. The abstract/introduction's rounded **40%, 140%, 180% commit increases** are cumulative autocomplete, +sync, +async stacks. The final headline is approximately **180% commits / 50% distinct repositories touched / 30% releases**. These are positive downstream gains, not evidence of zero benefit or global delivery decline.

Table 5 (p33 / PDF35), inspected visually as well as in extracted text, gives incremental generation estimates. Parentheses below reproduce the table's standard errors, in the same percentage units:

| Incremental row | Lines changed | Commits | PRs created | Distinct repos | Releases |
| --- | --- | --- | --- | --- | --- |
| Autocomplete | 228.2 (17.6) | 35.9 (2.9) | 11.0 (2.7) | 13.6 (1.7) | 10.2 (4.1) |
| Pooled sync | 741.3 (19.2) | 109.1 (2.7) | 65.5 (2.3) | 25.5 (1.0) | 20.3 (2.6) |
| Pooled async | 658.3 (74.7) | 33.6 (2.1) | 71.8 (5.6) | 13.8 (0.4) | **Not reported** |

- The §7.1 prose says **20.2%** sync releases; Table 5 says **20.3%**. Preserve that internal discrepancy; reader synthesis uses **about 20%**.
- For a transcription check, incremental commit values sum to `35.9 + 109.1 + 33.6 = 178.6%`; repos sum to `13.6 + 25.5 + 13.8 = 52.9%`, consistent with rounded Figure 1 headlines. The reported autocomplete/sync release values sum to `10.2 + 20.3 = 30.5%`. **No async release cell exists**: the cumulative release headline must not be described as a separately measured marginal async release effect. The table note and nearby prose give attribution/direct-release-construction reasons for omission; missing is not an estimated zero effect on real-world releases.
- This is an attenuation pattern across outcome estimates. Not every incremental row is monotone: async PR growth exceeds its commit growth. It does not measure a percent of commits lost at each stage or an equal-size production cohort with fixed human input.

## Model-calibrated result versus interpretation

§7.2, Figure 9 (p36 / PDF38) fits a hierarchical production model to the autocomplete pattern, assuming layer-constant parameters: approximately `theta = 0.75`, substitution elasticity `sigma = 0.25`. Figure 10 applies those parameters to sync/async predictions. **0.25 is calibrated**, not a measured review-hours coefficient, a replacement ratio or a productivity loss. The calibration and empirical outcome estimates are different claim classes.

The authors interpret attenuation as weak links/complementarity and discuss downstream human/distribution constraints. Repository interpretation is narrower: study the capacity hypothesis in Chapters 4–7; these data do not identify which stage constrains most organizations or establish review as the universal cause.

## Marketplace findings and competing explanations

§8.2 / PDF42–46 and Appendix B.6 study four marketplace catalogs. Figure 12's three-month usage series cover **iOS ratings, Android installs and Chrome installs** for new non-incumbent cohorts; SourceForge contributes an entry comparison, not an equivalent usage series. Three platforms show entry acceleration or reversal of a decline; SourceForge shows no acceleration. Early cohort usage is flat or declining, with the low-usage share increasing. Do not describe all four as an identical positive-entry/flat-usage result.

These descriptive series are not linked causal outcomes of the matched GitHub adopters. §8.2.4 explicitly allows scarce discovery/attention, entry selection, slow adoption/learning and AI-related demand. Ratings/downloads imperfectly proxy consumer value; the analysis does not measure all enterprise software, quality or total consumer surplus. Both increased releases and these limiting usage observations remain visible.

## What the source does not establish

No general quality decline, review-time multiplier, fixed verification capacity, universal bottleneck, inevitable technical debt, security effect, enterprise TCO loss, vendor motive or macroeconomic crisis. Production improvements, effective review automation and successful capacity/intake adaptation remain compatible with the May findings.

## Repository integration audit

Primary flow **C** after discovering September revision; the supplied-May use audit also satisfies the required changed-use checks. Before changed uses, both dimensions were reset and the verification date cleared. [Pre-edit treatment](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/63#issuecomment-6309465344) and [version note](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/63#issuecomment-6309440882) precede substantive edits.

The [N63 occurrence trace](../../governance/reviews/issue-63-2026-10-21-mechanism-audit.md) checks exact numbers, inference, neighboring conclusions and placement across README, R1, R2, bibliography and indexes. Main empirical synthesis is in R1 Chapter 1; R2 Chapter 7 links there and develops hypotheses instead of repeating the numbers. The [mechanism appendix](../../report/appendices/mechanism-hypotheses.md) separates findings, assumptions, hypotheses and scenarios. Protocol outcome: **Protocol clarification**, without new controls. Full current-version integration/analytical acceptance remain incomplete; no verification date.

## Independent review

- Primary reviewer: Sol; independent reviewer: `/root/sol_review_issue63` (separate Sol agent, did not implement).
- **Confirmed**, 21 October 2026, at candidate `1c0d33806824add200e5b215dd1f8194955ec441`, tree `1a8aa6b26b24b9e0901cbb8684443c3c7abd60a7`, within the **Sol preparation/source-transcription and limitation-disposition scope**. Original May PDF/table/figure, methods, calibration, marketplace limits and every current use independently checked; no material discrepancy found. Exact review/check record is in the [dated audit](../../governance/reviews/issue-63-2026-10-21-mechanism-audit.md).
- This outcome confirms neither the September original nor Astra's analytical acceptance, merge or source verification. The two reset status dimensions remain unchanged. The actual July review is preserved separately below. Faithful final recording/publication checks follow this scoped review.



</details>


The following prior brief body is retained verbatim from main `ada19312045fd859631bc6e8f230f25582eec084`. Its Verified/date/completion statements describe the earlier July state and are superseded for current status by the front matter and version boundary above.

<details>
<summary>Historical July 2026 brief and review, not current verification</summary>

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

- **Integration status:** Verified
- **Repository search completed:** Yes; source ID, author names, title fragments, distinctive claims, and attributed numbers were searched across `README.md`, `report/`, `protocols/`, `REFERENCES.md`, `evidence/SOURCES.md`, and evidence indexes on 2026-07-27
- **Report mentions checked:** `report/01_the_illusion.md` ("Writing Code vs. Shipping Code" section and Chapter 1 references) and `report/02_broken_mechanics.md` ("Production Attenuation," "Complementary Human Capital," and references)
- **Numeric claims checked:** Repository uses of the approximately 180% commit, 50% project, 30% release, and 0.25 model-elasticity values were checked against the reviewed brief and independently rechecked against the supplied publisher PDF
- **README claims and diagrams checked:** Yes; the Crisis Map no longer sequences heterogeneous study numbers, labels the lower-cost premise and downstream mechanism as repository synthesis, and bounds the only P-2026-01 empirical node to the studied settings
- **Protocol outcome:** No protocol change; no protocol currently attributes a threshold, control, or universal operating rule directly to P-2026-01
- **Corrections made:** Removed the Crisis Map's unrelated numeric sequence; labeled all map claim types; separated the Technical Bankruptcy warning scenario from the map's synthesis outcome; added the source boundary and non-findings; synchronized `Current use`
- **Current-use locations confirmed:** `README.md` Crisis Map and evidence boundary; `report/01_the_illusion.md`; `report/02_broken_mechanics.md`; bibliography and registry records in `REFERENCES.md` and `evidence/SOURCES.md`
- **Verification date:** 2026-07-27

### Claim-to-source trace

| Repository claim | Location | Exact source result | Relationship | Action |
| --- | --- | --- | --- | --- |
| Lower cost of producing code-like output | `README.md`, Crisis Map | The paper does not directly measure a general cost reduction for producing code-like output | Repository synthesis | Keep labeled as repository synthesis; do not attribute directly to P-2026-01 |
| Higher upstream coding activity in studied settings | `README.md`, Crisis Map | Adoption estimates increase for upstream coding-activity measures in the paper's matched event-study settings | Direct, bounded finding | P-2026-01 directly supports only this bounded empirical node; keep with source ID and scope label |
| Connection from the upstream-activity node to downstream verification and delivery-system risk | `README.md`, Crisis Map | The paper reports attenuation toward projects and releases but does not measure the complete depicted mechanism | Repository synthesis | Keep only as empirical support for the upstream-growth premise, with the downstream connection labeled by the map context as repository synthesis rather than a measured causal chain |
| Commit effects attenuate toward projects and releases | `report/01_the_illusion.md`, "Writing Code vs. Shipping Code" | Approximately 180% commits, 50% projects or repositories touched, and 30% releases for the cumulative asynchronous-agent generation | Direct finding across distinct outcomes in the paper's studied setting | Keep with nearby limitations and brief link |
| Production attenuation and complementary downstream effort | `report/02_broken_mechanics.md`, "Production Attenuation" and "Complementary Human Capital" | Attenuated outcome estimates; model-calibrated elasticity of substitution of approximately 0.25 | Direct finding plus model-calibrated interpretation | Keep with observational/model boundaries |
| Technical Bankruptcy | `README.md`, Crisis Map | Not measured or established by the paper | Warning scenario / repository hypothesis | Separate from the synthesis outcome and connect with a dashed scenario edge |

## Independent review

- **Primary agent or reviewer:** Codex primary agent
- **Independent reviewer:** GPT-5.6 Thinking
- **Flow reviewed:** Flow D — Crisis Map re-verification for P-2026-01
- **Materials independently checked:** Supplied publisher PDF; `README.md` Crisis Map and evidence boundary; `report/01_the_illusion.md`; `report/02_broken_mechanics.md`; `protocols/`; `REFERENCES.md`; `evidence/SOURCES.md`; this evidence brief
- **Outcome:** Confirmed
- **Discrepancies found:** The first draft of the map contained an unsupported `Evidence-backed inference` label and visually embedded the empirical node in a linear synthesis chain; both were corrected before verification
- **Corrections completed:** The lower-cost node is repository synthesis; P-2026-01 independently supports only the bounded upstream-activity premise; downstream bottleneck and delivery-risk connections remain repository synthesis; Technical Bankruptcy remains a dashed warning scenario
- **Human decision required:** None for this verification step; future source or repository changes must trigger the applicable re-review or re-verification flow
- **Review date:** 2026-07-27

The source is fully processed for the repository state verified on 2026-07-27:
`Evidence review = Reviewed brief`, `Integration audit = Verified`, and
`Last verified = 2026-07-27`.

</details>