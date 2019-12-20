# Advent of code, day 20
import numpy as np

# open file
# input = open("advent20_input.txt", "r")
input = open("advent20_test_input.txt", "r")
# input = open("advent20_test_input2.txt", "r")

# make a dict for ascii characters
asciichars = dict()
for i in range(127):
    asciichars[chr(i)] = i

input_array = []
grid = []
# read string into array
maxlen = 0
for line in input:
    grid_line = []
    for n in range(len(line)-1):  # ignore the line return at the end
        grid_line.append(asciichars[line[n]])

    grid.append(grid_line)
    input_array.append(line[:-1])

    if len(line)-1 > maxlen:
        maxlen = len(line)-1

# initial thoughts: this is similar to a previous robot example, isn't it?

# ohhh... add spaces to grid where required...
# HACK for first test, add 2 to maxlen
maxlen += 2

for j in range(len(grid)):
    if len(grid[j]) < maxlen:
        for i in range(maxlen-len(grid[j])):
            grid[j].append(asciichars[" "])


print(input_array)
print(grid)

def is_uppercase(charindex):
    return (charindex > 64) and (charindex < 91)

# need to make a portal grid... ?
direction_dict = dict()
portal_grid = []
for j in range(len(grid)):
    portal_row = []
    for i in range(len(grid[j])):
        # if the grid has a capital letter on one side and a . opposite,
        # and spaces to the other two sides then record it at the point of the .
        if (j==0) or (j==(len(grid)-1)) or (i==0) or (i==(len(grid[j])-1)):
            portal_row.append('0')
        else:
            # test around the grid value if it's an uppercase letter (ascii 65-90)
            if (grid[j][i] > 64) and (grid[j][i] < 91):
                # 4 cases: 1) letter above, . below, space each side
                if (is_uppercase(grid[j-1][i])) and (
                    grid[j+1][i] == asciichars["."]) and (
                    grid[j][i-1] == asciichars[" "]) and (
                    grid[j][i+1] == asciichars[" "]):
                    portal_row.append(chr(grid[j-1][i])+chr(grid[j][i]))
                    direction_dict[(i,j)] = 2 # SOUTH
                # 2) letter below, . above, space each side
                elif (is_uppercase(grid[j+1][i])) and (
                    grid[j-1][i] == asciichars["."]) and (
                    grid[j][i-1] == asciichars[" "]) and (
                    grid[j][i+1] == asciichars[" "]):
                    portal_row.append(chr(grid[j][i])+chr(grid[j+1][i]))
                    direction_dict[(i,j)] = 1 # NORTH
                # 3) letter to the left, . to right, space above, below
                elif (is_uppercase(grid[j][i-1])) and (
                    grid[j][i+1] == asciichars["."]) and (
                    grid[j-1][i] == asciichars[" "]) and (
                    grid[j+1][i] == asciichars[" "]):
                    portal_row.append(chr(grid[j][i-1])+chr(grid[j][i]))
                    direction_dict[(i,j)] = 4 # EAST
                # 4) letter to the right, . to left, space above, below
                elif (is_uppercase(grid[j][i+1])) and (
                    grid[j][i-1] == asciichars["."]) and (
                    grid[j-1][i] == asciichars[" "]) and (
                    grid[j+1][i] == asciichars[" "]):
                    portal_row.append(chr(grid[j][i])+chr(grid[j][i+1]))
                    direction_dict[(i,j)] = 3 # WEST
                else:
                    portal_row.append('0')
            else:
                portal_row.append('0')

            dummy = False

    portal_grid.append(portal_row)

print(portal_grid)

# how do we make links from one portal to the other so that it can be traversed correctly?
portal_dict = dict()
for j in range(len(portal_grid)):
    for i in range(len(portal_grid[j])):
        if (portal_grid[j][i] != '0'):
            for y in range(len(portal_grid)):
                for x in range(len(portal_grid[y])):
                    if (i!=x) and (j!=y) and (portal_grid[j][i]==portal_grid[y][x]):
                        portal_dict[(i,j)] = (x,y)

print(portal_dict)
print(direction_dict)

# Feed in the grid (numbers corresponding to ascii) and it prints the ascii
def draw_grid(grid):
    print("\n")
    for j in range(len(grid)):
        str = ""
        for i in range(len(grid[j])):
            str += chr(grid[j][i])  # reads ascii value

        print(str)

    print("\n")

def get_start_position(grid, portal_grid):
    for j in range(len(portal_grid)):
        for i in range(len(portal_grid[j])):
            if portal_grid[j][i] == 'AA':
                if (grid[j-1][i] == asciichars["."]):
                    return i, j-1
                elif (grid[j+1][i] == asciichars["."]):
                    return i, j+1
                elif (grid[j][i-1] == asciichars["."]):
                    return i-1, j
                elif (grid[j][i+1] == asciichars["."]):
                    return i+1, j

# AA and ZZ behave like walls for the purposes of the robot
def is_AA(i, j):
    return (portal_grid[j][i] == 'AA')

def is_ZZ(i, j):
    return (portal_grid[j][i] == 'ZZ')

def is_portal(i, j):
    if (is_AA) or (is_ZZ):
        return False
    else:
        return True

def move_robot(grid, distance, robot_x, robot_y, input):

    # work out where the robot faces next
    if input == 1:  # NORTH
        grid_north = grid[robot_y-1][robot_x]
        # grid_north is a wall or a portal
        if ((grid_north == asciichars['#']) or is_uppercase(grid_north)):
            # go EAST
            output = 4
            if is_portal(robot_x, robot_y-1):
                (robot_x, robot_y) = portal_dict[(robot_x, robot_y-1)]
                # where do we go next?
                new_direction = direction_dict[(robot_x, robot_y)]
                print('new_direction: ', new_direction)
                if new_direction == 1: # NORTH
                    robot_y -= 1
                    output = 3 # WEST
                elif new_direction == 2: # SOUTH
                    robot_y += 1
                    output = 4 # EAST
                elif new_direction == 3: # WEST
                    robot_x -= 1
                    output = 2 # SOUTH
                elif new_direction == 4: # EAST
                    robot_x += 1
                    output = 1 # NORTH
        else: # grid_north is empty (.) or a key
            if (distance[robot_y-1][robot_x] == 0):
                distance[robot_y-1][robot_x] = distance[robot_y][robot_x]+1
            grid[robot_y][robot_x] = asciichars['.']
            robot_y -= 1
            # go WEST
            output = 3
    if input == 2:  # SOUTH
        grid_south = grid[robot_y+1][robot_x]
        # grid_south is a wall or a door
        if ((grid_south == asciichars['#']) or (is_uppercase(grid_south))):
            # go WEST
            output = 3
            if is_portal(robot_x, robot_y-1):
                (robot_x, robot_y) = portal_dict[(robot_x, robot_y-1)]
                # where do we go next?
                new_direction = direction_dict[(robot_x, robot_y)]
                print('new_direction: ', new_direction)
                if new_direction == 1: # NORTH
                    robot_y -= 1
                    output = 3 # WEST
                elif new_direction == 2: # SOUTH
                    robot_y += 1
                    output = 4 # EAST
                elif new_direction == 3: # WEST
                    robot_x -= 1
                    output = 2 # SOUTH
                elif new_direction == 4: # EAST
                    robot_x += 1
                    output = 1 # NORTH        else: # grid_south is empty (.) or a key
            if (distance[robot_y+1][robot_x] == 0):
                distance[robot_y+1][robot_x] = distance[robot_y][robot_x]+1
            robot_y += 1
            # go EAST
            output = 4
    if input == 3:  # WEST
        grid_west = grid[robot_y][robot_x-1]
        # grid_west is a wall or a door
        if ((grid_west == asciichars['#']) or (is_uppercase(grid_west))):
            # go NORTH
            output = 1
            if is_portal(robot_x, robot_y-1):
                (robot_x, robot_y) = portal_dict[(robot_x, robot_y-1)]
                # where do we go next?
                new_direction = direction_dict[(robot_x, robot_y)]
                print('new_direction: ', new_direction)
                if new_direction == 1: # NORTH
                    robot_y -= 1
                    output = 3 # WEST
                elif new_direction == 2: # SOUTH
                    robot_y += 1
                    output = 4 # EAST
                elif new_direction == 3: # WEST
                    robot_x -= 1
                    output = 2 # SOUTH
                elif new_direction == 4: # EAST
                    robot_x += 1
                    output = 1 # NORTH        else: # grid_west is empty (.) or a key
            if (distance[robot_y][robot_x-1] == 0):
                distance[robot_y][robot_x-1] = distance[robot_y][robot_x]+1
            robot_x -= 1
            # go SOUTH
            output = 2
    if input == 4:  # EAST
        grid_east = grid[robot_y][robot_x+1]
        # grid_east is a wall or a door
        if ((grid_east == asciichars['#']) or (is_uppercase(grid_east))):
            # go SOUTH
            output = 2
            if is_portal(robot_x, robot_y-1):
                (robot_x, robot_y) = portal_dict[(robot_x, robot_y-1)]
                # where do we go next?
                new_direction = direction_dict[(robot_x, robot_y)]
                print('new_direction: ', new_direction)
                if new_direction == 1: # NORTH
                    robot_y -= 1
                    output = 3 # WEST
                elif new_direction == 2: # SOUTH
                    robot_y += 1
                    output = 4 # EAST
                elif new_direction == 3: # WEST
                    robot_x -= 1
                    output = 2 # SOUTH
                elif new_direction == 4: # EAST
                    robot_x += 1
                    output = 1 # NORTH
        else: # grid_north is empty (.) or a key
            if (distance[robot_y][robot_x+1] == 0):
                distance[robot_y][robot_x+1] = distance[robot_y][robot_x]+1
            robot_x += 1
            # go SOUTH
            output = 1

    # robot might have moved
    grid[robot_y][robot_x] = asciichars['@']

    return grid, distance, robot_x, robot_y, output

def make_distance_map(grid, portal_grid, start_x, start_y):
    distance = np.zeros((len(grid[0]),len(grid)), dtype=np.int32)
    robot_x = start_x
    robot_y = start_y

    # searching grid finishes once start square has been visited 4 times
    start_visited = 0
    input = 1 # start by going north
    # distance grid starts at 1 at current location
    distance[start_y][start_x] = 1
    grid[start_y][start_x] = asciichars['@']

    while True:
        # move the robot
        grid, distance, robot_x, robot_y, output = move_robot(
            grid, distance, robot_x, robot_y, input)

        print("robot at ", robot_x, robot_y, input, output)
#        draw_grid(grid)
#        print(distance)
        if robot_x == start_x and robot_y == start_y:
            start_visited += 1
            print('start visited: ', start_visited)
            draw_grid(grid)
            print(distance)

        if start_visited == 4:
            break

        input = output

    # at this point look at the distance grid and find keys that are in it
    # we can probably decide at this point which key to choose
    found_keys = []
    distances = []
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            # is there a distance at this point?
            if (distance[j][i] != 0):
                # if there is then is there a key?
                if ((grid[j][i] > 96) and (grid[j][i] < 123)):
                    found_keys.append([i,j])
                    distances.append[distance[j][i]]

    print('found keys: ', found_keys)
    print('distances: ', distances)
    return found_keys[0], distances[0]

def part1(grid, portal_grid):

    draw_grid(grid)

    start_x, start_y = get_start_position(grid, portal_grid)
    print("start at: ", start_x, start_y)

    # make a distance map from current position and grid
    distance = make_distance_map(grid, portal_grid, start_x, start_y)

    return distance

def part2():

    answer = 0

    return answer

print("Part 1 answer: ", part1(grid, portal_grid))
print("Part 2 answer: ", part2())
