+++
source_ids = ["D-2026-05", "D-2026-06", "D-2026-07"]
evidence_review = "Reviewed brief"
integration_audit = "In progress"
last_verified = "—"
independent_review = "Review unavailable"
current_use = ["TERMINOLOGY_AND_ATTRIBUTION.md", "README.md", "REFERENCES.md"]
+++

# Project provenance: precursor article, repository creation, and Subprime Code publication

## Review scope

This brief records three public documentary records used only to establish the provenance of this project's own inspectable work: a January 2026 precursor article and discussion, the GitHub repository creation timestamp, and the February 2026 Subprime Code publication by Vitalii Oborskyi.

These records document the development path of the project's delivery-system synthesis. They do **not** establish coinage of the phrase **Subprime Code Crisis**, independent validation of the thesis, or priority over every related idea.

## Sources reviewed

### D-2026-05 — January DOU precursor

- **Author:** Vitalii Oborskyi
- **Title:** *Ілюзія економії: чому заміна розробників на AI — це шлях до технічного дефолту*
- **Publisher / host:** DOU
- **Published:** 2026-01-05 15:30, as displayed by DOU
- **Canonical public page:** https://dou.ua/forums/topic/57244/
- **Publication status:** dated public practitioner/research article authored by the project creator; not an independent validation source.

### D-2026-06 — GitHub repository metadata

- **Record:** GitHub REST repository metadata for `UncertaintyArchitectureGroup/The-Subprime-Code-Crisis`
- **Repository owner:** Uncertainty Architecture Group
- **Repository:** `The-Subprime-Code-Crisis`
- **Documented creation timestamp:** `2026-02-06T17:16:44Z`
- **Canonical public record:** https://api.github.com/repos/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis
- **Publication status:** platform metadata for the public repository; establishes the repository object's creation timestamp, not the date on which every underlying idea was first developed.

### D-2026-07 — February DOU Subprime Code publication

- **Author:** Vitalii Oborskyi
- **Title:** *Субпрайм-криза коду: чому AI-асистенти роблять нас повільнішими — і дані це доводять*
- **Publisher / host:** DOU
- **Published:** 2026-02-10 08:40, as displayed by DOU
- **Canonical public page:** https://dou.ua/forums/topic/57846/
- **Publication status:** dated public practitioner/research article authored by the project creator; not an independent validation source.

## Documentary purpose

The sources answer a narrow provenance question: **what public record exists for the development of this project's own delivery-system formulation, and by what dates?**

They are not used as evidence that the Subprime Code Crisis mechanism is empirically true. Empirical and theoretical support for the report remains governed by the other sources in the Evidence Library.

## Documented facts

### 1. The core delivery-system mechanism predates the repository

The 2026-01-05 DOU article already contains, before this repository existed, several ideas that later became central to the repository:

1. AI makes syntax generation unusually cheap while architecture, dependency management, business-logic fit, verification, and maintenance remain costly.
2. Faster generation can increase technical-debt accumulation rather than delivery value.
3. Code-generation capacity and human reading/review capacity become asymmetric.
4. Senior engineers can become overloaded by generated output requiring validation and debugging.
5. Individual output can rise while team delivery speed falls because review becomes a bottleneck.
6. Local activity or perceived productivity should not be equated with Value Stream acceleration.

The January article therefore provides a public precursor formulation of the repository's later delivery-system argument. It does not use the later project title **The Subprime Code Crisis**.

### 2. The January discussion is part of the documented development path

DOU preserves dated author comments under the January article. In those discussions Oborskyi further distinguishes generated volume from Value Stream improvement, describes review and debugging as places where writing-time savings can be lost, and frames AI assistance as a multiplier whose safety depends on expert validation.

The later 2026-02-10 article explicitly states that both work on the earlier article and discussions with readers caused the author to examine the available evidence more closely, and describes the new article as a logical continuation of that work.

This establishes a documented author-reported development relationship from the precursor article and its discussion to the later Subprime Code synthesis. It does not reconstruct every influence or establish that every later formulation was present in every January comment.

### 3. The public repository existed before the February DOU publication

GitHub's repository metadata records `created_at = 2026-02-06T17:16:44Z` for `UncertaintyArchitectureGroup/The-Subprime-Code-Crisis`.

The DOU Subprime Code article was published on 2026-02-10. The public chronology is therefore:

```text
2026-01-05  DOU precursor article
      ↓
January 2026 DOU discussion and refinement
      ↓
2026-02-06  public GitHub repository created
      ↓
2026-02-10  DOU Subprime Code article published
```

The GitHub timestamp establishes repository-object creation, not when private drafting or every component idea first existed.

### 4. The February article connects the formulation to the repository

The 2026-02-10 article publicly documents the mature Subprime Code formulation. It:

- frames the problem as a system-level delivery problem rather than merely code-generation quality;
- distinguishes subjective/local coding speed from end-to-end delivery outcomes;
- identifies review as a downstream bottleneck under increased AI-generated change volume;
- describes a mismatch between generation volume and verification capacity;
- presents deferred review, rework, maintainability, and operating cost as the mechanism behind the crisis framing; and
- explicitly identifies the article as an adaptation of the first chapters of the open GitHub report *The Subprime Code Crisis*.

The article therefore creates a dated externally hosted attribution edge among **Vitalii Oborskyi**, **The Subprime Code Crisis**, the GitHub repository, and **Uncertainty Architecture Group**.

## Formulation fingerprint

For provenance purposes, the public January-to-February development path can be summarized as the following project-authored systems formulation:

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

The January article documents substantial elements of this chain before the repository existed; the February article states the developed synthesis explicitly and ties it to the GitHub report.

This is **repository interpretation / systems formulation** documented by dated public records. The records establish public articulation and provenance, not universal causal validity.

## Repository interpretation

Together, the records support the following bounded provenance statement:

> The repository's attributable delivery-system synthesis has an inspectable public precursor in Vitalii Oborskyi's 2026-01-05 DOU article and ensuing discussion, followed by creation of the public GitHub repository on 2026-02-06 and explicit publication of the Subprime Code synthesis on DOU on 2026-02-10.

This is deliberately different from a claim of phrase ownership. Earlier third-party uses of **Subprime Code** and **The Subprime Code Crisis** remain visible in the separate terminology-provenance record. Phrase provenance and analytical provenance are different questions.

## What these sources do not establish

These sources do **not** establish:

- that Vitalii Oborskyi coined **Subprime Code**, **Subprime Code Crisis**, or **The Subprime Code Crisis**;
- that the repository was the first public work to compare AI-generated code with subprime finance or technical debt;
- that no earlier private, deleted, unindexed, or differently worded delivery-system analysis existed;
- that the repository influenced Richard Ewing, Nick Vigier, Igor Światowski, or any other author;
- that later overlapping formulations were derived from this project;
- that similarity proves copying or appropriation;
- that a GitHub creation date is the first date on which the underlying ideas existed;
- that DOU independently validated the articles' analytical or empirical claims merely by hosting them;
- that the complete systems mechanism is a directly measured causal chain; or
- trademark ownership or legal priority in a product or service name.

## Limitations and conflicts

- D-2026-05 and D-2026-07 are authored by the project creator and therefore have a direct authorship interest. They are strong timestamped provenance records but not independent validation.
- The statement that January discussion contributed to the later work is supported by the February article's retrospective author account. It should be treated as documented author provenance, not independently observed intellectual history.
- DOU publication metadata is a platform record and may be reformatted or migrated; the currently inspected pages are the operative public surfaces.
- D-2026-06 establishes repository-object creation, not private intellectual development or first publication of every component idea.
- Search indexes and platform records are not complete historical archives.

## Claim-to-source trace

| Repository statement | Source | Relationship | Boundary |
| --- | --- | --- | --- |
| The delivery-system mechanism had a public precursor before the repository | D-2026-05 | Documentary provenance | Establishes January wording and argument, not phrase coinage |
| Reader discussion contributed to the follow-up investigation | D-2026-07, with the DOU comment record around D-2026-05 | Documentary author account | Does not reconstruct every influence |
| Public repository object existed by 2026-02-06T17:16:44Z | D-2026-06 | Platform documentary record | Creation timestamp only |
| Oborskyi publicly documented the explicit Subprime Code formulation by 2026-02-10 | D-2026-07 | Documentary provenance | Public formulation, not independent validation |
| The February publication explicitly links the synthesis to the GitHub report | D-2026-07 | Documentary attribution | Establishes the publication-to-repository edge only |

## Repository locations using the sources

- `TERMINOLOGY_AND_ATTRIBUTION.md` — project-analysis provenance and chronology boundary.
- `README.md` — concise reader-facing provenance edge adjacent to citation guidance.
- `REFERENCES.md` — human-readable documentary bibliography.

No report chapter or operational protocol currently relies on these sources for empirical support.

## Repository integration audit

- **Integration status:** In progress
- **Repository search completed:** Yes — searched author identity, project title, repository creation date, DOU precursor wording, and provenance references.
- **Report mentions checked:** Yes — no report claim requires D-2026-05, D-2026-06, or D-2026-07 as empirical support; no report change proposed.
- **Numeric claims checked:** Yes — only publication dates and the GitHub creation timestamp are introduced by these documentary records.
- **README claims and diagrams checked:** Yes — planned use is limited to provenance/citation guidance; Key Takeaways, Claim confidence map, Evidence Map logic, and Crisis Map semantics remain unchanged.
- **Protocol outcome:** No protocol change.
- **Corrections made:** Added the precursor → discussion → repository → explicit publication lineage and separated analytical provenance from phrase origin and independent validation.
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
