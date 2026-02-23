SELECT emp_name, dept_id, salary,
RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS salary_rank
FROM employees;
