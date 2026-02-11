#Q.5-Replace all multiple spaces with single space in a string.
import re
Text = """User     name:     Shreya    
Phone:     (123)   456-7890
Alternate    :   987-654-3210    
Email    :    example@test.com
Address:    221B     Baker   Street,     London"""

Pattern = r'[ ]+'

print(re.sub(Pattern,' ',Text))
