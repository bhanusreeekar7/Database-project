# FutureFinance

**An explainable AI-driven financial decision intelligence platform with Monte Carlo scenario simulation.** FutureFinance is a DBMS-first academic project: the web interface is backed by a normalized MySQL model, secure REST API, database reports, audit trail, views, stored procedures, triggers, indexes, and transaction examples.

## Problem and objectives

People see balances but struggle to connect income, spending, goals, portfolio risk, and possible futures. FutureFinance consolidates that information, quantifies uncertainty with Monte Carlo simulation, and gives rules-based recommendations that expose their evidence rather than acting as a black box.

Its objectives are to demonstrate relational database design to 3NF; provide authenticated financial CRUD; deliver analytic reporting; model goal and portfolio outcomes; and explain every financial-health score and recommendation.

## Features

- JWT login/registration with bcrypt passwords and per-user authorization.
- Income, expenses, investments, and goal CRUD operations.
- Dashboard cards, category chart, health-score breakdown, and INR formatting.
- Thousands of stochastic investment paths with percentile outcomes and goal probability.
- Explainable rules for low savings, emergency-fund gaps, and highest-spend review.
- What-if scenario persistence and a MySQL audit trail.
- MySQL views, stored procedures, triggers, indexed columns, joins, aggregates, subqueries, window functions, and transaction sample.

## Architecture

```text
React + Vite + Recharts  →  FastAPI + SQLAlchemy + JWT  →  MySQL 8
                                      │
                         NumPy Monte Carlo / explainable rules
```

## Database architecture

The database scripts are deliberately separate so they can be demonstrated independently:

- `database/schema.sql` — keys, constraints, relationships and indexes.
- `database/seed.sql` — five representative users and financial records.
- `database/views.sql` — five reporting views.
- `database/procedures.sql` — monthly summary, goal progress, and expense report procedures.
- `database/triggers.sql` — audit, goal validation, and timestamp maintenance.
- `database/queries.sql` — evaluation-ready SELECT, JOIN, GROUP BY, HAVING, window, subquery, and transaction examples.

See [the ER diagram](docs/er-diagram.md). The schema reaches 3NF: each table represents one entity; non-key attributes depend on its key; user, category, and investment facts are not repeated in transactional rows. Fixed controlled vocabularies use MySQL ENUM constraints to prevent misspelled categories.

## Install and run

Prerequisites: MySQL 8+, Python 3.11+, and Node 20+.

```powershell
# 1. Database (run in this order)
mysql -u root -p < database/schema.sql
mysql -u root -p futurefinance < database/seed.sql
mysql -u root -p futurefinance < database/views.sql
mysql -u root -p futurefinance < database/procedures.sql
mysql -u root -p futurefinance < database/triggers.sql

# 2. API
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
uvicorn app.main:app --reload

# 3. UI (new terminal)
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`. The seeded-account hash is documented as `FutureFinance@123`; create a fresh account if your bcrypt implementation uses a different compatible hash. API docs appear at `http://localhost:8000/docs`.

## API reference

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/auth/register`, `/api/auth/login` | Create session / issue JWT |
| GET/POST/PUT/DELETE | `/api/income`, `/api/expenses`, `/api/investments`, `/api/goals` | Protected CRUD |
| GET | `/api/dashboard`, `/api/financial-health`, `/api/insights` | Derived reporting |
| POST/GET | `/api/simulation/run`, `/api/simulation/{id}` | Store/run estimate |
| GET/POST | `/api/scenarios` | Save what-if assumptions |

Pass `Authorization: Bearer <token>` for protected endpoints. FastAPI/Pydantic validates inputs; SQLAlchemy parameterizes database access; foreign-key ownership checks prevent cross-user reads/writes.

## Methodologies

**Monte Carlo.** For every month, return is sampled from a normal distribution with user-provided expected annual return and volatility, transformed to a monthly mean and standard deviation. The model compounds the current portfolio and adds contribution. It reports p10/p25/median/p75/p90 final values and the share of paths achieving the goal. It is an estimate, not investment advice or a guarantee.

**Explainable AI and health.** This intentionally starts with deterministic, inspectable rules, designed to be replaceable by an ML/LLM service later. Insights include the triggering metric, reason, expected impact, and strength. Health scoring publishes its five components: savings rate (25), debt management (25), emergency fund (20), investment diversification (15), goal progress (15).

## Academic demonstration checklist

Run the scripts and show the dashboard, the simulation endpoint, `CALL generate_expense_report(1)`, an insert that appears in `audit_logs`, and the queries file. This visibly covers CRUD, normalization, PK/FK/unique/check constraints, joins, aggregates, GROUP BY/HAVING, subqueries, views, stored procedures, triggers, transactions, indexes, reporting, and API-to-database interaction.

## Tests and viva

See [test cases](docs/test-cases.md).

1. **Why 3NF?** It avoids update anomalies by storing each fact once under the key that determines it.
2. **Why use indexes?** User/date and user/type report filters avoid full-table scans as data grows.
3. **Why a trigger and an audit table?** The database records important data changes even if a different client writes to it.
4. **Why SQLAlchemy?** It maps relations to application models and uses parameterized statements, reducing SQL-injection risk.
5. **Why Monte Carlo instead of one return estimate?** It presents an outcome range and target probability under uncertainty.
6. **Why is the AI explainable?** Every rule includes its data, threshold, reason, and likely impact.

## Future enhancements

Budget import, recurring transactions, scenario comparison charts, database-backed simulation path results, scheduled reports, and an advisory model with a human-review workflow.
