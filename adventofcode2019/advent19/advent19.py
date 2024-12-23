# Advent of code 2019, day 19
import numpy as np

# open file
input = open("advent19_input.txt", "r")

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
for i in range(100):
    input_data.append(0)

# make a separate copy for part2
part2_input_data = []
for i in range(len(input_data)):
    part2_input_data.append(input_data[i])
# print(input_data)

# global asciichars dict
asciichars = dict()
for i in range(127):
    asciichars[chr(i)] = i

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
            if len(outputs)==1:
                return outputs, op_pos, relative_base, input_data
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

        print(str)

    print("\n")

def get_beam_size(input_data, relative_base, size, draw):
    op_pos = 0
    grid = np.zeros((size,size), dtype=np.int32)

    n_points = 0

    # inputs in this case are just (x, y) coordinates
    # probably a good idea not to change the position or relative base between calls
    inputs = []
    for j in range(size):
        for i in range(size):
            inputs += [i, j]
            outputs, _op_pos, _relative_base, _input_data = get_value(
                input_data, inputs, op_pos, relative_base)
            if outputs[0] == 0:
                grid[j][i] = asciichars['.']
            elif outputs[0] == 1:
                grid[j][i] = asciichars['#']
                n_points += 1

    if draw:
        draw_grid(grid)

    return n_points


def part1(input_data, relative_base):
    answer = get_beam_size(input_data, relative_base, 50, True)

    return answer

def part2(input_data, relative_base):

    # make the grid
    beam_sizes = []
    for n in range(3):
        print("Grid size calc: ", 10**n)
        beam_sizes.append(get_beam_size(input_data, relative_base, 10**n, False))

    print(beam_sizes)

    op_pos = 0
    # looking for a complete 100x100 grid of tractor beam, so 1000x1000 might be
    # big enough? by a little bit of guesswork based on the above beam size
    # calcs I found that it needed to be ~ 1100x1100
    size = 1100
    grid = np.zeros((size,size), dtype=np.int32)

    n_points = 0

    # make the grid - no need to make all of it, just start from a "sensible" place
    for j in range(800,size):
#         print("make grid row ", j)
        n_beams = 0
        for i in range(size):
            input = [i, j]
            outputs, _op_pos, _relative_base, _input_data = get_value(
                input_data, input, op_pos, relative_base)

            if outputs[0] == 0:
                grid[j][i] = asciichars['.']
            elif outputs[0] == 1:
                grid[j][i] = asciichars['#']
                n_points += 1
                n_beams += 1

#         print("this row has ", n_beams, " beams")


    # loop over the grid again and search for 100x100 grids with just beam
    loc_i = loc_j = 0
    found = False
    for j in range(800,size-100):
#         print("searching on grid row ", j)
        for i in range(size-100):
            sum = 0
            if grid[j][i] == asciichars['#']:
                emptyfound = False
                for y in range(j,j+100):
                    for x in range(i,i+100):
                        if grid[y][x] == asciichars['#']:
                            sum += 1
                        else:
                            emptyfound = True
                            break

                    if emptyfound:
                        break

            if sum == 10000:
                loc_i = i
                loc_j = j
                found = True
                break

        if found:
            break

    answer = (loc_i * 10000) + loc_j

    return answer


relative_base = 0
answer1 = part1(input_data, relative_base)
print('Part1: ', answer1)
print('\n')

answer2 = part2(part2_input_data, relative_base)
print('Part2: ', answer2)
