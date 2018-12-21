# Advent of code, day 15

# really tried with this, struggling to work out where it's gone wrong
# what's here at the moment works for all the test input

# open file
input = open("advent15_input.txt", "r")
#input = open("advent15_test_input_target.txt", "r")
#input = open("advent15_test_input_movement.txt", "r")
#input = open("advent15_test_input_combat1.txt", "r")
#input = open("advent15_test_input_combat2.txt", "r")
#input = open("advent15_test_input_combat3.txt", "r")
#input = open("advent15_test_input_combat4.txt", "r")
#input = open("advent15_test_input_combat5.txt", "r")
#input = open("advent15_test_input_combat6.txt", "r")

game_status = []
units = []
hp = 200
elf_attack = 20
num_elves = 0

order = 1
# read string into array
for line in input:
    game_line = []
    for i in range(len(line)):
        if (line[i] != "\n"):
            game_line.append(line[i])
        if (line[i] == "E"):
            units.append(["E",i,len(game_status),order,hp])
            order += 1
        if (line[i] == "G"):
            units.append(["G",i,len(game_status),order,hp])
            order += 1

    game_status.append(game_line)


# define a function to print the grid
def print_grid(grid):
    for j in range(len(grid)):
        line_string = ''
        for i in range(len(grid[j])):
            line_string += str(grid[j][i])

        print(line_string)

    print(' ')


# define a function to get goblins and elves from units
def get_goblins_and_elves(units):
    goblins = []
    elves = []
    for i in range(len(units)):
        if (units[i][0] == "E"):
            elves.append(units[i])
        elif (units[i][0] == "G"):
            goblins.append(units[i])

    return goblins, elves


# define a function to get a distance grid from a coordinate
def get_distance_grid(grid, x, y):
    distance_grid = []
    for j in range(len(grid)):
        distance_line = []
        for i in range(len(grid[j])):
            distance_line.append(grid[j][i])

        distance_grid.append(distance_line)

#    print_grid(distance_grid)
    # start from x,y
    distance_grid[y][x] = 0
    filled = False
    coords_to_do = [[x,y]]
#    print('coords_to_do: ', coords_to_do)
    dist = 1
    while (not filled):
        new_coords = []
        for n in range(len(coords_to_do)):
            xd = coords_to_do[n][0]
            yd = coords_to_do[n][1]
#            print(xd, yd)
            if (distance_grid[yd-1][xd] == "."):
                distance_grid[yd-1][xd] = dist
                new_coords.append([xd,yd-1])
            if (distance_grid[yd][xd-1] == "."):
                distance_grid[yd][xd-1] = dist
                new_coords.append([xd-1,yd])
            if (distance_grid[yd][xd+1] == "."):
                distance_grid[yd][xd+1] = dist
                new_coords.append([xd+1,yd])
            if (distance_grid[yd+1][xd] == "."):
                distance_grid[yd+1][xd] = dist
                new_coords.append([xd,yd+1])

        if (len(new_coords) == 0):
            filled = True
        else:
            dist += 1
            coords_to_do = []
            for m in range(len(new_coords)):
                coords_to_do.append(new_coords[m])
#            print('coords_to_do: ', coords_to_do)

#    print_grid(distance_grid)
    return distance_grid


# define function to move unit
def move_unit(unit, grid, enemies):
    xu = unit[1]
    yu = unit[2]
#    print(xu, yu)

    potential_target_squares = []
    # loop over enemies, print . location
    for n in range(len(enemies)):
        xe = enemies[n][1]
        ye = enemies[n][2]
        # visit possible squares in "reading order"
        if (grid[ye-1][xe] == "."):
            potential_target_squares.append([xe,ye-1])
        if (grid[ye][xe-1] == "."):
            potential_target_squares.append([xe-1,ye])
        if (grid[ye][xe+1] == "."):
            potential_target_squares.append([xe+1,ye])
        if (grid[ye+1][xe] == "."):
            potential_target_squares.append([xe,ye+1])

#    print('unit: ', unit, ' target_squares: ', potential_target_squares)
    # which of these squares are reachable at present?
    # and which of the reachable squares is closest (tie: reading order)
    reachable_squares = []
    distance = 1000
    direction = None
    for m in range(len(potential_target_squares)):
        # make a distance grid for this target square
        xt = potential_target_squares[m][0]
        yt = potential_target_squares[m][1]
        # print('target square: ', xt, yt)
        distance_grid = get_distance_grid(grid, xt, yt)
        # print_grid(distance_grid)

        # now this has been done, are any of the squares next to the unit
        # filled with a number
        if (isinstance(distance_grid[yu-1][xu], int)):
            if (distance_grid[yu-1][xu] < distance):
                distance = distance_grid[yu-1][xu]
                direction = "U"
        if (isinstance(distance_grid[yu][xu-1], int)):
            if (distance_grid[yu][xu-1] < distance):
                distance = distance_grid[yu][xu-1]
                direction = "L"
        if (isinstance(distance_grid[yu][xu+1], int)):
            if (distance_grid[yu][xu+1] < distance):
                distance = distance_grid[yu][xu+1]
                direction = "R"
        if (isinstance(distance_grid[yu+1][xu], int)):
            if (distance_grid[yu+1][xu] < distance):
                distance = distance_grid[yu+1][xu]
                direction = "D"

    return direction


# define function for combat
def combat(unit, units):
    min_hp = 201
    min_unit_loc = 0
    xu = unit[1]
    yu = unit[2]
    # loop over enemies (who should be in reading order)
    for n in range(len(units)):
        if (unit[0] == "E"):
            if (units[n][0] == "G"):
                if ((units[n][1] == xu) and (units[n][2] == yu-1)):
                    if (units[n][4] < min_hp):
                        min_hp = units[n][4]
                        min_unit_loc = n
                elif ((units[n][1] == xu-1) and (units[n][2] == yu)):
                    if (units[n][4] < min_hp):
                        min_hp = units[n][4]
                        min_unit_loc = n
                elif ((units[n][1] == xu+1) and (units[n][2] == yu)):
                    if (units[n][4] < min_hp):
                        min_hp = units[n][4]
                        min_unit_loc = n
                elif ((units[n][1] == xu) and (units[n][2] == yu+1)):
                    if (units[n][4] < min_hp):
                        min_hp = units[n][4]
                        min_unit_loc = n
        elif (unit[0] == "G"):
            if (units[n][0] == "E"):
                if ((units[n][1] == xu) and (units[n][2] == yu-1)):
                    if (units[n][4] < min_hp):
                        min_hp = units[n][4]
                        min_unit_loc = n
                elif ((units[n][1] == xu-1) and (units[n][2] == yu)):
                    if (units[n][4] < min_hp):
                        min_hp = units[n][4]
                        min_unit_loc = n
                elif ((units[n][1] == xu+1) and (units[n][2] == yu)):
                    if (units[n][4] < min_hp):
                        min_hp = units[n][4]
                        min_unit_loc = n
                elif ((units[n][1] == xu) and (units[n][2] == yu+1)):
                    if (units[n][4] < min_hp):
                        min_hp = units[n][4]
                        min_unit_loc = n

    # print
    print('unit ', unit, ' fights against unit ', min_unit_loc)
    if (unit[0] == "E"):
        units[min_unit_loc][4] -= elf_attack
    else:
        units[min_unit_loc][4] -= 3

    if (units[min_unit_loc][4] <= 0):
        return min_unit_loc
    else:
        return None


print_grid(game_status)
print('units: ', units)

combat_round = 1
n_elves = 0
combat_continues = True
while (combat_continues):
    goblins, elves = get_goblins_and_elves(units)
    num_elves = len(elves)
    if (combat_round == 1):
        n_elves = num_elves
    print('combat_round: ', combat_round)
#    print('elves: ', elves)
#    print('goblins: ', goblins)
    print('units: ', units)

    # loop over units
    one_moved = False
    for n in range(len(units)):
        if (n < len(units)):
            dead_array = []
            # move the unit if none of the surrounding (up, left, down, right)
            # squares have an oppposing unit in them
            xu = units[n][1]
            yu = units[n][2]
            if (units[n][0] == "E"):
#                print('unit ', units[n], ' moves ', move_unit(units[n], game_status, goblins))
                if ((game_status[yu-1][xu] != "G") and
                    (game_status[yu][xu-1] != "G") and
                    (game_status[yu][xu+1] != "G") and
                    (game_status[yu+1][xu] != "G")):
                    direction = move_unit(units[n], game_status, goblins)
                else:
                    # otherwise combat :-/
                    direction = None
                    dead_units = combat(units[n], units)
                    if (dead_units is not None):
                        dead_array.append(dead_units)
                print('unit ', units[n], ' moves ', direction)
            elif (units[n][0] == "G"):
#                print('unit ', units[n], ' moves ', move_unit(units[n], game_status, elves))
                if ((game_status[yu-1][xu] != "E") and
                    (game_status[yu][xu-1] != "E") and
                    (game_status[yu][xu+1] != "E") and
                    (game_status[yu+1][xu] != "E")):
                    direction = move_unit(units[n], game_status, elves)
                else:
                    # otherwise combat :-/
                    direction = None
                    dead_units = combat(units[n], units)
                    if (dead_units is not None):
                        dead_array.append(dead_units)
                print('unit ', units[n], ' moves ', direction)

            # update the grid now rather than at the end of all units
            if (direction is not None):
                one_moved = True
                xu = units[n][1]
                yu = units[n][2]
                new_xu = 0
                new_yu = 0
                if (direction == "U"):
                    game_status[yu][xu] = "."
                    units[n][2] -= 1
                    new_yu = yu-1
                    new_xu = xu
                elif (direction == "L"):
                    game_status[yu][xu] = "."
                    units[n][1] -= 1
                    new_yu = yu
                    new_xu = xu-1
                elif (direction == "R"):
                    game_status[yu][xu] = "."
                    units[n][1] += 1
                    new_yu = yu
                    new_xu = xu+1
                elif (direction == "D"):
                    game_status[yu][xu] = "."
                    units[n][2] += 1
                    new_yu = yu+1
                    new_xu = xu

                game_status[new_yu][new_xu] = units[n][0]

                goblins, elves = get_goblins_and_elves(units)
                # now initiate combat if necessary
                if (units[n][0] == 'E'):
                    if ((game_status[new_yu-1][new_xu] == "G") or
                        (game_status[new_yu][new_xu-1] == "G") or
                        (game_status[new_yu][new_xu+1] == "G") or
                        (game_status[new_yu+1][new_xu] == "G")):
                        dead_units = combat(units[n], units)
                        if (dead_units is not None):
                            dead_array.append(dead_units)
                elif (units[n][0] == 'G'):
                    if ((game_status[new_yu-1][new_xu] == "E") or
                        (game_status[new_yu][new_xu-1] == "E") or
                        (game_status[new_yu][new_xu+1] == "E") or
                        (game_status[new_yu+1][new_xu] == "E")):
                        dead_units = combat(units[n], units)
                        if (dead_units is not None):
                            dead_array.append(dead_units)

            if (len(dead_array) > 0):
                print('length of dead array: ', len(dead_array))
                xdead = units[dead_array[0]][1]
                ydead = units[dead_array[0]][2]
                print('xdead, ydead: ', xdead, ydead)
                game_status[ydead][xdead] = "."
                units.pop(dead_array[0])
                goblins, elves = get_goblins_and_elves(units)
                if (dead_array[0] < n):
                    n -= 1
                # I think I need to adjust the loop counter now... ?
                # this doesn't work, put a test at the start of the loop

    print_grid(game_status)
    # units may have changed reading order!
    units = sorted(units, key = lambda x: (x[2], x[1]))

    if ((len(elves) == 0) or (len(goblins) ==  0)):
        combat_continues = False

    combat_round += 1


print('n_elves start: ', n_elves, ' current_elves: ', num_elves, ' elf_attack: ', elf_attack)
if (len(elves) == 0):
    print("The goblins won")
    remaining_hp = 0
    for n in range(len(units)):
        if (units[n][0] == 'G'):
            remaining_hp += units[n][4]

    print("With remaining hp: ", remaining_hp)
    print("outcome: ", (combat_round-2)*remaining_hp)
elif (len(goblins) == 0):
    print("The elves won")
    remaining_hp = 0
    for n in range(len(units)):
        if (units[n][0] == 'E'):
            remaining_hp += units[n][4]

    print("With remaining hp: ", remaining_hp)
    print("outcome: ", (combat_round-2)*remaining_hp)
