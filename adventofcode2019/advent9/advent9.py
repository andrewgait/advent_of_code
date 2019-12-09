# Advent of code, day 9

# open file
input = open("advent9_input.txt", "r")
# input = open("advent9_test_input.txt", "r")
# input = open("advent9_test_input2.txt", "r")
# input = open("advent9_test_input3.txt", "r")

# read string into array
for line in input:
    input_string = line

input_list = input_string.split(",")
input_data = []
for i in range(len(input_list)):
    input_data.append(int(input_list[i]))

print(len(input_data))
codelen = len(input_data)

# extra memory space needed?
for i in range(1000):
    input_data.append(0)

# make a separate copy for part2
part2_input_data = []
for i in range(len(input_data)):
    part2_input_data.append(input_data[i])
# print(input_data)

def get_operating_values(input_data, op_pos, par1, par2, par3, relative_base):
    if par1 == 2:
        loc1 = input_data[op_pos+1]+relative_base
    else:
        loc1 = input_data[op_pos+1]
    if par2 == 2:
        loc2 = input_data[op_pos+2]+relative_base
    else:
        loc2 = input_data[op_pos+2]

#     print(op_pos, par1, par2)
#     print(loc1, loc2)

    if par1 == 1:
        val1 = loc1
    else:
        val1 = input_data[loc1]
    if par2 == 1:
        val2 = loc2
    else:
        val2 = input_data[loc2]

    if par3 == 2:
        val3 = input_data[op_pos+3] + relative_base
    else:
        val3 = input_data[op_pos+3]

    return val1, val2, val3

def get_value(base_input_data, input1, input2, first_input, op_pos,
              relative_base):
    input_data = []
    for i in range(len(base_input_data)):
        input_data.append(base_input_data[i])

    outputs = []

    while op_pos < len(input_data):

        opcode = input_data[op_pos]
        par3 = (opcode // 10**4)
        next = opcode - (par3 * 10**4)
        par2 = (next // 10**3)
        next = next - (par2 * 10**3)
        par1 = (next // 10**2)
        next = next - (par1 * 10**2)
        instruction = next

        if (instruction == 99) or (instruction == 0):
            break

        if (instruction==1):
            # add
            val1, val2, val3 = get_operating_values(
                input_data, op_pos, par1, par2, par3, relative_base)

            store_at = val3


            value = val1 + val2
            input_data[store_at] = value
            op_pos += 4
        elif (instruction==2):
            # multiply
            val1, val2, val3 = get_operating_values(
                input_data, op_pos, par1, par2, par3, relative_base)

            store_at = val3

            value = val1 * val2
            input_data[store_at] = value
            op_pos += 4
        elif (instruction==3):
            # input value
            store_at = input_data[op_pos+1]
            if par1 == 2:
                store_at = relative_base + input_data[op_pos+1]
            if first_input:
                input_data[store_at] = input1
                first_input = False
            else:
                input_data[store_at] = output[-1]
            op_pos += 2
        elif (instruction==4):
            # output value
            value_at = input_data[op_pos+1]
            if par1 == 0:
                output = input_data[value_at]
            elif par1 == 2:
                output = input_data[value_at+relative_base]
            else:
                output = value_at
            op_pos += 2
            outputs.append(output)
        elif (instruction==5):
            # jump if non-zero
            val1, val2, val3 = get_operating_values(
                input_data, op_pos, par1, par2, par3, relative_base)

            if val1 != 0:
                op_pos = val2
            else:  # "Do nothing" i.e. move on to the next instruction
                op_pos += 3
        elif (instruction==6):
            # jump if zero
            val1, val2, val3 = get_operating_values(
                input_data, op_pos, par1, par2, par3, relative_base)

            if val1 == 0:
                op_pos = val2
            else:  # "Do nothing" i.e. move on to the next instruction
                op_pos += 3
        elif (instruction==7):
            # if 1 less than 2
            val1, val2, val3 = get_operating_values(
                input_data, op_pos, par1, par2, par3, relative_base)

            store_at = val3

            if (val1 < val2):
                input_data[store_at] = 1
            else:
                input_data[store_at] = 0
            op_pos += 4
        elif (instruction==8):
            # if equals
            val1, val2, val3 = get_operating_values(
                input_data, op_pos, par1, par2, par3, relative_base)

            store_at = val3

            if (val1 == val2):
                input_data[store_at] = 1
            else:
                input_data[store_at] = 0
            op_pos += 4
        elif (instruction==9):
            # adjust the relative base
            if par1 == 1:
                relative_base += input_data[op_pos+1]
            elif par1 == 0:
                relative_base += input_data[input_data[op_pos+1]]
            else:
                relative_base += input_data[input_data[op_pos+1]+relative_base]

            op_pos += 2

    return outputs, op_pos, input_data

def part1(input_data, input1, relative_base):
    op_pos = 0
    output, op_pos, input_data = get_value(input_data, input1, input1,
                                           True, op_pos, relative_base)

    return output, op_pos, input_data

def part2(input_data, input1, relative_base):
    op_pos = 0
    output, op_pos, input_data = get_value(input_data, input1, input1,
                                           True, op_pos, relative_base)

    return output, op_pos, input_data

relative_base = 0
print(input_data)
print('Part1: ', part1(input_data, 1, relative_base))

relative_base = 0
print(part2_input_data)
print('Part2: ', part2(part2_input_data, 2, relative_base))