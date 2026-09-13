"""Smoke test for the command-line entry point, not assessment correctness."""

import json
from pathlib import Path
import subprocess
import sys
import unittest


class CliTests(unittest.TestCase):
    def test_module_outputs_one_result_per_customer(self):
        root = Path(__file__).resolve().parent.parent
        completed = subprocess.run(
            [sys.executable, "-m", "relevance"],
            cwd=root,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=True,
        )
        results = json.loads(completed.stdout)
        customers = json.loads((root / "data/customers.json").read_text(encoding="utf-8"))
        self.assertEqual(len(results), len(customers))
        self.assertEqual(
            [result["customer_id"] for result in results],
            [customer["id"] for customer in customers],
        )
        for result in results:
            self.assertIn(result["status"], {"affected", "not_affected", "needs_review"})
            self.assertIsInstance(result["reason"], str)
            self.assertTrue(result["reason"].strip())


if __name__ == "__main__":
    unittest.main()
