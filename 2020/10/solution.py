#!/usr/bin/env python3

import argparse
import collections
from functools import reduce

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
        content = [int(line.strip()) for line in f]
        return content

def prepare_list(data):
    data.sort()
    data.insert(0, 0)
    data.append(data[-1]+3)
    return data

def measure_gaps(data):
    gaps = [j-i for i, j in zip(data, data[1:])]
    return gaps

## Part 1
answer = None

distribution = collections.Counter(measure_gaps(prepare_list(get_input())))
answer = distribution[1] * distribution[3]
solution(answer, 1625)

## Part 2
answer = None

run_combos = {1:1, 2:2, 3:4, 4:7}

def run_list(data):
    run_list = []
    current_run = 0
    for item in data:
        if item == 1:
            current_run += 1
        else:
            if current_run > 0:
                run_list.append(run_combos[current_run])
            current_run = 0
    return run_list

gaps = measure_gaps(prepare_list(get_input()))
runs = run_list(gaps)
answer = reduce(lambda x, y: x*y, runs)
solution(answer, 3100448333024)
