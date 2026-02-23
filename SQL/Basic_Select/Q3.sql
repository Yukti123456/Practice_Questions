SELECT d.dept_name, COUNT(e.emp_id) AS emp_count
FROM departments d
JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_name
HAVING COUNT(e.emp_id) > 5;
