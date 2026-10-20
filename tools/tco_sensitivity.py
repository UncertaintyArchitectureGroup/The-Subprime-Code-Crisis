#!/usr/bin/env python3
"""Reproduce explicitly hypothetical cash/capacity scenarios, not empirical ROI."""

import argparse
from decimal import Decimal, InvalidOperation
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUTS = REPO_ROOT / "report/appendices/tco-scenarios.json"


def number(row, key, *, signed=False):
    value = row[key]
    if isinstance(value, bool):
        raise ValueError(f"{key}: boolean is not a quantity")
    try:
        result = Decimal(str(value))
    except InvalidOperation as exc:
        raise ValueError(f"{key}: expected a finite decimal") from exc
    if not result.is_finite() or (not signed and result < 0):
        raise ValueError(f"{key}: invalid quantity")
    return result


def evaluate(row):
    seats = row["seats"]
    if type(seats) is not int or seats < 0:
        raise ValueError("seats: expected a nonnegative integer")
    monthly_price = number(row, "license_usd_per_seat_month")
    setup_cash = number(row, "new_external_setup_cash_usd")
    annual_cash = number(row, "new_annual_cash_usd")
    setup_hours = number(row, "existing_staff_setup_hours")
    annual_hours = number(row, "existing_staff_net_annual_hours_delta", signed=True)
    rate = number(row, "capacity_usd_per_hour")
    existing_pool = number(row, "existing_platform_annual_cost_pool_usd")
    allocation = number(row, "existing_platform_allocation_fraction")
    if allocation > 1:
        raise ValueError("existing platform allocation must be between zero and one")

    license_cash = seats * monthly_price * 12
    cash_y1 = license_cash + setup_cash + annual_cash
    cash_steady = license_cash + annual_cash
    capacity_y1 = (setup_hours + annual_hours) * rate
    capacity_steady = annual_hours * rate
    amounts = {
        "license_annual_usd": license_cash,
        "cash_increment_y1_usd": cash_y1,
        "cash_increment_steady_year_usd": cash_steady,
        "capacity_delta_y1_usd": capacity_y1,
        "capacity_delta_steady_year_usd": capacity_steady,
        "cash_plus_capacity_delta_y1_usd": cash_y1 + capacity_y1,
        "cash_plus_capacity_delta_steady_year_usd": cash_steady + capacity_steady,
        "existing_platform_allocation_memo_usd": existing_pool * allocation,
    }
    # Round only displayed amounts, in cents, using Decimal's half-even rule.
    return {"id": row["id"], **{k: format(v, ".2f") for k, v in amounts.items()}}


def reproduce(inputs):
    if inputs["currency"] != "USD" or inputs["model_version"] != 1:
        raise ValueError("expected model version 1 and USD inputs")
    if inputs["input_status"] != "hypothetical_not_empirical_estimates":
        raise ValueError("inputs must declare their hypothetical status")
    rows = inputs["scenarios"]
    ids = [r["id"] for r in rows]
    if not rows or any(not isinstance(i, str) or not i for i in ids) or len(ids) != len(set(ids)):
        raise ValueError("scenario IDs must be nonempty and unique")
    return {
        "model_version": 1,
        "currency": "USD",
        "status": "illustrative_cash_and_capacity_deltas_not_total_tco_or_roi",
        "results": [evaluate(row) for row in rows],
    }


def render(inputs):
    return json.dumps(reproduce(inputs), indent=2, ensure_ascii=False) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", type=Path, default=DEFAULT_INPUTS)
    parser.add_argument("--check", type=Path, help="fail if a committed JSON result differs")
    args = parser.parse_args()
    try:
        result = render(json.loads(args.inputs.read_text(), parse_float=Decimal))
        if args.check:
            if args.check.read_text() != result:
                parser.error("published results differ; regenerate from reviewed inputs")
            print("Hypothetical scenario results reproduce; economic assumptions remain subject to review.")
        else:
            print(result, end="")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
