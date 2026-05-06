import json
import pathlib
import sys

import frontmatter
import jsonschema
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent

SCHEMA_PATH = ROOT / "schemas" / "scenario.schema.json"
SCENARIOS_PATH = ROOT / "scenarios"

with open(SCHEMA_PATH, "r") as f:
    schema = json.load(f)

validator = jsonschema.Draft7Validator(schema)

errors_found = False

for md_file in SCENARIOS_PATH.glob("*.md"):
    print(f"Validating: {md_file.name}")

    post = frontmatter.load(md_file)

    errors = sorted(
        validator.iter_errors(post.metadata),
        key=lambda e: e.path
    )

    if errors:
        errors_found = True
        print("❌ Validation failed")

        for error in errors:
            path = ".".join(str(p) for p in error.path)
            print(f"  - {path}: {error.message}")

    else:
        print("✅ Valid")

if errors_found:
    sys.exit(1)

print("\nAll scenarios valid.")
