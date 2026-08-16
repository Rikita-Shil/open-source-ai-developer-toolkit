missing = required_fields - metadata.keys()

if missing:
    errors.append(
        f"{metadata_file}: missing {', '.join(sorted(missing))}"
    )
    continue

valid_difficulties = {
    "Beginner",
    "Intermediate",
    "Advanced",
}

difficulty = metadata.get("difficulty")

if difficulty not in valid_difficulties:
    errors.append(
        f"{metadata_file}: invalid difficulty '{difficulty}'"
    )
    continue

print(f"✓ {metadata_file}")