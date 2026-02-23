SELECT d.dept_name,
SUM(CASE WHEN YEAR(e.hire_date)=2022 THEN 1 ELSE 0 END) AS "2022",
SUM(CASE WHEN YEAR(e.hire_date)=2023 THEN 1 ELSE 0 END) AS "2023",
SUM(CASE WHEN YEAR(e.hire_date)=2024 THEN 1 ELSE 0 END) AS "2024"
FROM departments d
LEFT JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_name;
