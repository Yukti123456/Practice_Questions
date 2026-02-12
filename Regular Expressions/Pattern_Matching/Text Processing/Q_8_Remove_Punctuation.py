#Q_8- Remove all punctuation from text except periods and commas.

import re

Text = """ Hello! My name is Riya@ Sharma, & I live in Bhopal, India*.
          Yesterday, I met Mr. Verma (at) 10:30 a.m. — 
          he said:, "#Are you coming to the meeting\?"""
         
Pattern = r'[^\w\s\.,]'

print(re.sub(Pattern,"",Text))
