import json

BASE_PATH = "01-python-foundations/exercises/01-ticket-triage"

tickets = [
    {"id": "T001", "category": "billing", "priority": 4, "age_hours": 30, "customer_tier": "enterprise"},
    {"id": "T002", "category": "login", "priority": 2, "age_hours": 5, "customer_tier": "free"},
    {"id": "T003", "category": "outage", "priority": 5, "age_hours": 2, "customer_tier": "enterprise"},
    {"id": "T004", "category": "billing", "priority": 3, "age_hours": 50, "customer_tier": "pro"},
    {"id": "T005", "category": "feature_request", "priority": 1, "age_hours": 72, "customer_tier": "free"},
    {"id": "T006", "category": "login", "priority": 4, "age_hours": 25, "customer_tier": "pro"},

    {
        "id": "T007",
        "category": "billing",
        "priority": 4
    },

    {
    "id": "T008",
    "category": "billing",
    "priority": 9,
    "age_hours": -4,
    "customer_tier": "gold"
    },

    {
        "id": "T009",
        "category": "billing",
        "priority": "high",
        "age_hours": 10,
        "customer_tier": "pro"
    }

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
    if ticket["priority"] < 1 or ticket ["priority"] > 5:
        return False
    
    if ticket["age_hours"] < 0:
        return False    

    if ticket["customer_tier"] not in ["free", "pro", "enterprise"]:
        return False 

    return True    

invalid_ticket = {
    "id": "T007",
    "category": "billing",
    "priority": 4
},

escalation_queue = []

def process_ticket(ticket: dict) -> None:
    if not has_required_fields(ticket):
        print(ticket.get("id", "UNKNOWN"), "has missing required fields")
        return

    if not has_valid_types(ticket):
        print(ticket.get("id", "UNKNOWN"), "has invalid data types")
        return

    if not has_valid_values(ticket):
        print(ticket.get("id", "UNKNOWN"), "has invalid values")
        return

    try:
        result = classify_ticket(ticket)
        sla_status = is_sla_breached(ticket)
    except (KeyError, TypeError) as error:
        print(ticket.get("id", "UNKNOWN"), "processing error:", error)
        return

    print(
        ticket["id"],
        "->",
        result,
        "| SLA Breached:",
        sla_status
    )

def load_tickets_from_json(file_path: str) -> list[dict]:
    try:
        with open(file_path, "r") as file:
            return json.load(file)

    except FileNotFoundError as error:
        print("Ticket file not found:", error)
        return []

    except json.JSONDecodeError as error:
        print("Invalid JSON:", error)
        return []

for ticket in tickets:
    if not has_required_fields(ticket):
        print(ticket.get("id", "UNKNOWN"), "has missing required fields")
        continue

    if not has_valid_types(ticket):
        print(ticket.get("id", "UNKNOWN"), "has invalid data types")
        continue
    
    if not has_valid_values(ticket):
        print(ticket.get("id", "UNKNOWN"), "has invalid values")
        continue

    try:
        result = classify_ticket(ticket)
        sla_status = is_sla_breached(ticket)

    except (KeyError, TypeError) as error:
        print(ticket.get("id", "UNKNOWN"), "processing error:", error)
        continue

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

test_ticket = {
    "id": "T010",
    "priority": 4
}

with open(
    f"{BASE_PATH}/system_name.txt",
    "r"
) as file:
    system_name = file.read().strip()

print(system_name)

with open(
    f"{BASE_PATH}/run_summary.txt",
    "w"
) as file:
    file.write("Escalation Count: ")
    file.write(str(len(escalation_queue)))

with open(
    f"{BASE_PATH}/run_summary.txt",
    "a"
) as file:
    file.write("\nEscalation Queue: ")
    file.write(str(escalation_queue))
    file.write("\n")

with open(
    f"{BASE_PATH}/sample_ticket.json",
    "r"
) as file:
    sample_ticket = json.load(file)

print(sample_ticket)
print(sample_ticket["id"])

output_ticket = {
    "id": "T011",
    "category": "technical",
    "priority": 5,
    "age_hours": 30,
    "customer_tier": "enterprise"
}

with open(
    f"{BASE_PATH}/output_ticket.json",
    "w"
) as file:
    json.dump(output_ticket, file, indent=2)
    file.write("\n")

sample_tickets = load_tickets_from_json(
    f"{BASE_PATH}/sample_tickets.json"
)

for ticket in sample_tickets:
    process_ticket(ticket)