#Q_9- Extract dates in formats: DD-MM-YYYY,DD/MM/YYY,YYY-MM-DD.

import re

text = """Yesterday, Riya submitted her project on 12-02-2025 at the office.
        Her previous internship started on 05/08/2023 and ended on 2023-11-30.

        The company was founded on 15-09-2010, while its first product was launched on 2011-01-25.
        A meeting is scheduled for 28/03/2026, and the final report must be submitted by 2026-04-10.

        Riya’s birthday is on 07-07-2003, and her sister’s birthday is on 2001-12-19.
        They are planning a trip starting 14/01/2027 and returning on 2027-01-25."""

Pattern = r'(?:\d{2}[-/]\d{2}[-/]\d{4}|\d{4}[-]\d{2}[-]\d{2})'

matches = re.findall(Pattern, text)

print("Extract dates in formats: DD-MM-YYYY,DD/MM/YYY,YYY-MM-DD are:\n\n ",matches)

