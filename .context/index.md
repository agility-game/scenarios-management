---
module-name: "[PROJECT NAME]"
description: "[PROJECT DESCRIPTION]"
version: "1.1.0-RFC"
technologies:
  - "Markdown"
related-modules:
  - name: "[SIMPLE PROJECT ROOT]"
    path: [PATH]
    description: "[DESCRIPTION]"
    repository: "[REPOSITORY]"
architecture:
  style: "[ARCHITECTURE STYLE]"
  components:
    - name: "[COMPONENT NAME]"
      description: "[COMPONENT DESCRIPTION]"
  patterns:
    - name: "[PATTERN NAME]"
      usage: "[PATTERN USAGE DESCRIPTION]" 
status: "active"
---

# [REPOSITORY TITLE]

This repository contains [REPOSITORY CONTENT]. It is [DESCRIPTION].

## Repository Structure

The repository consists of:
- `CODEBASE-CONTEXT.md`: The main specification document
- `README.md`: Project overview and documentation
- `[DIRECTORY]`: [DESCRIPTION]

## Related Tools

The primary implementation tool for this specification is the `@codebase-context/cc-cli` package, which provides command-line utilities for:
- Creating and managing .context directories
- Validating context files against the specification
- Generating context documentation

For implementation details and usage, visit the [cc-cli package on NPM](https://www.npmjs.com/package/@codebase-context/cc-cli).
