UPDATE employees
SET salary = salary * 1.10
WHERE dept_id = (
    SELECT dept_id FROM departments WHERE dept_name='IT'
)
AND hire_date < '2020-01-01';
