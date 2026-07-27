# Writing Code vs. Shipping Code

> **Navigation:** [🏠 Home](../README.md) | [📉 Part 1: The Illusion](01_the_illusion.md) | [⚙️ Part 2: Broken Mechanics](02_broken_mechanics.md) | [📚 Evidence Brief](../evidence/primary/2026-writing-code-vs-shipping-code.md)

AI coding tools can produce large gains at the code-writing layer without producing proportional gains in shipped or used software. The relevant question is therefore not only how quickly code is generated, but how much of that upstream gain survives the full production chain.

```text
Generated code
      ↓
   Commits
      ↓
Pull requests
      ↓
  Releases
      ↓
Customer value
```

NBER Working Paper 35275 studies this distinction using data on more than 100,000 GitHub developers, AI-usage telemetry, public GitHub activity, and four application marketplaces. The authors report large increases in coding activity after adoption of successive generations of AI tools, but much smaller increases at higher production layers.

For the cumulative generation that includes asynchronous agents, the reported effect is approximately:

- **+180% commits**;
- **+50% distinct projects or repositories touched**;
- **+30% releases**.

For specific generations, the same attenuation pattern appears:

- autocomplete: **+228.2% lines changed**, **+35.9% commits**, **+10.2% releases**;
- synchronous agents: **+741.3% lines changed**, **+65.5% pull requests**, **+20.3% releases**.

These values come from specific matched event-study samples and specifications. They are evidence of a measured gradient across production stages, not universal constants for every team or organization.

## Production attenuation

The evidence shows that upstream activity is not equivalent to final output. Each downstream stage requires additional work: integration, review, coordination, testing, release management, distribution, discovery, and adoption. When those stages do not scale with code generation, part of the upstream gain is absorbed before it reaches users.

The paper also reports that new-application supply increased across major marketplaces while total usage within the first three months did not increase. This does not prove that individual AI-assisted applications lack value. It does show that more software entering marketplaces did not yet produce a proportional expansion in measured aggregate usage.

> **Architecture insight**
>
> AI scales code generation faster than most organizations scale verification, integration, release, and adoption capacity. Metrics such as generated lines, accepted suggestions, or commits can therefore overstate delivered value.

## What this evidence establishes

The study supports claims that:

- AI-tool adoption can substantially increase upstream coding activity;
- measured gains attenuate between code production and shipped output;
- downstream human work remains complementary to AI-generated output;
- releases and usage are necessary outcome measures alongside code-production metrics.

## What it does not establish

The study does not by itself prove that:

- AI-generated code is generally lower quality than human-written code;
- AI adoption reduces productivity in every organization;
- all additional commits, pull requests, or releases are waste;
- review is the only downstream bottleneck;
- AI coding tools cause technical debt, security defects, or maintenance failure.

Those claims require separate evidence. The full source assessment, methodology, caveats, and interpretation boundaries are documented in the [NBER evidence brief](../evidence/primary/2026-writing-code-vs-shipping-code.md).
