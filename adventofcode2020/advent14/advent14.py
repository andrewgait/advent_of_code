# Advent of code, day 14
import numpy

# open file
input = open("advent14_input.txt", "r")
# input = open("advent14_test_input.txt", "r")
# input = open("advent14_test_input2.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    # looks like the largest index in the mem array in input is ~67k
    mem_array = numpy.zeros(100000, dtype=numpy.int64)

    bin_len = 36
    current_mask = ['X'] * bin_len

    n = len(input_array)
    for i in range(n):
        if input_array[i][0:2] == "ma":
            splitspace = input_array[i].split(" ")
            for j in range(bin_len):
                current_mask[j] = splitspace[-1][j]
        else:
            splitspace = input_array[i].split(" ")
            value = int(splitspace[-1][:-1])
            binary_val = format(value, "0"+str(bin_len)+"b")
            splitsqbr = splitspace[0].split("]")
            location = int(splitsqbr[0][4:])

            new_binary_str = ""
            for j in range(bin_len):
                if (current_mask[j] == "X"):
                    new_binary_str += binary_val[j]
                else:
                    new_binary_str += current_mask[j]

            new_value = int(new_binary_str, 2)

            mem_array[location] = new_value

    answer = sum(mem_array)

    return answer

def part2():

    # locations are not quite as obvious, so make a dict instead
    mem_dict = dict()

    bin_len = 36
    current_mask = ['0'] * bin_len

    n = len(input_array)
    for i in range(n):
        if input_array[i][0:2] == "ma":
            splitspace = input_array[i].split(" ")
            for j in range(bin_len):
                current_mask[j] = splitspace[-1][j]
        else:
            # this time the location is what is changed
            splitspace = input_array[i].split(" ")
            value = int(splitspace[-1][:-1])
            splitsqbr = splitspace[0].split("]")

            location = int(splitsqbr[0][4:])
            binary_loc = format(location, "0"+str(bin_len)+"b")

            n_x = 0
            for j in range(bin_len):
                if (current_mask[j] == "X"):
                    n_x += 1

            array_len = pow(2, n_x)
            new_binary_str = [""] * array_len
            max_len = array_len
            factor = 1
            for j in range(bin_len):
                if (current_mask[j] == "0"):
                    for i in range(array_len):
                        new_binary_str[i] += binary_loc[j]
                elif (current_mask[j] == "1"):
                    for i in range(array_len):
                        new_binary_str[i] += current_mask[j]
                else:
                    # current_mask[j] == "X"
                    for n in range(factor):
                        for i in range(n * max_len, (n * max_len) + max_len // 2):
                            new_binary_str[i] += "0"
                        for i in range((n * max_len) + (max_len//2), (n+1) * max_len):
                            new_binary_str[i] += "1"

                    # reduce max_n_x
                    max_len = max_len // 2
                    factor = factor * 2

            for i in range(array_len):
                location = int(new_binary_str[i], 2)
                mem_dict[location] = value

    answer = sum(mem_dict.values())

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
