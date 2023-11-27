import numpy as np

file = open("Day6 input.txt", "r")
lines = file.readlines()
file.close()

lights = np.full((1000, 1000), False, dtype=bool)


def toggle1(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            lights[i, j] = not lights[i, j]


def turn_on1(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            lights[i, j] = True


def turn_off1(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            lights[i, j] = False


def get_instruction(instr):
    instruction = instr.split(" ")

    if instruction[0] == "toggle":
        x1, y1 = instruction[1].split(",")
        x2, y2 = instruction[3].split(",")
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)

        return "toggle", x1, y1, x2, y2

    else:
        x1, y1 = instruction[2].split(",")
        x2, y2 = instruction[4].split(",")

        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        if instruction[1] == "on":
            return "on", x1, y1, x2, y2
        else:
            return "off", x1, y1, x2, y2


for line in lines:
    instruction, x1, y1, x2, y2 = get_instruction(line)

    match (instruction):
        case ("on"):
            turn_on1(x1, y1, x2, y2)
        case ("off"):
            turn_off1(x1, y1, x2, y2)
        case ("toggle"):
            toggle1(x1, y1, x2, y2)

print(sum(sum(row) for row in lights))

lights = np.full((1000, 1000), 0, dtype=int)


def toggle2(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            lights[i, j] += 2


def turn_on2(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            lights[i, j] += 1


def turn_off2(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if lights[i, j] > 0:
                lights[i, j] -= 1


for line in lines:
    instruction, x1, y1, x2, y2 = get_instruction(line)

    match (instruction):
        case ("on"):
            turn_on2(x1, y1, x2, y2)
        case ("off"):
            turn_off2(x1, y1, x2, y2)
        case ("toggle"):
            toggle2(x1, y1, x2, y2)

print(sum(sum(row) for row in lights))
