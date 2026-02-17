# Q18_ Use group by with multiple aggregations:count of employees,sum of salaries,max age per separtment.
import pandas as pd
df = pd.read_excel("data.csv")
result = df.groupby("Department").agg(
    Total_Employess=("EmpID", "count"),
    Total_Salary=("Salary", "sum"),
    Max_Age=("Age", "max")
)
print(result)
