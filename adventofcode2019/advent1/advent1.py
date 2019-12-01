# Advent of code, day 1
import math

# open file
input = open("advent1_input.txt", "r")

input_data = []

# read string into array
for line in input:
    input_data.append(int(line))

# input_data = [12, 14, 1969, 100756]
print(input_data)

def part1(input_data):

    fuel = 0
    for i in range(len(input_data)):
        fuel += math.floor(input_data[i] / 3) - 2

    return fuel

def part2(input_data):

    total_fuel = 0
    for i in range(len(input_data)):
        sum = 0
        fuel = math.floor(input_data[i] / 3) - 2
        while (fuel > 0):
            sum += fuel
            fuel = math.floor(fuel / 3) - 2

        total_fuel += sum

    return total_fuel

print('Part 1: ', part1(input_data))  # with my input_data, this is 3273471
print('Part 2: ', part2(input_data))  # with my input_data, this is 4907345