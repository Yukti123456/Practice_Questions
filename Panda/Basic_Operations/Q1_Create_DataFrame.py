#Q1. Create DataFrame and filter Salary

import pandas as pd

data = {
    "Name": ["Amit", "Riya", "John","Shreya"],
    "Age": [24, 27, 21,23],
    "Salary": [45000, 60000, 55000,30000]
}

df = pd.DataFrame(data)

# Filter employees with salary > 50000
filtered_df = df[df["Salary"] > 50000]
print(filtered_df)
