n = int(input("Enter n: "))

i = 0
while (2 ** i) <= (n ** 2):
    print(2 ** i, end=" ")
    i += 1