tickets = [
    {"id": "T001", "category": "billing", "priority": 4, "age_hours": 30, "customer_tier": "enterprise"},
    {"id": "T002", "category": "login", "priority": 2, "age_hours": 5, "customer_tier": "free"},
    {"id": "T003", "category": "outage", "priority": 5, "age_hours": 2, "customer_tier": "enterprise"},
    {"id": "T004", "category": "billing", "priority": 3, "age_hours": 50, "customer_tier": "pro"},
    {"id": "T005", "category": "feature_request", "priority": 1, "age_hours": 72, "customer_tier": "free"},
    {"id": "T006", "category": "login", "priority": 4, "age_hours": 25, "customer_tier": "pro"},
]

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

counts = {
    "CRITICAL": 0,
    "HIGH": 0,
    "NORMAL": 0
}

def is_sla_breached(ticket: dict) -> bool:
    age_hours = ticket["age_hours"]
    sla_limit = 24
    is_breached = age_hours > sla_limit
    
    return is_breached

def should_escalate(result: str, sla_status: bool) -> bool:
    return result == "HIGH" and sla_status

escalation_queue = []

for ticket in tickets:
    result = classify_ticket(ticket)
    sla_status = is_sla_breached(ticket)

    counts[result] += 1

    if sla_status: 
        print(ticket["id"], "requires SLA review")

    if should_escalate(result, sla_status):
        if ticket ["id"] not in escalation_queue:
            escalation_queue.append(ticket["id"])
        
        print(ticket ["id"], "requires escalation")    

    print(
        ticket["id"],
        "->",
        result,
        "| SLA Breached:",
        sla_status
    )

print(counts)
print("Escalation Queue:", escalation_queue)
print("Escalation Count:", len(escalation_queue))