# AI/ML Product Portfolio — Development & Time Log

This log tracks time invested across technical learning, portfolio development, evaluation, documentation.

Its purpose is to provide a clear record of:

- technical capability development
- featured-project progression
- product reasoning and decision-making
- evaluation and experimentation work
- portfolio documentation
- technical and product learning

Progress is tracked by **session number rather than calendar day**.

Multiple sessions may be completed on the same day, and gaps between sessions do not affect the learning sequence. Calendar dates are retained for time accounting and project history, while session numbers reflect the actual order of development.

---

# Summary

## Technical Learning by Area

| Category | Hours |
|---|---:|
| Foundations | 0.0 |
| Python | 4.33 |
| Data Analysis | 0.0 |
| Machine Learning | 0.0 |
| Applied AI | 0.0 |
| AI Systems | 0.0 |
| **Total Learning Time** | **4.33** |

> Learning-area hours represent the technical capability developed during portfolio work. Project hours are tracked separately below because the same session may simultaneously contribute to both technical learning and a featured project. These totals should not be added together.

---

# Portfolio Investment by Project

| Project | Status | Hours |
|---|---|---:|
| AI Workflow Opportunity & ROI Analyzer | Not Started | 0.0 |
| Document Q&A RAG Assistant | In Progress | 2.50 |
| AI Experimentation & Model Selection Lab | Not Started | 0.0 |
| AI Support Triage System | In Progress | 4.33 |
| Agentic Workflow Guardrail Simulator | Not Started | 0.0 |
| **Total Portfolio Project Time** |  | **6.83** |

> Portfolio project hours represent verified time invested in building, testing, evaluating, and documenting featured projects. Some projects began before the current structured session sequence; verified historical development time is included where an existing project time log is available.

> Technical Learning hours and Portfolio Project hours measure different dimensions of the work and should not be added together. Technical Learning currently reflects the structured learning sessions tracked in this portfolio, while Portfolio Project hours may also include verified development completed before those sessions began.

---

# Session Log

## September 2026

### Session 1 — Ticket Triage Foundations

**Date:** September 27, 2026  
**Area:** Python Foundations  
**Project:** AI Support Triage System  
**Duration:** 50 minutes

**Concept Tags:** PCEP Core · Practical / Portfolio

### Objective

Build a simple deterministic support-ticket classification system using Python.

### Work Completed

- Created ticket dataset
- Built `classify_ticket()` function
- Used `if / elif / else`
- Applied Boolean logic
- Iterated through tickets
- Counted classification outcomes
- Documented exercise in README
- Created Git feature branch
- Committed changes
- Opened and merged pull request

### Technical Concepts

- Dictionaries
- Functions
- Conditionals
- Boolean operators
- Loops
- Basic aggregation
- Git branches
- Pull requests

### Lessons Learned

Rule ordering matters when multiple conditions can match the same input.

The most restrictive or highest-priority condition should be evaluated first so that a broader rule does not incorrectly capture a case intended for a more important classification.

### Product & Strategy Application

A deterministic rules-based system can provide a transparent baseline before introducing machine learning.

This makes it possible to evaluate whether additional model complexity creates enough measurable product value to justify higher cost, lower explainability, or additional operational complexity.

---

### Session 2 — Variables, Booleans & SLA Logic

**Date:** September 27, 2026  
**Area:** Python Foundations  
**Project:** AI Support Triage System  
**Duration:** 30 minutes

**Concept Tags:** PCEP Core · PCAP Foundation · Practical / Portfolio

### Objective

Understand variables, data types, comparison operators, Boolean values, function return behavior, and reusable business logic by adding SLA breach detection.

### Work Completed

- Added `is_sla_breached()` function
- Retrieved values from ticket dictionaries
- Defined an SLA business-rule threshold
- Compared ticket age against the SLA threshold
- Returned Boolean SLA status
- Integrated SLA status into ticket output
- Debugged a missing dictionary brace
- Corrected indentation issues
- Reinforced the difference between `print()` and `return`
- Separated ticket priority from SLA compliance

### Technical Concepts

- Variables
- Dictionaries
- Integers
- Strings
- Booleans
- Comparison operators
- Functions
- `return`
- Type hints
- Indentation
- Syntax debugging
- Business-rule separation

### Lessons Learned

Comparison expressions return Boolean values: `True` or `False`.

Business-rule thresholds should be separated from record-specific data so the logic remains clear, reusable, and easy to modify.

A Python `SyntaxError` may point to where Python finally recognizes a problem rather than the exact location where the error originally occurred.

`print()` displays a value to the user, while `return` sends a value back to the code that called the function.

### Product & Strategy Application

Priority and SLA compliance represent different product dimensions.

Priority reflects the **business urgency** of a ticket, while SLA status reflects whether a **service commitment** has been met.

Keeping these dimensions separate makes the system easier to reason about, modify, measure, and eventually evaluate against more advanced approaches.

### Session 3 — Loops, Collections & Reusable Decision Logic

**Date:** September 29, 2026  
**Area:** Python Foundations  
**Project:** AI Support Triage System  
**Duration:** 30 minutes

**Concept Tags:** PCEP Core · Practical / Portfolio

### Objective

Understand how Python lists and `for` loops can repeatedly apply reusable decision logic across multiple support-ticket records.

### Work Completed

- Reviewed variables, Booleans, dictionary access, functions, and `return`
- Reinforced the distinction between values and data types
- Distinguished lists from dictionaries
- Practiced tracing `for` loops manually
- Applied `is_sla_breached()` across multiple tickets
- Added SLA-based review routing
- Consolidated classification and SLA logic into one ticket-processing loop
- Verified classification counts remained correct
- Identified a potential stale-variable / execution-scope failure mode

### Technical Concepts

- Lists
- Dictionaries
- `for` loops
- Iteration
- Dictionary key access
- Function reuse
- Boolean conditions
- `if`
- Variable scope
- Execution frequency
- Aggregation
- Code tracing
- Logical debugging

### Lessons Learned

A `for` loop processes one item from a collection at a time, with the loop variable representing the current item. Logic that must execute for every record needs to remain inside the loop.

Code can be syntactically valid while still producing incorrect behavior if logic executes at the wrong scope or frequency.

### Product & Strategy Application

The triage prototype now behaves as a simple decision pipeline: each ticket is classified, evaluated for SLA status, conditionally routed for review, and included in aggregate metrics.

This provides a deterministic baseline that can later be compared against ML-assisted classification or routing approaches.

# Session 4 — Boolean Logic & Compound Decision Rules

**Date:** September 30, 2026  
**Duration:** 30 minutes  
**Project:** AI Support Triage System  
**Learning Area:** Python Foundations

## Objective

Strengthen Boolean logic and combine multiple conditions to create more precise escalation decisions.

## Work Completed

- Reviewed `and`, `or`, and `not`
- Practiced compound Boolean expressions
- Combined ticket classification with SLA status
- Added escalation logic requiring both a `HIGH` classification and a breached SLA

Implemented:

    if result == "HIGH" and sla_status:
        print(ticket["id"], "requires escalation")

Validated that only `T001` and `T006` met both escalation conditions.

## Technical Concepts

- Boolean expressions
- `and`
- `or`
- `not`
- compound conditions
- nested decision logic

## Product Capability Developed

Developed the ability to combine multiple operational signals into one product decision.

The system now distinguishes between tickets requiring SLA review and tickets requiring escalation.

## Product Decision / Insight

A single signal is often insufficient for a meaningful automated decision. An SLA breach alone may not justify escalation, and a HIGH-priority ticket alone may not have breached service expectations.

## Failure Mode / Edge Case

Using `or` instead of `and` would significantly increase escalation volume by escalating tickets that satisfy only one condition.

## Lessons Learned

- `and` requires both conditions to be true
- `or` requires only one condition to be true
- Boolean operators directly encode business policy
- small logical changes can materially change product behavior

---

# Session 5 — Lists as Working Queues

**Date:** September 30, 2026  
**Duration:** 30 minutes  
**Project:** AI Support Triage System  
**Learning Area:** Python Foundations

## Objective

Use Python lists to persist escalation decisions and create a reusable working queue.

## Work Completed

Created an empty escalation queue:

    escalation_queue = []

Added qualifying ticket IDs:

    if result == "HIGH" and sla_status:
        escalation_queue.append(ticket["id"])
        print(ticket["id"], "requires escalation")

Added aggregate output after all tickets were processed:

    print("Escalation Queue:", escalation_queue)
    print("Escalation Count:", len(escalation_queue))

Validated:

    Escalation Queue: ['T001', 'T006']
    Escalation Count: 2

## Technical Concepts

- empty lists
- `.append()`
- `len()`
- list methods
- loop scope
- aggregation
- storing results for later use

## Product Capability Developed

Moved the system from printing individual decisions to maintaining a reusable operational output.

The escalation queue can later support:

- human review
- ticket assignment
- reporting
- workflow integrations
- escalation metrics

## Product Decision / Insight

A decision system becomes more useful when its outputs can be stored and consumed by another process. Printing a decision communicates an event; maintaining a queue creates structured output that another workflow can use.

## Failure Mode / Edge Case

Placing aggregate queue output inside the loop produces incomplete intermediate results. The queue must also be initialized outside the loop so earlier results are preserved.

## Lessons Learned

- `.append()` adds an item to a list
- `len()` returns the number of elements
- list initialization location matters
- code inside a loop executes once per item
- aggregate outputs usually belong after the loop

---

# Session 6 — Indexing, Membership & Duplicate Prevention

**Date:** September 30, 2026  
**Duration:** 30 minutes  
**Project:** AI Support Triage System  
**Learning Area:** Python Foundations

## Objective

Learn list indexing and membership checks while protecting the escalation workflow from duplicate entries.

## Work Completed

Reviewed:

- zero-based indexing
- `in`
- `not in`
- nested `if` statements

Added duplicate prevention:

    if result == "HIGH" and sla_status:
        if ticket["id"] not in escalation_queue:
            escalation_queue.append(ticket["id"])

        print(ticket["id"], "requires escalation")

Validated:

    Escalation Queue: ['T001', 'T006']
    Escalation Count: 2

## Technical Concepts

- zero-based indexing
- list membership
- `in`
- `not in`
- nested conditions
- duplicate prevention
- `IndexError`
- basic idempotency

## Product Capability Developed

Introduced protection against duplicate downstream actions.

This is an early example of idempotent workflow behavior: repeated processing should not create unintended duplicate effects.

## Product Decision / Insight

Duplicate prevention matters because repeated automated actions can create duplicate escalations, notifications, assignments, incorrect reporting, and unnecessary operational work.

## Failure Mode / Edge Case

Without:

    ticket["id"] not in escalation_queue

the same ticket could be added multiple times if the routing logic were executed repeatedly.

Attempting to access a list position that does not exist can also produce an `IndexError`.

## Lessons Learned

- Python indexing begins at `0`
- `in` tests whether a value exists
- `not in` tests whether a value does not exist
- nested conditions allow more precise logic
- duplicate prevention is both a programming and product-reliability concern

---

# Session 7 — Functions, Parameters & Reusable Routing Logic

**Date:** September 30, 2026  
**Duration:** 30 minutes  
**Project:** AI Support Triage System  
**Learning Area:** Python Foundations

## Objective

Refactor escalation logic into a reusable function and strengthen understanding of parameters, arguments, return values, and separation of concerns.

## Work Completed

Created:

    def should_escalate(result: str, sla_status: bool) -> bool:
        return result == "HIGH" and sla_status

Replaced the inline escalation condition with:

    if should_escalate(result, sla_status):
        if ticket["id"] not in escalation_queue:
            escalation_queue.append(ticket["id"])

        print(ticket["id"], "requires escalation")

Validated the complete workflow:

    T001 requires SLA review
    T001 requires escalation
    T001 -> HIGH | SLA Breached: True
    T002 -> NORMAL | SLA Breached: False
    T003 -> CRITICAL | SLA Breached: False
    T004 requires SLA review
    T004 -> NORMAL | SLA Breached: True
    T005 requires SLA review
    T005 -> NORMAL | SLA Breached: True
    T006 requires SLA review
    T006 requires escalation
    T006 -> HIGH | SLA Breached: True
    {'CRITICAL': 1, 'HIGH': 2, 'NORMAL': 3}
    Escalation Queue: ['T001', 'T006']
    Escalation Count: 2

## Technical Concepts

- function definition
- parameters
- arguments
- Boolean return values
- type hints
- reusable decision logic
- function placement
- separation of concerns
- refactoring

## Product Capability Developed

Separated escalation policy from workflow execution.

Instead of embedding the business rule directly inside the processing loop, the system now expresses it through:

    should_escalate(...)

This makes the rule easier to understand, modify, test, reuse, and explain.

## Product Decision / Insight

Business rules should be isolated from workflow execution where practical.

This improves maintainability because the escalation policy can change without requiring the entire processing loop to be redesigned.

## Failure Mode / Edge Case

Function placement and indentation matter. Defining the function in the wrong location or placing workflow logic after a `return` statement can create unreachable or incorrectly scoped code.

Parameter and argument terminology also requires continued reinforcement:

- **Parameter** = placeholder defined by the function
- **Argument** = actual value supplied when calling it

Example:

    should_escalate("HIGH", True)

Here:

- `result` and `sla_status` are parameters
- `"HIGH"` and `True` are arguments

## Lessons Learned

- functions make decision logic reusable
- parameters define what information a function needs
- arguments provide the actual values
- `return` sends a value back to the caller
- Boolean functions are useful for business decision rules
- refactoring improves readability and maintainability

# Session 8 — Input Validation & Defensive Decision Logic

**Date:** October 2, 2026  
**Duration:** 30 minutes  
**Project:** AI Support Triage System  
**Learning Area:** Python Foundations

## Objective

Add input validation to the ticket-triage workflow so incomplete tickets are identified before classification, SLA evaluation, and escalation logic.

## Work Completed

Created a required-fields list:

    required_fields = [
        "id",
        "category",
        "priority",
        "age_hours",
        "customer_tier"
    ]

Created a reusable validation function:

    def has_required_fields(ticket: dict) -> bool:
        for field in required_fields:
            if field not in ticket:
                return False

        return True

Tested the validation function against both an incomplete ticket and an existing valid ticket:

    print("Invalid Ticket Valid:", has_required_fields(invalid_ticket))
    print("Existing Ticket Valid:", has_required_fields(tickets[0]))

Validated the expected result:

    Invalid Ticket Valid: False
    Existing Ticket Valid: True

Integrated validation into the main processing loop:

    for ticket in tickets:
        if not has_required_fields(ticket):
            print(ticket.get("id", "UNKNOWN"), "has missing required fields")
            continue

Added an intentionally incomplete ticket:

    {
        "id": "T007",
        "category": "billing",
        "priority": 4
    }

Validated the complete workflow:

    Invalid Ticket Valid: False
    Existing Ticket Valid: True
    T001 requires SLA review
    T001 requires escalation
    T001 -> HIGH | SLA Breached: True
    T002 -> NORMAL | SLA Breached: False
    T003 -> CRITICAL | SLA Breached: False
    T004 requires SLA review
    T004 -> NORMAL | SLA Breached: True
    T005 requires SLA review
    T005 -> NORMAL | SLA Breached: True
    T006 requires SLA review
    T006 requires escalation
    T006 -> HIGH | SLA Breached: True
    T007 has missing required fields
    {'CRITICAL': 1, 'HIGH': 2, 'NORMAL': 3}
    Escalation Queue: ['T001', 'T006']
    Escalation Count: 2

## Technical Concepts

- input validation
- required fields
- dictionary membership
- `in`
- `not in`
- `.get()`
- fallback values
- Boolean validation functions
- `not`
- `continue`
- fail-fast logic
- defensive programming
- control flow

## Product Capability Developed

Added a validation layer before downstream decision logic.

Instead of assuming that every incoming ticket contains complete data, the system now checks whether the required fields exist before attempting classification.

The workflow now follows:

    Input
      ↓
    Validation
      ↓
    Valid? ── No → Flag and skip
      ↓ Yes
    Classification
      ↓
    SLA Evaluation
      ↓
    Escalation

This makes the workflow more resilient to malformed or incomplete input.

## Product Decision / Insight

Invalid inputs should be stopped before they enter downstream business logic.

Once a ticket has already been determined to be incomplete, continuing into classification or SLA processing creates unnecessary work and increases the risk of runtime errors or incorrect decisions.

Validation therefore acts as a control layer protecting the rest of the workflow.

## Failure Mode / Edge Case

Attempting to process a ticket without all required fields can cause downstream failures.

For example:

    ticket["age_hours"]

will raise a `KeyError` if `"age_hours"` does not exist.

The validation function prevents this by checking each required key before processing continues.

Dictionary membership also required reinforcement:

    "priority" in ticket

checks whether `"priority"` exists as a **key**, not whether a particular value exists.

Safe dictionary access also required reinforcement:

    ticket.get("id", "UNKNOWN")

means:

- return the value associated with `"id"` if the key exists
- return `"UNKNOWN"` if the key does not exist

`continue` changes control flow by immediately ending the current loop iteration and moving to the next ticket.

## Lessons Learned

- validate incoming data before applying business logic
- dictionary membership checks keys rather than values
- `not in` is useful for detecting missing required fields
- `.get()` provides safer dictionary access when a key may be missing
- Boolean functions can encapsulate validation rules
- `not` reverses a Boolean result
- `continue` skips the remainder of the current loop iteration
- fail-fast logic prevents unnecessary downstream processing
- validation improves reliability and makes workflow failures easier to control

---

# Actual Time by Week

## Week Ending September 27, 2026

| Activity | Hours |
|---|---:|
| Python / Technical Learning | 1.33 |
| Product / Jira | 0.0 |
| Dedicated Portfolio Build Block | 0.0 |
| Weekly Assessment | 0.0 |
| **Total Focused Time** | **1.33** |

## Week Ending October 4, 2026

| Category | Hours |
|---|---:|
| Python / Technical Learning | 3.00 |
| Product / Jira | 1.00 |
| Dedicated Portfolio Build Block | 0.0 |
| Weekly Assessment | 0.0 |
| **Total Focused Time** | **4.00** |

> Portfolio project hours overlap with technical-learning hours and are therefore tracked separately rather than added again to the weekly total.

---

# Logging Guidelines

Each training session should record:

1. Session number
2. Date
3. Area
4. Project
5. Duration
6. Concept tags
7. Objective
8. Work completed
9. Technical concepts practiced
10. Lessons learned
11. Product & strategy application

When relevant, also record:

- PCEP concepts practiced
- PCAP concepts practiced
- Jira issue or product requirement advanced
- Bugs or failure modes discovered
- Evaluation results
- Architecture or product trade-offs
- Spaced-repetition topics that need to be revisited

Time should reflect actual focused work rather than estimated project duration.

---

# Session Numbering

Training progression is session-based rather than day-based.

For example:

```text
Session 1
Session 2
Session 3
Session 4
...