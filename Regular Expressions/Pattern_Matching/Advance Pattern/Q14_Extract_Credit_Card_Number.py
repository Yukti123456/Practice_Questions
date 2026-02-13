#Q.14_Extract credit card numbers(groups of 4 digits separated by spaces or hypens).

import re

Text ="""Riya used her card 1234 5678 9012 3456 for shopping.
      Her brother mistakenly entered 9876-5432-1098-7654 on another site.

      Invalid entries found were:
      1234567890123456,
      1234 567 8901 2345,
      1234-5678-9012."""
      
Pattern = r'\b(?:\d{4}[-\s]){3}\d{4}\b'

Matches= re.findall(Pattern,Text)

print("Credit Card Numbers: ",Matches)
