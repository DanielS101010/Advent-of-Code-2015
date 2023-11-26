file = open("Day3 input.txt", "r")
samples = file.read()
file.close()
# first number is x axis, second number is y axis
position_santa = (0, 0)
visited_houses = []


def update_position(direction, position):
    match direction:
        case "^":
            position = [position[0], position[1] - 1]

        case "v":
            position = [position[0], position[1] + 1]

        case "<":
            position = [position[0] - 1, position[1]]

        case ">":
            position = [position[0] + 1, position[1]]

    if position not in visited_houses:
        visited_houses.append(position)

    return position


for char in samples:
    position_santa = update_position(char, position_santa)

print(len(visited_houses) + 1)

# part 2
position_santa = (0, 0)
position_robo_santa = (0, 0)

visited_houses = []

for i, char in enumerate(samples):
    if i % 2 == 0:
        position_santa = update_position(char, position_santa)
    else:
        position_robo_santa = update_position(char, position_robo_santa)

print(len(visited_houses))
