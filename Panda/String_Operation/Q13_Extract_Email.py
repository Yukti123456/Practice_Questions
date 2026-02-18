#Q13-Extract domain from email addresses.

import pandas as pd

df = pd.DataFrame({
    "Name": [" Amit Sharma ", "Riya Verma", "JOHN sMITH"],
    "Email": ["amit@gmail.com", "riya@yahoo.com", "john123@outlook.com"],
    "City": ["Bhopal", "Indore", "Delhi"]
})
df["Domain"] = df["Email"].str.split("@").str[1]
print(df)
