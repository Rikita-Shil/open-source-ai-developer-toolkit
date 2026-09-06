#!/usr/bin/env python3

import json
from pathlib import Path

SKILLS_DIR = Path("skills")
errors = []

for metadata_file in SKILLS_DIR.rglob("metadata.json"):
    try:
        with metadata_file.open(encoding="utf-8") as file:
            metadata = json.load(file)

        tags = metadata.get("tags")

        if not isinstance(tags, list) or not tags:
            errors.append(f"{metadata_file}: missing or empty tags")
            continue

        if not all(isinstance(tag, str) and tag.strip() for tag in tags):
            errors.append(f"{metadata_file}: contains invalid tags")
            continue

        print(f"✓ {metadata_file}")

    except (json.JSONDecodeError, OSError) as error:
        errors.append(f"{metadata_file}: {error}")

if errors:
    print("\nMetadata tag validation failed:")

    for error in errors:
        print(f"✗ {error}")

    raise SystemExit(1)

print("\n✓ All module metadata tags are valid.")
