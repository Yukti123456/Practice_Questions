#Q6- Find the top 3 highest-paid employees in each department.
import pandas as pd
df = pd.read_excel("data.csv)
top3 = df.sort_values(["Department", "Salary"], ascending=[True, False].groupby("Department").head(3))
print(top3)
