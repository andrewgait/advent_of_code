# Advent of code, day 6

# open file
input = open("advent6_input.txt", "r")

# input = [[1, 1],[1, 6],[8, 3],[3, 4],[5, 5],[8, 9]]

# build a big enough 2d array, from data 500x500 should be fine
size = 500  # 10
coord_grid = []
for i in range(size):
    coord_line = []
    for j in range(size):
        coord_line.append(0)

    coord_grid.append(coord_line)

# read string into array
input_data = []
label = 1
for line in input:
    dataxy = line.rsplit(', ', 1)
    # dataxy = line
    x = int(dataxy[0])
    y = int(dataxy[1])
    input_data.append([x,y,label])
    label += 1

# print(coord_grid)

# loop over the coordinate grid and work out the distances for each one
limit = 10000 # 32
part2_region_size = 0
for i in range(size):
    for j in range(size):
        # find the closest value to this coordinate
        min_dist = size*2
        location = 0
        distances = []
        sum_distances = 0
        for k in range(len(input_data)):
            this_dist = abs(input_data[k][0]-i)+abs(input_data[k][1]-j)
            sum_distances += this_dist
            distances.append(this_dist)
            if (this_dist < min_dist):
                min_dist = this_dist
                location = input_data[k][2]

        if (sum_distances < limit):
            part2_region_size += 1

        # Does the minimum value occur more than once in the distances array
        num_mins = distances.count(min_dist)

        if (num_mins == 1):
            coord_grid[i][j] = location
        else:
            coord_grid[i][j] = 999

print('part 2, region(', limit, ') = ', part2_region_size)

# print(coord_grid)

# make a list of labels that hit the edge of the grid
labels_at_edge = set()
for i in range(size):
    labels_at_edge.add(coord_grid[i][0])
    labels_at_edge.add(coord_grid[i][size-1])
    labels_at_edge.add(coord_grid[0][i])
    labels_at_edge.add(coord_grid[size-1][i])

print(labels_at_edge)
print(label)

maxsize = 0
maxloc = 0

for l in range(label):
    if (l in labels_at_edge):
        print('label ', l, ' is at the edge')
    else:
        # loop and count the instances
        labelsize = 0
        for i in range(size):
            for j in range(size):
                if (coord_grid[i][j] == l):
                    labelsize += 1

        print('label ', l, ' is interior and has size ', labelsize)
        if (labelsize > maxsize):
            maxsize = labelsize
            maxloc = l

print('label ', maxloc, ' is max size: ', maxsize)

## Failed attempt at doing this distance by distance below

# this_coord_grid = []
# for i in range(size):
#     this_coord_line = []
#     for j in range(size):
#         this_coord_line.append(coord_grid[i][j])
#
#     this_coord_grid.append(this_coord_line)
#
# print(this_coord_grid)
#
# def coord_test(coord_grid, i, j, k, done_this_step):
#     if (coord_grid[i][j] == 0):
#         return k
#     elif ((coord_grid[i][j] != k) and (done_this_step[i][j] == 1)):
#         return 999
#     else:
#         return coord_grid[i][j]
#
# grid_unfinished = True
# while grid_unfinished:
#     done_this_step = []
#     for i in range(size):
#         done_line = []
#         for j in range(size):
#             done_line.append(0)
#         done_this_step.append(done_line)
#
#     for i in range(size):
#         for j in range(size):
#             if ((coord_grid[i][j] != 0) and (coord_grid[i][j] != 999)):
#                 # add the coordinates up, down, left, right
#                 if (i != (size-1)):
#                     this_coord_grid[i+1][j] = coord_test(
#                         coord_grid, i+1, j, coord_grid[i][j], done_this_step)
#                     if (this_coord_grid[i+1][j] == coord_grid[i][j]):
#                         done_this_step[i+1][j] = 1
#                 if (i != 0):
#                     this_coord_grid[i-1][j] = coord_test(
#                         coord_grid, i-1, j, coord_grid[i][j], done_this_step)
#                     if (this_coord_grid[i-1][j] == coord_grid[i][j]):
#                         done_this_step[i-1][j] = 1
#                 if (j != (size-1)):
#                     this_coord_grid[i][j+1] = coord_test(
#                         coord_grid, i, j+1, coord_grid[i][j], done_this_step)
#                     if (this_coord_grid[i][j+1] == coord_grid[i][j]):
#                         done_this_step[i][j+1] = 1
#                 if (j != 0):
#                     this_coord_grid[i][j-1] = coord_test(
#                         coord_grid, i, j-1, coord_grid[i][j], done_this_step)
#                     if (this_coord_grid[i][j-1] == coord_grid[i][j]):
#                         done_this_step[i][j-1] = 1
#
#     print(this_coord_grid)
#
#     found_zero = False
#     for i in range(size):
#         for j in range(size):
#             if (this_coord_grid[i][j] == 0):
#                 found_zero = True
#                 break
#
#     if found_zero:
#         print('carrying on')
#         coord_grid = []
#         for i in range(size):
#             coord_line = []
#             for j in range(size):
#                 coord_line.append(this_coord_grid[i][j])
#
#             coord_grid.append(coord_line)
#
#     else:
#         print('we are done?')
#         grid_unfinished = False
#
# print(this_coord_grid)