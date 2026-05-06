# Agility Game Scenario Schema Design

## Purpose

The Agility Game scenario schema defines a standard format for playable
software engineering scenarios.

Examples:
- refactoring katas
- buggy codebases
- deployment simulations
- testing exercises

## Goals

The schema should be:

- editor-friendly
- machine-readable
- extensible
- AI-compatible

## Design Principles

### Scenarios are AI-agent agnostic

Scenarios define:
- problems
- missions
- scoring
- capabilities

Scenarios do NOT hardcode specific AI employees.

### AI employees are resolved separately

Example roles:
- qa-engineer
- devops-engineer
- code-quality-investigator

NocoBase or runtime systems map these roles to actual AI employees.

### Runtime integration

The schema supports:
- automated testing
- CI/CD integration
- scoring systems
- multiplayer gameplay
