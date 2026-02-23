DELETE FROM employees e
WHERE NOT EXISTS (
    SELECT 1
    FROM employee_projects ep
    JOIN projects p 
        ON ep.project_id = p.project_id
    WHERE ep.emp_id = e.emp_id
    AND p.start_date <= DATE(CONCAT(YEAR(CURDATE())-1,'-12-31'))
    AND (
        p.end_date IS NULL 
        OR p.end_date >= DATE(CONCAT(YEAR(CURDATE())-1,'-01-01'))
    )
);
