# Example

## Input

Create tests for a login form with email and password fields.

## Expected Output

### Unit Tests

- Accept a valid email format.
- Reject an invalid email format.
- Reject an empty password.
- Disable submission while the request is running.

### Integration Tests

- Submit valid credentials and redirect the user.
- Display an error for invalid credentials.
- Preserve the form state after a failed request.

### Edge Cases

- Extremely long email input.
- Leading and trailing spaces.
- Multiple rapid submissions.

### Manual Verification

- Test keyboard-only navigation.
- Confirm the error message is visible.
- Confirm the password is not exposed in logs.
