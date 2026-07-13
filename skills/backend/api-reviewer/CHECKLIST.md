# API Reviewer Checklist

Use this checklist when reviewing an API.

## API Design

- [ ] Resource names are consistent
- [ ] URLs follow REST conventions
- [ ] HTTP methods are used correctly
- [ ] API versioning is defined where appropriate

---

## Request Validation

- [ ] Required fields are validated
- [ ] Invalid inputs return appropriate errors
- [ ] Input sanitisation is present
- [ ] Data types are validated

---

## Authentication & Authorization

- [ ] Authentication is required where necessary
- [ ] Authorization rules are enforced
- [ ] Sensitive endpoints are protected
- [ ] Secrets are not exposed

---

## Response Quality

- [ ] Correct HTTP status codes
- [ ] Consistent JSON responses
- [ ] Helpful error messages
- [ ] No sensitive information in responses

---

## Security

- [ ] SQL Injection risks reviewed
- [ ] XSS risks reviewed
- [ ] CORS configuration reviewed
- [ ] Rate limiting considered

---

## Performance

- [ ] Pagination implemented where needed
- [ ] Database queries are efficient
- [ ] Large responses avoided
- [ ] Caching considered

---

## Documentation

- [ ] API endpoints documented
- [ ] Authentication documented
- [ ] Request examples included
- [ ] Response examples included

---

## Final Review

- [ ] Production ready
- [ ] No critical issues remain