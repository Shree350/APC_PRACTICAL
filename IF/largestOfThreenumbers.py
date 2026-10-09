num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))
num3 = int(input("Enter a number 3: "))

if num1 > num2 and num1>num3:
    print("number 1 is big")
elif num2 > num1 and num2>num3:
    print("number 2 is big")
else:
    print("number 3 is big")
