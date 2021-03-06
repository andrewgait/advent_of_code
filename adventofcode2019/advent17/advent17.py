# Advent of code 2019, day 17
import numpy as np

# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

# open file
input = open("advent17_input.txt", "r")
# input = open("advent17_test_input.txt", "r")
# input = open("advent17_test_input2.txt", "r")
# input = open("advent17_test_input3.txt", "r")

input_string = None

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
for i in range(10000):
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

def get_value(base_input_data, input, op_pos, relative_base):
    input_data = []
    for i in range(len(base_input_data)):
        input_data.append(base_input_data[i])

    outputs = []

    input_read = False

    while op_pos < len(input_data):

        opcode = input_data[op_pos]
#         print('opcode ', opcode)
        par3 = (opcode // 10**4)
        next = opcode - (par3 * 10**4)
        par2 = (next // 10**3)
        next = next - (par2 * 10**3)
        par1 = (next // 10**2)
        next = next - (par1 * 10**2)
        instruction = next

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
            if not input_read:
                store_at = input_data[op_pos+1]
                if par1 == 2:
                    store_at = relative_base + input_data[op_pos+1]
#                print('instruction3, input, outputs: ', input, outputs)
                input_data[store_at] = input.pop(0)
                op_pos += 2
#                 input_read = True
            else:
                break
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
            # in this case the output needs to be returned, not appended ?
            outputs.append(output)
            # when it gets to two outputs, send it
#             if len(outputs)==1:
#                 return outputs, op_pos, relative_base, input_data
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
        elif (instruction==99):
            break

    return outputs, op_pos, relative_base, input_data

def draw_grid(grid):
    for j in range(len(grid)):
        str = ""
        for i in range(len(grid[j])):
            str += chr(grid[j][i])  # reads ascii value

#             if grid[j][i] == 0:
#                 str += "_"  # not checked region
#             elif grid[j][i] == 46:
#                 str += "."  # checked, dot (empty)
#             elif grid[j][i] == 35:
#                 str += "#"  # checked, scaffold
#             elif grid[j][i] == 3:
#                 str += "D"  # where droid currently is
#             elif grid[j][i] == 4:
#                 str += "O"  # where oxygen tank is

        print(str)

    print("\n")

def part1(input_data, relative_base):

    op_pos = 0
    input = 0


    outputs, op_pos, relative_base, input_data = get_value(
        input_data, input, op_pos, relative_base)

    print(input)
    print(len(outputs), outputs)

    print([chr(i) for i in range(127)])
    grid = []
    grid_row = []

    for n in range(len(outputs)-1):  # I don't know why but I'm getting two 10s
        if outputs[n] == 10:  # newline
            grid.append(grid_row.copy())
            grid_row = []
        else:
            grid_row.append(outputs[n])

    print(grid)

    draw_grid(grid)

    # within the grid find every intersection of scaffolds (35)
    # Loop over interior as there can't be an intersection on the edge
    answer = 0
    for j in range(1,len(grid)-1):
        for i in range(1,len(grid[j])-1):
            if grid[j][i] == 35:
                # everything around it needs to be 35 as well
                if ((grid[j-1][i] == 35) and (grid[j+1][i] == 35) and
                    (grid[j][i-1] == 35) and (grid[j][i+1] == 35)):
                    answer += i*j
                    # set grid value to O just for fun
                    grid[j][i] = 79

    draw_grid(grid)

    return answer

def make_asciis(input, asciichars):
    ascii_inst = []
    for n in range(len(input)):
        if input[n]=='12': # 12 isn't an ascii character!  Use two 6s!
            ascii_inst.append(asciichars['6'])
            ascii_inst.append(asciichars[','])
            ascii_inst.append(asciichars['6'])
        else:
            ascii_inst.append(asciichars[input[n]])

    ascii_inst.append(asciichars['\n'])

    return ascii_inst


def part2(input_data, relative_base):

    op_pos = 0

    # make a dict for ascii characters
    asciichars = dict()
    for i in range(127):
        asciichars[chr(i)] = i

    # A visual inspection of my scaffold tells me the full instructions are
#     full_input = [L4,L6,L8,L12,L8,R12,L12,L8,R12,L12,L4,L6,L8,L12,
#                   L8,R12,L12,R12,L6,L6,L8,L4,L6,L8,L12,R12,L6,L6,L8,
#                   L8,R12,L12,R12,L6,L6,L8]

    # ok so routines can be (remembering commas need to be converted!)
    input_A = ['L',',','4',',','L',',','6',',','L',',','8',',','L',',','12']
    input_B = ['L',',','8',',','R',',','12',',','L',',','12']
    input_C = ['R',',','12',',','L',',','6',',','L',',','6',',','L',',','8']

    full_input = ['A',',','B',',','B',',','A',',','B',',','C',',','A',',','C',
                  ',','B',',','C']

    # convert these into ascii numbers
    full = make_asciis(full_input, asciichars)
    A = make_asciis(input_A, asciichars)
    B = make_asciis(input_B, asciichars)
    C = make_asciis(input_C, asciichars)

    # Read all the instructions!
    video = [asciichars['n'], asciichars['\n']]

    all_inst = full + A + B + C + video

    print('all_inst: ', all_inst)

    input_data[0] = 2

    outputs, op_pos, relative_base, input_data = get_value(
        input_data, all_inst, op_pos, relative_base)
    print(len(outputs), outputs)

    answer = outputs[-1]

    return answer


relative_base = 0
print(len(input_data), input_data)
answer1 = part1(input_data, relative_base)
print('Part1: ', answer1)
print('\n')

answer2 = part2(part2_input_data, relative_base)
print('Part2: ', answer2)
