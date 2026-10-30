import re

mobile = input("Enter mobile number: ").strip()

pattern = r"[6-9][0-9]{9}"

if re.fullmatch(pattern, mobile):
    print(f"the mobile number {mobile} is valid")
else:
    print(f"the mobile number {mobile} is invalid")
