SELECT p.project_name, SUM(ep.hours_worked) AS total_hours
FROM projects p
JOIN employee_projects ep ON p.project_id = ep.project_id
GROUP BY p.project_name;
