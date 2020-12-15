#!/usr/bin/env python3

import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("input", help="The file with puzzle input")
parser.add_argument("--debug", help="Ignore solution assertions", action="store_true")
args = parser.parse_args()

def solution(value, check):
    if not args.debug:
        assert(value == check)
    print(value)

def get_lines():
    with open(args.input, 'r') as f:
        content = [line.strip() for line in f]
        return content

def process_lines(lines):
    cmds = []
    for line in lines:
        m = re.search("(mask) = ([X10]{36})", line)
        if not m:
            m = re.search("(mem)\[(\d+)\] = (\d+)", line)
        cmds.append(m.groups())
    return(cmds)

def update_mask(new_mask):
    global mask
    mask = new_mask

def mask_value(value):
    result = ''
    for v, m in zip(value, mask):
        if m in ['1', '0']:
            result += m
        else:
            result += v
    return result

def process_cmd1(cmd):
    if cmd[0] == 'mask':
        update_mask(cmd[1])
    else:
        value = "{:036b}".format(int(cmd[2]))
        result = mask_value(value)
        return (cmd[1], result)

## Part 1
cmds = process_lines(get_lines())
mask = cmds[0][1]
memory = {}
for cmd in cmds[1:]:
    result = process_cmd1(cmd)
    if type(result) is tuple:
        (addr, val) = result
        memory[addr] = val

total = sum([int(memory[addr], 2) for addr in memory])
solution(total, 7817357407588)

## Part 2
memory = {}
cmds = process_lines(get_lines())
mask = cmds[0][1]

def mask_value2(value):
    result = ''
    for v, m in zip(value, mask):
        if m == '0':
            result += v
        elif m in ['1', 'X']:
            result += m
    return result

def process_cmd2(cmd):
    if cmd[0] == 'mask':
        update_mask(cmd[1])
    else:
        addr = "{:036b}".format(int(cmd[1]))
        addr = mask_value2(addr)
        return (addr, cmd[2])

def wipe_matches(new_addr):
    global memory
    for addr in memory:
        match = True
        for (n, a) in zip(new_addr, addr):
            if n == a == 'X':
                pass
            elif n == 'X':
                pass
            elif a == 'X':
                pass

for cmd in cmds[1:]:
    result = process_cmd2(cmd)
    if type(result) is tuple:
        (addr, val) = result
        copies = addr.count('X')
        wipe_matches(addr)
        memory[addr] = (copies, val)

print(memory)
#total = sum([int(memory[addr], 2) for addr in memory])
#solution(total, 7817357407588)


