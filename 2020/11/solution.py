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

def get_after(before):
    width = len(before[0])
    height = len(before)

    output = []
    for row in range(height):
        out_row = ''
        for col in range(width):
            adj = []
            if row > 0:
                adj += before[row-1][max(col-1,0):col+2]
            if col > 0:
                adj.append(before[row][col-1])
            if col < width - 1:
                adj.append(before[row][col+1])
            if row < height - 1:
                adj += before[row+1][max(col-1,0):col+2]

            if before[row][col] == 'L' and '#' not in adj:
                out_row += '#'
            elif before[row][col] == '#' and adj.count('#') >= 4:
                out_row += 'L'
            else:
                out_row += before[row][col]
        output.append(out_row)
    #[print(line) for line in output]
    return output

def look_around(before):
    width = len(before[0])
    height = len(before)

    output = []
    for row in range(height):
        out_row = ''
        for col in range(width):
            #print("Coordinate: {}, {}".format(row, col))
            adj = []

            # up left
            for i,j in zip(range(row), range(col)):
                val = before[row-(i+1)][col-(j+1)]
                #print("\tup left {},{} = {}".format(row-(i+1),col-(j+1),val))
                if val in ['L', '#']:
                    adj.append(val)
                    break

            # up
            for i in range(row):
                val = before[row-(i+1)][col]
                #print("\tup {},{} = {}".format(row-(i+1),col,val))
                if val in ['L', '#']:
                    adj.append(val)
                    break

            # up right
            for i,j in zip(range(row), range(col+1,width)):
                val = before[row-(i+1)][j]
                #print("\tup right {},{} = {}".format(row-(i+1),j,val))
                if val in ['L', '#']:
                    adj.append(val)
                    break

            # left
            for i in range(col):
                val = before[row][col-(i+1)]
                #print("\tleft {},{} = {}".format(row,col-(i+1),val))
                if val in ['L', '#']:
                    adj.append(val)
                    break

            # right
            for i in range(col+1,width):
                val = before[row][i]
                #print("\tright {},{} = {}".format(row,i,val))
                if val in ['L', '#']:
                    adj.append(val)
                    break

            # down left
            for i,j in zip(range(row+1,height), range(col)):
                val = before[i][col-(j+1)]
                #print("\tdown left {},{} = {}".format(i,col-(j+1),val))
                if val in ['L', '#']:
                    adj.append(val)
                    break

            # down
            for i in range(row+1,height):
                val = before[i][col]
                #print("\tdown {},{} = {}".format(i,col,val))
                if val in ['L', '#']:
                    adj.append(val)
                    break

            # down right
            for i,j in zip(range(row+1,height), range(col+1,width)):
                val = before[i][j]
                #print("\tdown right {},{} = {}".format(i,j,val))
                if val in ['L', '#']:
                    adj.append(val)
                    break


            if before[row][col] == 'L' and '#' not in adj:
                out_row += '#'
            elif before[row][col] == '#' and adj.count('#') >= 5:
                out_row += 'L'
            else:
                out_row += before[row][col]
        output.append(out_row)
    #[print(line) for line in output]
    return output


## Part 1
answer = None
after = None
before = get_input()
while after != before:
    if after is not None:
        before = after
    after = get_after(before)
answer = sum([line.count('#') for line in after])
solution(answer, 2319)

## Part 2
answer = None
after = None
before = get_input()
while after != before:
    if after is not None:
        before = after
    after = look_around(before)
answer = sum([line.count('#') for line in after])
solution(answer, 2117)
