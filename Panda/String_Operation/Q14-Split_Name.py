#Q14- Split "Full_Name" column into 'First_Name' and 'Last_Name'.

import pandas as pd

df = pd.DataFrame({
    "full_name": ["Amit Sharma", "Riya Verma", "John Smith"]
})

print(df)
df[["First Name","Last Name"]] = df["full_name"].str.split(" ",expand=True)
print(df)
