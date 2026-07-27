# Evidence discovery playbook

This playbook is a mandatory procedural extension of [`AGENTS.md`](../AGENTS.md) for Flow E. `AGENTS.md` is canonical and has precedence; resolve conflicts in its favor. Read it in full before this playbook. Flow E is discovery, not evidence acceptance, and cannot directly change report claims, protocols, source statuses, confidence classifications, or repository maps.

## 1. Search Strategy

Before searching, create a written strategy that records:

- the repository claim, evidence gap, uncertainty, or topic being investigated;
- the purpose of the search: freshness, contradiction testing, replication search, gap filling, or broader landscape review;
- the search date and freshness window;
- databases, indexes, repositories, institutional sites, and other channels to search;
- representative queries and terminology variants;
- target evidence types and publication periods;
- populations, tasks, tools, outcomes, and settings of interest;
- known blind spots and expected search limitations.

Use multiple query families that deliberately seek positive, negative, null, mixed, contradictory, replication, and critique evidence. A search designed only to confirm the repository thesis is invalid.

Prioritize original and inspectable sources:

1. peer-reviewed journals and conference proceedings;
2. authoritative preprint repositories;
3. original institutional or laboratory publications;
4. official datasets, filings, standards, and technical reports;
5. credible industry research with inspectable methods;
6. secondary synthesis and practitioner commentary for discovery only.

Record enough detail for another reviewer to rerun representative searches.

## 2. Inclusion

Define inclusion criteria before candidate selection. Criteria should address:

- direct or material relevance to the search question;
- identifiable authorship or responsible publishing entity;
- accessible abstract, methods, dataset description, or full text sufficient for screening;
- clear publication date and version;
- identifiable population, task, intervention or exposure, comparator, and outcome where applicable;
- evidence type allowed by the search strategy;
- time period and language boundaries;
- minimum methodological transparency appropriate to the source type.

A source may be included for contradiction, limitation, replication, context, or null results. Inclusion does not mean that the source supports the repository thesis.

## 3. Exclusion

Define exclusion criteria before final screening. Common reasons include:

- duplicate or derivative reporting when an original source is available;
- promotional material without inspectable methods or underlying evidence;
- inaccessible claims that cannot be checked beyond a search snippet;
- unclear authorship, date, version, or source identity;
- irrelevance to the defined population, task, outcome, or repository claim;
- commentary presented as empirical evidence;
- superseded versions when the authoritative version is available;
- unverifiable numbers or claims with no traceable source;
- material methodological opacity that prevents even bounded interpretation.

Do not exclude a source merely because it is unfavorable, null, contradictory, industry-funded, a preprint, or produced by a vendor. Record the concern and assess it explicitly.

Every excluded candidate in a claim-critical or systematic search must retain an exclusion reason in the Candidate Register.

## 4. Research Entity Assessment

For every candidate that survives initial screening, identify:

- authors and affiliations;
- laboratory, university, company, consortium, standards body, public agency, or other responsible entity;
- whether the entity created, owns, sells, funds, administers, or controls the studied product, platform, benchmark, or dataset;
- prior relevant research or publication record when material;
- disclosed advocacy, policy, commercial, or institutional position;
- independence of data collection and analysis where determinable.

Entity reputation is context, not evidence quality. A prestigious institution does not cure weak methods, and a commercial affiliation does not automatically invalidate results.

## 5. Publication Status

Record the exact publication state:

- working paper;
- preprint;
- submitted manuscript;
- accepted manuscript;
- peer-reviewed conference paper;
- peer-reviewed journal article;
- institutional report;
- technical report;
- dataset or data release;
- standard, filing, or other documentary source;
- correction, retraction, expression of concern, or superseded version.

Verify peer-review claims from the publisher or venue when practical. An arXiv, SSRN, DOI, repository page, or conference upload does not by itself establish peer review.

Publication status affects confidence and review depth but is not a binary acceptance rule.

## 6. Funding

Record:

- disclosed funders and grant identifiers;
- employer sponsorship or internal company research;
- provision of tools, compute, data, recruitment, or researcher access;
- funder role in study design, analysis, publication, or approval;
- absence of a funding statement when one would normally be expected;
- whether the measured vendor or platform financed the work.

Funding is a risk and context signal, not an automatic reason for inclusion or exclusion.

## 7. Conflicts

Record disclosed and reasonably identifiable conflicts, including:

- employment, consulting, equity, patents, advisory roles, or vendor relationships;
- ownership or commercial interest in the evaluated product or method;
- control over the measured dataset or benchmark;
- advocacy or policy commitments directly related to the conclusion;
- publication approval rights or contractual restrictions;
- conflicts declared absent by the authors;
- conflicts that remain unknown.

Separate documented conflicts from repository inference. Do not imply misconduct without evidence.

## 8. Scope

For each candidate, state the exact evidence boundary:

- population and experience level;
- sample size and selection mechanism;
- task type, duration, and complexity;
- tool, model, version, configuration, and access conditions;
- study or operational setting;
- comparator or baseline;
- observation period;
- outcomes and metric definitions;
- causal, experimental, quasi-experimental, observational, documentary, or theoretical design;
- unit of analysis;
- what the source directly establishes;
- what the source does not establish.

Title, abstract, or headline similarity is insufficient for scope classification.

## 9. External Validity

Assess whether and how the source may generalize beyond its observed setting. Examine:

- representativeness of participants, organizations, tasks, tools, and environments;
- artificial or benchmark conditions versus production work;
- short-term measurement versus maintenance and lifecycle effects;
- individual activity versus team, delivery-system, organizational, industry, or economic outcomes;
- differences between novice, intermediate, and expert populations;
- model, product, and workflow version dependence;
- selection, survivorship, novelty, and observer effects;
- geographic, organizational, and regulatory boundaries;
- whether claimed generalization exceeds the measured unit of analysis.

Record external validity as a bounded assessment, not a single quality score. A narrow study may be rigorous and still support only a narrow claim.

## 10. Replication

Search explicitly for:

- direct replications;
- conceptual replications;
- independent reanalyses;
- corrections and critiques;
- contradictory studies using comparable outcomes;
- follow-up studies with different populations, tools, tasks, or periods;
- repeated findings from the same authors or organization;
- evidence that the result has not yet been independently tested.

Record whether replication is independent, partial, failed, mixed, contested, or unavailable. Repeated vendor or laboratory publications are not independent replication unless data collection and analysis are genuinely independent.

Replication status must inform candidate priority and later claim confidence, but absence of replication does not automatically exclude a new source.

## 11. Canonical Version

For every candidate:

- identify the canonical title, authors, date, identifier, and URL;
- distinguish preprint, accepted manuscript, published version, dataset, appendix, correction, summary, and commentary;
- prefer the latest authoritative version for review;
- preserve links and dates for materially different earlier versions;
- identify retractions, corrections, expressions of concern, and superseding publications;
- avoid registering the same research object as multiple independent sources;
- record when no authoritative canonical version can be established.

When versions materially differ, route the source through Flow C after registration or document the version relationship before Flow A begins.

## 12. Candidate Register

Maintain a Candidate Register for every claim-critical, systematic, or multi-source discovery task.

Each entry must contain:

| Field | Required record |
| --- | --- |
| Candidate ID | Temporary search identifier |
| Citation | Title, authors or entity, year |
| Canonical URL | Best current authoritative link |
| Canonical version | Version and publication state |
| Search provenance | Database, site, query, and search date |
| Relevance | Direct, adjacent, contextual, or not relevant |
| Relationship | May support, weaken, contradict, replicate, or contextualize |
| Inclusion result | Included, excluded, or held |
| Decision reason | Specific screening rationale |
| Research entity | Authors, affiliations, and responsible organization |
| Funding | Disclosed, absent, or unknown |
| Conflicts | Disclosed, inferred risk, none declared, or unknown |
| Scope | Population, task, tool, setting, period, and outcome |
| External validity | Main generalization boundaries |
| Replication | Independent, partial, failed, mixed, same-entity, or unavailable |
| Proposed routing | Flow A, Flow C, context only, hold, or reject |

Candidates must not disappear from the record because they are inconvenient, unfavorable, duplicated, or rejected. Deduplicate them while preserving the decision trail.

## 13. Candidate Decision and Routing

Assign exactly one provisional outcome:

- `Accept for Flow A` — a new evidence object warrants registration and full review;
- `Route to Flow C` — an existing registered source has a newer, corrected, peer-reviewed, or superseding version;
- `Hold` — potentially relevant but awaiting access, clarification, comparison, or authoritative publication;
- `Context only` — useful for terminology, landscape, or interpretation but not accepted as evidence for a material claim;
- `Reject` — does not meet inclusion criteria or meets an exclusion criterion.

For each accepted candidate, state which repository claim it may support, weaken, contradict, replicate, or contextualize. Acceptance into Flow A is not permission to cite the source in the report.

## 14. Independent Search Review

A second agent or reviewer that did not perform the primary search must independently:

- read the Search Strategy, Inclusion, and Exclusion criteria;
- rerun representative queries across more than one search channel;
- search specifically for omitted positive, negative, null, mixed, contradictory, replication, and critique evidence;
- verify a sample of excluded and held candidates;
- verify canonical versions and publication statuses;
- challenge Research Entity, Funding, Conflicts, Scope, External Validity, and Replication assessments;
- inspect Candidate Register completeness and deduplication;
- assess whether candidate routing follows the declared criteria.

Record one outcome:

- `Confirmed`;
- `Corrections required`;
- `Unresolved disagreement`;
- `Review unavailable`.

If corrections are required, update the search and Candidate Register, then repeat independent review. If disagreement remains or independent review is unavailable, escalate to the human user before accepting candidates.

For Flow E, Independent Search Review satisfies the repository-wide Independent Review requirement when it:

- reviews the complete Flow E output;
- is performed by a reviewer who did not conduct the primary search;
- uses the standard repository review outcomes;
- records the required review metadata.

A separate second reviewer is not required when the Independent Search Review already covers the complete Flow E output and meets these conditions.

Flow E is complete only when:

- the Search Strategy is recorded;
- Inclusion and Exclusion criteria are explicit;
- all screened candidates are traceable in the Candidate Register;
- canonical versions, publication status, research entity, funding, conflicts, scope, external validity, and replication are assessed for accepted candidates;
- candidate routing is explicit;
- Independent Search Review is `Confirmed`;
- unresolved disagreements and material omissions are absent.

Accepted new sources enter Flow A. Changed or superseding versions of registered sources enter Flow C. Flow E notes, abstracts, summaries, or Candidate Register entries do not substitute for registration, evidence review, an evidence brief, integration audit, or repository-wide verification.
