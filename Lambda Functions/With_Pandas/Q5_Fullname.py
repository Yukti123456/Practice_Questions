import pandas as pd

df = pd.DataFrame({
    "First_Name": ["Yukti", "Amit"],
    "Last_Name": ["Sahu", "Sharma"]
})

df["Full_Name"] = df.apply(lambda x: x["First_Name"] + " " + x["Last_Name"], axis=1)

print(df)
