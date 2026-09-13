"""Existing implementation to investigate and improve during the exercise."""


def assess_customer(customer: dict, rule: dict) -> dict:
    """Return a customer's assessment for the supplied fictional rule."""
    installation = customer["installation"]
    capacity = installation.get("capacity_t_h") or 0
    affected = (
        installation["type"] == rule["installation_type"]
        and capacity >= rule["minimum_capacity_t_h"]
    )

    return {
        "customer_id": customer["id"],
        "rule_id": rule["id"],
        "status": "affected" if affected else "not_affected",
        "reason": "Rule applies." if affected else "Rule does not apply.",
    }
