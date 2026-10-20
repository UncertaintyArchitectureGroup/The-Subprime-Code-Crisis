"""Accounting-boundary and published-result checks for the illustrative model."""

import copy
import json
from pathlib import Path
import unittest

from tools.tco_sensitivity import DEFAULT_INPUTS, evaluate, render


class TcoSensitivityTests(unittest.TestCase):
    def setUp(self):
        self.row = {
            "id": "hand_computed",
            "seats": 2,
            "license_usd_per_seat_month": "10",
            "new_external_setup_cash_usd": "100",
            "new_annual_cash_usd": "60",
            "existing_staff_setup_hours": "2",
            "existing_staff_net_annual_hours_delta": "-4",
            "capacity_usd_per_hour": "50",
            "existing_platform_annual_cost_pool_usd": "10000",
            "existing_platform_allocation_fraction": "0.1",
        }

    def test_hand_computed_cash_and_capacity_are_separate(self):
        result = evaluate(self.row)
        self.assertEqual(result["license_annual_usd"], "240.00")
        self.assertEqual(result["cash_increment_y1_usd"], "400.00")
        self.assertEqual(result["cash_increment_steady_year_usd"], "300.00")
        self.assertEqual(result["capacity_delta_y1_usd"], "-100.00")
        self.assertEqual(result["cash_plus_capacity_delta_y1_usd"], "300.00")
        self.assertEqual(result["cash_plus_capacity_delta_steady_year_usd"], "100.00")

    def test_existing_allocation_does_not_become_incremental_spending(self):
        before = evaluate(self.row)
        self.row["existing_platform_allocation_fraction"] = "0.9"
        after = evaluate(self.row)
        self.assertEqual(after.pop("existing_platform_allocation_memo_usd"), "9000.00")
        before.pop("existing_platform_allocation_memo_usd")
        self.assertEqual(before, after)

    def test_one_off_setup_is_absent_in_steady_year(self):
        self.row["new_external_setup_cash_usd"] = "999999"
        self.row["existing_staff_setup_hours"] = "999999"
        result = evaluate(self.row)
        self.assertEqual(result["cash_increment_steady_year_usd"], "300.00")
        self.assertEqual(result["capacity_delta_steady_year_usd"], "-200.00")

    def test_released_capacity_is_not_cash_savings(self):
        self.row["existing_staff_net_annual_hours_delta"] = "-1000"
        result = evaluate(self.row)
        self.assertEqual(result["cash_increment_y1_usd"], "400.00")
        self.assertLess(float(result["cash_plus_capacity_delta_y1_usd"]), 0)

    def test_zero_seats_produces_no_license_charge_or_ratio(self):
        self.row["seats"] = 0
        self.assertEqual(evaluate(self.row)["license_annual_usd"], "0.00")

    def test_invalid_units_and_quantities_rejected(self):
        for key, value in [("seats", True), ("seats", 1.5),
                           ("license_usd_per_seat_month", "NaN"),
                           ("new_annual_cash_usd", "-1"),
                           ("existing_platform_allocation_fraction", "1.01")]:
            with self.subTest(key=key, value=value):
                row = copy.deepcopy(self.row)
                row[key] = value
                with self.assertRaises(ValueError):
                    evaluate(row)

    def test_committed_output_reproduces_from_hypothetical_inputs(self):
        inputs = json.loads(DEFAULT_INPUTS.read_text())
        output = Path(DEFAULT_INPUTS.parent, "tco-results.json").read_text()
        self.assertEqual(render(inputs), output)


if __name__ == "__main__":
    unittest.main()
