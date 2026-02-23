SELECT emp_name,
salary,
salary - AVG(salary) OVER (PARTITION BY dept_id) AS difference
FROM employees;
