---
$schema: https://raw.githubusercontent.com/agility-game/scenarios-management/main/schemas/scenario.schema.json

schema_version: 1.0.0

id: dusty-golden-apples

title: Dusty Golden Apples

summary: >
  A legacy Python refactoring case inspired by the
  Gilded Rose kata.

type: kata

language: python

difficulty: intermediate

tags:
  - python
  - refactoring
  - testing
  - legacy-code

source:
  kind: github
  upstream_repository: emilybache/GildedRose-Refactoring-Kata
  upstream_path: python

spaces:
  primary:
    - refactoring
    - unit-tests
    - technical-debt

required_capabilities:
  - refactoring
  - characterization-testing
  - maintainability-analysis

recommended_ai_employees:
  - code-smell-detective
  - marcus-rodriguez
  - sarah-chen
  - jenkins
---

# Dusty Golden Apples

## Story

The inventory system of a mysterious old shop has become fragile.

Business rules are scattered.
Tests are incomplete.
Nobody fully understands the code anymore.

The player must improve the system without breaking behavior.

---

# Missions

## Mission 1 — Understand Current Behavior

Read the legacy code before changing anything.

Success:
- identify code smells
- summarize current behavior

---

## Mission 2 — Add Characterization Tests

Protect current behavior with tests.

Success:
- tests pass
- edge cases covered

---

## Mission 3 — Refactor Safely

Improve readability while preserving behavior.

Success:
- tests remain green
- complexity reduced

---

# AI Employee Hints

## Code Smell Detective

> I found several suspects:
> long conditionals,
> hidden business rules,
> and duplicated logic.

## Marcus Rodriguez

> What behavior is currently unprotected by tests?

## Sarah Chen

> Keep changes incremental.
> Small safe commits beat heroic rewrites.

## Jenkins

```text
[TESTS] PASSED
Coverage: 64%
``` id="f76kml"
