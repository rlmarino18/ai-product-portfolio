# Applied AI Product & Strategy Portfolio — Time Log

This log tracks time invested across technical learning, portfolio development, evaluation, documentation, and interview preparation.

The purpose is to maintain an accurate record of effort, project progression, and lessons learned throughout the portfolio.

---

## Summary

| Category | Hours |
|---|---:|
| Foundations | 0.0 |
| Python | 0.0 |
| Data Analysis | 0.0 |
| Machine Learning | 0.0 |
| Applied AI | 0.0 |
| AI Systems | 0.0 |
| Featured Projects | 0.0 |
| Assessments | 0.0 |
| Interview Preparation | 0.0 |
| **Total** | **0.0** |

---

## Featured Project Summary

| Project | Status | Hours |
|---|---|---:|
| AI Workflow Opportunity & ROI Analyzer | Not Started | 0.0 |
| RAG Product Quality & Launch Readiness Lab | Not Started | 0.0 |
| AI Experimentation & Model Selection Lab | Not Started | 0.0 |
| AI Support Triage System | In Progress | 0.0 |
| Agentic Workflow Guardrail Simulator | Not Started | 0.0 |

---

# Session Log

## September 2026

### 2026-09-27 — Day 1: Ticket Triage Foundations

## Area: Python Foundations  
## Project: AI Support Triage System  
## Duration: 50 minutes

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

Rule ordering matters when multiple conditions can match the same input. The most restrictive or highest-priority condition should be evaluated first.

### Product & Strategy Application

A deterministic rules-based system can provide a transparent baseline before introducing machine learning. This makes it possible to compare whether additional model complexity creates measurable product value.

### Interview Translation

Built a rule-based support triage prototype to establish a deterministic baseline before introducing ML. The exercise reinforced how product requirements translate into executable decision logic and how rule precedence affects system behavior.

### 2026-09-27 — Day 2: Variables, Booleans & SLA Logic

## Area: Python Foundations  
## Project: AI Support Triage System  
## Duration: 30 minutes

## Objective:
Understand variables, data types, comparison operators, Boolean values, and function return behavior by adding SLA breach detection.

## Work Completed:
- Added `is_sla_breached()` function
- Retrieved values from ticket dictionaries
- Defined an SLA business-rule threshold
- Returned Boolean SLA status
- Integrated SLA status into ticket output
- Debugged a missing dictionary brace and indentation issues

## Technical Concepts:
- Variables
- Dictionaries
- Integers
- Booleans
- Comparison operators
- Functions
- `return`
- Type hints
- Indentation
- Syntax debugging

## Lessons Learned: 
Comparison expressions return Boolean values. Business-rule thresholds should be separated from record-specific data so they can be reused and changed cleanly.

## Product & Strategy Application:**  
Priority and SLA compliance represent different product dimensions. Keeping them separate makes the system easier to reason about, modify, and evaluate.

## Interview Translation: 
Extended a rule-based triage prototype by separating prioritization logic from SLA compliance and implementing reusable Boolean decision logic.

---

# Weekly Totals

## Week of September 28, 2026

| Activity | Hours |
|---|---:|
| Technical Drills | 0.0 |
| Portfolio Build | 0.0 |
| Weekly Assessment | 0.0 |
| Interview Practice | 0.0 |
| **Total** | **0.0** |

---

# Logging Guidelines

Each session should record:

1. Date
2. Session or project
3. Duration
4. Objective
5. Work completed
6. Technical concepts practiced
7. Lessons learned
8. Product & strategy application
9. Interview translation

Time should reflect actual focused work rather than estimated project duration.

---

# Why This Log Exists

The purpose of this log is not to maximize the number of hours recorded.

It provides evidence of:

- consistent technical development
- progressive project complexity
- deliberate practice
- iteration and experimentation
- product decision-making
- technical-to-business translation

The final portfolio should demonstrate both what was built and the reasoning developed while building it.