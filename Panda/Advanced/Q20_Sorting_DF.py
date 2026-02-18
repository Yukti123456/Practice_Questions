import pandas as pd
data = pd.DataFrame({
    "EmpID": [101, 102, 103, 104, 105, 106],
    "Name": ["Amit", "Riya", "John", "Pooja", "Rahul", "Neha"],
    "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"],
    "Age": [28, 32, 29, 26, 35, 30],
    "Salary": [45000, 52000, 60000, 48000, 65000, 54000],
    "City": ["Bhopal", "Indore", "Pune", "Bhopal", "Delhi", "Indore"]
})
sorted = data.sort_values(by =["Department","Salary"], ascending=[True, False])

print("Datframe after sorting:\n"sorted)
