# Module Validation Specification

## Purpose

This document defines the validation requirements for every module in the Open Source AI Developer Toolkit.

## Required Structure

Each module must contain:

- README.md
- SKILL.md
- CHECKLIST.md
- examples.md
- sample-input.md
- metadata.json

## Metadata Validation

The metadata file should conform to:

schemas/module-metadata.schema.json

Required fields:

- name
- category
- version
- author
- difficulty

Optional fields:

- tags

## Validation Goals

Every module should pass the following checks:

- Required files exist.
- Markdown files are readable.
- Metadata follows the schema.
- Examples are present.
- Sample input is included.

## Future Automation

Planned GitHub Actions will automatically:

- Validate metadata.json files.
- Verify required module files.
- Report validation errors during pull requests.
