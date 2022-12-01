# Advent of code 2022, day 1

# open file
input = open("advent1_input.txt", "r")
# input = open("advent1_test_input1.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line[:-1])

def part1():

    most_cals = 0
    cals = []

    cals_tot = 0
    for input in input_array:
        if len(input) == 0:
            cals.append(cals_tot)
            cals_tot = 0
        else:
            cals_tot += int(input)

    print(cals)

    answer = max(cals)

    return answer

def part2():

    most_cals = 0
    cals = []

    cals_tot = 0
    for input in input_array:
        if len(input) == 0:
            cals.append(cals_tot)
            cals_tot = 0
        else:
            cals_tot += int(input)

    print(cals)

    # I'm guessing this might run into problems if any of the values in cals are equal
    first = max(cals)
    cals.remove(first)
    second = max(cals)
    cals.remove(second)
    third = max(cals)

    answer = first + second + third

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
