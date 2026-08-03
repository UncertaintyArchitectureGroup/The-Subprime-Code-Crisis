# Repository Scope

## Status and precedence

This document is the dedicated subject-boundary reference for *The Subprime Code Crisis*: what the repository studies, what it does not attempt to establish, and how adjacent topics may be used. It expands the purpose and boundary principles in [`AGENTS.md`](AGENTS.md) and [`DOCTRINE.md`](DOCTRINE.md) without overriding them.

[`AGENTS.md`](AGENTS.md) remains canonical for workflows, approval, source states, verification, contributor obligations, and repository-level purpose and boundaries. [`DOCTRINE.md`](DOCTRINE.md) defines research and interpretation principles. [`GLOSSARY.md`](GLOSSARY.md) defines canonical terminology. [`ARTIFACT_MODEL.md`](ARTIFACT_MODEL.md) provides the dedicated reader-facing artifact map.

This scope does not determine whether a factual claim is true, create evidence status, or override original sources. It limits the questions the repository is intended to answer.

## Core research question

> How does AI-assisted software development change the end-to-end software-delivery system, and what evidence, mechanisms, risks, and operating controls are needed to govern that change responsibly?

The unit of analysis is the complete delivery system rather than code generation alone.

## In scope

| Area | Included questions and artifacts |
| --- | --- |
| **AI-assisted software development** | Code assistants, coding agents, autonomous or semi-autonomous implementation, review, testing, documentation, and related development workflows |
| **Delivery-system effects** | How local acceleration interacts with requirements, architecture, review, QA, security, integration, release, operations, maintenance, and product adoption |
| **Local productivity and throughput** | Distinctions among generated output, task completion, commits, pull requests, releases, production use, customer value, reliability, and total delivery cost |
| **Verification capacity** | Human and automated capacity to understand, review, test, secure, integrate, release, operate, and maintain candidate changes |
| **Software quality and maintainability** | Defects, rework, churn, duplication, complexity, architecture fit, security exposure, operational stability, and maintenance burden when tied to AI-assisted delivery |
| **Human and organizational effects** | Reviewer load, skill development, accountability, incentives, team composition, decision rights, adoption pressure, and operating-model changes |
| **Economic and ROI implications** | Costs, benefits, bottleneck transfer, infrastructure requirements, and downstream cost exposure when directly connected to software delivery |
| **Evidence and claim governance** | Source quality, evidence briefs, claim boundaries, contradictory evidence, confidence, terminology provenance, correction, and traceability |
| **Risk mechanisms and scenarios** | Bounded systems inferences, risk scenarios, warning scenarios, and conditions under which they may or may not emerge |
| **Operational responses** | Adaptable controls, metrics, gates, roles, escalation paths, disclosure practices, organizational policy, and feedback loops |
| **Implementation evidence** | Inspectable case studies, measured pilots, failures, corrections, replications, and operational feedback relevant to the repository's claims or protocols |

## Out of scope

| Area | Boundary |
| --- | --- |
| **General AI or AGI safety** | Alignment, existential risk, consciousness, geopolitical competition, and broad societal effects are outside scope unless a narrowly defined connection to software-delivery risk is necessary |
| **General enterprise AI transformation** | AI use in sales, marketing, finance, HR, customer service, or other functions is outside scope unless it directly changes software-delivery systems |
| **Model architecture and training research** | Training methods, scaling laws, hardware, token economics, and benchmark leadership are not studied for their own sake; they may appear only when they materially affect software-delivery claims |
| **Tool tutorials and prompt collections** | The repository is not a coding tutorial, prompt library, IDE guide, or catalogue of agent configurations |
| **Vendor rankings or procurement recommendations** | It does not rank vendors, declare one tool universally safest, or recommend purchases without a defined delivery context and inspectable evidence |
| **Universal bans or universal adoption mandates** | It does not argue that all AI-generated code should be prohibited or that every organization should adopt the same operating model |
| **Definitive macroeconomic forecasts** | Financial-crisis analogies and industry-wide collapse outcomes remain metaphors or scenarios, not established forecasts or investment advice |
| **Legal, regulatory, or compliance advice** | Laws, standards, and regulatory obligations may be documented as context, but the repository does not provide legal advice or certify compliance |
| **General software-engineering doctrine** | Topics unrelated to AI-assisted delivery are not included merely because they are important software-engineering practices |
| **Confidential investigations** | Proprietary code, undisclosed client information, private organizational allegations, and non-consensual personal data are not repository evidence |

## Adjacent-topic rule

An adjacent topic may be included only when all of the following are true:

1. it has a direct and stated relationship to an in-scope research question;
2. the relationship is bounded rather than implied through rhetoric or analogy;
3. material factual claims follow the evidence and source-processing rules in `AGENTS.md`;
4. the topic does not silently expand the repository into a general AI, economic, legal, or management framework; and
5. removing the adjacent material would materially weaken the reader's ability to understand the in-scope claim, mechanism, or protocol.

Examples:

- model capability data may be relevant when it changes the scale or autonomy of software work that requires verification;
- company spending may be relevant when it supports a bounded claim about the infrastructure surrounding AI-assisted delivery;
- labor or organizational research may be relevant when it directly addresses review capacity, role changes, accountability, or delivery outcomes.

## Scope boundaries for claims

- **In scope does not mean established.** A topic may fall within the repository boundary while the evidence remains weak, mixed, or absent.
- **Out of scope does not mean false or unimportant.** It means the repository is not the appropriate place to establish or govern that topic.
- **A metaphor does not expand scope.** Mortgage, bubble, bankruptcy, crash, and collapse language does not authorize claims about financial markets or inevitable macroeconomic outcomes.
- **A protocol does not expand the evidence claim.** Practical controls may address plausible risks, but their existence does not prove those risks universally present.
- **One organization does not define the industry.** Case studies and internal measurements remain bounded by their context.
- **One tool generation does not define all AI-assisted development.** Claims must preserve tool, model, workflow, population, period, and task boundaries where material.

## Intended audience

The repository is written primarily for:

- engineering and technology executives;
- software architects and senior engineers;
- delivery, program, and product leaders;
- QA, security, platform, and operations leaders;
- researchers studying AI-assisted software development;
- organizations designing measurable and reversible adoption programs.

The repository may be useful to investors, policymakers, educators, and vendors, but it does not replace domain-specific financial, legal, policy, or academic analysis.

## Scope change discipline

A substantive expansion or contraction of scope requires explicit maintainer approval, a reviewable change, synchronization with `AGENTS.md`, `DOCTRINE.md`, `README.md`, `ARTIFACT_MODEL.md`, and `GLOSSARY.md` where applicable, and independent review under `AGENTS.md`.

Do not broaden the scope merely because a related topic is popular, rhetorically useful, or available as a source. New evidence should improve the repository's answer to its core question rather than turn the repository into a general catalogue of AI concerns.