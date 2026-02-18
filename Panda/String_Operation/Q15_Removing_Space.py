#Q15- Convert all text in 'City' column to title case and remove leading/trailing spaces.

import pandas as pd

df = pd.DataFrame({
    "EmpID": [101, 102, 103, 104, 105],
    "Name": ["Amit Sharma", "Riya Verma", "John Smith", "Pooja Mehta", "Rahul Jain"],
    "City": ["  bhopal", "DELHI  ", "  new york  ", "mUmBaI", "  indore  "],
    "Salary": [50000, 60000, 55000, 70000, 65000]
})

print("Before Cleaning:\n")
print(df)
df["City"] = df["City"].str.strip().str.title()

print("\nAfter Cleaning:\n")
print(df)
