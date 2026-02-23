SELECT emp_name,
       hire_date,
       salary,
       SUM(salary) OVER (ORDER BY hire_date) AS running_total
FROM employees;
