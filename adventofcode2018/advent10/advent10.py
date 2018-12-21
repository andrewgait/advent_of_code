# Advent of code, day 10

# open file
input = open("advent10_input.txt", "r")
# input = open("advent10_test_input.txt", "r")

# read string into array
initial_coords = []
coordinates = []
velocities = []
coord_length = 6  # 2 for test, 6 for actual
vel_length = 2  # 2 for both
base = 10  # for both
second_base = 12
max_x = 0
min_x = 0
max_y = 0
min_y = 0
for line in input:
    x_start = base
    x_end = x_start+(coord_length)
    y_start = x_end+2
    y_end =  y_start+(coord_length)
    v_start = y_end+second_base
    v_end = v_start+(vel_length)
    w_start = v_end+2
    w_end = w_start+(vel_length)
    x_coord = int(line[x_start:x_end])
    if (x_coord > max_x):
        max_x = x_coord
    if (x_coord < min_x):
        min_x = x_coord
    y_coord = int(line[y_start:y_end])
    if (y_coord > max_y):
        max_y = y_coord
    if (y_coord < min_y):
        min_y = y_coord
    initial_coords.append([x_coord, y_coord])
    coordinates.append([0, 0])
    velocities.append([int(line[v_start:v_end]),
                       int(line[w_start:w_end])])

print('initial coordinates: ', initial_coords)
print('velocities: ', velocities)
print('min_x, min_y: ', min_x, min_y)
print('max_x, min_y: ', max_x, max_y)
print('len(coordinates): ', len(coordinates))

begin_time = 10600
time = 10700
max_adjacency = 0
max_time = 0
for t in range(begin_time, time):
    # want the grid to start at [0,0], so add min_x_min_y to max_x_max_y
#    grid = []
#    viewer_size = 500
#    for j in range(-viewer_size, viewer_size):
#        initial_line = []
#        for i in range(-viewer_size, viewer_size):
#            initial_line.append(0)
#        grid.append(initial_line)
#
#    grid_x = len(initial_line)
#    grid_y = len(grid)

    # print('coordinates: ', coordinates)
    # loop over coordinates and put them in the grid
#    counted_coords = 0
#    for n in range(len(coordinates)):
#        if (((coordinates[n][0]) >= -viewer_size) and
#            ((coordinates[n][0]) < viewer_size) and
#            ((coordinates[n][1]) >= -viewer_size) and
#            ((coordinates[n][1]) < viewer_size)):
#            grid[coordinates[n][1]+viewer_size][coordinates[n][0]+viewer_size] = 1
#            counted_coords += 1

    # print out new grid.  how... convert to string and print line by line?
    # doing a best guess, it's probably a good idea to only print the central region as that's
    # where the message is most likely to show up...
#    print('centre of grid at time ', t)
#    for j in range(grid_y):
#    if (counted_coords > 10):
        # do another test on this grid for adjacent coords
#        adjacent_coords = 0
        # loop over grid
#        for i in range((viewer_size*2)-1):
#            for j in range((viewer_size*2)-1):
#                if ((grid[i][j]==1) and (grid[i+1][j]==1)):
#                    adjacent_coords += 1
#                if ((grid[i][j+1]==1) and (grid[i][j]==1)):
#                    adjacent_coords += 1

#        if (adjacent_coords > 0):
#            print('adjacent_coords in view area!: ', adjacent_coords)
#            for j in range(viewer_size*2):
#                this_line = ''
    #        for i in range(grid_x):
#                for i in range(viewer_size*2):
#                    this_line += str(grid[j][i])
                    #this_line += str(grid[j][(grid_x/2])

#                print(this_line)

#            print(' ')
    # now make a new set of coordinates using the velocities
    for n in range(len(velocities)):
        coordinates[n][0] = initial_coords[n][0]+(t*(velocities[n][0]))
        coordinates[n][1] = initial_coords[n][1]+(t*(velocities[n][1]))
#        new_coords.append([coordinates[n][0]+velocities[n][0],
#                           coordinates[n][1]+velocities[n][1]])

    adjacency = 0
    for n in range(len(coordinates)):
        for m in range(len(coordinates)):
            if (m != n):
                if ((abs((coordinates[n][0])-(coordinates[m][0])) <= 1) and
                    (abs((coordinates[n][1])-(coordinates[m][1])) <= 1)):
                   adjacency += 1

#    print('time: ', t, ' adjacency: ', adjacency)
    if (adjacency > max_adjacency):
        max_adjacency = adjacency
        max_time = t

#    initial_grid = new_grid
#    coordinates = new_coords

max_x = 0
max_y = 0
min_x = 100000
min_y = 100000
for n in range(len(velocities)):
    coordinates[n][0] = initial_coords[n][0]+(max_time*(velocities[n][0]))
    coordinates[n][1] = initial_coords[n][1]+(max_time*(velocities[n][1]))
    if (coordinates[n][0] > max_x):
       max_x = coordinates[n][0]
    if (coordinates[n][0] < min_x):
       min_x = coordinates[n][0]
    if (coordinates[n][1] > max_y):
       max_y = coordinates[n][1]
    if (coordinates[n][1] < min_y):
       min_y = coordinates[n][1]

print('min_x, max_x, min_y, max_y: ', min_x, max_x, min_y, max_y)

grid = []
for j in range(min_y-1, max_y+2):
    line = []
    for j in range(min_x-1, max_x+2):
        line.append(0)
    grid.append(line)

for n in range(len(coordinates)):
    grid[coordinates[n][1]-min_y+1][coordinates[n][0]-min_x+1] = 1

print('grid at time: ', max_time)
for j in range(len(grid)):
    this_line = ''
    for i in range(len(line)):
        this_line += str(grid[j][i])
 
    print(this_line)

print(' ')

# I then "solved" this by looking at the largest adjacent values in the output
# and looking at the print out for the largest, followed by stuff on each side
# My answer was KFLBHXGK for the mesage in part 1
# and then part 2 was how many seconds this took: luckily I printed this in the output too.
# The answer for part 2 was 10659

# It would be interesting in the future to work on a quicker method for this:
# one thought I had would be to do a proper adjacency measure over time for the
# coordinate set, then pick the max of this and look at the full "image" at this time.
# If that image was unclear, then search in a spiral around that (presuming the
# nearby adjacency measures are adequately high) until finding the correct answer.

