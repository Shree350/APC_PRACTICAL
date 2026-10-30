import re

text = "Ojas has 2 cars and 3 bikes"

# 1. match(): checks the beginning
print("1. match:", re.match(r"Ojas", text))

# 2. fullmatch(): checks the entire string
print("2. fullmatch:", re.fullmatch(r"Ojas has 2 cars and 3 bikes", text))

# 3. search(): finds the first occurrence
print("3. search:", re.search(r"\d+", text).group())

# 4. findall(): finds all occurrences
print("4. findall:", re.findall(r"\d+", text))

# 5. split(): splits the string
print("5. split:", re.split(r"\s+", text))

# 6. sub(): replaces matching text
print("6. sub:", re.sub(r"\d+", "#", text))
