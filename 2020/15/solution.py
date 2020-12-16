#!/usr/bin/env python3

import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("input", help="The file with puzzle input")
parser.add_argument("--debug", help="Ignore solution assertions", action="store_true")
args = parser.parse_args()

def solution(value, check):
    print("Expected: {}, Got: {}".format(check, value))
    if not args.debug:
        assert(value == check)

def get_lines():
    with open(args.input, 'r') as f:
        content = [line.strip() for line in f]
        return content

## Part 1
examples = [
        ([0,3,6], 436),
        ([1,3,2], 1),
        ([2,1,3], 10),
        ([1,2,3], 27),
        ([2,3,1], 78),
        ([3,2,1], 438),
        ([3,1,2], 1836),
        ([12,1,16,3,11,0], 1696)
        ]
for example, answer in examples:
    d = {example[0]: [1], example[1]: [2], example[2]: [3]}
    d = {}
    for i,v in enumerate(example):
        d[v] = [i+1]
    print(d)
    last = example[2]
    for idx in range(len(example)+1, 30000000+1):
        if len(d[last]) == 1:
            last = 0
        else:
            last = d[last][-1] - d[last][-2]
        d[last] = [idx] if last not in d else d[last] + [idx]
    solution(last, answer)

## Part 2
answer = None
solution(answer, None)
