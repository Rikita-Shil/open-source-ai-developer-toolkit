#!/usr/bin/env python3

import json
from pathlib import Path

SKILLS_DIR = Path("skills")

required_fields = {
    "name",
    "category",
    "version",
    "author",
    "difficulty",
}

errors = []

for metadata_file in SKILLS_DIR.rglob("metadata.json"):
    try:
        with metadata_file.open(encoding="utf-8") as file:
            metadata = json.load(file)

        missing = required_fields - metadata.keys()

        if missing:
            errors.append(
                f"{metadata_file}: missing {', '.join(sorted(missing))}"
            )
        else:
            print(f"✓ {metadata_file}")

    except json.JSONDecodeError as error:
        errors.append(f"{metadata_file}: invalid JSON ({error})")

if errors:
    print("\nValidation failed:")

    for error in errors:
        print(f"✗ {error}")

    raise SystemExit(1)

print("\nAll module metadata files passed validation.")
