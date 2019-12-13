# Advent of code 2019, day 13
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# open file
input = open("advent13_input.txt", "r")
# input = open("advent13_test_input.txt", "r")
# input = open("advent13_test_input2.txt", "r")
# input = open("advent13_test_input3.txt", "r")

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
for i in range(2000):
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
                print('instruction3, input, outputs: ', input, outputs)
                input_data[store_at] = input
                op_pos += 2
                input_read = True
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
#             if len(outputs)==2:
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
            if grid[j][i] == 0:
                str += "."
            elif grid[j][i] == 1:
                str += "W"
            elif grid[j][i] == 2:
                str += "B"
            elif grid[j][i] == 3:
                str += "P"
            elif grid[j][i] == 4:
                str += "O"
        print(str)

    print("\n")

def make_first_grid(outputs):

    min_y = min_x = 99999
    max_x = max_y = 0

    score = 0
    for n in range(0,len(outputs),3):
        if outputs[n] == -1 and outputs[n+1] == 0:
            score = outputs[n+2]
        else:
            if outputs[n] < min_x:
                min_x = outputs[n]
            if outputs[n] > max_x:
                max_x = outputs[n]
            if outputs[n+1] < min_y:
                min_y = outputs[n+1]
            if outputs[n+1] > max_y:
                max_y = outputs[n+1]

    print('grid: ', min_x, max_x, min_y, max_y, ' score: ', score)
    # make an array with this size (cheating for now because I know mins are 0)

    grid = np.zeros((max_y+1, max_x+1), dtype=np.int64)

    for n in range(0,len(outputs),3):
        if outputs[n] == -1 and outputs[n+1] == 0:
            score = outputs[n+2]
        else:
            grid[outputs[n+1]][outputs[n]] = outputs[n+2]

    print("Score is ", score)

    draw_grid(grid)

    return grid, score

def display_grid_and_score(outputs, grid):
    score = 0
    print(outputs)
    for n in range(0,len(outputs),3):
        print(n)
        if outputs[n] == -1 and outputs[n+1] == 0:
            score = outputs[n+2]
        else:
            grid[outputs[n+1]][outputs[n]] = outputs[n+2]

    print("Score is ", score)
    draw_grid(grid)

    return grid, score

def count_blocks_in_grid(grid):
    count_blocks = 0
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if (grid[j][i] == 2):
                count_blocks += 1

    return count_blocks

def get_ball_paddle_x(grid):
    ball_x = 0
    paddle_x = 0
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if (grid[j][i] == 3):
                paddle_x = i
            if (grid[j][i] == 4):
                ball_x = i

    return ball_x, paddle_x


def part1(input_data, relative_base):
    op_pos = 0
    input = 0  # seems from instructions as though this isn't needed?
    outputs, op_pos, relative_base, input_data = get_value(
        input_data, input, op_pos, relative_base)

    print(op_pos, relative_base, len(outputs), outputs)

    grid, score = make_first_grid(outputs)

    # find 2 (block tile) in grid
    count_blocks = count_blocks_in_grid(grid)

    return count_blocks


def part2(input_data, relative_base):

    op_pos = 0
    input_data[0] = 2
    input = 0
    outputs, op_pos, relative_base, input_data1 = get_value(
        input_data, input, op_pos, relative_base)

    print(op_pos, relative_base, len(outputs), outputs)

    grid, score = make_first_grid(outputs)

    grids = []
    grids.append(grid.copy())

    while True:
        # work out the input based on where the ball_x and paddle_x are
        ball_x, paddle_x = get_ball_paddle_x(grid)
        if ball_x < paddle_x:
            input = -1
        elif ball_x > paddle_x:
            input = 1
        else:
            input = 0

#         print("input is ", input)
        outputs, op_pos, relative_base, input_data = get_value(
            input_data, input, op_pos, relative_base)
#         print(op_pos, relative_base, len(outputs), outputs)

        grid, score = display_grid_and_score(outputs, grid)

        grids.append(grid.copy())
        # Finish when number of blocks is zero
        count_blocks = count_blocks_in_grid(grid)

        print("Blocks: ", count_blocks)

        if count_blocks == 0:
            break

    return score, grids

relative_base = 0
print(len(input_data), input_data)
print('Part1: ', part1(input_data, relative_base))
print('\n')

relative_base = 0
print(' part2 input ', len(part2_input_data))
print(part2_input_data)
score, grids = part2(part2_input_data, relative_base)
print('Part2: ', score)

# Can "grids" be animated?
print(len(grids))
print("\n")

x = np.linspace(0, 1, len(grids[0][0])+1)
y = np.linspace(0, 1, len(grids[0])+1)
xmesh, ymesh = np.meshgrid(x,y)

fig = plt.figure()
ims = []
print("Animating ", len(grids), " grids")
for n in range(len(grids)):
# for n in range(100):
    if n % 500 == 0:
        print(n)
    array = np.flipud(np.array(grids[n]))
# print(array)
    ims.append((plt.pcolor(xmesh, ymesh, array),))

im_ani = animation.ArtistAnimation(fig, ims, interval=10, repeat_delay=3000,
                                   blit=True)

plt.show()
