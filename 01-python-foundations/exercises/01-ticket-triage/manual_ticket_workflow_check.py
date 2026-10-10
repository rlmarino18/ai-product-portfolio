from ticket_logic import classify_ticket, is_sla_breached, should_escalate
from ticket_validation import (
    has_required_fields,
    has_valid_types,
    has_valid_values,
)


ticket = {
    "id": "TEST-008",
    "category": "billing",
    "priority": 4,
    "age_hours": 30,
    "customer_tier": "enterprise"
}


assert has_required_fields(ticket) is True
assert has_valid_types(ticket) is True
assert has_valid_values(ticket) is True

result = classify_ticket(ticket)
sla_status = is_sla_breached(ticket)
escalation_status = should_escalate(result, sla_status)

assert result == "HIGH"
assert sla_status is True
assert escalation_status is True

print("Test passed: valid HIGH ticket flows correctly through the workflow")