# Advent of code 2022, day 12
import numpy as np

# open file
input = open("advent12_input.txt", "r")
# input = open("advent12_test_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def visitedall(visitedgrid, nx, ny):
    visit_all = True
    for y in ny:
        for x in nx:
            if visited_grid[y][x] == 0:
                visit_all = False
                break

    return visit_all

def calculate_steps(grid, start, end, nx, ny, min_step):

    # print("starting at ", start, " with end ", end, " min_step ", min_step)
    stepgrid = np.zeros((ny,nx), dtype=int)
    visitedgrid = np.zeros((ny,nx), dtype=int)

    current_list = [start]
    visitedgrid[start[0]][start[1]] = 1
    at_end = False
    step = 0

    while (not at_end):
    # for step in range(50):
        neighbours = []
        step += 1
        # print(step, current_list)
        for current in current_list:
            # Check up, down, left, right
            current_x = current[1]
            current_y = current[0]
            current_value = grid[current_y][current_x]
            if current_x == start[1] and current_y == start[0]:
                current_value = "a"
            if ((current_x + 1) < nx):
                if (visitedgrid[current_y][current_x+1] == 0):
                    grid_value = grid[current_y][current_x+1]
                    if grid_value == "E":
                        grid_value = "z"
                    if ord(grid_value) - ord(current_value) <= 1:
                        neighbours.append([current_y, current_x+1])
                        visitedgrid[current_y][current_x+1] = 1
                        stepgrid[current_y][current_x+1] = step
                        if [current_y,current_x+1] == end:
                            at_end = True
                            break

            if ((current_x - 1) >= 0):
                if (visitedgrid[current_y][current_x-1] == 0):
                    grid_value = grid[current_y][current_x-1]
                    if grid_value == "E":
                        grid_value = "z"
                    if ord(grid_value) - ord(current_value) <= 1:
                        neighbours.append([current_y, current_x-1])
                        visitedgrid[current_y][current_x-1] = 1
                        stepgrid[current_y][current_x-1] = step
                        if [current_y,current_x-1] == end:
                            at_end = True
                            break

            if ((current_y + 1) < ny):
                if (visitedgrid[current_y+1][current_x] == 0):
                    grid_value = grid[current_y+1][current_x]
                    if grid_value == "E":
                        grid_value = "z"
                    if ord(grid_value) - ord(current_value) <= 1:
                        neighbours.append([current_y+1, current_x])
                        visitedgrid[current_y+1][current_x] = 1
                        stepgrid[current_y+1][current_x] = step
                        if [current_y+1,current_x] == end:
                            at_end = True
                            break

            if ((current_y - 1) >= 0):
                if (visitedgrid[current_y-1][current_x] == 0):
                    grid_value = grid[current_y-1][current_x]
                    if grid_value == "E":
                        grid_value = "z"
                    if ord(grid_value) - ord(current_value) <= 1:
                        neighbours.append([current_y-1, current_x])
                        visitedgrid[current_y-1][current_x] = 1
                        stepgrid[current_y-1][current_x] = step
                        if [current_y-1,current_x] == end:
                            at_end = True
                            break

        current_list = neighbours

        if step > min_step:
            at_end = True

    return step

def part1():
    grid = []
    start = []
    end = []

    ny = 0

    for input_line in input_array:
        grid_line = []
        nx = 0
        for n in range(len(input_line)-1):
            grid_line.append(input_line[n])
            if input_line[n] == "S":
                start = [ny,nx]
            if input_line[n] == "E":
                end = [ny,nx]
            nx += 1
        grid.append(grid_line)
        ny += 1

    print(grid)
    print(start, end, nx, ny)

    # The max possible steps is the size of the grid
    min_step = nx * ny
    step = calculate_steps(grid, start, end, nx, ny, min_step)

    answer = step

    return answer

def part2():

    grid = []
    starts = []
    end = []

    ny = 0

    for input_line in input_array:
        grid_line = []
        nx = 0
        for n in range(len(input_line)-1):
            if input_line[n] == "S" or input_line[n] == "a":
                grid_line.append("a")
                starts.append([ny,nx])
            else:
                grid_line.append(input_line[n])
            if input_line[n] == "E":
                end = [ny,nx]
            nx += 1
        grid.append(grid_line)
        ny += 1

    print(grid)
    print(starts, end, nx, ny)

    # The max steps is the size of the grid
    min_step = nx * ny
    for start in starts:
        step = calculate_steps(grid, start, end, nx, ny, min_step)
        print("start ", start, " has at least ", step, " steps ")
        if step < min_step:
            min_step = step

    answer = min_step

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
