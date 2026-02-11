#Q.5-Validate password:8-15 characters, at least one uppercase, one lowercase, one digit, one special character.

import re

passwords = ["Shreya@123","test456","valiD23@","123@123","Invid@1"]

Pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^a-zA-Z0-9]).{8,15}$"

for i in passwords:
    if re.search(Pattern, i):
        print(i, "→ Password Criteria Match")
    else:
        print(i, "→ Password Criteria doesn't Match")
