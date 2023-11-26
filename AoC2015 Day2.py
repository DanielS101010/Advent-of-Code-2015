file = open("Day2 input.txt", "r")
lines = file.readlines()
file.close()

size_wrapping_paper = 0
length_ribbon = 0


# Part 1
def size_of_wrapping_paper(length, width, height):
    side1 = 2 * length * width
    side2 = 2 * width * height
    side3 = 2 * length * height

    return int(side1 + side2 + side3 + min(side1, side2, side3) / 2)


# Part 2
def length_of_ribbon(length, width, height):
    sides = sorted([length, width, height])

    perimeter = 2 * (sides[0] + sides[1])
    bow = length * width * height

    return perimeter + bow


for line in lines:
    dimensions = line.split("x")

    size_wrapping_paper += size_of_wrapping_paper(int(dimensions[0]), int(dimensions[1]), int(dimensions[2]))
    length_ribbon += length_of_ribbon(int(dimensions[0]), int(dimensions[1]), int(dimensions[2]))

print(size_wrapping_paper)
print(length_ribbon)
