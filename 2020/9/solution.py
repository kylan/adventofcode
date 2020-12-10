#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input", help="The file with puzzle input")
parser.add_argument("-w", "--window", help="The window size for calculation", type=int, default=25)
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

#example window = 5
#input window = 25
window = args.window
nums = get_input()

## Part 1
answer = None

def find_error(nums, window):
    while len(nums) > window:
        total = nums[window]
        found = False
        idx = 0
        while idx < window and not found:
            found = total - nums[idx] in nums[idx:window]
            idx += 1
        if not found:
            return(total)

        nums.pop(0)

answer = find_error(nums, window)

solution(answer, 542529149)

## Part 2
total = answer

def find_middle(nums, total):
    for idx, num in enumerate(nums):
        if num > total / 2:
            return idx - 1

def work_backward(nums, total):
    while len(nums):
        offset = -1
        while sum(nums[offset:]) < total:
            offset -= 1
        if sum(nums[offset:]) == total:
            return nums[offset:]
        nums.pop()

nums = get_input()
idx = find_middle(nums, total)
contiguous_set = work_backward(nums[:idx], total)
answer = min(contiguous_set) + max(contiguous_set)
solution(answer, 75678618)
