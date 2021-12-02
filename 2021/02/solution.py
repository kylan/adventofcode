
def scan(name, window_size):
    depths = []

    with open(name) as f:
        depths = [int(d) for d in f.read().splitlines()]

    count = 0
    i = window_size
    last_depth = sum(depths[i-window_size:i])

    while i < len(depths):
        i += 1
        depth = sum(depths[i-window_size:i])
        if depth > last_depth:
            count += 1
        else:
            pass
        last_depth = depth

    print(count)

# Part One
for name in ('sample.txt', 'input.txt'):
    scan(name, 1)

# Part Two
for name in ('sample.txt', 'input.txt'):
    scan(name, 3)