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
answer = None

print([freq for (freq, gap) in frequencies])
print([freq - gap for (freq, gap) in frequencies])

solution(answer, None)
