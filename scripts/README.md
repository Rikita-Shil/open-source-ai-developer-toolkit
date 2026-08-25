# Validation Scripts

This directory contains utilities used to validate the Open Source AI Developer Toolkit.

## Available Scripts

### validate-all.sh

Runs all repository validation checks.

```bash
./scripts/validate-all.sh
```

### validate-metadata.py

Checks module metadata files for required fields and valid values.

```bash
./scripts/validate-metadata.py
```

### check-module-structure.py

Checks that developer modules contain the required files.

```bash
./scripts/check-module-structure.py
```

## Before Committing

Run:

```bash
./scripts/validate-all.sh
```

Resolve any reported errors before submitting changes.
