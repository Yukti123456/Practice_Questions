CREATE VIEW emp_project_summary AS
SELECT e.emp_name,
       d.dept_name,
       COUNT(ep.project_id) AS project_count
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id
LEFT JOIN employee_projects ep ON e.emp_id = ep.emp_id
GROUP BY e.emp_name, d.dept_name;
