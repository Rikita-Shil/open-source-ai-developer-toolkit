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

valid_difficulties = {
    "Beginner",
    "Intermediate",
    "Advanced",
}

errors = []
passed = 0
total = 0

for metadata_file in sorted(SKILLS_DIR.rglob("metadata.json")):
    total += 1

    try:
        with metadata_file.open(encoding="utf-8") as file:
            metadata = json.load(file)

        if not isinstance(metadata, dict):
            errors.append(
                f"{metadata_file}: metadata must be a JSON object"
            )
            continue

        missing = required_fields - metadata.keys()

        if missing:
            errors.append(
                f"{metadata_file}: missing fields "
                f"{', '.join(sorted(missing))}"
            )
            continue

        empty_fields = [
            field
            for field in required_fields
            if metadata[field] is None
            or (
                isinstance(metadata[field], str)
                and not metadata[field].strip()
            )
        ]

        if empty_fields:
            errors.append(
                f"{metadata_file}: empty fields "
                f"{', '.join(sorted(empty_fields))}"
            )
            continue

        difficulty = metadata["difficulty"]

        if not isinstance(difficulty, str) or difficulty not in valid_difficulties:
            errors.append(
                f"{metadata_file}: invalid difficulty '{difficulty}' "
                f"(expected Beginner, Intermediate, or Advanced)"
            )
            continue

        passed += 1
        print(f"✓ {metadata_file}")

    except json.JSONDecodeError as error:
        errors.append(
            f"{metadata_file}: invalid JSON "
            f"(line {error.lineno}, column {error.colno})"
        )

print("\nMetadata Validation Summary")
print("-------------------------")
print(f"Files checked: {total}")
print(f"Passed: {passed}")
print(f"Failed: {len(errors)}")

if errors:
    print("\nValidation errors:")

    for error in errors:
        print(f"✗ {error}")

    raise SystemExit(1)

print("\n✓ All module metadata files passed validation.")
