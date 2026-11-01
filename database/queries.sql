USE futurefinance;
-- 1 GROUP BY monthly category report
SELECT category,SUM(amount) FROM expenses WHERE user_id=? AND spent_on>=DATE_FORMAT(CURDATE(),'%Y-%m-01') GROUP BY category ORDER BY SUM(amount) DESC;
-- 2 subquery: users below a savings-rate threshold
SELECT u.name FROM users u JOIN financial_health_summary h ON h.user_id=u.id WHERE h.savings_rate<20;
-- 3 expenses exceed income
SELECT user_id,month FROM monthly_financial_summary WHERE monthly_expenses>monthly_income;
-- 4 portfolio allocation
SELECT * FROM investment_portfolio_summary WHERE user_id=?;
-- 5 goals behind schedule
SELECT * FROM goal_progress_summary WHERE user_id=? AND progress_pct < (DATEDIFF(CURDATE(),DATE_SUB(target_date,INTERVAL 1 YEAR))/365)*100;
-- 6 highest spend by user with window function
WITH ranked AS (SELECT user_id,category,SUM(amount) total,DENSE_RANK() OVER(PARTITION BY user_id ORDER BY SUM(amount) DESC) r FROM expenses GROUP BY user_id,category) SELECT * FROM ranked WHERE r=1;
-- 7 transaction example: create an expense and audit succeeds atomically
START TRANSACTION; INSERT INTO expenses(user_id,category,amount,spent_on) VALUES(1,'Food',450,CURDATE()); COMMIT;
