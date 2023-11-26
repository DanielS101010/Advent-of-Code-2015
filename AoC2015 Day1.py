file = open("Day1 input.txt", "r")
samples = file.read()
file.close()

floor = 0
counter = 0
firstTime = True

for sample in samples:
    counter += 1
    if sample == "(":
        floor += 1
    else:
        floor -= 1

    if floor < 0 and firstTime:
        print(counter)
        firstTime = False
print(floor)
