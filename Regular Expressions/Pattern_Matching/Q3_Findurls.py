#Q.3- Find all URLS in a text string

import re

text = """
Visit our website at https://google.com
Also check http://example.org/test
Or go to www.github.com for code
Invalid: htt://wrong.com
"""
pattern = r"(https?://\S+|www\.\S+)"
urls = re.findall(pattern, text)
print("Urls in Given strings are: "urls)
