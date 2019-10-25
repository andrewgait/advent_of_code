# Advent of code, day 3
#
# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23---> ...

import math
from prompt_toolkit import input

# open file
#input = open("advent3_input.txt", "r")

# read string into array
#for line in input:

input=312051

coords = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

def part1(goal):
    x = y = dx = 0
    dy = -1
    step = 0

    while True:
        step += 1
        if goal == step:
            return abs(x) + abs(y)
        if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy

print(part1(input))

def part2(input):
    x = y = dx = 0
    dy = -1
    grid = {}

    while True:
        total = 0
        for offset in coords:
            ox, oy = offset
            if (x+ox, y+oy) in grid:
                total += grid[(x+ox, y+oy)]
        if total > int(input):
            return total
        if (x, y) == (0, 0):
            grid[(0, 0)] = 1
        else:
            grid[(x, y)] = total
        if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy

print(part2(input))