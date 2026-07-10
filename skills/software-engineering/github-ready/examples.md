# Example

## Input

Check whether my SvelteKit project is ready to push to GitHub.

## Expected Output

### Repository Summary

The project has a clear structure and a README, but it requires a final security review.

### Blocking Issues

- A production environment file is still tracked.
- Temporary console logs expose a service URL.

### Recommended Improvements

- Remove tracked environment files.
- Confirm the build succeeds.
- Add setup instructions to the README.

### Safe Git Commands

```bash
git status
git diff
git ls-files | grep -E '(^|/)\.env'

Then check:

```bash
git status
git log --oneline -5
eof

