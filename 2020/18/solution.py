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
        content = [line.strip().replace(' ', '') for line in f]
        print(content)
        return content

test_input = [
        ("1 + 1", 2),
        ("2 * 3 + (4 * 5)", 26),
        ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 437),
        ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 12240),
        ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 13632)
        ]

## Part 1
    
def divide(expression):
    if '(' not in expression:
        return None

    first = 0
    for i, c in enumerate(expression):
        if c == '(':
            first = i
            break

    depth = 0
    for i, c in enumerate(expression[first:]):
        if c == '(':
            depth += 1
        if c == ')':
            depth -= 1
        if depth == 0:
            last = first + i
            left = expression[0:first]
            middle = expression[first+1:last]
            right = expression[last+1:]
            #print("Expression {}\nLeft {}\nMiddle {}\nRight {}".format(expression,left,middle,right))
            return(left, middle, right)

def calculate(expression):
    print(expression)
    return expression

def process(expression):
    match = divide(expression)
    if match:
        left, middle, right = match
        return process(left) + \
                process(middle) + \
                process(right)
    else:
        return calculate(expression)

for expression, answer in test_input:
    result = process(expression)
    solution(result, answer)

## Part 2
answer = None

solution(answer, None)
