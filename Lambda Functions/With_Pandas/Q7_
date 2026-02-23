import pandas as pd

df = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Salary": [40000, 60000, 70000],
    "Age": [25, 45, 35]
})

filtered = df[df.apply(lambda row: row["Salary"] > 50000 and row["Age"] < 40, axis=1)]

print(filtered)
