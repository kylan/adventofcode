#!/usr/bin/env python3

import re
import sys

def get_input():
    with open(sys.argv[1], 'r') as f:
        content = [line.strip() for line in f]
        return content


## Part 1
answer = None

rules = {}
entries = get_input()
for entry in entries:
    #rule = re.findall('(\d+)* *(\w+ \w+) bag', entry)
    rule = re.findall('(\w+ \w+) bag', entry)
    rules[rule[0]] = rule[1:]

def who_has(bag_type):
    bag_list = []
    for bag in rules:
        if bag_type in rules[bag]:
            bag_list += [x for x in who_has(bag) if x not in bag_list]
    return(bag_list + [bag_type])

# answer is one less because shiny gold alone doesn't count
answer = len(who_has('shiny gold')) - 1

assert(answer == 254)
print(answer)

## Part 2
answer = None

rules = {}
entries = get_input()
for entry in entries:
    rule = re.findall('(\d+)* *(\w+ \w+) bag', entry)
    rules[rule[0]] = rule[1:]

def bag_count(top_bag):
    total = 0
    for (count, bag) in rules[('', top_bag)]:
        if count:
            total += int(count) * (1 + bag_count(bag))
    return total

answer = bag_count('shiny gold')

assert(answer == 6006)
print(answer)
