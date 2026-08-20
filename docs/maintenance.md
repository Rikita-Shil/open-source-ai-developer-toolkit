# Project Maintenance

This guide outlines basic maintenance practices for the Open Source AI Developer Toolkit.

## Regular Checks

Maintainers should periodically:

- Review open issues and pull requests.
- Run the metadata validation script.
- Check that documentation matches the current project structure.
- Review module examples for accuracy.
- Keep the changelog updated.

## Before Merging Changes

Run:

```bash
./scripts/validate-metadata.py
```

Confirm that validation passes and review the changed files before merging.

## Goal

Keep the toolkit consistent, maintainable, and easy for contributors to extend.
