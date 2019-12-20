# Advent of code, day 20
import numpy as np

# open file
input = open("advent20_input.txt", "r")
# input = open("advent20_test_input.txt", "r")
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
# HACK for first test, add 2 to maxlen maxlen += 2

for j in range(len(grid)):
    if len(grid[j]) < maxlen:
        for i in range(maxlen-len(grid[j])):
            grid[j].append(asciichars[" "])

    print(len(grid[j]), j)


# print(input_array)
# print(grid)

print('maxlen is ', maxlen)

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

# print(portal_grid)

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
print('maxlen ', maxlen, len(grid), len(grid[0]))

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
    if not is_uppercase(grid[j][i]):
        return False
    elif (is_AA(i,j) or is_ZZ(i,j)):
        print(" not portal at ", i, j, portal_grid[j][i], is_AA(i,j), is_ZZ(i,j), grid[j][i])
        return False
    else:
        print(" portal at ", i, j, portal_grid[j][i], is_AA(i,j), is_ZZ(i,j), grid[j][i])
        return True

def make_distance_map(grid, portal_grid, start_x, start_y):
    distance = np.zeros((len(grid),len(grid[0])), dtype=np.int32)
    robot_x = start_x
    robot_y = start_y

    current_step = [(start_x, start_y)]

    # searching grid finishes once start square has been visited 4 times
    start_visited = 0
    input = 1 # start by going north
    # distance grid starts at 1 at current location 
    distance[start_y][start_x] = 0
    # grid[start_y][start_x] = asciichars['@']

    count = 0
    found_ZZ = False
    while True:
        # move the robot
        # grid, distance, robot_x, robot_y, output = move_robot(
        #     grid, distance, robot_x, robot_y, input)
        count += 1

        next_step = []
        print(len(current_step), len(next_step))
        for n in range(len(current_step)):
            x = current_step[n][0]
            y = current_step[n][1]
            if ((grid[y-1][x] == asciichars["."]) and (distance[y-1][x] == 0)):
                next_step.append((x,y-1))
                distance[y-1][x] = count
            elif is_portal(x,y-1):
                (new_x, new_y) = portal_dict[(x,y-1)]
                new_dir = direction_dict[(new_x, new_y)]
                if new_dir == 1:
                    new_y -= 1
                elif new_dir == 2:
                    new_y += 1
                elif new_dir == 3:
                    new_x -= 1
                elif new_dir == 4:
                    new_x += 1
                if distance[new_y][new_x] == 0:
                    next_step.append((new_x, new_y))
                    distance[new_y][new_x] = count
            elif is_ZZ(x,y-1):
                found_ZZ = True
            if ((grid[y+1][x] == asciichars["."]) and (distance[y+1][x] == 0)):
                next_step.append((x,y+1))
                distance[y+1][x] = count
            elif is_portal(x,y+1):
                (new_x, new_y) = portal_dict[(x,y+1)]
                new_dir = direction_dict[(new_x, new_y)]
                if new_dir == 1:
                    new_y -= 1
                elif new_dir == 2:
                    new_y += 1
                elif new_dir == 3:
                    new_x -= 1
                elif new_dir == 4:
                    new_x += 1
                if distance[new_y][new_x] == 0:
                    next_step.append((new_x, new_y))
                    distance[new_y][new_x] = count
            elif is_ZZ(x,y+1):
                found_ZZ = True
            if ((grid[y][x-1] == asciichars["."]) and (distance[y][x-1] == 0)):
                next_step.append((x-1,y))
                distance[y][x-1] = count
            elif is_portal(x-1,y):
                (new_x, new_y) = portal_dict[(x-1,y)]
                new_dir = direction_dict[(new_x, new_y)]
                if new_dir == 1:
                    new_y -= 1
                elif new_dir == 2:
                    new_y += 1
                elif new_dir == 3:
                    new_x -= 1
                elif new_dir == 4:
                    new_x += 1
                if distance[new_y][new_x] == 0:
                    next_step.append((new_x, new_y))
                    distance[new_y][new_x] = count
            elif is_ZZ(x-1,y):
                found_ZZ = True
            if ((grid[y][x+1] == asciichars["."]) and (distance[y][x+1] == 0)):
                next_step.append((x+1,y))
                distance[y][x+1] = count
            elif is_portal(x+1,y):
                (new_x, new_y) = portal_dict[(x+1,y)]
                new_dir = direction_dict[(new_x, new_y)]
                if new_dir == 1:
                    new_y -= 1
                elif new_dir == 2:
                    new_y += 1
                elif new_dir == 3:
                    new_x -= 1
                elif new_dir == 4:
                    new_x += 1
                if distance[new_y][new_x] == 0:
                    next_step.append((new_x, new_y))
                    distance[new_y][new_x] = count
            elif is_ZZ(x+1,y):
                found_ZZ = True

#        draw_grid(grid)
#        print(distance)
#        if robot_x == start_x and robot_y == start_y:
#            start_visited += 1
#        print('start visited: ', start_visited)
#        draw_grid(grid)
#        print(distance.tolist())

        if found_ZZ:
            break

        current_step = []
        if len(next_step) > 2:
            print(len(current_step), len(next_step), next_step[0:3])
        else:
            print(len(current_step), len(next_step), next_step)
        for n in range(len(next_step)):
            current_step.append(next_step[n])

    draw_grid(grid)

    print(distance)

    return count-1


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
