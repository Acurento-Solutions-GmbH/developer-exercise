"""Initial examples, deliberately not a complete specification of correctness."""

import unittest

from relevance.assessment import assess_customer


class AssessmentTests(unittest.TestCase):
    def setUp(self):
        self.rule = {
            "id": "DEMO-001",
            "installation_type": "F-01",
            "minimum_capacity_t_h": 5,
        }

    def test_known_capacity_above_threshold_is_affected(self):
        customer = {
            "id": "TEST-001",
            "installation": {"type": "F-01", "capacity_t_h": 8},
        }
        result = assess_customer(customer, self.rule)
        self.assertEqual(result["status"], "affected")
        self.assertEqual(result["customer_id"], customer["id"])
        self.assertEqual(result["rule_id"], self.rule["id"])

    def test_known_capacity_below_threshold_is_not_affected(self):
        customer = {
            "id": "TEST-002",
            "installation": {"type": "F-01", "capacity_t_h": 3},
        }
        result = assess_customer(customer, self.rule)
        self.assertEqual(result["status"], "not_affected")


if __name__ == "__main__":
    unittest.main()
