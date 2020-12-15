# Advent of code, day 15

# open file
input = open("advent15_input.txt", "r")
# input = open("advent15_test_input.txt", "r")
# input = open("advent15_test_input2.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    answer = 0

    start_values = input_array[0].split(",")
    n = len(start_values)

    values = []
    for i in range(n):
        values.append(int(start_values[i]))

    for i in range(n, 2020):
        if (values[i-1] not in values[0:i-1]):
            values.append(0)
        else:
            # loop backwards and find the previous value
            loop_val = i-2
#             print(values)
            while values[i-1] != values[loop_val]:
                loop_val -= 1
            values.append(i - 1 - loop_val)

    print(values)

    answer = values[-1]

    return answer

def part2():

    answer = 0

    start_values = input_array[0].split(",")
    n = len(start_values)

    values_dict = dict()
    for i in range(n):
        last_value = int(start_values[i])
        values_dict[int(start_values[i])] = []
        values_dict[int(start_values[i])].append(i)

    for i in range(n, 30000000):
#         if (i % 10000 == 0):
#             print(i)
        if (len(values_dict[last_value]) == 1):
            if 0 not in values_dict.keys():
                values_dict[0] = []
            values_dict[0].append(i)
            last_value = 0
        else:
            # loop backwards and find the previous value
            new_value = values_dict[last_value][-1] - values_dict[last_value][-2]
            if new_value not in values_dict.keys():
                values_dict[new_value] = []
            values_dict[new_value].append(i)
            last_value = new_value

    answer = last_value

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
