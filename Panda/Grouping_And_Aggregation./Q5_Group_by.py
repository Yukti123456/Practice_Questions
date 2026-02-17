#Q5- Group by'departmnet'and calculate mean,median and std deviation of salaries.
import pandas as pd
import numpy as np

data = {
    "EmpID": [101, 102, 103, 104, 105, 106],
    "Name": ["Amit", "Riya", "John", "Pooja", "Rahul", "Neha"],
    "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"],
    "Age": [28, 32, 29, 26, 35, 30],
    "Salary": [45000, 52000, 60000, 48000, 65000, 54000],
    "City": ["Bhopal", "Indore", "Pune", "Bhopal", "Delhi", "Indore"]
}

df = pd.DataFrame(data)
result = df.groupby("Department")["Salary"].agg(
    Mean="mean",
    Std="std",
    Mode=lambda x: x.mode()[0]
)
print(result)
