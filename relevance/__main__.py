"""Run with python3 -m relevance. Uses only the Python standard library."""

import argparse
import json
from pathlib import Path

from .assessment import assess_customer


def main() -> None:
    data_dir = Path(__file__).resolve().parent.parent / "data"
    parser = argparse.ArgumentParser(description="Assess fictional customer relevance.")
    parser.add_argument("--customers", type=Path, default=data_dir / "customers.json")
    parser.add_argument("--rule", type=Path, default=data_dir / "rule.json")
    args = parser.parse_args()

    customers = json.loads(args.customers.read_text(encoding="utf-8"))
    rule = json.loads(args.rule.read_text(encoding="utf-8"))
    results = [assess_customer(customer, rule) for customer in customers]
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
