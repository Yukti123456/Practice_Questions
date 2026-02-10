Q2. Extract all Phone Numbers from text in the format: (123) 456-7890,123-245-7890,123.456.7890

import re
text = """ 
For any Quries Call me at (123) 456-7890 or 987-654-3210.
Office number is 111.222.3333.
Invalid number: 1234567890
Thankyou
"""

pattern = r'\(?\d{3}\)?[.\-\s]\d{3}[.\-]\d{4}'

phones = re.findall(pattern, text)
print("Extracted phone numbers:", phones)
