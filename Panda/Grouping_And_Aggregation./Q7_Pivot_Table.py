#Q7_Create a pivot table showing average salary by Department and Age group (20-30,31-40,41+).

import pandas as pd

data = {
    "Name": ["Amit", "Neha", "Ravi", "Priya", "Karan", "Anjali", "Rahul"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance", "IT"],
    "Age": [25, 32, 45, 29, 38, 41, 27],
    "Salary": [50000, 60000, 90000, 55000, 65000, 80000, 52000]
}

df = pd.DataFrame(data)

print(df)

bins = [20, 30, 40, 100]
labels = ["20-30", "31-40", "41+"]

df["Age_Group"] = pd.cut(df["Age"], bins=bins, labels=labels)

print(df)
bins = [20, 30, 40, 100]
labels = ["20-30", "31-40", "41+"]

df["Age_Group"] = pd.cut(df["Age"], bins=bins, labels=labels)

print(df)

pivot_table = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="Age_Group",
    aggfunc="mean"
)

print(pivot_table)

