SELECT d.dept_name
FROM departments d
WHERE NOT EXISTS (
    SELECT 1
    FROM employees e
    JOIN employee_projects ep ON e.emp_id = ep.emp_id
    WHERE e.dept_id = d.dept_id
);
