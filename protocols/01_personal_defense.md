# Protocol 1: The Personal Defense
## Verify Generated Changes Before Acceptance

> **Navigation:** [🏠 Home](../README.md) | [🧭 Doctrine](../DOCTRINE.md) | [📖 Glossary](../GLOSSARY.md) | [🛡️ Protocols Index](README.md) | **Protocol 1** | [Protocol 2: Operational Defense](02_operational_defense.md)

Here, **"vibe coding"** refers to accepting plausible generated output without adequate verification. This protocol addresses that risk; it does not estimate its prevalence or treat all AI-assisted work as equivalent.

The practices below propose boundaries for accepting changes. Adapt them to the work's risk and check their effectiveness in the local workflow.

---

## 1. The Containment Rule

Restrict AI-generated code according to the cost of failure, durability of the artifact, and depth of verification required. Do not let the model silently expand its role from syntax generation into architecture ownership.

### 🟢 Green Zone — low-cost and disposable

Use AI more freely where execution and outputs are isolated, easy to inspect, and inexpensive to discard. These examples assume effects are confined to disposable copies and isolated outputs:

- **Disposable scripts:** one-off parsing or local automation on disposable copies, with isolated outputs.
- **Data transformation:** converting JSON to SQL, mapping types, reshaping fixtures.
- **Boilerplate:** standard structures that already follow an accepted local pattern.
- **Unit-test scaffolding:** test structure and cases, with assertions reviewed manually.
- **Documentation drafts:** initial docstrings, examples, or internal notes.

### 🟠 Controlled Zone — useful, but review-bound

Use AI only with explicit references and mandatory verification:

- ordinary feature code;
- adapters and integration code;
- refactoring inside a well-understood module;
- test generation for existing behavior;
- repetitive changes across known patterns.

### 🔴 Protected Zone — human-owned decisions

Do not accept AI output without deep review and explicit accountability:

- **Core business logic:** algorithms that define the product's value or obligations.
- **Security controls:** authentication, authorization, encryption, secrets, validation.
- **State and concurrency:** transactions, distributed state, race conditions, retries.
- **Architecture:** service boundaries, data ownership, API contracts, platform choices.
- **Irreversible operations:** destructive migrations, financial operations, compliance logic.

---

## 2. Pattern: Disposable Boundary

### Intent

Keep model-generated output outside the durable system until it has been verified, adapted, and accepted by a responsible engineer.

### Problem

AI lowers the cost of producing plausible code. That makes it easy for provisional output to enter the permanent codebase or alter persistent state before anyone has established whether it fits the architecture, preserves invariants, or is worth maintaining.

### Pattern

Create an explicit boundary between **generated artifacts** and **accepted changes to durable code, data, or operational state**.

```mermaid
flowchart LR
    A[AI-generated artifact] --> B[Disposable boundary]
    B --> C[Verification]
    C --> D[Human adaptation]
    D --> E[Stable system]
    C -->|fails| F[Discard or regenerate]
```

Treat the artifact before the boundary as replaceable and keep its effects isolated. Applying its outputs or running it against persistent or shared state crosses the acceptance boundary, even if the script will be discarded afterward. Accepted effects remain owned.

### Suitable disposable zones

- throwaway prototypes;
- local scripts;
- generated examples;
- migration drafts;
- test scaffolds;
- candidate implementations in temporary branches;
- code produced only to explore an interface or failure mode.

### Protected core zones

- domain models and invariants;
- public interfaces;
- security-sensitive paths;
- shared libraries;
- long-lived abstractions;
- data schemas and migrations;
- operationally critical workflows.

### Required controls before crossing the boundary

1. The engineer can explain what the code does and why it exists.
2. Tests validate the relevant behavior, not merely line coverage.
3. The implementation fits an accepted local pattern or has an explicit reason not to.
4. Security, data integrity, failure handling, and recovery limits are understood. Stopping execution does not undo completed irreversible effects.
5. Duplicated functionality and unnecessary abstractions have been removed.
6. The code is small enough to review meaningfully.

### Example

A model generates a script that converts historical CSV exports into a new format. A rehearsal uses disposable copies and isolated outputs, with the transformation checked for edge cases. Before the script or its output changes persistent data, the responsible engineer applies the data-change risk class, validates the intended transformation, and accepts the recovery limits. Discarding the script afterward does not make those effects disposable. If the logic becomes a permanent import service, it also needs adaptation to the production architecture, tests, and review as durable code.

### Failure modes

- a prototype is promoted directly into production;
- generated abstractions become shared infrastructure without design review;
- temporary code acquires hidden consumers and can no longer be discarded;
- tests validate only the model's own assumptions;
- engineers confuse successful execution with architectural fitness.

### Why this matters for the Subprime Code Crisis

The proposed risk mechanism includes provisional output affecting durable code, data, or operations without adequate acceptance. A disposable boundary is intended to interrupt that path. Whether it reduces later rework or maintenance burden requires local evidence; the boundary does not guarantee correctness or prevent all debt.

---

## 3. Pattern: Reference-Bounded Adaptation

### Intent

Reduce model uncertainty by grounding changes in trusted local references instead of asking the model to invent a new solution from a broad prompt.

### Problem

A model can produce a locally plausible implementation that introduces a second architectural style, duplicates an existing mechanism, violates an implicit invariant, or ignores the organization's actual conventions.

### Pattern

Before asking for code, identify the accepted references that define the solution space.

```mermaid
flowchart LR
    A[Task] --> B[Select trusted references]
    B --> C[AI proposes bounded adaptation]
    C --> D[Verify behavior and fit]
    D --> E[Merge]
    D -->|does not conform| F[Revise or reject]
```

The model should adapt from known-good material rather than invent a new architectural answer whenever an accepted implementation already exists.

### Accepted reference types

- an existing implementation of the same pattern;
- an approved architecture decision record;
- coding and security standards;
- a known-good module;
- tests that express current behavior;
- an interface or schema contract;
- explicit non-functional constraints;
- a documented failure-handling pattern.

### Workflow

1. **Select the reference.** Identify the implementation, contract, test, or decision that should govern the change.
2. **State the adaptation boundary.** Explain what may change and what must remain invariant.
3. **Request a delta, not a reinvention.** Ask the model to adapt the reference to the new case.
4. **Compare structurally.** Review naming, error handling, dependencies, observability, and test shape against the reference.
5. **Verify independently.** Run tests and inspect behavior without relying on the model's explanation.
6. **Record justified deviations.** If the change intentionally breaks the pattern, make that decision explicit.

### Example

A team needs a new outbound API client. Instead of asking the model to "build a resilient client," the engineer provides the existing approved client, retry policy, telemetry conventions, interface contract, and tests. The model is asked to adapt that pattern to the new endpoint without introducing new dependencies or changing retry semantics.

### Failure modes

- using an outdated or already flawed reference;
- supplying too many conflicting references;
- treating superficial similarity as proof of correctness;
- copying a pattern into a context with different risk characteristics;
- allowing the model to alter hidden invariants while preserving the visible structure.

### Why this matters for the Subprime Code Crisis

Reference-bounded work is intended to make variation easier to compare, review and reject. A flawed reference or poor fit can preserve errors. Evaluate review effort, deviations and quality rather than assume the practice reduces defects or maintenance cost.

---

## 4. Skills for Verification and Maintenance

Develop the skills needed to evaluate, explain and maintain accepted changes alongside prompt fluency. This is professional-development advice, not a forecast of salaries or demand.

Focus on:

- system design;
- debugging and root-cause analysis;
- security;
- performance engineering;
- data integrity;
- testing strategy;
- operational failure analysis.

These skills matter because the professional value of an engineer is not the amount of syntax they can generate. It is their ability to make reliable decisions under incomplete information and accept responsibility for the result.

---

## 5. The Commitment

Adopt this stance:

> **"If I didn't read it, I didn't write it. If I don't understand it, I won't commit it. If I cannot verify it, it does not cross the boundary."**

Keep the accountable owner and acceptance evidence visible. A repository author field records attribution; it does not determine legal liability.

---

## Relationship to the protocol stack

```mermaid
flowchart TD
    A["Protocol 1: Engineer boundaries"]
    --> B["Protocol 2: Team controls"]
    --> C["Protocol 3: Evidence disclosure"]
    --> D["Protocol 4: Organizational control model"]
```

This protocol addresses the individual engineer's decision boundary. [Protocol 2](02_operational_defense.md) covers team controls, [Protocol 3](03_public_defense.md) evidence disclosure, and [Protocol 4](04_systemic_cure.md) organizational ownership and feedback.

---

**Next:** [📊 Protocol 2: The Operational Defense](02_operational_defense.md)
