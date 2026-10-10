def classify_ticket(ticket: dict) -> str:
    if ticket["category"] == "outage" or ticket["priority"] == 5:
        return "CRITICAL"

    elif ticket["priority"] >= 4 or (
        ticket["age_hours"] > 24
        and ticket["customer_tier"] == "enterprise"
    ):
        return "HIGH"

    else:
        return "NORMAL"

def is_sla_breached(ticket: dict) -> bool:
    age_hours = ticket["age_hours"]
    sla_limit = 24
    is_breached = age_hours > sla_limit

    return is_breached

def should_escalate(result: str, sla_status: bool) -> bool:
    return result == "HIGH" and sla_status
    