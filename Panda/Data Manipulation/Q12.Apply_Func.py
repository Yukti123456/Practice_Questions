#Q12_Apply a custom function to calculate tax(20% if salary > 60000,else 15%) using apply().

import pandas as pd

data = pd.DataFrame({
    "EmpID": [101, 102, 103, 104, 105, 106],
    "Name": ["Amit", "Riya", "John", "Pooja", "Rahul", "Neha"],
    "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"],
    "Age": [28, 32, 29, 26, 35, 30],
    "Salary": [45000, 52000, 60000, 48000, 65000, 54000],
    "City": ["Bhopal", "Indore", "Pune", "Bhopal", "Delhi", "Indore"]
})

def calc(Salary):
    if (Salary > 60000):
        Salary = Salary * 0.20
        return Salary
    else:
        Salary = Salary * 0.15
        return Salary

data["Tax"] = data["Salary"].apply(calc)
print("Tax:\n",data)
