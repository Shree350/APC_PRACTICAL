import re

name = input("Enter your name: ").strip()

pattern = r"[A-Za-z]+(?:[ '-][A-Za-z]+)*"

if re.fullmatch(pattern, name):
    print(f"the name {name} is valid")
else:
    print(f"the name {name} is invalid")
