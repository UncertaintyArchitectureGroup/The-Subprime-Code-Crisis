# Production Attenuation, Complementary Human Capital, and the Verification Bottleneck

> **Navigation:** [🏠 Home](../README.md) | [📉 Part 1: The Illusion](01_the_illusion.md) | [Writing Code vs. Shipping Code](01a_writing_code_vs_shipping_code.md) | [⚙️ Part 2: Broken Mechanics](02_broken_mechanics.md) | [📚 Evidence Brief](../evidence/primary/2026-writing-code-vs-shipping-code.md)

The mechanics of the Subprime Code Crisis are easier to understand when software delivery is treated as a production hierarchy rather than a single coding task.

```text
Generated output
      ↓
     Files
      ↓
    Commits
      ↓
Pull requests
      ↓
   Projects
      ↓
   Releases
      ↓
 Usage and realized value
```

Every layer combines upstream artifacts with additional effort. More code is useful only when teams can still review, integrate, test, release, operate, and improve it.

## Production Attenuation

**Production attenuation** is the reduction in measured productivity gain as work moves from upstream code generation toward shipped and used software.

NBER Working Paper 35275 reports a steep gradient across this hierarchy. For autocomplete, the estimated gain falls from **+228.2% in lines changed** to **+35.9% in commits** and **+10.2% in releases**. For synchronous agents, the measured effect falls from **+741.3% in lines changed** to **+65.5% in pull requests** and **+20.3% in releases**.

The relevant interpretation is not that downstream work destroys value. Downstream stages convert raw output into coherent and usable software. Attenuation appears when their capacity does not grow in proportion to upstream generation.

This reframes the central productivity question:

> Not “How much more code can the tool produce?” but “What proportion of the additional output survives into releases and customer value?”

A delivery system can therefore show rising activity while its end-to-end conversion rate falls.

## Complementary Human Capital

The paper models upstream AI-generated output and downstream human effort as complementary inputs. Code cannot simply substitute for review, integration, architecture, release judgment, product validation, or user adoption.

The authors calibrate a hierarchical production model and report an estimated elasticity of substitution of approximately **0.25** between upstream output and downstream human effort. Because this value is well below one, their model places the relationship in the complements region: abundant upstream output cannot easily replace limited downstream human capacity.

This value must be described precisely:

- it is **model-calibrated**, not directly observed;
- it is fitted to the paper’s autocomplete attenuation pattern;
- it depends on a stylized hierarchical production model;
- it is not a universal constant for software organizations;
- it does not imply that exactly 25% of AI output survives or that human effort contributes exactly 25% of value.

The useful conclusion is qualitative: when production stages are complementary, scaling only one stage produces bounded system-level gains.

## The Verification Bottleneck

As code generation becomes cheaper, verification becomes relatively more scarce.

Verification includes more than code review. It spans:

- checking intent against requirements;
- architectural fit and dependency impact;
- security and privacy analysis;
- testing and failure investigation;
- integration with existing systems;
- release readiness and rollback planning;
- production observation and incident response;
- validation that users receive meaningful value.

AI agents can intervene at progressively higher layers, including producing commits and pull requests. But unless they also reduce the trusted effort required to evaluate those outputs, they can increase the amount of work arriving at the verification boundary faster than the boundary can process it.

This creates two failure modes:

1. **Queue growth.** Teams preserve verification depth, but cycle time, work in progress, and context loss increase.
2. **Verification dilution.** Teams preserve apparent velocity by spending less verification effort per unit, increasing the probability that defects and misunderstood behavior escape downstream.

The bottleneck is therefore not inherently “the senior engineer.” It is the total trusted verification capacity of the socio-technical system: people, automated tests, static analysis, architecture rules, release controls, observability, and feedback from production.

## Operational implication

Organizations should measure the conversion funnel rather than only the generation layer:

```text
Generated → Proposed → Reviewed → Merged → Released → Used
```

A rise in generated output is beneficial only when the downstream pass-through remains healthy. When pass-through declines, adding more generation capacity increases inventory and risk rather than throughput.

> **Architecture insight**
>
> The binding constraint is moving from authoring toward verification and integration. AI adoption should therefore be capacity-aware: generation should scale only alongside the controls and human judgment required to turn generated artifacts into trusted outcomes.

## Evidence boundaries

The NBER study directly supports the existence of cross-layer attenuation and provides model-based evidence of complementarity. It does **not** independently establish lower code quality, higher defect rates, technical debt, security failures, or reviewer burnout. Those mechanisms require separate sources and should not be attributed to this paper alone.

See the [full evidence brief](../evidence/primary/2026-writing-code-vs-shipping-code.md) for methodology, limitations, and claims the source does not establish.
