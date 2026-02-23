SELECT emp_name,
salary,
LAG(salary) OVER (ORDER BY hire_date) AS previous_salary,
LEAD(salary) OVER (ORDER BY hire_date) AS next_salary
FROM employees;
