SELECT e.emp_name
FROM employees e
WHERE NOT EXISTS (
    SELECT p.project_id
    FROM projects p
    WHERE NOT EXISTS (
        SELECT 1
        FROM employee_projects ep
        WHERE ep.emp_id = e.emp_id
        AND ep.project_id = p.project_id
    )
);
