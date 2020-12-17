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

def get_rules(lines):
    rules = {}
    for line in lines:
        if line == '':
            return rules
        else:
            m = re.search('(\w+): (\d+)-(\d+) or (\d+)-(\d+)', line)
            rules[m.groups()[0]] = ((int(m.groups()[1]), int(m.groups()[2])),
                                    (int(m.groups()[3]), int(m.groups()[4])))

def get_your_ticket(lines):
    last_line = ''
    for line in lines:
        if last_line != 'your ticket:':
            last_line = line
        else:
            return map(int, line.split(','))

def get_nearby_tickets(lines):
    while lines.pop(0) != 'nearby tickets:':
        continue

    return [map(int, line.split(',')) for line in lines]

def calculate_range_union(rules):
    ranges = []
    for rule in rules:
        for (lo, hi) in rules[rule]:
            found = False
            for r in ranges:
                if lo <= r[1] and hi >= r[0]:
                    found = True
                    if lo < r[0]:
                        r[0] = lo
                    if hi > r[1]:
                        r[1] = hi
                    break
            if not found:
                ranges.append([lo, hi])
    print(ranges)
    return ranges

def parse(lines):
    rules = get_rules(lines)

    your_ticket = get_your_ticket(lines)

    nearby_tickets = get_nearby_tickets(lines)

    return(rules, your_ticket, nearby_tickets)

(rules, your_ticket, nearby_tickets) = parse(get_lines())

## Part 1
range_union = calculate_range_union(rules)

violations = []
for val in nearby_tickets:
    for t in val:
        in_range = False
        for rlo, rhi in range_union:
            if t >= rlo and t <= rhi:
                in_range = True
        if not in_range:
            violations.append(t)

solution(sum(violations), None)

## Part 2
answer = None
solution(answer, None)
