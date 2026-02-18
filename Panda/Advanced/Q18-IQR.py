import pandas as pd

df = pd.DataFrame({
    "emp_id": [101, 102, 103, 104, 105],
    "emp_name": ["Amit", "Neha", "Ravi", "Priya", "Karan"],
    "dept_id": [1, 2, 1, 3, 2],
    "salary": [350000, 60000, 55000, 20000, 65000]
})
Q1 = df["salary"].quantile(0.25)
Q3 = df["salary"].quantile(0.75)
Iqr = Q3 - Q1
lower_bound = Q1 - (1.5 * Iqr)
upper_bound = Q3 + (1.5 * Iqr)
df_clean = df[(df["salary"] > lower_bound) & (df["salary"] < upper_bound)]
print(df_clean)
