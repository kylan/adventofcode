#!/usr/bin/env python3

import sys

def get_input():
    with open(sys.argv[1], 'r') as f:
        content = [line.strip() for line in f]
        return content

## Part 1
answer = None

groups = []
group = None
entries = get_input()
for entry in entries:
    if group is None:
        group = set(entry)
    elif entry:
        group = group | set(entry)
    else:
        # empty line or EOL
        groups.append(group)
        group = None
groups.append(group)

answer = sum([len(g) for g in groups])

#assert(answer == 6903)
print(answer)

## Part 2
answer = None

groups = []
group = None
entries = get_input()
for entry in entries:
    if group is None:
        group = set(entry)
    elif entry:
        group = group & set(entry)
    else:
        # empty line or EOL
        groups.append(group)
        group = None
groups.append(group)

answer = sum([len(g) for g in groups])

assert(answer == 3493)
print(answer)
