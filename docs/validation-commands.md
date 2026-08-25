# Validation Commands

The Open Source AI Developer Toolkit includes validation scripts to help maintain repository quality.

## Run All Checks

```bash
./scripts/validate-all.sh
```

This is the recommended command before committing or opening a pull request.

## Validate Metadata

```bash
./scripts/validate-metadata.py
```

Checks module metadata for required fields and valid values.

## Validate Module Structure

```bash
./scripts/check-module-structure.py
```

Checks that modules contain the required files.

## Recommended Workflow

Before submitting changes:

1. Run the validation commands.
2. Fix any reported errors.
3. Review changes with `git status`.
4. Commit only the intended files.
