# ADR 0001: Project Architecture

## Status

Accepted

## Context

The Open Source AI Developer Toolkit is expected to grow into a collection of reusable AI-powered developer modules.

To keep the repository maintainable, each module follows a consistent structure and is grouped by domain.

## Decision

Every module will contain:

- README.md
- SKILL.md
- CHECKLIST.md
- examples.md
- sample-input.md
- metadata.json

Modules will be organised into categories such as:

- Software Engineering
- Backend
- Frontend
- Security
- Cloud
- Career
- AI

## Consequences

### Benefits

- Consistent repository structure
- Easier onboarding for contributors
- Scalable architecture
- Easier maintenance
- Reusable module template

### Trade-offs

- Slightly more files per module
- Contributors must follow the project structure
