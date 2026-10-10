required_fields = [
    "id",
    "category",
    "priority",
    "age_hours",
    "customer_tier"
]


def has_required_fields(ticket: dict) -> bool:
    for field in required_fields:
        if field not in ticket:
            return False

    return True


def has_valid_types(ticket: dict) -> bool:
    if not isinstance(ticket["id"], str):
        return False

    if not isinstance(ticket["category"], str):
        return False

    if not isinstance(ticket["priority"], int):
        return False

    if not isinstance(ticket["age_hours"], int):
        return False

    if not isinstance(ticket["customer_tier"], str):
        return False

    return True


def has_valid_values(ticket: dict) -> bool:
    if ticket["priority"] < 1 or ticket["priority"] > 5:
        return False

    if ticket["age_hours"] < 0:
        return False

    if ticket["customer_tier"] not in ["free", "pro", "enterprise"]:
        return False

    return True