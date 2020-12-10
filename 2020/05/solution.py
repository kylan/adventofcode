#!/usr/bin/env python3

def get_input():
    with open('input.txt', 'r') as f:
        content = [line.strip() for line in f]
        return content

def convert(s):
    val = 0
    for c in s:
        val = val << 1
        if c in ('B', 'R'):
            val = val | 1
    return(val)

entries = get_input()

boarding_passes = {}

## Part 1
answer = 0

for entry in entries:
    row = convert(entry[:-3])
    col = convert(entry[-3:])
    pass_id = row * 8 + col
    boarding_passes[pass_id] = (row, col)
    answer = max(answer, row * 8 + col)

assert(answer == 915)
print(answer)

## Part 2
answer = None

for key in sorted(boarding_passes.keys()):
    if key + 1 not in boarding_passes and key + 2 in boarding_passes:
        answer = key + 1

assert(answer == 699)
print(answer)
