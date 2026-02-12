import re
Text = """Yesterday, the temperature in Bhopal was -5.6 degrees, but last week it was 12 degrees.
          The company reported a profit of 1500.75 dollars, while last year it faced a loss 
          of -320.50 dollars.

        Riya scored 89.5 in Mathematics, 76 in Physics, and -2 marks were deducted for late submission.
        The stock price moved from 105.25 to -98.75 within 3 days.

        The values recorded were 0.5, -0.75, 200, -1000, 45.0 and 7"""

Pattern = r'-?\d+(?:\.\d+)?'

matches = re.findall(Pattern, Text)

print("Below are numbers with optional (.) and (-) Sign:\n ")
for numbers in matches:
    print(numbers)
