SELECT e1.*
FROM employees e1
WHERE (
    SELECT COUNT(DISTINCT e2.salary)
    FROM employees e2
    WHERE e2.dept_id = e1.dept_id
    AND e2.salary > e1.salary
) < 3;
