#Q9_Merge two dataframe:employees and department on dept_id,keeping all employess even without department match.

import pandas as pd

employee = pd.DataFrame({
    "emp_id": [101, 102, 103, 104, 105],
    "emp_name": ["Amit", "Neha", "Ravi", "Priya", "Karan"],
    "dept_id": [1, 2, 1, 3, 2],
    "salary": [50000, 60000, 55000, 70000, 65000]
})

print(employee)

department = pd.DataFrame({
    "dept_id": [1, 2, 3, 4],
    "dept_name": ["IT", "HR", "Finance", "Marketing"]
})

print(department)

merging = pd.merge(employee,department,on="dept_id",how="left")

print("DataFrame After merging:\n",merging)
