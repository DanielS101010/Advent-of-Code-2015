file = open("Day7 input.txt", "r")
lines = file.readlines()
file.close()


def bitwise_and(x1, x2):
    return x1 & x2


def bitwise_or(x1, x2):
    return x1 | x2


def leftshift(x1, x2):
    return x1 << x2


def rightshift(x1, x2):
    return x1 >> x2


def bitwise_complement(x1):
    return ~x1 & 0xFFFF  # 16-bit complement


def calculate_wires(b):
    wires = {}
    wires_len = -1  # wires length starts at 0, wires_len should be lower

    while wires_len < len(wires):
        wires_len = len(wires)
        for line in lines:
            parts = [part.strip() for part in line.split(" ")]
            if parts[-1] == "b" and b is not None:
                wires["b"] = int(b)
                continue
            if len(parts) == 3:
                if parts[0] in wires:
                    wires[parts[2]] = wires[parts[0]]

                elif parts[0].isdigit() and parts[0] not in wires:
                    wires[parts[2]] = int(parts[0])

            elif len(parts) == 4:
                # if parts[3] in wires:
                #    continue
                if parts[1] in wires:
                    wires[parts[3]] = int(bitwise_complement(wires[parts[1]]))

            elif len(parts) == 5:
                if parts[4] in wires:
                    continue

                if parts[0].isdigit():
                    val1 = int(parts[0])
                elif parts[0] in wires:
                    val1 = wires[parts[0]]
                else:
                    continue

                if parts[2].isdigit():
                    val2 = int(parts[2])
                elif parts[2] in wires:
                    val2 = wires[parts[2]]
                else:
                    continue

                match parts[1]:

                    case ("OR"):
                        wires[parts[4]] = int(bitwise_or(val1, val2))

                    case ("AND"):
                        wires[parts[4]] = int(bitwise_and(val1, val2))

                    case ("RSHIFT"):
                        if parts[0] in wires:
                            wires[parts[4]] = int(rightshift(wires[parts[0]], int(parts[2])))
                        elif parts[0].isnumeric():
                            wires[parts[4]] = int(rightshift(int(parts[0]), wires[parts[2]]))

                    case ("LSHIFT"):
                        if parts[0] in wires:
                            wires[parts[4]] = int(leftshift(wires[parts[0]], int(parts[2])))
                        elif parts[0].isnumeric():
                            wires[parts[4]] = int(leftshift(int(parts[0]), wires[parts[2]]))

    return wires["a"]


a = calculate_wires(None)
print(a)

new_a = calculate_wires(a)
print(new_a)
