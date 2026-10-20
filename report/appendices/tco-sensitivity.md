# Conditional cost sensitivity for an AI-assisted delivery pilot

[Chapter 2](../01_the_illusion.md#chapter-2-evaluating-the-cost-of-ai-assisted-delivery) · [Historical source context](cost-context.md) · [Inputs](tco-scenarios.json) · [Reproduced results](tco-results.json)

**Status: hypothetical sensitivity example, without empirical calibration.** Every numerical
input is an invented assumption. Cases A/B/C are not estimates, confidence
intervals, recommended budgets, calibrated probabilities or a low/most-likely/high
forecast. The former $7–27M transformation benchmark and universal 30–120-times
ratio are withdrawn. These examples do not validate them under another label.

## Define the comparison before counting costs

Compare a specified use case with its credible no-tool alternative over the same
period, workload and quality boundary. Record existing capability, paid seats,
active use, contract/usage charges and new work actually needed. A team reusing
an effective platform may need little new setup; another may incur substantial
integration or verification work. Neither is established by corporate R&D totals.

This calculator shows **gross additional cash** and a separate **capacity-valued
engineering-time delta**. It does not compute the full baseline TCO, business
benefit, defects, risk loss or ROI. To assess total economics, combine a compatible
baseline and measured deltas, then evaluate delivered benefits and quality. Do
not add a cash-only baseline to a capacity-valued result without reconciling the
basis.

The cash calculation assumes **zero avoided baseline expenditure**. Retired
licenses, cancelled contracts and other cash reductions are excluded; subtract
independently established reductions before interpreting a local net cash change.
The JSON `cash_increment_*` fields hold these gross additions under that
assumption. Combining them with capacity value does not account for omitted cash
reductions or delivered business benefits.

## Parameters and accounting boundary

All amounts are USD; each displayed model year has 12 paid months. Steady year
means a later 12-month year under unchanged assumed prices, seats and recurring
work. It is not a forecast of renewal prices or the first year's actual rollout.

| Symbol / input | Unit and meaning | Treatment |
| --- | --- | --- |
| N / seats | Paid seats, not active users or measured adoption | 1,000 in each toy case |
| p / license price | USD per paid seat/month | Assumed $20; **not a current or historical vendor quote/plan** |
| U / new external setup cash | One-time additional cash, beyond the no-tool alternative | Year 1 only; excludes already-funded staff time valued below |
| O / new annual cash | Additional annual usage/infrastructure/contracts or new paid labor | Each year; excludes license and costs already counted in U or staff-hour deltas |
| S / existing staff setup | One-time diverted hours of already-funded staff | Capacity use, not an extra payroll bill; Year 1 only |
| H / existing staff recurring delta | Annual net hours versus baseline, across coding/review/test/rework/operations | Positive = more effort, negative = released capacity; excludes S and paid work already in U/O |
| w / capacity valuation | Assumed USD per existing-staff hour | $75 in toy cases; opportunity-cost sensitivity, not an observed wage or guaranteed realizable saving |
| B × a / existing platform allocation | Existing annual cost pool times an allocated fraction | **Memo only**, already present in baseline; never added to the incremental results |

If a new hire/contractor is costed in O, do not also value those same paid hours
in H. A net hours input must cover saved coding time as well as added review and
maintenance within the defined boundary; counting only burdens would bias it.
Released hours are not automatically reduced payroll or useful extra delivery.
Realized savings or benefits require evidence that the freed capacity was used or
the cash cost avoided.

## Formulas

Let annual license cash `L = 12 × N × p`.

- First-year gross additional cash: `C1 = L + U + O`.
- Steady-year gross additional cash: `Cs = L + O`.
- Capacity-valued deltas: `V1 = w × (S + H)`; `Vs = w × H`.
- Optional cash-plus-capacity comparison: `D1 = C1 + V1`; `Ds = Cs + Vs`.
- Existing allocated cost memo: `M = B × a`, excluded from C/V/D.

Negative D indicates released capacity valued above new cash **under the toy
assumptions**; it is not cash profit or positive ROI. No licensing percentage or
universal multiplier is inferred. Any later per-seat/ratio presentation must name
its denominator; the license formula explicitly uses paid seats and months.

## Inspectable hypothetical inputs

| Input | A: reuse and released capacity | B: setup, flat recurring effort | C: setup and added effort |
| --- | --- | --- | --- |
| Paid seats / price / months | 1,000 / $20 / 12 | 1,000 / $20 / 12 | 1,000 / $20 / 12 |
| U, external one-time cash | $20,000 | $150,000 | $800,000 |
| O, additional annual cash | $30,000 | $90,000 | $250,000 |
| S, existing staff setup hours | 1,000 | 3,000 | 10,000 |
| H, net recurring hours/year | −6,000 | 0 | +12,000 |
| w, assumed capacity value/hour | $75 | $75 | $75 |
| B / a, existing allocation memo | $3,000,000 / 5% | $3,000,000 / 5% | $3,000,000 / 5% |

These cases deliberately include benefits and burdens without assigning relative
likelihood. They are not scaled from Menlo, CloudZero, GitClear or issuer filings.
Replace them with local evidence before using the model for a decision.

## Reproduced outputs

| Conditional output | A | B | C |
| --- | --- | --- | --- |
| Annual license cash L | $240,000 | $240,000 | $240,000 |
| First-year gross additional cash C1 | $290,000 | $480,000 | $1,290,000 |
| Steady-year gross additional cash Cs | $270,000 | $330,000 | $490,000 |
| First-year capacity value V1 | −$375,000 | $225,000 | $1,650,000 |
| Steady-year capacity value Vs | −$450,000 | $0 | $900,000 |
| Cash plus capacity D1 | −$85,000 | $705,000 | $2,940,000 |
| Cash plus capacity Ds | −$180,000 | $330,000 | $1,390,000 |
| Existing allocation M, memo only | $150,000 | $150,000 | $150,000 |

The outputs are arithmetic consequences of inputs, not evidence of typical
enterprise costs. Year-1 and steady-year results keep setup from recurring.
Amounts are computed in decimal arithmetic and displayed to cents, using
half-even rounding; the table uses whole dollars because these inputs produce
integer amounts.

## Reproduction and validation

From the repository root, with Python standard library only:

```bash
python3 tools/tco_sensitivity.py
python3 tools/tco_sensitivity.py --check report/appendices/tco-results.json
python3 -m unittest tests.test_tco_sensitivity
```

The [calculator](../../tools/tco_sensitivity.py) reads the committed input JSON;
the committed output JSON is checked by a test for drift. Tests separately check
a hand-calculated fixture, one-time/recurring separation, allocation exclusion,
signed time savings, zero seats and invalid inputs. Tests validate implementation
and reproduction, not economic assumptions or deployment outcomes.

## Evaluation limits

1. Numerical examples are optional analytical aids; keeping them is an editorial
   judgment, not a result established by passing tests.
2. Accept or revise the cash/capacity boundary, baseline comparator, omitted
   benefits/risks and treatment of reused infrastructure. Demand evidence before
   any real-world calibration or conversion of capacity into cash savings.
3. Judge whether Ch2's conditional conclusion and the appendix placement are
   proportionate to the originals. No universal minimum transformation or ROI
   effect follows from the example.

For a real decision, obtain local inputs and examine sensitivity to baseline,
quality, workload, prices and the realization of benefits before drawing an
economic conclusion.
