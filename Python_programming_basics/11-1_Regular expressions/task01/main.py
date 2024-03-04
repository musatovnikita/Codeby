import re

text = 'Московское время 10:36:06'

matches = re.findall(r'\b\d{2}:\d{2}:\d{2}\b', text)
for match in matches:
    print(match)