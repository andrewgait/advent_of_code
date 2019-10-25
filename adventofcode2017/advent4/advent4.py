# Advent of code, day 4
import numpy as np

# open file
input = open("advent4_input.txt", "r")

seta = set([5, 10, 15, 20, 5])
print(seta, len(seta))

def part1(input):
    count_valid = 0
    count_line = 0

    # read string into array
    for line in input:
        string_array = []
        length = len(line)
        current_start = 0
        for i in range(length):
            if ((line[i]==" ") or (line[i]=="\n")):
                string_array.append(line[current_start:i])
                current_start = i+1

        # Now check in string_array for matches
        sarr_size = len(string_array)
        invalid = False
        for i in range(sarr_size):
            for j in range(i+1, sarr_size):
                if (string_array[i] == string_array[j]):
                    invalid = True

        count_line += 1
        if not invalid:
            count_valid += 1

    return count_valid, count_line

print(part1(input))

def part2(input):
    count_valid = 0
    count_line = 0

    # read string into array
    for line in input:
        string_array = []
        length = len(line)
        current_start = 0
        for i in range(length):
            if ((line[i]==" ") or (line[i]=="\n")):
                string_array.append(line[current_start:i])
                current_start = i+1

        # Now check in string_array for anagrams
        sarr_size = len(string_array)
        invalid = False
        for i in range(sarr_size):
            for j in range(i+1, sarr_size):
                if (sorted(string_array[i]) == sorted(string_array[j])):
                    invalid = True
                    break

        count_line += 1
        if not invalid:
            count_valid += 1

    return count_valid, count_line

input2 = open("advent4_input.txt", "r")

print(part2(input2))

