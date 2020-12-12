#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input", help="The file with puzzle input")
parser.add_argument("--debug", help="Ignore solution assertions", action="store_true")
args = parser.parse_args()

def solution(value, check):
    if not args.debug:
        assert(value == check)
    print(value)

def get_input():
    with open(args.input, 'r') as f:
        content = [line.strip() for line in f]
        return content

## Part 1
answer = None
x,y = (0,0)
d = 0

def p1_move(count):
    (x, y) = (0, 0)
    pos = 1
    if d > 1:
        # Negative direction
        pos = -1
    if d % 2 == 0:
        # X-axis
        x = count
    else:
        # Y-axis
        y = count
    return(pos*x, pos*y)

def p1_parse(action):
    global x, y, d
    #print(action, x, y, d)
    cmd = action[0]
    mag = int(action[1:])
    if cmd == 'N':
        y += mag
    elif cmd == 'S':
        y -= mag
    elif cmd == 'E':
        x += mag
    elif cmd == 'W':
        x -= mag
    elif cmd == 'L':
        d = (d + mag // 90) % 4
    elif cmd == 'R':
        d = (d - mag // 90) % 4
    elif cmd == 'F':
        (horiz, vert) = p1_move(mag)
        x += horiz
        y += vert
    #print(x, y, d)

for cmd in get_input():
    p1_parse(cmd)

answer = abs(x) + abs(y)
solution(answer, 1496)

## Part 2
answer = None
x,y = (0,0)
d = 0

def p2_move(count):
    (x, y) = (0, 0)
    pos = 1
    if d > 1:
        # Negative direction
        pos = -1
    if d % 2 == 0:
        # X-axis
        x = count
    else:
        # Y-axis
        y = count
    return(pos*x, pos*y)

def p2_parse(action):
    global x, y, d
    #print(action, x, y, d)
    cmd = action[0]
    mag = int(action[1:])
    if cmd == 'N':
        y += mag
    elif cmd == 'S':
        y -= mag
    elif cmd == 'E':
        x += mag
    elif cmd == 'W':
        x -= mag
    elif cmd == 'L':
        d = (d + mag // 90) % 4
    elif cmd == 'R':
        d = (d - mag // 90) % 4
    elif cmd == 'F':
        (horiz, vert) = p2_move(mag)
        x += horiz
        y += vert
    #print(x, y, d)

for cmd in get_input():
    p2_parse(cmd)

answer = abs(x) + abs(y)
solution(answer, None)
