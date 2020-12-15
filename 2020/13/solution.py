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

data = get_input()
earliest = int(data[0])
frequencies = []
mod = 0
for item in data[1].split(','):
    if item.isdigit():
        frequencies.append((int(item), mod))
    mod += 1
print(frequencies)

## Part 1
soonest = (earliest, earliest)
for (freq, gap)  in frequencies:
    wait_time = freq - earliest % freq
    if wait_time < soonest[1]:
        soonest = [freq, wait_time]

solution(soonest[0] * soonest[1], 1835)

## Part 2

def compute(answer, data):
    frequencies = {}
    add = 0
    for item in data.split(','):
        if item.isdigit():
            frequencies[int(item)] = add
        add += 1

    keys = [k for k in reversed(sorted(frequencies))]
    step = keys[0]
    offset = frequencies[step]
    print(frequencies, step, offset)
    found = False
    while found is False:
        answer += step
        if answer % 10000000 == 0:
            print(answer)
        for k in keys:
            found = True
            calcs = []
            if (answer - offset + frequencies[k]) % k != 0:
                found = False
                break
    answer -= offset
    print(answer)

for start, item in [
        (0, '7,13,x,x,59,x,31,19'),
        (0, '67,7,59,61'),
        (0, '17,x,13,19'),
        (0, '67,x,7,59,61'),
        (0, '67,7,x,59,61'),
        (0, '1789,37,47,1889'),
        (0, data[1])]:
    compute(start, item)

solution(None, None)
