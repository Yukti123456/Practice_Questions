SELECT *
FROM (
    SELECT e.*,
           NTILE(10) OVER (PARTITION BY dept_id ORDER BY salary DESC) AS percentile_rank
    FROM employees e
) t
WHERE percentile_rank = 1;
