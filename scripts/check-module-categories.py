#!/usr/bin/env python3

import json
from pathlib import Path

SKILLS_DIR = Path("skills")

VALID_CATEGORIES = {
    "Software Engineering",
    "Security",
    "Backend",
    "Frontend",
    "Cloud",
    "AI",
    "Career",
    "University",
}

errors = []

for metadata_file in SKILLS_DIR.rglob("metadata.json"):
    try:
        with metadata_file.open(encoding="utf-8") as file:
            metadata = json.load(file)

        category = metadata.get("category")

        if category not in VALID_CATEGORIES:
            errors.append(
                f"{metadata_file}: invalid category '{category}'"
            )
        else:
            print(f"✓ {metadata_file}: {category}")

    except (json.JSONDecodeError, OSError) as error:
        errors.append(f"{metadata_file}: {error}")

if errors:
    print("\nModule category validation failed:")

    for error in errors:
        print(f"✗ {error}")

    raise SystemExit(1)

print("\n✓ All module categories are valid.")
