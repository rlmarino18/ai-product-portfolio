from ticket_validation import (
    has_required_fields,
    has_valid_types,
    has_valid_values,
)

wrong_type_ticket = {
    "id": "TEST-006",
    "category": "billing",
    "priority": "high",
    "age_hours": 10,
    "customer_tier": "pro"
}

type_result = has_valid_types(wrong_type_ticket)

assert type_result is False

print("Test passed: invalid data type is rejected")


invalid_value_ticket = {
    "id": "TEST-007",
    "category": "billing",
    "priority": 9,
    "age_hours": -2,
    "customer_tier": "gold"
}

value_result = has_valid_values(invalid_value_ticket)

assert value_result is False

print("Test passed: invalid business values are rejected")

valid_ticket = {
    "id": "TEST-004",
    "category": "billing",
    "priority": 3,
    "age_hours": 10,
    "customer_tier": "pro"
}

result = has_required_fields(valid_ticket)

assert result is True

print("Test passed: complete ticket contains all required fields")

invalid_ticket = {
    "id": "TEST-005",
    "category": "billing",
    "priority": 3
}

invalid_result = has_required_fields(invalid_ticket)

assert invalid_result is False

print("Test passed: incomplete ticket fails required-field validation")

