df = pd.DataFrame({
    "Name": ["Yukti", "Amit", "Ravi"],
    "Salary": [50000, 70000, 60000]
})

sorted_df = df.sort_values(by="Name", key=lambda x: x.str.len())

print(sorted_df)
