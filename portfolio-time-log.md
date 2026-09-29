# Applied AI Product & Strategy Portfolio — Time Log

This log tracks time invested across technical learning, portfolio development, evaluation, documentation, and interview preparation.

The purpose is to maintain an accurate record of effort, project progression, technical development, and product reasoning throughout the portfolio.

Progress is tracked by **session number rather than calendar day**. Multiple sessions may be completed in one day, and missed days do not affect the learning sequence.

---

# Summary

## Learning Area Hours

| Category | Hours |
|---|---:|
| Foundations | 0.0 |
| Python | 1.33 |
| Data Analysis | 0.0 |
| Machine Learning | 0.0 |
| Applied AI | 0.0 |
| AI Systems | 0.0 |
| Assessments | 0.0 |
| Interview Preparation | 0.0 |
| **Total Learning Time** | **1.33** |

> Project hours are tracked separately below because portfolio sessions may simultaneously count as Python, data, ML, or Applied AI learning. This avoids double-counting total time.

---

# Featured Project Summary

| Project | Status | Hours |
|---|---|---:|
| AI Workflow Opportunity & ROI Analyzer | Not Started | 0.0 |
| RAG Product Quality & Launch Readiness Lab | Not Started | 0.0 |
| AI Experimentation & Model Selection Lab | Not Started | 0.0 |
| AI Support Triage System | In Progress | 1.33 |
| Agentic Workflow Guardrail Simulator | Not Started | 0.0 |
| **Total Portfolio Project Time** |  | **1.33** |

---

# Certification Progress

| Certification | Status | Target |
|---|---|---|
| PCEP — Certified Entry-Level Python Programmer | In Progress | October 2026 |
| PCAP — Certified Associate Python Programmer | Planned | November 1, 2026 |

Python sessions are designed to support both certification readiness and portfolio development.

The learning model is:

**Explain → Demonstrate → You Try → Diagnose → Repeat → Apply → Explain Back → Spaced Repetition**

---

# Session Log

## September 2026

### Session 1 — Ticket Triage Foundations

**Date:** September 27, 2026  
**Area:** Python Foundations  
**Project:** AI Support Triage System  
**Duration:** 50 minutes

**Concept Tags:** PCEP Core · Practical / Portfolio · Interview-Relevant

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

### Interview Translation

Built a rule-based support triage prototype to establish a deterministic baseline before introducing ML. The exercise demonstrated how product requirements can be translated into executable decision logic and how rule precedence affects system behavior.

---

### Session 2 — Variables, Booleans & SLA Logic

**Date:** September 27, 2026  
**Area:** Python Foundations  
**Project:** AI Support Triage System  
**Duration:** 30 minutes

**Concept Tags:** PCEP Core · PCAP Foundation · Practical / Portfolio · Interview-Relevant

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

### Interview Translation

Extended a rule-based support triage prototype by separating prioritization logic from SLA compliance and implementing reusable Boolean decision logic. This allowed business urgency and service-level performance to be evaluated independently.

### Session 3 — Loops, Collections & Reusable Decision Logic

**Date:** September 29, 2026  
**Area:** Python Foundations  
**Project:** AI Support Triage System  
**Duration:** 30 minutes

**Concept Tags:** PCEP Core · Practical / Portfolio · Interview-Relevant

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

### Interview Translation

Built a reusable ticket-processing pipeline that applies independent classification and SLA rules across multiple records, routes breached tickets for review, and aggregates outcomes while maintaining separation between business urgency and service-level compliance.

---

# Weekly Totals

## Week Ending September 27, 2026

| Activity | Hours |
|---|---:|
| Python / Technical Learning | 1.33 |
| Product / Jira | 0.0 |
| Dedicated Portfolio Build Block | 0.0 |
| Weekly Assessment | 0.0 |
| Interview Practice | 0.0 |
| **Total Focused Time** | **1.33** |

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
12. Interview translation

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