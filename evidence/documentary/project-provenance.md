+++
source_ids = ["D-2026-05", "D-2026-06"]
evidence_review = "Reviewed brief"
integration_audit = "In progress"
last_verified = "—"
independent_review = "Review unavailable"
current_use = ["TERMINOLOGY_AND_ATTRIBUTION.md", "README.md", "REFERENCES.md"]
+++

# Project provenance: public repository and February 2026 formulation

## Review scope

This brief records two public records used only to establish the provenance of this project's own inspectable work: the GitHub repository creation timestamp and a dated DOU publication by Vitalii Oborskyi that publicly states the project's delivery-system formulation.

These records are documentary provenance. They do **not** establish coinage of the phrase **Subprime Code Crisis**, independent validation of the project's thesis, or priority over every related idea.

## Sources reviewed

### D-2026-05 — DOU publication by Vitalii Oborskyi

- **Author:** Vitalii Oborskyi
- **Title:** *Субпрайм-криза коду: чому AI-асистенти роблять нас повільнішими — і дані це доводять*
- **Publisher / host:** DOU
- **Published:** 2026-02-10 08:40, as displayed by DOU
- **Canonical public page:** https://dou.ua/forums/topic/57846/
- **Publication status:** dated public practitioner/research article authored by the project creator; not an independent validation source.

### D-2026-06 — GitHub repository metadata

- **Record:** GitHub REST repository metadata for `UncertaintyArchitectureGroup/The-Subprime-Code-Crisis`
- **Repository owner:** Uncertainty Architecture Group
- **Repository:** `The-Subprime-Code-Crisis`
- **Documented creation timestamp:** `2026-02-06T17:16:44Z`
- **Canonical public record:** https://api.github.com/repos/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis
- **Publication status:** platform metadata for the public repository; establishes the repository object's creation timestamp, not the date on which every underlying idea was first developed.

## Documentary purpose

The sources answer a narrow provenance question: **what public record exists for this project's own research object and formulation, and by what date?**

They are not used as evidence that the Subprime Code Crisis mechanism is empirically true. Empirical and theoretical support for the report remains governed by the other sources in the Evidence Library.

## Documented facts

### Repository boundary

GitHub's repository metadata records `created_at = 2026-02-06T17:16:44Z` for `UncertaintyArchitectureGroup/The-Subprime-Code-Crisis`.

This provides an externally served platform timestamp for the existence of the public repository object. It does not establish when private drafting, earlier discussions, or unpublished analysis began.

### Public formulation on DOU

DOU displays the article under Vitalii Oborskyi with the date and time **10 February 2026, 08:40**.

The article publicly documents a formulation that is materially more specific than ownership of a phrase. In the article, Oborskyi:

1. frames the problem as a **system-level delivery problem**, not merely code-generation quality;
2. distinguishes the subjective/local speed of producing code from end-to-end delivery outcomes;
3. describes senior work shifting from authoring toward review and debugging;
4. identifies Code Review as a downstream bottleneck under increased AI-generated change volume;
5. argues that isolated coding-task gains do not by themselves establish improved system throughput; and
6. presents deferred review, rework, maintainability, and delivery cost as the mechanism behind the crisis framing.

The article also explicitly identifies itself as the first in a series analyzing the mechanism using independent research and links readers to this GitHub repository.

## Formulation fingerprint

For provenance purposes, the February 2026 public formulation can be summarized as the following project-authored systems chain:

```text
lower cost / higher speed of code generation
        ↓
more upstream change volume
        ↓
review and verification capacity does not automatically scale
        ↓
bottleneck migration toward review / debugging / downstream delivery work
        ↓
local coding productivity can diverge from end-to-end delivery throughput
        ↓
deferred rework, maintainability, and operating cost accumulates
```

This is a **repository interpretation / systems formulation** documented by the dated DOU publication. The DOU article is evidence that Oborskyi publicly articulated this formulation by that date; it is not independent evidence that every causal link is universally valid.

## Source-author interpretation

Because D-2026-05 is authored by Vitalii Oborskyi, its analytical conclusions are the source author's own interpretation. The page is useful for provenance precisely because it is a dated public expression of that interpretation, but it must not be counted as independent corroboration of the repository's thesis.

D-2026-06 contains platform metadata rather than an analytical interpretation.

## Repository interpretation

Together, the two records support a bounded provenance statement:

- the public GitHub repository object existed no later than **2026-02-06T17:16:44Z**; and
- a detailed delivery-system formulation attributable to Vitalii Oborskyi was publicly hosted by DOU no later than **2026-02-10 08:40** as displayed on the page.

The repository therefore has a dated public record for its own contribution that is separable from the history of the phrase itself.

## What these sources do not establish

These sources do **not** establish:

- that Vitalii Oborskyi coined **Subprime Code**, **Subprime Code Crisis**, or **The Subprime Code Crisis**;
- that no earlier person articulated any similar technical-debt, review, or mortgage-crisis analogy;
- that the repository's formulation influenced Richard Ewing, Nick Vigier, Igor Światowski, or any other author;
- that later overlapping formulations were derived from this project;
- that a GitHub creation date is the first date on which the underlying ideas existed;
- that DOU independently validated the article's empirical claims merely by hosting it; or
- that the complete systems mechanism is a directly measured causal chain.

Those distinctions are essential to the repository's independent-convergence and evidence-boundary rules.

## Limitations and conflicts

- D-2026-05 is authored by the project creator and therefore has a direct authorship interest. It is a strong timestamped provenance record but not independent validation.
- DOU publication metadata is a platform record and may be reformatted or migrated; the currently inspected page is the operative public surface.
- D-2026-06 establishes repository-object creation, not private intellectual development or first publication of every component idea.
- Search indexes and platform records are not complete historical archives.

## Claim-to-source trace

| Repository claim | Location | Exact documentary support | Relationship | Action |
| --- | --- | --- | --- | --- |
| Public repository object existed by 2026-02-06 | `TERMINOLOGY_AND_ATTRIBUTION.md`; `README.md` | GitHub REST `created_at = 2026-02-06T17:16:44Z` | Documented fact | Keep, with scope boundary |
| Oborskyi publicly documented the delivery-system formulation by 2026-02-10 | `TERMINOLOGY_AND_ATTRIBUTION.md`; `README.md` | DOU page displays author/date and contains local-vs-system productivity, review-bottleneck, and downstream-cost argument | Documented provenance | Add, explicitly not independent validation |
| Project contribution is separable from phrase coinage | `TERMINOLOGY_AND_ATTRIBUTION.md`; `README.md` | Dated project formulation plus separately documented earlier/parallel terminology records | Repository interpretation | Keep bounded; do not convert into coinage claim |

## Repository integration audit

- **Integration status:** In progress
- **Repository search completed:** searched author identity and project-provenance terms; author attribution currently appears in README, `TERMINOLOGY_AND_ATTRIBUTION.md`, and `CITATION.cff`.
- **Report mentions checked:** no report claim requires D-2026-05 or D-2026-06 as empirical support; no report change proposed.
- **Numeric claims checked:** only dates/timestamps are introduced by these documentary records.
- **README claims and diagrams checked:** attribution section is updated; Key Takeaways, Claim confidence map, Evidence Map logic, and Crisis Map are unchanged.
- **Protocol outcome:** No protocol change.
- **Corrections made:** add bounded project-provenance record and distinguish public formulation provenance from phrase origin and independent validation.
- **Current-use locations confirmed:** `TERMINOLOGY_AND_ATTRIBUTION.md`, `README.md`, `REFERENCES.md`.
- **Verification date:** —

## Independent review

- **Primary agent or reviewer:** ChatGPT
- **Independent reviewer:** unavailable
- **Flow reviewed:** Flow A — Add source
- **Materials independently checked:** unavailable
- **Outcome:** Review unavailable
- **Discrepancies found:** no independent assessment
- **Corrections completed:** primary review only
- **Human decision required:** maintainer review and merge decision; no `Verified` status may be claimed without independent confirmation.
- **Review date:** 2026-08-31
