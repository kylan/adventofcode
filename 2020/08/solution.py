#!/usr/bin/env python3

import re
import sys

def get_input():
    with open(sys.argv[1], 'r') as f:
        content = [line.strip() for line in f]
        return content

def parse(lines):
    parsed = []
    for line in lines:
        parsed.append(re.findall('(\S+)', line))
    return parsed

## Part 1
answer = None

def execute(instructions):
    global pc
    global acc

    visited = []
    num_instructions = len(instructions)
    while pc < num_instructions:
        nxt = (pc, instructions[pc])
        if nxt in visited:
            #for entry in visited:
            #    print(entry)
            #print(nxt)
            return
        visited.append(nxt)
        cmd, val = instructions[pc]
        if cmd == 'nop':
            pc += 1
        elif cmd == 'acc':
            acc += int(val)
            pc += 1
        elif cmd == 'jmp':
            pc += int(val)

instructions = parse(get_input())
pc = 0
acc = 0
execute(instructions)

answer = acc
assert(answer == 1818)
print(answer)

## Part 2
answer = None

terminated = False
edit = 0
while not terminated:
    instructions = parse(get_input())
    instr = instructions[edit][0]
    if instructions[edit][0] == 'nop':
        instructions[edit][0] = 'jmp'
    elif instructions[edit][0] == 'jmp':
        instructions[edit][0] = 'nop'
    else:
        edit += 1
        continue
    pc = 0
    acc = 0
    execute(instructions)
    if pc >= len(instructions):
        terminated = True
        #print('Line to edit: {}'.format(edit))
    else:
        edit += 1

answer = acc
assert(answer == 631)
print(answer)
