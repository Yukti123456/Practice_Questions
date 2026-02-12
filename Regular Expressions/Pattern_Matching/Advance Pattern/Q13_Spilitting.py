#Q13-Spilit text by multiple delimiters(comma,semicolon,pipe).

import re

Text = """Riya,22|Bhopal;Engineer
Aman;25|Mumbai,Developer
Neha|24;Indore,Designer
Rahul,30|Delhi;Manager"""

Pattern = r'\s*[,|;]'

matches = re.split(Pattern, Text)

print("Split text by multipke delimiters(,;|) :\n ",matches)
