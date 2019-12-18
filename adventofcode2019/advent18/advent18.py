# Advent of code, day 18
import numpy as np

# open file
# input = open("advent18_input.txt", "r")
input = open("advent18_test_input.txt", "r")
# input = open("advent18_test_input2.txt", "r")
# input = open("advent18_test_input3.txt", "r")
# input = open("advent18_test_input4.txt", "r")
# input = open("advent18_test_input5.txt", "r")

# make a dict for ascii characters
asciichars = dict()
for i in range(127):
    asciichars[chr(i)] = i

input_array = []
grid = []
# read string into array
for line in input:
    grid_line = []
    for n in range(len(line)-1):  # ignore the line return at the end
        grid_line.append(asciichars[line[n]])

    grid.append(grid_line)
    input_array.append(line[:-1])

# initial thoughts: this is similar to a previous robot example, isn't it?
print(input_array)
print(grid)

# Feed in the grid (numbers corresponding to ascii) and it prints the ascii
def draw_grid(grid):
    print("\n")
    for j in range(len(grid)):
        str = ""
        for i in range(len(grid[j])):
            str += chr(grid[j][i])  # reads ascii value

        print(str)

    print("\n")

def get_start_position(grid):
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if chr(grid[j][i]) == '@':
                return i, j

def find_keys_and_doors_in_grid(grid):
    # keys are lowercase letters, which are ascii characters 97-122
    # doors are uppercase letters, which are ascii characters 65-90
    keys_dict = dict()
    doors_dict = dict()
    n_keys = 0
    n_doors = 0
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if grid[j][i] > 96 and grid[j][i] < 123:
                keys_dict[grid[j][i]] = [i,j]
                n_keys += 1
            elif grid[j][i] > 64 and grid[j][i] < 91:
                doors_dict[grid[j][i]] = [i,j]
                n_doors += 1

    return n_keys, keys_dict, n_doors, doors_dict

def is_door(grid_val):
    if grid_val > 64 and grid_val < 91:
        return True
    else:
        return False

def move_robot(grid, distance, robot_x, robot_y, input):

    # work out where the robot faces next
    if input == 1:  # NORTH
        grid_north = grid[robot_y-1][robot_x]
        # grid_north is a wall or a door
        if ((grid_north == asciichars['#']) or (is_door(grid_north))):
            # go EAST
            output = 4
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
        if ((grid_south == asciichars['#']) or (is_door(grid_south))):
            # go WEST
            output = 3
        else: # grid_south is empty (.) or a key
            if (distance[robot_y+1][robot_x] == 0):
                distance[robot_y+1][robot_x] = distance[robot_y][robot_x]+1
            robot_y += 1
            # go EAST
            output = 4
    if input == 3:  # WEST
        grid_west = grid[robot_y][robot_x-1]
        # grid_west is a wall or a door
        if ((grid_west == asciichars['#']) or (is_door(grid_west))):
            # go SOUTH
            output = 2
        else: # grid_west is empty (.) or a key
            if (distance[robot_y][robot_x-1] == 0):
                distance[robot_y][robot_x-1] = distance[robot_y][robot_x]+1
            robot_x -= 1
            # go NORTH
            output = 1
    if input == 4:  # EAST
        grid_east = grid[robot_y][robot_x+1]
        # grid_east is a wall or a door
        if ((grid_east == asciichars['#']) or (is_door(grid_east))):
            # go NORTH
            output = 1
        else: # grid_north is empty (.) or a key
            if (distance[robot_y][robot_x+1] == 0):
                distance[robot_y][robot_x+1] = distance[robot_y][robot_x]+1
            robot_x += 1
            # go SOUTH
            output = 2

    # robot might have moved
    grid[robot_y][robot_x] = asciichars['@']

    return grid, distance, robot_x, robot_y

def make_distance_map_and_find_key(grid, start_x, start_y):
    distance = np.zeros((len(grid[0]),len(grid)), dtype=np.int32)
    robot_x = start_x
    robot_y = start_y

    # searching grid finishes once start square has been visited 4 times
    start_visited = 0
    input = 1 # start by going north
    # distance grid starts at 1 at current location
    distance[start_y][start_x] = 1

    while True:
        # edit the move robot function to deal with doors as well as walls
        grid, distance, robot_x, robot_y, output = move_robot(
            grid, distance, robot_x, robot_y, input)

#        draw_grid(grid)
#        print(distance)
        if robot_x == start_x and robot_y == start_y:
            start_visited += 1
            print('start visited: ', start_visited)

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

def remove_door_from_grid(grid, key, doors_dict):
    door = doors_dict[key-32]
    found_door = False
    print('Removing door ', door, chr(door))
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if grid[j][i] == door:
                grid[j][i] = asciichars['.']
                found_door = True
                break
        if found_door:
            break

    return grid

def part1(grid):

    draw_grid(grid)

    start_x, start_y = get_start_position(grid)
    print("start at: ", start_x, start_y)

    n_keys, keys_dict, n_doors, doors_dict  = find_keys_and_doors_in_grid(grid)

    print('keys ', n_keys, keys_dict)
    print('doors ', n_doors, doors_dict)

    # The clever thing here is to work out which key to go to... (obviously)
    # I think it's probably based on which door is nearest?
    keys_collected = []
    n_keys_left = n_keys

    distance_travelled = 0

    while n_keys_left > 0:
        # make a distance map from current position and grid
        next_key, key_distance = make_distance_map_and_find_key(
            grid, start_x, start_y)
        keys_collected.append(next_key)
        n_keys_left -= 1
        distance_travelled += key_distance

        # remove the door that this key corresponded to from the grid
        grid = remove_door_from_grid(grid, next_key)

        draw_grid(grid)


    return distance_travelled

def part2():

    answer = 0

    return answer

print("Part 1 answer: ", part1(grid))
print("Part 2 answer: ", part2())
