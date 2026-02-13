#Q.16_Find repeated words in a sentence (e.g "the the" or "is is")

import re

text = "this is a test and this is fun"

pattern =  r'\b(\w+)\b(?=.*\b\1\b)'

matches = re.findall(pattern, text)

print("Repeated words:", matches)

