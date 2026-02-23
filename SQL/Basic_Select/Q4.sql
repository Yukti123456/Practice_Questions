SELECT *
FROM employees
WHERE hire_date >= CURDATE() - INTERVAL 2 YEAR;
