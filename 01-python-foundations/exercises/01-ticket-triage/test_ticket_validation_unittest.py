import unittest

from ticket_validation import (
    has_required_fields,
    has_valid_types,
    has_valid_values,
)


class TestTicketValidation(unittest.TestCase):

    def test_complete_ticket_has_required_fields(self):
        ticket = {
            "id": "TEST-011",
            "category": "billing",
            "priority": 3,
            "age_hours": 10,
            "customer_tier": "pro"
        }

        result = has_required_fields(ticket)

        self.assertTrue(result)


    def test_incomplete_ticket_fails_required_fields(self):
        ticket = {
            "id": "TEST-012",
            "category": "billing",
            "priority": 3
        }

        result = has_required_fields(ticket)

        self.assertFalse(result)


    def test_invalid_type_is_rejected(self):
        ticket = {
            "id": "TEST-013",
            "category": "billing",
            "priority": "high",
            "age_hours": 10,
            "customer_tier": "pro"
        }

        result = has_valid_types(ticket)

        self.assertFalse(result)


    def test_invalid_value_is_rejected(self):
        ticket = {
            "id": "TEST-014",
            "category": "billing",
            "priority": 9,
            "age_hours": -2,
            "customer_tier": "gold"
        }

        result = has_valid_values(ticket)

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()