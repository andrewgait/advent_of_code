# Advent of code, day 2

# open file
input = open("advent2_input.txt", "r")
# input = open("advent2_test_input.txt", "r")
# input = open("advent2_test_input2.txt", "r")
# input = open("advent2_test_input3.txt", "r")

# read string into array
for line in input:
    input_string = line

input_list = input_string.split(",")
input_data = []
for i in range(len(input_list)):
    input_data.append(int(input_list[i]))

base_input_data = []
for i in range(len(input_list)):
    base_input_data.append(input_data[i])
# print(input_data)

def get_value(base_input_data, input1, input2):
    op_pos = 0
    input_data = []
    for i in range(len(base_input_data)):
        input_data.append(base_input_data[i])

    input_data[1] = input1
    input_data[2] = input2
#     print(input_data)

    while op_pos < len(input_data):

        if (input_data[op_pos]==1):
            store_at = input_data[op_pos+3]
            loc1 = input_data[op_pos+1]
            loc2 = input_data[op_pos+2]
            value = input_data[loc1] + input_data[loc2]
            input_data[store_at] = value
        elif (input_data[op_pos]==2):
            store_at = input_data[op_pos+3]
            loc1 = input_data[op_pos+1]
            loc2 = input_data[op_pos+2]
            value = input_data[loc1] * input_data[loc2]
            input_data[store_at] = value
        else:
            break

#         print(op_pos, input_data)
        op_pos += 4

    return input_data

def part1(input_data):
    input_data = get_value(input_data, 12, 2)

    return input_data[0]

def part2():
    done = False
    for noun in range(100):
        for verb in range(100):
            test_data = get_value(base_input_data, noun, verb)
            if (test_data[0] == 19690720):
                print('break at noun, verb', noun, verb)
                done = True
                break
        if done:
            break

    return 100*noun + verb

print(input_data)
print(part1(input_data))
print(base_input_data)
print(part2())