#Q16- Filter rows where 'Name' contains 'John' or 'Jane'(case-insensitive')

import pandas as pd

df = pd.DataFrame({
    "Name": ["John Smith", "Jane Doe", "Amit Sharma", "Johnny Walker", "Riya"]
})

print(df)
filtered = df[df["Name"].str.contains(r"\b(John|Jane)\b", case=False, na=False)]
print("After Filting Data\n: ",filtered)
