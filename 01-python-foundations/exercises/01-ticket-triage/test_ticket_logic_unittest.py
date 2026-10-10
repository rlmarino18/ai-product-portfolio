import unittest

from ticket_logic import (
    classify_ticket,
    is_sla_breached,
    should_escalate,
)


class TestTicketLogic(unittest.TestCase):

    def test_outage_is_critical(self):
        ticket = {
            "id": "TEST-009",
            "category": "outage",
            "priority": 2,
            "age_hours": 1,
            "customer_tier": "free"
        }

        result = classify_ticket(ticket)

        self.assertEqual(result, "CRITICAL")


    def test_normal_login_is_normal(self):
        ticket = {
            "id": "TEST-010",
            "category": "login",
            "priority": 2,
            "age_hours": 3,
            "customer_tier": "free"
        }

        result = classify_ticket(ticket)

        self.assertEqual(result, "NORMAL")


    def test_ticket_over_24_hours_breaches_sla(self):
        ticket = {
            "id": "TEST-015",
            "category": "billing",
            "priority": 3,
            "age_hours": 30,
            "customer_tier": "pro"
        }

        result = is_sla_breached(ticket)

        self.assertTrue(result)


    def test_high_breached_ticket_escalates(self):
        result = should_escalate(
            result="HIGH",
            sla_status=True
        )

        self.assertTrue(result)

    def test_high_ticket_without_sla_breach_does_not_escalate(self):
        result = should_escalate(
            result="HIGH",
            sla_status=False
        )
        
        self.assertFalse(result)  

if __name__ == "__main__":
    unittest.main()