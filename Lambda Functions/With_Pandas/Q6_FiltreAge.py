df = pd.DataFrame({
    "Name": ["William", "Bhumi", "Shreya"],
    "Age": [78, 40, 13]
})

df["Category"] = df["Age"].apply(
    lambda x: "Young" if x < 30 else ("Middle" if x <= 50 else "Senior")
)

print(df)
