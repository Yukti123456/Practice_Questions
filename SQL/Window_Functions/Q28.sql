SELECT emp_name,
dept_id,
salary,
SUM(salary) OVER (PARTITION BY dept_id ORDER BY salary) /
SUM(salary) OVER (PARTITION BY dept_id) * 100 AS cumulative_percent
FROM employees;
