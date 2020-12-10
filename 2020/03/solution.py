def get_input():
    with open('input.txt', 'r') as f:
        content = [line.strip() for line in f]
        return content

## Part 1

entries = get_input()
def get_trees(horiz, vert=1):
    count = 0

    rows = len(entries)
    row_len = len(entries[0])
    for row in range(rows):
        #print(row, vert, row % vert == 0, row // vert)
        if row % vert == 0 and entries[row][row//vert * horiz % row_len] == '#':
            count += 1

    return(count)

## Part 1

answer = get_trees(3, 1)
assert(answer == 211)
print(answer)

## Part 2

answers = [
        get_trees(1, 1),
        get_trees(3, 1),
        get_trees(5, 1),
        get_trees(7, 1),
        get_trees(1, 2)]

answer = answers[0] * answers[1] * answers[2] * answers[3] * answers[4]
assert(answer == 3584591857)
print(answer)
