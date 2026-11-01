USE futurefinance;
DELIMITER //
CREATE PROCEDURE calculate_monthly_financial_summary(IN p_user_id BIGINT) BEGIN SELECT * FROM monthly_financial_summary WHERE user_id=p_user_id ORDER BY month DESC; END//
CREATE PROCEDURE calculate_goal_progress(IN p_user_id BIGINT) BEGIN SELECT *,ROUND(GREATEST(0,target_amount-current_amount)/GREATEST(1,TIMESTAMPDIFF(MONTH,CURDATE(),target_date)),2) required_monthly_savings FROM goal_progress_summary WHERE user_id=p_user_id; END//
CREATE PROCEDURE generate_expense_report(IN p_user_id BIGINT) BEGIN SELECT category,SUM(amount) total,AVG(amount) average_transaction,COUNT(*) transactions FROM expenses WHERE user_id=p_user_id GROUP BY category HAVING SUM(amount)>0 ORDER BY total DESC; END//
DELIMITER ;
