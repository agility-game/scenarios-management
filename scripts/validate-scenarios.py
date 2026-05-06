import json
import pathlib
import sys

import frontmatter
import jsonschema


ROOT = pathlib.Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "schemas" / "scenario.schema.json"
SCENARIOS_PATH = ROOT / "scenarios"


def main() -> int:
    with open(SCHEMA_PATH, "r", encoding="utf-8") as file:
        schema = json.load(file)

    validator = jsonschema.Draft7Validator(schema)
    errors_found = False

    scenario_files = sorted(SCENARIOS_PATH.glob("*.md"))

    if not scenario_files:
        print("No scenario markdown files found.")
        return 1

    for md_file in scenario_files:
        print(f"Validating: {md_file.name}")

        post = frontmatter.load(md_file)

        if not post.metadata:
            errors_found = True
            print("❌ Validation failed")
            print("  - frontmatter: missing YAML frontmatter")
            continue

        errors = sorted(
            validator.iter_errors(post.metadata),
            key=lambda error: list(error.path),
        )

        if errors:
            errors_found = True
            print("❌ Validation failed")

            for error in errors:
                path = ".".join(str(part) for part in error.path) or "<root>"
                print(f"  - {path}: {error.message}")
        else:
            print("✅ Valid")

    if errors_found:
        return 1

    print("\nAll scenarios valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
