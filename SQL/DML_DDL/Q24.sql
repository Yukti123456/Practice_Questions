SELECT emp_name, hire_date, COUNT(*)
FROM employees
GROUP BY emp_name, hire_date
HAVING COUNT(*) > 1;
