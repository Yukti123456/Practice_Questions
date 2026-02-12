import re

Text = """ Yesterday, Riya visited Delhi with her Friend Aman.
         They went to India Gate and later had Coffee at Starbucks. 
         On Sunday,they planned to travel to Mumbai by Train."""
         
Pattern = r'\b[A-Z][a-z]*\b'

print(re.findall(Pattern,Text))
