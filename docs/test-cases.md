# Test cases

| ID | Action | Expected result |
|---|---|---|
| T01 | Register a unique email/password | User and blank profile created; JWT returned |
| T02 | Login with wrong password | HTTP 401; no token |
| T03 | Create expense with negative amount | HTTP 422 validation error |
| T04 | Request another user's expense ID | HTTP 404; authorization boundary preserved |
| T05 | Add, update and delete investment | CRUD change persists and audit trigger records update |
| T06 | Run 5,000 simulations | Percentiles, chart paths and goal probability returned |
| T07 | Run `CALL generate_expense_report(1)` | Per-category aggregate report ordered by total |
| T08 | Insert goal with historical target date | MySQL trigger rejects the row |
| T09 | Query portfolio view | Allocation percentage totals to approximately 100% per user |
| T10 | Add income and expense then dashboard | Card totals and transparent health breakdown update |
