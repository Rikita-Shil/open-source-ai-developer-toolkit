# Example

## Input

Check my SvelteKit project before I push it to GitHub.

## Output

Security Summary

The project is mostly safe, but environment files and debug logs should be reviewed.

Critical Risks

- Do not commit .env files.
- Remove temporary console logs containing URLs or keys.

Suggested Fixes

- Add .env files to .gitignore.
- Move secrets into environment variables.
- Review Supabase RLS policies.

Verdict

Needs Minor Changes before pushing.
