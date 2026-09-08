#!/usr/bin/env python3

import json
from pathlib import Path

SKILLS_DIR = Path("skills")
seen = {}
duplicates = []

for metadata_file in SKILLS_DIR.rglob("metadata.json"):
    try:
        with metadata_file.open(encoding="utf-8") as file:
            metadata = json.load(file)

        name = metadata.get("name")

        if not isinstance(name, str) or not name.strip():
            continue

        normalized_name = name.strip().lower()

        if normalized_name in seen:
            duplicates.append(
                (name, seen[normalized_name], metadata_file)
            )
        else:
            seen[normalized_name] = metadata_file

    except (json.JSONDecodeError, OSError) as error:
        print(f"Warning: Could not read {metadata_file}: {error}")

if duplicates:
    print("Duplicate module names found:")

    for name, first_file, second_file in duplicates:
        print(f"✗ {name}")
        print(f"  - {first_file}")
        print(f"  - {second_file}")

    raise SystemExit(1)

print(f"✓ No duplicate module names found across {len(seen)} modules.")
