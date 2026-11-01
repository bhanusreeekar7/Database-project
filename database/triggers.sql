USE futurefinance;
DELIMITER //
CREATE TRIGGER audit_expense_insert AFTER INSERT ON expenses FOR EACH ROW BEGIN INSERT INTO audit_logs(user_id,action,table_name,record_id,details) VALUES(NEW.user_id,'INSERT','expenses',NEW.id,JSON_OBJECT('amount',NEW.amount,'category',NEW.category)); END//
CREATE TRIGGER audit_investment_update AFTER UPDATE ON investments FOR EACH ROW BEGIN INSERT INTO audit_logs(user_id,action,table_name,record_id,details) VALUES(NEW.user_id,'UPDATE','investments',NEW.id,JSON_OBJECT('old_value',OLD.current_value,'new_value',NEW.current_value)); END//
CREATE TRIGGER validate_goal_date BEFORE INSERT ON financial_goals FOR EACH ROW BEGIN IF NEW.target_date<=CURDATE() THEN SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='Goal target date must be in the future'; END IF; END//
DELIMITER ;
