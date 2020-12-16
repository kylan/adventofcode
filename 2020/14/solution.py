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
    #print("New mask: {}".format(mask))

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
update_mask(cmds[0][1])
memory = {}
for cmd in cmds[1:]:
    result = process_cmd1(cmd)
    if type(result) is tuple:
        (addr, val) = result
        memory[addr] = val

total = sum([int(memory[addr], 2) for addr in memory])
solution(total, 7817357407588)

## Part 2
def is_overlap(old, new):
    if old == new:
        return False
    for o, n in zip(old, new):
        if o != n and 'X' not in [o, n]:
            return False
    """
    print('----Overlap-----------------------------------')
    print(old)
    print(new)
    print('----------------------------------------------')
    """
    return True

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

memory = {}
cmds = process_lines(get_lines())
update_mask(cmds[0][1])

for cmd in cmds[1:]:
    result = process_cmd2(cmd)
    if type(result) is tuple:
        (addr, val) = result
        for existing in memory:
            if is_overlap(existing, addr):
                replace = ''
                for i, (e, a) in enumerate(zip(existing, addr)):
                    if e == 'X' and a == '1':
                        replace += '0' + existing[i+1:]
                        break
                    elif e == 'X' and a == '0':
                        replace += '1' + existing[i+1:]
                        break
                    elif a == 'X':
                        print("aha!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! {}".format(e))
                    else:
                        replace += e
                assert(len(replace) == 36)
                memory[replace] = memory.pop(existing)
        memory[addr] = val

total = 0
for addr in sorted(memory, key=str):
    subtotal = (2 ** addr.count('X')) * int(memory[addr])
    print('{}\t{}\t{}'.format(addr, 2 ** addr.count('X'), memory[addr]))
    total += subtotal
print(total)
total = sum([(2 ** addr.count('X')) * int(memory[addr]) for addr in memory])
solution(total, None)


