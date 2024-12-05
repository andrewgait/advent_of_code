# Advent of code 2024, day 4
from collections import defaultdict
import re

# open file
input = open("advent4_input.txt", "r")
# input = open("advent4_test_input1.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def groups(data, func):
    grouping = defaultdict(list)
    for y in range(len(data)):
        for x in range(len(data[y])):
            grouping[func(x, y)].append(data[y][x])
    return list(map(grouping.get, sorted(grouping)))


test = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
cols = groups(test, lambda x, y: x)
rows = groups(test, lambda x, y: y)
fdiag = groups(test, lambda x, y: x + y)
bdiag = groups(test, lambda x, y: x - y)

print(fdiag)


def part1():

    # I guess here there are six things to search for:
    #
    # - SAMX, XMAS in a horizontal line (easy)
    # - SAMX, XNAS in a vertical line (harder)
    # - SAMX, XMAS in a diagonal line (how... ?)
    #   - there are diagonals from top left to bottom right
    #   - and from top right to bottom left

    width = len(input_array[0])-1
    height = len(input_array)
    print(width, height)

    answer = 0
    h = 0
    v = 0
    d = 0

    # Horizontal
    for input in input_array:
        xmas_h = [m.start() for m in re.finditer('XMAS', input)]
        samx_h = [m.start() for m in re.finditer('SAMX', input)]
        h += len(xmas_h) + len(samx_h)

    # Vertical
    for w in range(width):
        input_v = [input[w] for input in input_array]
        input_v_string = ""
        for n in range(len(input_v)):
            input_v_string += input_v[n]
        xmas_v = [m.start() for m in re.finditer('XMAS', input_v_string)]
        samx_v = [m.start() for m in re.finditer('SAMX', input_v_string)]
        v += len(xmas_v) + len(samx_v)

    # Diagonals, thanks to https://stackoverflow.com/a/43311126
    fdiag_strs = groups(input_array, lambda x, y: x + y)
    bdiag_strs = groups(input_array, lambda x, y: x - y)

    for fdiag in fdiag_strs:
        input_fdiag = ""
        for n in range(len(fdiag)):
            input_fdiag += fdiag[n]
        xmas_fdiag = [m.start() for m in re.finditer('XMAS', input_fdiag)]
        samx_fdiag = [m.start() for m in re.finditer('SAMX', input_fdiag)]
        d += len(xmas_fdiag) + len(samx_fdiag)

    for bdiag in bdiag_strs:
        input_bdiag = ""
        for n in range(len(bdiag)):
            input_bdiag += bdiag[n]
        xmas_bdiag = [m.start() for m in re.finditer('XMAS', input_bdiag)]
        samx_bdiag = [m.start() for m in re.finditer('SAMX', input_bdiag)]
        d += len(xmas_bdiag) + len(samx_bdiag)


    print("horizontal ", h)
    print("vertical ", v)
    print('diagonal ', d)


    answer = h + v + d

    return answer

def part2():

    answer = 0

    width = len(input_array[0])-1
    height = len(input_array)

    # The X-MAS shapes have to have an A in the middle, so search for As not on the edge
    for h in range(1,height-1):
        for w in range(1,width-1):
            if input_array[h][w] == 'A':
                # There are four configurations Ms top, Ss bottom= and opposite
                # or Ms left, Ss right and opposite
                if (input_array[h-1][w-1] == 'M' and input_array[h-1][w+1] == 'M' and
                    input_array[h+1][w+1] == 'S' and input_array[h+1][w-1] == 'S'):
                    answer += 1
                elif (input_array[h-1][w-1] == 'S' and input_array[h-1][w+1] == 'S' and
                      input_array[h+1][w+1] == 'M' and input_array[h+1][w-1] == 'M'):
                    answer += 1
                elif (input_array[h-1][w-1] == 'M' and input_array[h-1][w+1] == 'S' and
                      input_array[h+1][w+1] == 'S' and input_array[h+1][w-1] == 'M'):
                    answer += 1
                elif (input_array[h-1][w-1] == 'S' and input_array[h-1][w+1] == 'M' and
                      input_array[h+1][w+1] == 'M' and input_array[h+1][w-1] == 'S'):
                    answer += 1

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
