import re

text = """Several students from Bhopal, Mumbai, and Chennai participated actively.
          During the session, participants asked questions about Python, Kubernetes,
          Docker, and Jenkins."""

Pattern = r'\b[A-Za-z]{5,10}\b'

matches = re.findall(Pattern, text)

print("Words with netween 5-10 character long are: :\n ")
for word in matches:
    print(word)
