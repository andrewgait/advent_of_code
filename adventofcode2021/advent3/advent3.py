# Advent of code, day 3
import copy

# open file
input = open("advent3_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def bit_sum(inputs, n_inputs, m):
    sum_0 = 0
    sum_1 = 0
    for n in range(n_inputs):
        if inputs[n][m] == 0:
            sum_0 += 1
        else:
            sum_1 += 1

    return sum_0, sum_1


def part1():

    answer = 0

    # list of lists needed
    inputs = []
    n_inputs = len(input_array)
    print(n_inputs)
    n_line = len(input_array[0])
    for n in range(n_inputs):
        line_inputs = []
        for m in range(n_line-1):
            line_inputs.append(int(input_array[n][m]))
        inputs.append(line_inputs)

    string_0 = ""
    string_1 = ""

    for m in range(n_line-1):
        sum_0, sum_1 = bit_sum(inputs, n_inputs, m)
        if sum_0 > sum_1:
            string_0 += "0"
            string_1 += "1"
        else:
            string_0 += "1"
            string_1 += "0"

    # print(inputs)
    print(string_0, string_1)
    print(int(string_0, 2), int(string_1, 2))
    answer = int(string_0, 2) * int(string_1, 2)

    return answer

def part2():

    answer = 0

    # list of lists needed
    inputs = []
    n_inputs = len(input_array)
    print(n_inputs)
    n_line = len(input_array[0])
    for n in range(n_inputs):
        line_inputs = []
        for m in range(n_line-1):
            line_inputs.append(int(input_array[n][m]))
        inputs.append(line_inputs)

    # Do the oxygen generator rating
    # while len(inputs) > 1:
    for m in range(n_line-1):
        sum_0, sum_1 = bit_sum(inputs, n_inputs, m)

        if sum_0 > sum_1:
            selected = 0
        else:
            selected = 1

        new_inputs = []
        for n in range(n_inputs):
            if inputs[n][m] == selected:
                new_inputs.append(inputs[n])

        if len(new_inputs) == 1:
            break
        else:
            inputs = copy.deepcopy(new_inputs)
            n_inputs = len(inputs)

    print("final for oxygen: ", new_inputs)

    oxygen_string = ""
    for m in range(n_line-1):
        oxygen_string += str(new_inputs[0][m])

    oxygen_rating = int(oxygen_string, 2)
    print("oxygen rating: ", oxygen_rating)

    # And now the co2 rating
    # list of lists needed
    inputs = []
    n_inputs = len(input_array)
    print(n_inputs)
    n_line = len(input_array[0])
    for n in range(n_inputs):
        line_inputs = []
        for m in range(n_line-1):
            line_inputs.append(int(input_array[n][m]))
        inputs.append(line_inputs)

    for m in range(n_line-1):
        sum_0, sum_1 = bit_sum(inputs, n_inputs, m)

        if sum_0 > sum_1:
            selected = 1
        else:
            selected = 0

        new_inputs = []
        for n in range(n_inputs):
            if inputs[n][m] == selected:
                new_inputs.append(inputs[n])

        if len(new_inputs) == 1:
            break
        else:
            inputs = copy.deepcopy(new_inputs)
            n_inputs = len(inputs)

    print("final for co2: ", new_inputs)

    co2_string = ""
    for m in range(n_line-1):
        co2_string += str(new_inputs[0][m])

    co2_rating = int(co2_string, 2)
    print("co2 rating: ", co2_rating)

    answer = oxygen_rating * co2_rating

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
