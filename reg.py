import re

text = "The quick brown fox"
pattern = r"quick"

search = re.search(pattern,text)
if search:
    print("pattern found:",search.group())
else:
    print("pattern not found")
       