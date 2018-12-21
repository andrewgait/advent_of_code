# Advent of code, day 17

# the version in advent17.py works, but takes FOREVER
# this is an attempt to rewrite from the water's PoV

# open file
input = open("advent17_input.txt", "r")
#input = open("advent17_test_input.txt", "r")
#input = open("advent17_test_input2.txt", "r")


def char_from_val(val):
    characters = [".", "#", "|", "~", "+"]
    return characters[val]


def val_from_char(char):
    characters = [".", "#", "|", "~", "+"]
    return characters.index(char)


# function to render slice
def render_slice(grid):
    # render grid
    for j in range(len(grid)):
        str_line = ''
        for i in range(len(grid[j])):
            str_line += char_from_val(grid[j][i])

        print(str_line)

    print(' ')


spring = [500, 0]

# store x- and y- veins
x_veins = []
y_veins = []

max_x = 0
max_y = 0
min_x = 99999
min_y = 99999
# read input
for line in input:
    x_vein = []
    y_vein = []
    data = line.split(' ', 1)
    if (data[0][0] == "x"):
        # add the x value
        x_val = int(data[0][2:-1])
        x_vein.append(x_val)
        if (x_val > max_x):
            max_x = x_val
        # append the y values
        str_ys = data[1].split('..', 1)
        y_min = int(str_ys[0][2:])
        x_vein.append(y_min)
        if (y_min < min_y):
            min_y = y_min
        y_max = int(str_ys[1])
        x_vein.append(y_max)
        if (y_max > max_y):
            max_y = y_max

        x_veins.append(x_vein)
    elif (data[0][0] == "y"):
        # add the y value
        y_val = int(data[0][2:-1])
        if (y_val > max_y):
            max_y = y_val
        y_vein.append(y_val)
        # append the x values
        str_xs = data[1].split('..', 1)
        x_min = int(str_xs[0][2:])
        y_vein.append(x_min)
        if (x_min < min_x):
            min_x = x_min
        x_max = int(str_xs[1])
        y_vein.append(x_max)
        if (x_max > max_x):
            max_x = x_max

        y_veins.append(y_vein)

print('min/max: ', min_x, min_y, max_x, max_y)

# more work here
# pad coordinates from max on each side
pad = 4
initial_grid = []
for j in range(max_y+1):
    initial_line = []
    for i in range(max_x-min_x+pad+1):
        initial_line.append(val_from_char("."))

    initial_grid.append(initial_line)

# add the spring
initial_grid[spring[1]][spring[0]-(min_x-2)] = val_from_char("+")

# list the clay
clay = []

# loop and add clay veins
for n in range(len(x_veins)):
    x = x_veins[n][0]-(min_x-2)
    ymin = x_veins[n][1]
    ymax = x_veins[n][2]
    for y in range(ymin, ymax+1):
        initial_grid[y][x] = val_from_char("#")
        clay.append([x,y])

for n in range(len(y_veins)):
    y = y_veins[n][0]
    xmin = y_veins[n][1]-(min_x-2)
    xmax = y_veins[n][2]-(min_x-2)
    for x in range(xmin, xmax+1):
        initial_grid[y][x] = val_from_char("#")
        clay.append([x,y])

# print initial grid to check
render_slice(initial_grid)

# print('clay: ', clay)

# list different states of water
settled_water = []
# the initial moving water is directly below the spring
moving_water = [[spring[0]-(min_x-2),spring[1]+1]]
initial_grid[spring[1]+1][spring[0]-(min_x-2)] = val_from_char("|")

grid = initial_grid
gridx = len(grid[0])
gridy = len(grid)
# loop while water added
water_added = True
sumwater = 0
xminsearch = 0
xmaxsearch = 0
timecount = 0
while (water_added):
    # now set it to false, only set to true if something is added
    water_added = False

    # loop over moving water
    moving_to_append = []
    settled_to_append = []
    for n in range(len(moving_water)):
        x = moving_water[n][0]
        y = moving_water[n][1]
        if (y < gridy-1):
            if (grid[y+1][x] == val_from_char(".")):
                grid[y+1][x] = val_from_char("|")
                moving_to_append.append([x,y+1])
                water_added = True
            elif ((grid[y+1][x] == val_from_char("#")) or
                  (grid[y+1][x] == val_from_char("~"))):
                if (grid[y][x+1] == val_from_char(".")):
                    grid[y][x+1] = val_from_char("|")
                    moving_to_append.append([x+1,y])
                    water_added = True
                if (grid[y][x-1] == val_from_char(".")):
                    grid[y][x-1] = val_from_char("|")
                    moving_to_append.append([x-1,y])
                    water_added = True

    for n in range(len(clay)):
        xc = clay[n][0]
        yc = clay[n][1]
        sum = 0
        finish = False
        while not finish:
            if (grid[yc][xc+1+sum] == val_from_char("|")):
                sum += 1
            elif (grid[yc][xc+1+sum] == val_from_char("#")):
                # we found the end
                if (sum > 0):  # watch out for two #s next to each other
                    for n in range(sum):
                        grid[yc][xc+1+n] = val_from_char("~")
                    water_added = True
                finish = True
            else:
                finish = True


    for m in range(len(moving_to_append)):
        moving_water.append(moving_to_append[m])

    timecount += 1
    if ((timecount % 1000) == 0):
        print('time: ', timecount)

render_slice(grid)

# end of while loop
sumlines = 0
sumstill = 0
for j in range(min_y, len(grid)):  # only sum from the min_y coordinate!
    for i in range(len(grid[j])):
        if (grid[j][i] == val_from_char("|")):
           sumlines += 1
        elif (grid[j][i] == val_from_char("~")):
           sumstill += 1

print('there are ', sumlines+sumstill, ' squares with ~ or |, out of ', (max_x-min_x)*(max_y-min_y),
      '\n of which ', sumstill, ' are at rest')
