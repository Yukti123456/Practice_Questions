SELECT YEAR(hire_date) AS hire_year,
       COUNT(*) AS emp_count
FROM employees
GROUP BY YEAR(hire_date);
