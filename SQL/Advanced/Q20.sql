SELECT emp_id + 1 AS missing_id
FROM employees
WHERE (emp_id + 1) NOT IN (SELECT emp_id FROM employees);
