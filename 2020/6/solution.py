#!/usr/bin/env python3

import sys

def get_input():
    with open(sys.argv[1], 'r') as f:
        content = [line.strip() for line in f]
        return content

## Part 1
answer = None

groups = []
group = ''
entries = get_input()
for entry in entries:
    if entry:
        for c in entry:
            if not c in group:
                group = group + c
    else:
        # empty line or EOL
        groups.append(group)
        group = ''
groups.append(group)

answer = sum([len(g) for g in groups])

assert(answer == 6903)
print(answer)

## Part 2
answer = None

#assert(answer == TODO)
print(answer)
