# Advent of code, day 3
import numpy as np

# open file
input = open("advent3_input.txt", "r")
# input = open("advent3_test_input.txt", "r")
# input = open("advent3_test_input2.txt", "r")
# input = open("advent3_test_input3.txt", "r")

input_lists = []

# read string into array
for line in input:
    input_string = line[:-1]
    input_list = input_string.split(",")
    input_lists.append(input_list)

print(input_lists)

def print_grid(grid, gridsize):
    grid_chars = [".", "o", "|", "-", "+", "X"]
    for i in range(gridsize):
        string = ""
        for j in range(gridsize):
            string = string+grid_chars[grid[i][j]]
        print(string)

def make_grids(input_lists, gridsize, start_at):
    print("Make grids")
    grid = np.zeros((gridsize, gridsize), dtype=np.int32)
    number_grid1 = np.zeros((gridsize, gridsize), dtype=np.int32)
    number_grid2 = np.zeros((gridsize, gridsize), dtype=np.int32)

    grid[start_at][start_at] = 1
    x_at = start_at
    y_at = start_at
    max_x = 0
    min_x = gridsize
    max_y = 0
    min_y = gridsize

    print("First wire")
    count = 0
    input1size = len(input_lists[0])
    for n in range(input1size):
        # Read first character
        char = input_lists[0][n][0]
        num = int(input_lists[0][n][1:])
        if char=="U":
            for m in range(num):
                grid[y_at+m+1][x_at] = 2
                if number_grid1[y_at+m+1][x_at] != 0:
                    count += 1
                else:
                    count += 1
                    number_grid1[y_at+m+1][x_at] = count
            y_at += num
        elif char=="D":
            for m in range(num):
                grid[y_at-m-1][x_at] = 2
                if number_grid1[y_at-m-1][x_at] != 0:
                    count += 1
                else:
                    count += 1
                    number_grid1[y_at-m-1][x_at] = count
            y_at -= num
        elif char=="L":
            for m in range(num):
                grid[y_at][x_at-m-1] = 3
                if number_grid1[y_at][x_at-m-1] != 0:
                    count += 1
                else:
                    count += 1
                    number_grid1[y_at][x_at-m-1] = count
            x_at -= num
        elif char=="R":
            for m in range(num):
                grid[y_at][x_at+m+1] = 3
                if number_grid1[y_at][x_at+m+1] != 0:
                    count += 1
                else:
                    count += 1
                    number_grid1[y_at][x_at+m+1] = count
            x_at += num

        if grid[y_at][x_at] != 1:
            grid[y_at][x_at] = 4

        if x_at > max_x:
            max_x = x_at
        if x_at < min_x:
            min_x = x_at
        if y_at > max_y:
            max_y = y_at
        if y_at < min_y:
            min_y = y_at


    # Save the grid for the first wire; wires crossing themselves should
    # not create an X
    print("Save first grid")
    grid_atone = np.copy(grid)
#     for i in range(gridsize):
#         grid_row = []
#         for j in range(gridsize):
#             grid_row.append(grid[i][j])
#         grid_atone.append(grid_row)

    count = 0
    x_at = start_at
    y_at = start_at
    input2size = len(input_lists[1])
    print("Second wire")
    for n in range(input2size):
        # Read first character
        char = input_lists[1][n][0]
#         print(char)
        num = int(input_lists[1][n][1:])
#         print(num, x_at, y_at)
        if char=="U":
            for m in range(num):
                if grid_atone[y_at+m+1][x_at] != 0:
                    grid[y_at+m+1][x_at] = 5
                else:
                    grid[y_at+m+1][x_at] = 2
                if number_grid2[y_at+m+1][x_at] != 0:
                    count += 1
                else:
                    count += 1
                    number_grid2[y_at+m+1][x_at] = count
            y_at += num
        elif char=="D":
            for m in range(num):
                if grid_atone[y_at-m-1][x_at] != 0:
                    grid[y_at-m-1][x_at] = 5
                else:
                    grid[y_at-m-1][x_at] = 2
                if number_grid2[y_at-m-1][x_at] != 0:
                    count += 1
                else:
                    count += 1
                    number_grid2[y_at-m-1][x_at] = count
            y_at -= num
        elif char=="L":
            for m in range(num):
                if grid_atone[y_at][x_at-m-1] != 0:
                    grid[y_at][x_at-m-1] = 5
                else:
                    grid[y_at][x_at-m-1] = 3
                if number_grid2[y_at][x_at-m-1] != 0:
                    count += 1
                else:
                    count += 1
                    number_grid2[y_at][x_at-m-1] = count
            x_at -= num
        elif char=="R":
            for m in range(num):
                if grid_atone[y_at][x_at+m+1] != 0:
                    grid[y_at][x_at+m+1] = 5
                else:
                    grid[y_at][x_at+m+1] = 3
                if number_grid2[y_at][x_at+m+1] != 0:
                    count += 1
                else:
                    count += 1
                    number_grid2[y_at][x_at+m+1] = count
            x_at += num

        if grid[y_at][x_at] != 1:
            grid[y_at][x_at] = 4

        if x_at > max_x:
            max_x = x_at
        if x_at < min_x:
            min_x = x_at
        if y_at > max_y:
            max_y = y_at
        if y_at < min_y:
            min_y = y_at

    print('mins: ', min_x, min_y)
    print('maxs: ', max_x, max_y)

    return grid, number_grid1, number_grid2, min_x, max_x, min_y, max_y

def part1(input_lists, gridsize):
    # Make a grid... from input, needs to be about 5000x5000, and start in middle
#     gridsize = 20
    start_at = gridsize // 2
    grid, numbers1, numbers2, min_x, max_x, min_y, max_y = make_grids(
        input_lists, gridsize, start_at)
#     print_grid(grid, gridsize)
    print('searching for Xs')

    # Loop over grid, find Xs, find distance to port (start_at)
    min_distance = (gridsize+gridsize)*10
    for i in range(min_x, max_x+1):
        for j in range(min_y, max_y+1):
            if (grid[j][i] == 5):
                distance = abs(j-start_at) + abs(i-start_at)
                print("X at ", i, j, " distance ", distance)
                if distance < min_distance:
                    min_distance = distance

    return min_distance

def part2(input_lists, gridsize):
    start_at = gridsize // 2
    grid, numbers1, numbers2, min_x, max_x, min_y, max_y = make_grids(
        input_lists, gridsize, start_at)

    print("work out steps to intersections")
    # Find an intersection
    min_wire_distance = 1000000000000
#     wire_distance = 0
    for i in range(min_x, max_x+1):
        for j in range(min_y, max_y+1):
            if (grid[j][i] == 5):
                # work backwards from here to get distance?
                # No! simply read numbers from number grids!
                wire1 = numbers1[j][i]
                wire2 = numbers2[j][i]
                wire_distance = wire1 + wire2
                if wire_distance < min_wire_distance:
                    min_wire_distance = wire_distance

    return min_wire_distance

# gridsize = 20000 was too small for input
print("Part 1: closest distance: ", part1(input_lists, 30000))
print("Part 2: min wire distance: ", part2(input_lists, 30000))

