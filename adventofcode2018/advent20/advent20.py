# Advent of code, day 20
import numpy as np
import matplotlib.pyplot as plt


# open file
input = open("advent20_input.txt", "r")
#input = open("advent20_test_input.txt", "r")
#input = open("advent20_test_input2.txt", "r")
#input = open("advent20_test_input3.txt", "r")
#input = open("advent20_test_input4.txt", "r")
#input = open("advent20_test_input5.txt", "r")

def char_from_val(val):
    characters = [".", "#", "|", "-", "?", "X", "o"]
    return characters[val]


def val_from_char(char):
    characters = [".", "#", "|", "-", "?", "X", "o"]
    return characters.index(char)


def render_grid(grid):
    # render grid
    for j in range(len(grid)):
        str_line = ''
        for i in range(len(grid[j])):
            str_line += char_from_val(grid[j][i])

        print(str_line)

    print(' ')

# set the walls of the current location
def set_walls(grid, x, y):
    # wherever you land in a direction, the four directions
    # NE, NW, SE, SW are all walls
    grid[y-1][x-1] = val_from_char("#")
    grid[y-1][x+1] = val_from_char("#")
    grid[y+1][x-1] = val_from_char("#")
    grid[y+1][x+1] = val_from_char("#")

    # N, E, S, W are either doors already, or ?s
    # to east
    if (grid[y][x+1] != val_from_char("|")):
        grid[y][x+1] = val_from_char("?")
    # to west
    if (grid[y][x-1] != val_from_char("|")):
        grid[y][x-1] = val_from_char("?")
    # to south
    if (grid[y+1][x] != val_from_char("-")):
        grid[y+1][x] = val_from_char("?")
    # to north
    if (grid[y-1][x] != val_from_char("-")):
        grid[y-1][x] = val_from_char("?")

    return grid


# how big is the actual grid... ?
gridsize = 220
grid = []
for j in range(gridsize):
    gridline = []
    for i in range(gridsize):
        gridline.append(val_from_char("o"))
    grid.append(gridline)

# start in the middle
startx = gridsize // 2
starty = gridsize // 2

x = startx
y = starty

# initial set of branch coordinates
branchx = []
branchy = []

# read string into array
for line in input:
    for ch in line:
        if (ch == "^"):
            # at the beginning
            grid[y][x] = val_from_char("X")
            # NE, NW, SE, SW are all walls
            grid = set_walls(grid, x, y)
        elif (ch == "N"):
            # move north
            y -= 2
            grid[y][x] = val_from_char(".")
            # we just came through a door to the south
            grid[y+1][x] = val_from_char("-")
            grid = set_walls(grid, x, y)
        elif (ch == "S"):
            # move south
            y += 2
            grid[y][x] = val_from_char(".")
            # we just came through a door to the north
            grid[y-1][x] = val_from_char("-")
            grid = set_walls(grid, x, y)
        elif (ch == "E"):
            # move east
            x += 2
            grid[y][x] = val_from_char(".")
            # we just came through a door to the west
            grid[y][x-1] = val_from_char("|")
            grid = set_walls(grid, x, y)
        elif (ch == "W"):
            # move west
            x -= 2
            grid[y][x] = val_from_char(".")
            # we just came through a door to the east
            grid[y][x+1] = val_from_char("|")
            grid = set_walls(grid, x, y)
        elif (ch == "("):
            # set the current location
            branchx.append(x)
            branchy.append(y)
            print('open(', branchx, branchy, x, y)
        elif (ch == ")"):
            # this is at the end of some instructions, go back to
            # where we were at the start... ?
            x = branchx[-1]
            y = branchy[-1]
            del branchx[-1]
            del branchy[-1]
            print('close)', branchx, branchy, x, y)
        elif (ch == "|"):
            # return back to branch location set earlier?
            x = branchx[-1]
            y = branchy[-1]
            print('pipe|', branchx, branchy, x, y)
        elif (ch == "$"):
            # at the end; loop, convert all ?s to walls #
            render_grid(grid)
            for j in range(gridsize):
                for i in range(gridsize):
                    if (grid[j][i] == val_from_char("?")):
                        grid[j][i] = val_from_char("#")


render_grid(grid)

# resize the grid... ?
resize_grid = []
distance_grid = []
for j in range(gridsize):
    resize_line = []
    distance_line = []
    for i in range(gridsize):
        if (grid[j][i] != val_from_char("o")):
            resize_line.append(grid[j][i])
            distance_line.append(0)
            if (grid[j][i] == val_from_char("X")):
                resize_x = len(resize_line)-1
                resize_y = len(resize_grid)

    if (len(resize_line) > 0):
        resize_grid.append(resize_line)
        distance_grid.append(distance_line)


print(line)
print(' ')
render_grid(resize_grid)

print('X is at ', resize_x, resize_y)

new_grid_size = len(resize_grid)

# so I think... on this grid we have now, we can simply measure
# distances in a clever-ish way
def test_doors(grid, distance_grid, x, y, distance):
    work_done = False
    if (grid[y][x+1] == val_from_char("|")):
        if (distance_grid[y][x+2] == 0):
            distance_grid[y][x+2] = distance
            work_done = True
    if (grid[y][x-1] == val_from_char("|")):
        if (distance_grid[y][x-2] == 0):
            distance_grid[y][x-2] = distance
            work_done = True
    if (grid[y+1][x] == val_from_char("-")):
        if (distance_grid[y+2][x] == 0):
            distance_grid[y+2][x] = distance
            work_done = True
    if (grid[y-1][x] == val_from_char("-")):
        if (distance_grid[y-2][x] == 0):
            distance_grid[y-2][x] = distance
            work_done = True

    return distance_grid, work_done


distance = 1
distance_grid[resize_y][resize_x] = distance

work_done = True
while work_done:
    work_done = False
    if (distance == 1):
        distance += 1
        # go from X
        distance_grid, work_done = test_doors(
            resize_grid, distance_grid, resize_x, resize_y, distance)
    else:
        # loop and find all current distances
        for j in range(new_grid_size):
            for i in range(new_grid_size):
                if (distance_grid[j][i] == distance):
                    distance_grid, done = test_doors(
                        resize_grid, distance_grid, i, j, distance+1)

                    if (done):
                        work_done = True

        distance += 1

thousand_doors = 0
door_limit = 1000

for j in range(new_grid_size):
    print(distance_grid[j])
    for i in range(new_grid_size):
        if ((distance_grid[j][i]-1) >= door_limit):
            thousand_doors += 1


# here I have had to start the distance from 1 at my current location, so the distance is -2
print('the furthest room is ', distance-2, ' doors away')
print('there are ', thousand_doors, ' rooms through at least 1000 doors')

distances = np.asarray(distance_grid)

plt.imshow(distances, cmap='hot', interpolation='nearest', title='distance plot to rooms')
plt.colorbar()
plt.show()
