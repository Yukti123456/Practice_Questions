Q10_Concatenate 3 dataframe vertically and remove duplicates rows.
  
import pandas as pd

df1 = pd.DataFrame({
    "emp_id": [101, 102, 103],
    "emp_name": ["Amit", "Neha", "Ravi"],
    "salary": [50000, 60000, 55000]
})
df2 = pd.DataFrame({
    "emp_id": [104, 105, 102],   # 102 is duplicate
    "emp_name": ["Priya", "Karan", "Neha"],
    "salary": [70000, 65000, 60000]
})
df3 = pd.DataFrame({
    "emp_id": [106, 103],   # 103 duplicate
    "emp_name": ["Priya", "Ravi"],
    "salary": [72000, 55000]
})
result = pd.concat([df1,df2,df3],ignore_index=True).drop_duplicates(subset="emp_id")
print(result)
