def count_lines():
    f = open("storylines.txt", "r")
    count = 0
    total = 0

    for line in f:
        total +=1
        if not line.startswith("T"):
            count += 1

    f.close()
    print("Number of lines =", total)
    print("Number of lines =", count)

count_lines()
