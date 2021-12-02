def solve1(name):
    horiz = 0
    depth = 0

    with open(name) as f:
        commands = [c.split() for c in f.read().splitlines()]

    for dir, mag in commands:
        mag = int(mag)
        if dir == "forward":
            horiz += mag
        elif dir == "up":
            depth -= mag
        elif dir == "down":
            depth += mag

    print(horiz * depth)


def solve2(name):
    horiz = 0
    depth = 0
    aim = 0

    with open(name) as f:
        commands = [c.split() for c in f.read().splitlines()]

    for dir, mag in commands:
        mag = int(mag)
        if dir == "forward":
            horiz += mag
            depth += aim * mag
        elif dir == "up":
            aim -= mag
        elif dir == "down":
            aim += mag

    print(horiz * depth)


# Part One
for name in ["sample.txt", "input.txt"]:
    solve1(name)

# Part Two
for name in ["sample.txt", "input.txt"]:
    solve2(name)
