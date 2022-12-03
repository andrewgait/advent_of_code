# Advent of code 2022, day 3

# open file
input = open("advent3_input.txt", "r")
# input = open("advent3_test_input1.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lower_dict = {}
upper_dict = {}

for n in range(len(lowercase)):
    lower_dict[lowercase[n]] = n+1
    upper_dict[uppercase[n]] = n+27

def part1():

    total = 0


    for input in input_array:
        input_len = len(input) - 1
        first = input[:input_len//2]
        second = input[input_len//2:]
        common = list(set(first).intersection(second))
        if common[0].isupper():
            total += upper_dict[common[0]]
        if common[0].islower():
            total += lower_dict[common[0]]

    answer = total

    return answer

def part2():

    total = 0

    array_len = len(input_array)

    for n in range(array_len//3):
        inputs = [input_array[n*3][:-1], input_array[3*n+1][:-1],
                  input_array[3*n+2][:-1]]
        common = list(
            set(inputs[0]).intersection(inputs[1]).intersection(inputs[2]))
        if common[0].isupper():
            total += upper_dict[common[0]]
        if common[0].islower():
            total += lower_dict[common[0]]

    answer = total

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
