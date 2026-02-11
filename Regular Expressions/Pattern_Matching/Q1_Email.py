Q1- Validate email addresses: Must contain @ Symbol, Domain, and extension.


import re
emails = [
    "shreya.rajput@gmail.com",
    "abc@yahoo.org",
    "user@domain.in",
    "wrongemail.com",
    "user@domain"
]

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

for email in emails:
    if re.match(pattern, email):
        print(email, ": Valid")
    else:
        print(email, ":  Invalid")
