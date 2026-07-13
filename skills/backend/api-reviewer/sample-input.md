# Sample API Review

The following Express.js endpoint can be used to test the API Reviewer module.

```javascript
app.post("/api/users", async (req, res) => {

    const { name, email } = req.body;

    const user = await db.users.insert({
        name,
        email
    });

    res.status(200).json(user);

});
```

## Things the Reviewer Should Identify

- Missing request validation
- Missing authentication
- Missing authorization
- No error handling
- Incorrect success status (201 is more appropriate)
- No rate limiting
- Missing input sanitisation
- No logging
- Missing API documentation

Expected overall score:

4/10

Deployment verdict:

Requires Significant Improvements