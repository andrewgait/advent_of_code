# Advent of code, day 18

# note: for part 2, the seqeunce repeats
# every 7000 minutes so I was able to use
# this to do the calculation for 1 billion minutes

# open file
input = open("advent18_input.txt", "r")
#input = open("advent18_test_input.txt", "r")


def char_from_val(val):
    characters = [".", "#", "|"]
    return characters[val]


def val_from_char(char):
    characters = [".", "#", "|"]
    return characters.index(char)


def render_grid(grid):
    # render grid
    for j in range(len(grid)):
        str_line = ''
        for i in range(len(grid[j])):
            str_line += char_from_val(grid[j][i])

        print(str_line)

    print(' ')

# three functions for changing based on the character
# the grid will be built so that the loop is over the interior
def change_open(grid, x, y):
    sumtree = 0
    # loop over the nearby grid, count trees
    for j in range(y-1,y+2):
        for i in range(x-1,x+2):
            # don't count the middle
            if ((i==x) and (j==y)):
                dummy = 0
            else:
                if (grid[j][i] == val_from_char("|")):
                    sumtree += 1

    if (sumtree > 2):
        return True
    else:
        return False


def change_tree(grid, x, y):
    sumlumber = 0
    # loop over the nearby grid, count lumberyards
    for j in range(y-1,y+2):
        for i in range(x-1,x+2):
            if ((i==x) and (j==y)):
                dummy = 0
            else:
                if (grid[j][i] == val_from_char("#")):
                    sumlumber += 1

    if (sumlumber > 2):
        return True
    else:
        return False


def change_lumberyard(grid, x, y):
    sumtree = 0
    sumlumber = 0
    # loop over the nearby grid, count trees and lumberyards
    for j in range(y-1,y+2):
        for i in range(x-1,x+2):
            if ((i==x) and (j==y)):
                dummy = 0
            else:
                if (grid[j][i] == val_from_char("#")):
                    sumlumber += 1
                elif (grid[j][i] == val_from_char("|")):
                    sumtree += 1

    if ((sumlumber > 0) and (sumtree > 0)):
        return False
    else:
        return True


grid = []
# read string into array
# what should happen here is that a ring of "."
# should be added around the whole grid as a halo,
# and this will deal with issues re: corner/edge cases
for line in input:
    gridline = []
    if (len(grid)==0):
        for n in range(len(line)+1):
            gridline.append(val_from_char("."))
        grid.append(gridline)
        gridline = []
        gridline.append(val_from_char("."))
        for n in range(len(line)):
            if (line[n] == "."):
                gridline.append(val_from_char("."))
            elif (line[n] == "|"):
                gridline.append(val_from_char("|"))
            elif (line[n] == "#"):
                gridline.append(val_from_char("#"))

        gridline.append(val_from_char("."))
        grid.append(gridline)
    else:
        gridline.append(val_from_char("."))
        for n in range(len(line)):
            if (line[n] == "."):
                gridline.append(val_from_char("."))
            elif (line[n] == "|"):
                gridline.append(val_from_char("|"))
            elif (line[n] == "#"):
                gridline.append(val_from_char("#"))

        gridline.append(val_from_char("."))
        grid.append(gridline)

gridline = []
for n in range(len(line)+2):
    gridline.append(val_from_char("."))

grid.append(gridline)

render_grid(grid)
gridx = len(grid[0])
gridy = len(grid)

print(gridx, gridy)

time = 0

while (time < 1000000000):
    new_grid = []

    new_line = []
    for i in range(gridx):
        new_line.append(val_from_char("."))

    new_grid.append(new_line)

    for j in range(1,gridy-1):
        new_line = []
        new_line.append(val_from_char("."))
        for i in range(1,gridx-1):
            if (grid[j][i] == val_from_char(".")):
                if (change_open(grid, i, j)):
                    new_line.append(val_from_char("|"))
                else:
                    new_line.append(val_from_char("."))
            elif (grid[j][i] == val_from_char("|")):
                if (change_tree(grid, i, j)):
                    new_line.append(val_from_char("#"))
                else:
                    new_line.append(val_from_char("|"))
            elif (grid[j][i] == val_from_char("#")):
                if (change_lumberyard(grid, i, j)):
                    new_line.append(val_from_char("."))
                else:
                    new_line.append(val_from_char("#"))

        new_line.append(val_from_char("."))
        new_grid.append(new_line)

    new_line = []
    for i in range(gridx):
        new_line.append(val_from_char("."))

    new_grid.append(new_line)


    # not sure if this needs to be
    grid = new_grid
#    render_grid(grid)
    time += 1

# render_grid(grid)

    # final grid calculation
    sumtree = 0
    sumlumber = 0
    for j in range(gridy):
        for i in range(gridx):
            if (grid[j][i] == val_from_char("|")):
                sumtree += 1
            if (grid[j][i] == val_from_char("#")):
                sumlumber += 1

    if (time % 1000 == 0):
        print('sumtree ', sumtree, ' x sumlumber ', sumlumber,
              ' = resource ', sumtree*sumlumber, ' time ', time)

