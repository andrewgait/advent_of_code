# Advent of code 2019, day 15
import numpy as np

# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

# open file
input = open("advent15_input.txt", "r")
# input = open("advent15_test_input.txt", "r")
# input = open("advent15_test_input2.txt", "r")
# input = open("advent15_test_input3.txt", "r")

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
#                print('instruction3, input, outputs: ', input, outputs)
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
            if grid[j][i] == 0:
                str += "_"  # not checked region
            elif grid[j][i] == 1:
                str += "."  # checked, empty
            elif grid[j][i] == 2:
                str += "#"  # checked, wall
            elif grid[j][i] == 3:
                str += "D"  # where droid currently is
            elif grid[j][i] == 4:
                str += "O"  # where oxygen tank is

        print(str)

    print("\n")

def move_robot(grid, distance, robot_x, robot_y, input, output):
    # work out where the robot faces next
    if input == 1:  # NORTH
        if output == 0:
            grid[robot_y-1][robot_x] = 2
        elif output == 1:
            grid[robot_y][robot_x] = 1
            grid[robot_y-1][robot_x] = 3
            if (distance[robot_y-1][robot_x] == 0):
                distance[robot_y-1][robot_x] = distance[robot_y][robot_x]+1
            robot_y -= 1
        elif output == 2:
            grid[robot_y-1][robot_x] = 4
            distance[robot_y-1][robot_x] = distance[robot_y][robot_x]+1
            robot_y -= 1
    if input == 2:  # SOUTH
        if output == 0:
            grid[robot_y+1][robot_x] = 2
        elif output == 1:
            grid[robot_y][robot_x] = 1
            grid[robot_y+1][robot_x] = 3
            if (distance[robot_y+1][robot_x] == 0):
                distance[robot_y+1][robot_x] = distance[robot_y][robot_x]+1
            robot_y += 1
        elif output == 2:
            grid[robot_y+1][robot_x] = 4
            distance[robot_y+1][robot_x] = distance[robot_y][robot_x]+1
            robot_y += 1
    if input == 3:  # WEST
        if output == 0:
            grid[robot_y][robot_x-1] = 2
        elif output == 1:
            grid[robot_y][robot_x] = 1
            grid[robot_y][robot_x-1] = 3
            if (distance[robot_y][robot_x-1] == 0):
                distance[robot_y][robot_x-1] = distance[robot_y][robot_x]+1
            robot_x -= 1
        elif output == 2:
            grid[robot_y][robot_x-1] = 4
            distance[robot_y][robot_x-1] = distance[robot_y][robot_x]+1
            robot_x -= 1
    if input == 4:  # EAST
        if output == 0:
            grid[robot_y][robot_x+1] = 2
        elif output == 1:
            grid[robot_y][robot_x] = 1
            grid[robot_y][robot_x+1] = 3
            if (distance[robot_y][robot_x+1] == 0):
                distance[robot_y][robot_x+1] = distance[robot_y][robot_x]+1
            robot_x += 1
        elif output == 2:
            grid[robot_y][robot_x+1] = 4
            distance[robot_y][robot_x+1] = distance[robot_y][robot_x]+1
            robot_x ++ 1

    return grid, distance, robot_x, robot_y

def get_oxygen_distance(grid, start_x, start_y):
    # Find the oxygen system
    ox_x = ox_y = 0
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if grid[j][i] == 4:
                ox_x = i
                ox_y = j

    return abs(start_x-ox_x)+abs(start_y-ox_y)


def part1(input_data, relative_base):

    op_pos = 0
    input = 0  # seems from instructions as though this isn't needed?
    # we need to move a robot around a grid
    size = 50
    grid = np.zeros((size,size), dtype=np.int32)
    distance = np.zeros((size,size), dtype=np.int32)

    start_x = start_y = robot_x = robot_y = size//2

    grid[robot_y][robot_x] = 3
    distance[robot_y][robot_x] = 1

    # north is 1, south is 2, west is 3, east is 4
    facing = 1
    input = 1

    while True:
        outputs, op_pos, relative_base, input_data = get_value(
            input_data, input, op_pos, relative_base)
        output = outputs[0]

        print(input, output)

        grid, distance, robot_x, robot_y = move_robot(
            grid, distance, robot_x, robot_y, input, output)

        draw_grid(grid)
        print(distance)

        if output == 2:
            if input == 1: # NORTH
                input = 3 # WEST
            elif input == 2: # SOUTH
                input = 4 # EAST
            elif input == 3: # WEST
                input = 2 # SOUTH
            elif input == 4: # EAST
                input = 1 # NORTH
            break
        elif output == 0:  # WALL
            # turn to face somewhere else?
            if input == 1: # NORTH
                input = 4 # EAST
            elif input == 2: # SOUTH
                input = 3 # WEST
            elif input == 3: # WEST
                input = 1 # NORTH
            elif input == 4: # EAST
                input = 2 # SOUTH
        elif output == 1:  # empty, moved forward
            # turn the opposite way to if there was a wall!
            if input == 1: # NORTH
                input = 3 # WEST
            elif input == 2: # SOUTH
                input = 4 # EAST
            elif input == 3: # WEST
                input = 2 # SOUTH
            elif input == 4: # EAST
                input = 1 # NORTH

    print(start_x, start_y)
    print(robot_x, robot_y)

    # the distance grid started at 1, so subtract 1 off the value here
    return (distance[robot_y][robot_x]-1, robot_x, robot_y, input_data,
            relative_base, input, op_pos, grid, distance)


def part2(input_data, relative_base, robot_x, robot_y,
          input, op_pos, grid, distance):

    # op_pos = 0
    # input = 0  # seems from instructions as though this isn't needed?
    # we need to move a robot around a grid
    size = 50
    # grid = np.zeros((size,size), dtype=np.int32)
    distance = np.zeros((size,size), dtype=np.int32)

    ox_x = ox_y = -1
    start_x = robot_x
    start_y = robot_y

    grid[robot_y][robot_x] = 3
    distance[robot_y][robot_x] = 1

    # north is 1, south is 2, west is 3, east is 4
    facing = 1
    input = 1

    # searching grid finishes once start square has been visited 4 times
    start_visited = 0

    while True:
        outputs, op_pos, relative_base, input_data = get_value(
            input_data, input, op_pos, relative_base)
        output = outputs[0]

#        print(input, output)

        grid, distance, robot_x, robot_y = move_robot(
            grid, distance, robot_x, robot_y, input, output)

#        draw_grid(grid)
#        print(distance)
        if robot_x == start_x and robot_y == start_y:
            start_visited += 1
            print('start visited: ', start_visited)

        if start_visited == 4:
            break

        if output == 2:
            ox_x = robot_x
            ox_y = robot_y

        if output == 0:  # WALL
            # turn to face somewhere else?
            if input == 1: # NORTH
                input = 4 # EAST
            elif input == 2: # SOUTH
                input = 3 # WEST
            elif input == 3: # WEST
                input = 1 # NORTH
            elif input == 4: # EAST
                input = 2 # SOUTH
        elif output == 1 or output == 2:  # empty, or oxygen, moved forward
            # turn the opposite way to if there was a wall!
            if input == 1: # NORTH
                input = 3 # WEST
            elif input == 2: # SOUTH
                input = 4 # EAST
            elif input == 3: # WEST
                input = 2 # SOUTH
            elif input == 4: # EAST
                input = 1 # NORTH

    print(start_x, start_y)

    grid[ox_y][ox_x] = 4
    draw_grid(grid)
    #    print(distance.tolist())

    # the distance grid started at 1, so subtract 1 off the max
    return np.max(distance) - 1


def test_robot_movement():
    # we need to move a robot around a grid
    size = 10
    grid = np.zeros((size,size), dtype=np.int32)
    distance = np.zeros((size,size), dtype=np.int32)

    start_x = start_y = robot_x = robot_y = size//2

    grid[robot_y][robot_x] = 3
    distance[robot_y][robot_x] = 1

    inputs = [1, 4, 1, 2, 4, 3, 3, 2, 2, 3, 1, 1, 1]
    outputs = [0, 1, 0, 0, 0, 1, 0, 1, 0, 2, 0, 0, 0]

    # north is 1, south is 2, west is 3, east is 4
    facing = 1
    while True:
#     for i in range(len(inputs)):
        input = inputs.pop(0)
        output = outputs.pop(0)
        print(input, output)

        grid, distance, robot_x, robot_y = move_robot(
            grid, distance, robot_x, robot_y, input, output)

        draw_grid(grid)
        print(distance)

        if output == 2:
            break

    # Ah. we're not working out here what the distance is, it's
    # how many robot movements it needs to get to where it just arrived...
    # ... and it's quite possible that there's a shorter route available
    # that it hasn't seen yet
    print(start_x, start_y)

    return get_oxygen_distance(grid, start_x, start_y)

print("Test, distance =  ", test_robot_movement())

relative_base = 0
print(len(input_data), input_data)
(answer, robot_x, robot_y, input_data, relative_base, input, op_pos, grid,
    distance) = part1(input_data, relative_base)
print('Part1: ', answer)
print('\n')

max_time = part2(input_data, relative_base, robot_x, robot_y,
                 input, op_pos, grid, distance)
print('Part2: ', max_time)
