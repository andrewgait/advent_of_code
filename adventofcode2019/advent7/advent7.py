# Advent of code, day 7
from itertools import permutations

# open file
input = open("advent7_input.txt", "r")
# input = open("advent7_test_input.txt", "r")
# input = open("advent7_test_input2.txt", "r")
# input = open("advent7_test_input3.txt", "r")
# input = open("advent7_test_input4.txt", "r")
# input = open("advent7_test_input5.txt", "r")

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

def get_value(base_input_data, input1, input2, first_input, op_pos):
    input_data = []
    for i in range(len(base_input_data)):
        input_data.append(base_input_data[i])

#     print(input_data)
    output = None

    while op_pos < len(input_data):

#         print('step: input_data: ', input_data, input1, input2, op_pos)
        opcode = input_data[op_pos]
        par3 = (opcode // 10**4)
        next = opcode - (par3 * 10**4)
        par2 = (next // 10**3)
        next = next - (par2 * 10**3)
        par1 = (next // 10**2)
        next = next - (par1 * 10**2)
        instruction = next

        if instruction == 99:
            output = None
            break
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
            if first_input:
                input_data[store_at] = input1
                first_input = False
            else:
                input_data[store_at] = input2
            op_pos += 2
        elif (instruction==4):
            value_at = input_data[op_pos+1]
            if par1 == 0:
                output = input_data[value_at]
            else:
                output = value_at
            op_pos += 2
            return output, op_pos, input_data
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


#         print(op_pos, input_data)

#     print('whats this: ', output, input_data, op_pos)
    return output, op_pos, input_data

def part1(input_data, input1):
    max_thrusters = 0
    n_amps = 5
    max_loc = []

    # loop over all amplifier possibilities
    perms = permutations(range(5))

#     for a in range(n_amps):
#         for b in range(n_amps):
#             for c in range(n_amps):
#                 for d in range(n_amps):
#                     for e in range(n_amps):
    op_pos = 0
    for perm in perms:
        output1, _op_pos, _data = get_value(input_data, perm[0], input1, True, op_pos)
        output2, _op_pos, _data = get_value(input_data, perm[1], output1, True, op_pos)
        output3, _op_pos, _data = get_value(input_data, perm[2], output2, True, op_pos)
        output4, _op_pos, _data = get_value(input_data, perm[3], output3, True, op_pos)
        output5, _op_pos, _data = get_value(input_data, perm[4], output4, True, op_pos)

        if output5 > max_thrusters:
            max_thrusters = output5
            max_loc = perm  # [i,j,k,m,n]

    return max_thrusters, max_loc

def part2(input_data, input1):
    max_thrusters = 0
    n_amps = 5
    max_loc = []
    feedback_mode = 5

    # loop over all amplifier possibilities
    perms = permutations(range(feedback_mode, feedback_mode+n_amps))
#     for i in range(feedback_mode, feedback_mode+n_amps):
#         for j in range(feedback_mode, feedback_mode+n_amps):
#             for k in range(feedback_mode, feedback_mode+n_amps):
#                 for m in range(feedback_mode, feedback_mode+n_amps):
#                     for n in range(feedback_mode, feedback_mode+n_amps):

    perms = [(9,8,7,6,5)]

#     print('start at', input_data)
    for perm in perms:
        op_pos1 = 0
        op_pos2 = 0
        op_pos3 = 0
        op_pos4 = 0
        op_pos5 = 0
        output1, op_pos1, input_data1 = get_value(input_data, perm[0], input1, True, op_pos1)
        output2, op_pos2, input_data2 = get_value(input_data, perm[1], output1, True, op_pos2)
        output3, op_pos3, input_data3 = get_value(input_data, perm[2], output2, True, op_pos3)
        output4, op_pos4, input_data4 = get_value(input_data, perm[3], output3, True, op_pos4)
        output5, op_pos5, input_data5 = get_value(input_data, perm[4], output4, True, op_pos5)

#         print(perm, output5, op_pos5, input_data5)
        # clearly this now keeps going, but I have no idea how it stops!  is it when output is zero?
        max_val = 0
        count = 0
        while count < 10:
            output1, op_pos1, input_data1 = get_value(input_data1, output5, output5, True, op_pos1)
            output2, op_pos2, input_data2 = get_value(input_data2, output1, output1, True, op_pos2)
            output3, op_pos3, input_data3 = get_value(input_data3, output2, output2, True, op_pos3)
            output4, op_pos4, input_data4 = get_value(input_data4, output3, output3, True, op_pos4)
            output5, op_pos5, input_data5 = get_value(input_data5, output4, output4, True, op_pos5)

            if output5:
#                 print('input_data: ', input_data5)
#                 print(perm, output5, count)
                if output5 > max_val:
                   max_val = output5
            else:
                break

            count += 1

            if max_val > max_thrusters:
                max_thrusters = max_val
                max_loc = perm  # [i,j,k,m,n]

#             for i in range(len(input_data1)):
#                 input_data1[i] = next_input_data1[i]
#                 input_data2[i] = next_input_data2[i]
#                 input_data3[i] = next_input_data3[i]
#                 input_data4[i] = next_input_data4[i]
#                 input_data5[i] = next_input_data5[i]

    return max_thrusters, max_loc

print(input_data)
print('Part1: ', part1(input_data, 0))
print(base_input_data)
print('Part2: ', part2(base_input_data, 0))