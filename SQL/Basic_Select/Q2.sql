SELECT e.*
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
WHERE e.emp_name LIKE 'A%'
AND d.dept_name = 'Sales';
