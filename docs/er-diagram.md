# FutureFinance ER diagram

```mermaid
erDiagram
  USERS ||--|| FINANCIAL_PROFILES : owns
  USERS ||--o{ INCOME : records
  USERS ||--o{ EXPENSES : records
  USERS ||--o{ INVESTMENTS : owns
  USERS ||--o{ FINANCIAL_GOALS : sets
  USERS ||--o{ LOANS : holds
  USERS ||--o{ SCENARIOS : creates
  USERS ||--o{ SIMULATION_RUNS : runs
  USERS ||--o{ AUDIT_LOGS : generates
  USERS { bigint id PK string email UK string password_hash }
  FINANCIAL_PROFILES { bigint id PK bigint user_id FK decimal monthly_income decimal savings }
  INCOME { bigint id PK bigint user_id FK decimal amount date received_on }
  EXPENSES { bigint id PK bigint user_id FK string category decimal amount date spent_on }
  INVESTMENTS { bigint id PK bigint user_id FK string investment_type decimal current_value }
  FINANCIAL_GOALS { bigint id PK bigint user_id FK decimal target_amount decimal current_amount }
  LOANS { bigint id PK bigint user_id FK decimal outstanding_amount }
  SCENARIOS { bigint id PK bigint user_id FK decimal expense_change_pct }
  SIMULATION_RUNS { bigint id PK bigint user_id FK int simulations decimal goal_target }
  AUDIT_LOGS { bigint id PK bigint user_id FK string action string table_name }
```

`users → financial_profiles` is one-to-one. Every other shown user relationship is one-to-many. Lookup values are constrained enums: this avoids duplicate category/type records while retaining 3NF for the data held by this application.
