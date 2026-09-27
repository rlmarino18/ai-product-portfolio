# Day 1 — Ticket Triage

## Objective

Build a simple rule-based support ticket classifier using Python dictionaries, functions, conditionals, loops, and aggregation.

## Classification Rules

### CRITICAL
- Category is `outage`
- OR priority is `5`

### HIGH
- Priority is `4` or greater
- OR ticket age is over 24 hours and the customer tier is `enterprise`

### NORMAL
- Everything else

## Results

- CRITICAL: 1
- HIGH: 2
- NORMAL: 3

## Concepts Practiced

- Python dictionaries
- Functions
- `if / elif / else`
- Boolean logic
- `for` loops
- Aggregation with dictionaries

## Product Takeaway

A deterministic rules-based system can provide a simple baseline before introducing machine learning. It is fast, explainable, cheap to operate, and useful for comparing whether a more complex AI approach actually adds value.