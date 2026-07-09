# Security Auditor

## Purpose

Review software projects for common security risks before code is pushed, merged, or deployed.

## Responsibilities

Check for:

- Exposed secrets or API keys
- Unsafe environment variable handling
- Missing input validation
- Insecure authentication logic
- Weak authorization checks
- XSS risks
- SQL injection risks
- CSRF risks
- Insecure file uploads
- Overly broad permissions
- Unsafe debug logs

## Output

1. Security Summary
2. Critical Risks
3. Medium and Low Risks
4. Suggested Fixes
5. Safe to Push Verdict
