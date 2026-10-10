from ticket_logic import classify_ticket, is_sla_breached, should_escalate

escalation_result = should_escalate(
    result="HIGH",
    sla_status=True
)

assert escalation_result is True

no_escalation_result = should_escalate(
    result="HIGH",
    sla_status=False
)

assert no_escalation_result is False

print("Test passed: HIGH ticket without SLA breach does not escalate")

print("Test passed: HIGH ticket with SLA breach requires escalation")

sla_ticket = {
    "id": "TEST-003",
    "category": "billing",
    "priority": 3,
    "age_hours": 30,
    "customer_tier": "pro"
}

sla_result = is_sla_breached(sla_ticket)

assert sla_result is True

print("Test passed: ticket older than 24 hours breaches SLA")

from ticket_logic import classify_ticket

ticket = {
    "id": "TEST-001",
    "category": "outage",
    "priority": 2,
    "age_hours": 1,
    "customer_tier": "free"
}

result = classify_ticket(ticket)

assert result == "CRITICAL"

print("Test passed: outage tickets are classified as CRITICAL")

normal_ticket = {
    "id": "TEST-002",
    "category": "login",
    "priority": 2,
    "age_hours": 3,
    "customer_tier": "free"
}

normal_result = classify_ticket(normal_ticket)

assert normal_result == "NORMAL"

print("Test passed: normal login ticket is classified as NORMAL")