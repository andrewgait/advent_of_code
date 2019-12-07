# Advent of code, day 5

# open file
input = open("advent5_input.txt", "r")
# input = open("advent5_test_input.txt", "r")
# input = open("advent5_test_input2.txt", "r")
# input = open("advent5_test_input3.txt", "r")
# input = open("advent5_test_input4.txt", "r")

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

def get_operating_values(input_data, op_pos, par1, par2):
    loc1 = input_data[op_pos+1]
    loc2 = input_data[op_pos+2]
    if par1 == 1:
        val1 = loc1
    else:
        val1 = input_data[loc1]
    if par2 == 1:
        val2 = loc2
    else:
        val2 = input_data[loc2]

    return val1, val2

def get_value(base_input_data, input):
    op_pos = 0
    input_data = []
    for i in range(len(base_input_data)):
        input_data.append(base_input_data[i])

#     print(input_data)
    output = 0

    while op_pos < len(input_data):

        opcode = input_data[op_pos]
        par3 = (opcode // 10**4)
        next = opcode - (par3 * 10**4)
        par2 = (next // 10**3)
        next = next - (par2 * 10**3)
        par1 = (next // 10**2)
        next = next - (par1 * 10**2)
        instruction = next

#         print(input_data)
#         print(instruction, par1, par2, par3)

        # parameter modes only change for instructions 1 and 2?
        if (instruction==1):
            store_at = input_data[op_pos+3]

            val1, val2 = get_operating_values(input_data, op_pos, par1, par2)

            value = val1 + val2
            input_data[store_at] = value
            op_pos += 4
        elif (instruction==2):
            store_at = input_data[op_pos+3]

            val1, val2 = get_operating_values(input_data, op_pos, par1, par2)

            value = val1 * val2
            input_data[store_at] = value
            op_pos += 4
        elif (instruction==3):
            store_at = input_data[op_pos+1]
            input_data[store_at] = input
            op_pos += 2
        elif (instruction==4):
            value_at = input_data[op_pos+1]
            if par1 == 0:
                output = input_data[value_at]
            else:
                output = value_at
            op_pos += 2
        elif (instruction==5):
            val1, val2 = get_operating_values(input_data, op_pos, par1, par2)
#             print('instruction=5, values: ', val1, val2)

            if val1 != 0:
                op_pos = val2
            else:  # "Do nothing" i.e. move on to the next instruction
                op_pos += 3
        elif (instruction==6):
            val1, val2 = get_operating_values(input_data, op_pos, par1, par2)
#             print('instruction=6, values: ', val1, val2)

            if val1 == 0:
                op_pos = val2
            else:  # "Do nothing" i.e. move on to the next instruction
                op_pos += 3
        elif (instruction==7):
            store_at = input_data[op_pos+3]

            val1, val2 = get_operating_values(input_data, op_pos, par1, par2)

            if (val1 < val2):
                input_data[store_at] = 1
            else:
                input_data[store_at] = 0
            op_pos += 4
        elif (instruction==8):
            store_at = input_data[op_pos+3]

            val1, val2 = get_operating_values(input_data, op_pos, par1, par2)

            if (val1 == val2):
                input_data[store_at] = 1
            else:
                input_data[store_at] = 0
            op_pos += 4


        else:
            break

#         print(op_pos, input_data)

    print('output is: ', output)
    return output, input_data

def part1(input_data, input):
    output, data = get_value(input_data, input)

    return output, data

def part2(input_data, input):
    output, data = get_value(input_data, input)

    return output, data

print(input_data)
print('Part1: ', part1(input_data, 1))
print(base_input_data)
print('Part2: ', part2(base_input_data, 5))