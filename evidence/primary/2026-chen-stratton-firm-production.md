+++
source_ids = ["P-2026-04"]
evidence_review = "Brief in progress"
integration_audit = "Not started"
last_verified = "—"
independent_review = "Confirmed"
current_use = []
+++

# Chen–Stratton: AI adoption and firm software production

> **Assessment candidate, 2026-10-22, #87.** Source review and the proposed
> interpretation below are prepared for the required treatment decision. No
> report claim, hypothesis verdict or protocol has been changed. This is not an
> accepted integration or a `Verified` source. See the
> [impact and treatment proposal](../../governance/reviews/issue-87-2026-10-22-source-impact.md).

## Identity, exact version and access

**P-2026-04** — Fiona Chen and James Stratton, *Artificial Intelligence in the
Firm: Bottlenecks in Software Production*. Job Market Paper, **4 August 2026**;
first version dated 7 January 2026. Both authors list Harvard affiliations on the
cover. [Canonical PDF](https://fion.ac/jellyfish.pdf), linked from
[Chen's research page](https://fion.ac/) and
[Stratton's research page](https://stratton.scholars.harvard.edu/).

Retrieved 2026-10-22: **78 pages**, 3,509,397 bytes; SHA256
`27f8d1fe0a2c145e700ae8835c997533fb4483e21a11f9c2385186bdb9f7c096`.
Locators below use physical PDF pages, which match the printed page numbers after
the cover. The mutable URL's search cache also exposes an earlier January text;
its sample and numbers are not this edition. PDF metadata and HTTP modification
dates do not replace the edition date on the cover. No original PDF is redistributed.

The cover, author pages and current CV identify a working/job-market paper.
Journal acceptance or completed peer review was not established. Cover disclosures:
Stripe Economics of AI Fellowship, Harvard Kennedy School's Stone Program and
Schmidt Sciences AI at Work funding; Jellyfish data partnership. The partner's
manuscript check concerned proprietary information, not scientific validation.
These relationships are relevant context, not evidence of improper conduct.
The proprietary records and analysis code were not obtained; this review reproduces
published-value arithmetic, **not regressions or raw-data results**.

## Research question, data and population

The study asks how firm adoption of coding assistants and agents relates to coding
activity, tracked software completion, employment and the review process.

| Dimension | Original description and review boundary |
| --- | --- |
| Data period | January 2021–March 2026, Jellyfish customers consenting to research and present through the analysis window (§2.1, p7; selection in §2.2, p11) |
| Overall coverage | 718 firms; 725,938 workers, **not 725,938 software developers** (Table 1, p52) |
| Activity records | 200,945,700 commits; 49,050,030 PRs; 68,281,845 Jira issues; 21,270,247 calendar events (Table 1) |
| Unequal source coverage | Version control: 99.6% of firms; task management: 94.4%; calendars: 29.7%. These are coverage shares, not outcome-specific regression sample sizes |
| Roles | Role information for 372,912 workers; 55.2% classified as software engineering, with other roles including product, revenue and administration (Table 3, p54) |
| Firm composition | Selected software-intensive organizations; mean January 2023 total employment 1,652 (SD 6,015), active Jellyfish engineers 241 (SD 363); substantial heterogeneity (Table 2, p53) |
| Additional data | Revelio employment profiles and partial HR information; a 100-engineer Prolific time-allocation survey; qualitative interviews with an internally inconsistent reported count |

Jira resolution is the authors' output proxy: interview accounts and workflow
examples connect it with completed/deployed work. The study does not independently
verify deployment or useful functionality for every resolved item. An epic is a
larger tracked grouping; neither issue nor epic counts measure user benefit.
The researchers do not observe code contents (p10). Activity/PR metadata therefore
cannot directly establish semantic defects, security or maintainability.

## Exposure, comparator and identification

Firm adoption is the earliest observed signal for a tool category. Business-seat
activation APIs identify Copilot/Cursor assistants and Claude Code; bot accounts,
commit signatures and PR-body signatures identify agents and review tools
(§2.4, pp13–16; Appendix F.1, pp63–65). Personal accounts or unintegrated use can
be missed. Firm adoption does not mean every worker used the tool. Assistant
take-up is restricted to the earlier period to separate it from agents; plots
show up to 16 post-adoption months for assistants and 12 for agents. Agent
adoption is an increment in an environment where assistants may already be used,
not a common pure-AI-versus-no-AI experiment.

The main analysis is a **firm-month staggered-adoption event study**, using
two-way fixed effects, firm/month effects, time-varying controls for baseline firm
size and firm-clustered standard errors. Month −1 is the reference and event-time
tails are binned (§3, pp16–18). Coding and completion outcomes are firm totals
divided by active Jellyfish workers in that firm-month (Figures 6–7), not output
per active labor-hour. Outcome-specific sample sizes and covariance between
different outcome estimates are not reported alongside these figures.

Identification requires comparable untreated trajectories for earlier, later and
non-adopting firms. The authors motivate timing variation through procurement
processes; adoption is **not randomized**. Table 4 (p55) shows adoption timing
related to firm size and some other characteristics. Controls do not establish
that remaining differences are exogenous.

**Material visual diagnostic:** several agent plots have earlier pre-period
estimates below zero that rise toward the reference period, including commits/PRs
(Figure 6C/E), merge latency (11A), change requests (12A) and reviewer participation
(13C). This review does not estimate a joint pretrend test, and the manuscript
does not report one for these outcomes. The figures cannot be described as
demonstrating flat pre-trends or validated causality. Appendix Figure 1 (p56)
compares alternative DiD estimators for **agent lines of code only**; it does not
establish equivalent robustness for all review or completion outcomes.

## Published estimates and reproduced calculations

These are **pooled coefficients**, not the larger month-12/month-16 endpoint
coefficients. Parentheses contain published standard errors in the same units.
The [calculation record](../../governance/reviews/issue-87-2026-10-22-numeric-checks.json)
retains inputs, formulas, locators and checks. Relative percentages below are
derived as `100 × coefficient / baseline mean`.

| Outcome | Agents: baseline; coefficient (SE) | Assistants: baseline; coefficient (SE) | Interpretation |
| --- | --- | --- | --- |
| Added lines per active worker-month, Fig 6A/B p39 | 5,016.57; +1,494.39 (582.83) | 3,498.08; +420.10 (370.59) | Approximately +29.8% / +12.0%; assistant interval includes zero |
| Commits per active worker-month, Fig 6C/D | 22.58; +4.57 (1.12) | 14.84; +1.40 (0.64) | Approximately +20.2% / +9.4%; positive estimates with intervals above zero |
| Created PRs per active worker-month, Fig 6E/F | 5.34; +1.22 (0.29) | 3.78; +0.19 (0.17) | Approximately +22.8% / +5.0%; assistant interval includes zero |
| Resolved issues per active worker-month, Fig 7A/B p40 | 3.67; +0.12 (0.17) | 2.70; +0.09 (0.10) | Approximately +3.3% for both, with intervals spanning zero |
| Resolved epics per active worker-month, Fig 7C/D | 0.16; +0.01 (0.01) | 0.11; 0.00 (0.01) | Uncertain, coarsely rounded estimates; do not derive precise relative bounds |
| PR submission-to-merge **elapsed days**, Fig 11 p44 | 7.03; +3.45 (1.60) | 9.34; −0.38 (0.97) | Approximately +49.1% / −4.1%; only the agent estimate excludes zero |
| Share of PRs with a formal change request, Fig 12A/B p45 | 13.00%; +11.84 pp (1.01 pp) | 14.23%; +0.94 pp (0.55 pp) | Agent relative change approximately +91.1%; **not a measured defect-rate increase** |
| Review comments per PR, Fig 12C/D | 1.66; +0.58 (0.11) | 1.98; +0.05 (0.07) | Approximately +34.9% / +2.5%; comments are not labor-hours |
| Workers reviewing at least one PR/month, Fig 13C/D p46 | 29.42%; +4.14 pp (1.28 pp) | 21.07%; +1.76 pp (0.61 pp) | Approximately +14.1% / +8.4% relative; extensive participation, not FTE reassignment |

For agents' issue completion, a normal approximation from printed numbers gives
`0.12 ± 1.96 × 0.17 = [−0.2132, 0.4532]` issues per active worker-month, or about
**−5.8% to +12.4%** of baseline. This preserves both the small positive point
estimate and uncertainty. It does not establish zero output benefit. The authors'
approximately 12% upper bound applies to this issue estimate, not every output
measure or epic estimate.

The corresponding approximate intervals are **+7.0% to +52.6%** for agent lines
of code and **+0.31 to +6.59 elapsed days** for merge latency (about +4.5% to +93.7%).
These transformations use rounded published coefficients and a normal critical
value, holding the printed baseline fixed; baseline uncertainty and covariance
are unavailable. Significant coding results plus nonsignificant completion
results are **not a statistical test of their difference**. Comparing the
completion upper bound with the coding point estimate does not test equality
against the full coding interval. No literal fraction of code lost in a common
delivery funnel is calculated.

### Other results that constrain the interpretation

- **Employment (Figures 8–9, pp41–42):** agents' overall log-employment coefficient
  is +0.01 (0.02), and active-engineer log employment −0.04 (0.05). Assistants'
  overall coefficient is 0.00 (0.01); their engineer estimate +0.07 (0.03) has
  differential pre-trends. Junior/senior splits do not establish a broad job-loss
  mechanism. The authors' 13.8% engineering-decline bound is a log-point
  approximation: −0.138 log points corresponds to about −12.9% under exponentiation.
  Short-run selected-firm evidence cannot settle later or economy-wide employment.
- **Coder participation (Figure 13A/B):** agent +1.03 pp (1.24), baseline 43.12%;
  assistant +0.69 pp (0.70), baseline 38.31%. These are uncertain participation
  changes. Coders and reviewers may be the same people; the categories are not
  exclusive departments.
- **PR size (Appendix Figure 5, p60):** agent −67.99 (126.91) lines, baseline
  1,167.97; assistant +66.07 (100.90), baseline 1,167.17. Nonsignificance does not
  prove identical scope, complexity or quality.
- **Task-size checks (Appendix Figure 4, p59):** figure-specific LLM-label
  coefficients are agent +0.02 (0.04), assistant 0.00 (0.03); predicted-cycle-time
  coefficients are −0.02 (0.04) and +0.02 (0.03). The reporting and scale
  ambiguities below limit a strong composition-adjustment claim.
- **Time allocation (Figure 10, p43):** telemetry-imputed shares are coding 42.0%,
  review 18.6%, management 39.5%; survey shares 30.8%, 21.8%, 47.4%.
  The imputation assigns elapsed time since the preceding work signal, capped at
  two hours, to each event, then averages worker shares. Jira resolution counts
  as coding; PR reviews/merges as review. The survey asks 100 Prolific engineers
  about a typical week. These are descriptive allocation proxies, **not adoption
  effects on instrumented active review hours**.
- **AI review tools (Figure 14, p47):** near-80% firm take-up by March 2026;
  23.3% of comments attributed to AI and 10.8% of PRs with at least one AI comment.
  These descriptive measures are not a controlled evaluation of AI-review
  effectiveness. The review-comment treatment outcome is not clearly documented
  as excluding bots; do not relabel every comment as human effort.

## Reporting ambiguities, limitations and search

The following are recorded rather than silently resolved:

1. Main §3.2 (p18) reports **17** interviewees; Appendix B (p48) reports **21**.
   Interview observations can motivate mechanisms but are not a quantified
   prevalence estimate or a controlled ownership test.
2. Main p20 assigns −0.02/+0.02 to the LLM-size measure; Appendix Figure 4 assigns
   these to predicted cycle time and +0.02/0.00 to the LLM measure. Use the
   panel-specific values when needed and preserve the discrepancy.
3. Appendix F.2 (pp66–67) describes labels clipped to 0–3, while the LLM panels
   show baseline means 5.08/5.11 and Appendix Figure 3 labels the prediction in
   hours. The transformation is not explained. Do not invent a conversion or
   treat this as demonstrated equivalence of task size. The model is trained
   against GPT labels, not measured expert task-hours; Table 6's MSE 0.4105 and
   MAE 0.5019 concern agreement with those labels.
4. Main prose rounds assistant reviewer participation to 10%; the precise
   figure values imply about 8.4%. Use the figure values for arithmetic.

Other material limits: selected consenting customers, incomplete adoption signals,
firm rather than individual exposure, changing tools and concurrent organizational
changes, outcome-specific coverage, pre-period movements, follow-up limits,
endogenous active-worker denominators and no accessible raw-data replication.
The handling of PRs that never merge, censoring and the exact bot exclusions in
review outcomes are not adequately specified to reconstruct those estimands.
Jira text-based size estimates and elapsed cycle-time predictions do not supply
ground-truth functionality, complexity, value or quality adjustment.

A bounded 2026-10-22 search checked the canonical PDF, author pages/CV, title and
author searches with correction/critique/replication terms, and author-linked
Jellyfish write-ups. No newer author-linked edition, formal erratum or accessible
independent replication of this exact August analysis was established. The
September 2025 and January 2026 partner write-ups concern earlier work; neither
they nor cached January search text count as independent corroboration. This
search is not a systematic review of all AI development research. The
[impact report](../../governance/reviews/issue-87-2026-10-22-source-impact.md)
preserves the existing positive, null and conflicting evidence packet.

## Model and source-author interpretation

Sections 5 and Appendix G model code production and review with coding productivity,
an incoming bug probability, a review-detection function and firm optimization.
The model distinguishes more draft output from a change in draft quality. Under
its assumptions, fixed review labor can attenuate the output response; increased
bug probability can increase optimal review intensity. Reallocation or better
technology may relax the constraint. These are analytical comparative statics,
not an estimated full-SDLC production function, mediation analysis or tested remedy.

The authors interpret the activity/completion/review pattern as a review bottleneck
and the comment/change-request shifts as a bug-rate channel. Our review retains
the measured shifts without treating that channel as directly identified: the
paper also permits changing review standards, and it lacks direct code-quality
measurement. Its statement that the bottleneck persists despite AI review is
stronger than a causal effectiveness result supplied by the descriptive uptake
data. Continued human participation can coexist with effective assistance.

## Proposed repository interpretation and comparison with NBER

**Proposed, pending the #87 treatment decision:** this is material firm-level
evidence that larger coding-activity estimates can coexist with a much smaller,
uncertain tracked-completion estimate and a lengthening review path. It strengthens
the case for evaluating the SDLC as a coupled system. It does not measure a
universal loss of productivity or make every proposed downstream consequence true.

The comparison uses the already accepted **September 2026 P-2026-01 brief**,
[Writing Code vs. Shipping Code](2026-writing-code-vs-shipping-code.md), rather
than reopening #63 or using the uploaded May version as a second study.

| Comparison | Chen–Stratton, August | NBER P-2026-01, September |
| --- | --- | --- |
| Observation/exposure unit | Firm-month; first recorded firm tool adoption, with incomplete worker take-up | Selected individual public-GitHub tool-adopter cohorts; different subscription/telemetry/trace signals |
| Data/design | Jellyfish private organizational activity, January 2021–March 2026; staggered firm DiD | GitHub histories January 2020–May 2026 and Microsoft telemetry; matched historical controls, with async agent outcomes using interrupted time series |
| Normalization | Firm activity/completion divided by active workers | Weekly individual outcomes normalized to own pre-period means; outcome populations differ |
| Coding/output boundary | Added lines, commits, PRs versus resolved Jira issues/epics | Commits/repositories versus recently contributed-to repositories with a GitHub release |
| Main pattern | Agent coding gains, small positive uncertain completion estimates, increased review latency and process activity | Positive release gains alongside larger activity gains; no separate marginal async release estimate |
| Mechanism evidence | Direct review-process indicators; no causal active-hours/capacity or ownership measure | Complementarity model calibration, not measured review overload or ownership |
| User/economic boundary | No linked user outcome or lifecycle return | Separate marketplace series, including modest positive Android usage; no linked individual-to-user ROI chain |

The papers use different analytical data and designs; Jellyfish telemetry is not
presented as a reuse of NBER's panel. They still share parts of the tool/GitHub
ecosystem, and person/repository overlap cannot be quantified from the publications.
Do not add their participant counts or call them disjoint random samples. They
provide convergent bounded observations, not automatically a macro/micro proof
of the same causal mechanism. Chen–Stratton's own NBER citation (p74) is to May,
retrieved June 19; its Appendix Figure 2 is not a comparison to September.

The proposed hypothesis treatment is H0-A/COD-1 **Provisional support** for the
observable activity/completion premise; H0-B gains review-process evidence while
its demand/capacity mechanism remains **Open**. REV-1 receives provisional support
for the agent-associated process pattern; its complete causal quality/ownership
proposition remains **Open**. REV-2 and INTG-1/2 remain **Open**. The full node
inventory and symmetric weakening/remedy tests appear in the impact report.

## What this source does not establish

It does not establish active human review hours increasing by 49%, code defects
nearly doubling, failed AI-review assistance, lost understanding/ownership,
industry-wide capacity saturation, burnout, persistent technical debt, higher
TCO, negative ROI or lost user benefit. It does not test the repository's proposed
controls. Those propositions need their own outcome evidence. Positive coding
effects, uncertain positive completion, assistant differences and the absence of
identified broad employment loss remain part of the finding.

## Known uses and repository integration audit

- **Accepted reader-facing uses:** none. This source is newly registered for #87.
- **Audit owner:** primary agent `/root`; supporting analyst
  `/root/issue87_existing_evidence` inspected existing uses and all report/protocol
  layers; `/root/issue87_source_identity` assisted source acquisition and arithmetic.
- **Audit state:** Not started for substantive integration; impact assessment
  prepared against main `00d2b65c27d18b78d8f6cbe597a3a6dfe762409a`.
- **Proposed paths, original locators, interpretation limits and protocol outcome:**
  [#87 impact report](../../governance/reviews/issue-87-2026-10-22-source-impact.md).
- **Numbers:** figure transcription plus normal/relative transformations in the
  linked calculation record; no raw-data replication.
- **Proposed protocol outcome:** No protocol change.
- **Last verified:** —. Report/register integration, all-use audit, synchronized
  status transitions, independent integration review and accepted-main verification
  remain required after the treatment decision. New material NBER use will require
  Flow D; this provisional proposal does not revise its accepted interpretation.

## Independent review

- Primary author: `/root`; source and context analysts named above are coauthors,
  not independent reviewers.
- Independent reviewer: `/root/issue87_independent_review`, who separately read the
  full pinned original, inspected key figures and recalculated core effects.
- Initial candidate assessment outcome: **Corrections required**, 2026-10-22.
  I87-01 identified imprecise deterioration/revision wording in the proposed report
  text; the proposal now names formal change requests/comments neutrally. The
  continuous-presence selection locator was also clarified to §2.2/p11.
- Corrected assessment/proposal: **Confirmed**, 2026-10-22, for brief SHA256
  `b15b7adf77560123a5d9b15a5c5fa6efc06f675fc804b4fc1153ba1e61e10a81`
  and the associated impact/numeric hashes recorded in the impact report. I87-01
  is resolved. This paragraph faithfully records that actual outcome; it does not
  expand its scope to substantive integration or maintainer approval.
- Source review remains `Brief in progress` at this proposal checkpoint;
  integration remains `Not started / —`.
- Review boundary: assessment and proposed treatment only; no accepted integration
  or future merge may be inferred. The impact report records the eventual outcome,
  discrepancies, corrections and exact reviewed candidate.
