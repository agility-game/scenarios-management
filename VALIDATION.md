# Validation

This repository validates Agility Game scenario markdown files by extracting YAML frontmatter and checking it against the scenario JSON Schema.

## Install dependencies

```bash
pip install -r requirements-dev.txt
```

## Validate scenarios

```bash
python scripts/validate-scenarios.py
```

## What is validated?

The validator checks each markdown scenario in:

```text
scenarios/*.md
```

against:

```text
schemas/scenario.schema.json
```

Only YAML frontmatter is strictly validated. The markdown body remains flexible for story, missions, hints, scoring notes, and gameplay instructions.
