# Troubleshooting

## Plugin Does Not Load

Check that `.claude-plugin/plugin.json` exists and contains valid JSON.

## Skill Is Not Available

Confirm the skill contains a valid `SKILL.md` file and is located inside the correct skills directory.

## Metadata Validation Fails

Run:

```bash
./scripts/validate-metadata.py
```

Review the reported module and correct any missing or invalid metadata.

## Git Issues

Use `git status` before committing to check which files have been modified or added.
