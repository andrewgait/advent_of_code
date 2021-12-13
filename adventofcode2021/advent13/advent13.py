# Advent of code, day 13

# open file
input = open("advent13_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def print_grid(grid):
    for j in range(len(grid)):
        print_line = ""
        for i in range(len(grid[0])):
            if grid[j][i] == 1:
                print_line += "#"
            else:
                print_line += "."

        print(print_line)

    print(" ")


def part1():

    answer = 0

    max_x = 0
    max_y = 0
    coords = []
    n = 0
    while input_array[n][0] != "\n":
        splitcomma = input_array[n].split(",")
        x = int(splitcomma[0])
        y = int(splitcomma[1])
        coords.append([x, y])
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

        n += 1

    folds = []
    for nn in range(n+1, len(input_array)):
        splitspace = input_array[nn].split(" ")
        splitequals = splitspace[2].split("=")
        folds.append([splitequals[0], int(splitequals[1])])

    print(coords)
    print(folds)

    max_x = max_x + 1
    max_y = max_y + 1

    # Make first grid
    grid = [[0 for x in range(max_x)] for y in range(max_y)]

    for n in range(len(coords)):
        grid[coords[n][1]][coords[n][0]] = 1

    print_grid(grid)

    # Now loop over folds (Note: a fold might not be exactly in the middle!)
    for n in range(len(folds)):
        new_grid = []
        if folds[n][0] == "x":
            new_max_x = folds[n][1]
            for y in range(max_y):
                new_grid_line = []
                for x in range(new_max_x):
                    if (2*new_max_x-x) > (max_x - 1):
                        if (grid[y][x] == 1):
                            new_grid_line.append(1)
                        else:
                            new_grid_line.append(0)
                    else:
                        if (grid[y][x] == 1) or (grid[y][(2*new_max_x)-x] == 1):
                            new_grid_line.append(1)
                        else:
                            new_grid_line.append(0)
                new_grid.append(new_grid_line)
            max_x = new_max_x
        else:
            new_max_y = folds[n][1]
            for y in range(new_max_y):
                new_grid_line = []
                for x in range(max_x):
                    if (2*new_max_y-y) > (max_y - 1):
                        if (grid[y][x] == 1):
                            new_grid_line.append(1)
                        else:
                            new_grid_line.append(0)
                    else:
                        if (grid[y][x] == 1) or (grid[(2*new_max_y)-y][x] == 1):
                            new_grid_line.append(1)
                        else:
                            new_grid_line.append(0)
                new_grid.append(new_grid_line)
            max_y = new_max_y

        # count dots after first step
        if n == 0:
            count_dots = 0
            for y in range(max_y):
                for x in range(max_x):
                    if (new_grid[y][x] == 1):
                        count_dots += 1

            answer = count_dots

        print_grid(new_grid)
        grid = new_grid


    return answer


def part2():

    # Part 2 was really just an extension of part 1, the answer is printed
    # (in dot form) at the end of part 1.  For my data it was PGHZBFJC

    answer = "PGHZBFJC"

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
