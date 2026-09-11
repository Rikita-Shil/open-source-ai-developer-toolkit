#!/usr/bin/env python3

import json
from pathlib import Path

SKILLS_DIR = Path("skills")
errors = []

for metadata_file in SKILLS_DIR.rglob("metadata.json"):
    try:
        with metadata_file.open(encoding="utf-8") as file:
            metadata = json.load(file)

        name = metadata.get("name")

        if not isinstance(name, str) or not name.strip():
            errors.append(f"{metadata_file}: missing or invalid module name")
        else:
            print(f"✓ {metadata_file}: {name}")

    except (json.JSONDecodeError, OSError) as error:
        errors.append(f"{metadata_file}: {error}")

if errors:
    print("\nModule name validation failed:")
    for error in errors:
        print(f"✗ {error}")
    raise SystemExit(1)

print("\n✓ All module names are valid.")
