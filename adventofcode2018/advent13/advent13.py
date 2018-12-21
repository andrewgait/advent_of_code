# Advent of code, day 13

# open file
input = open("advent13_input.txt", "r")
#input = open("advent13_test_input1.txt", "r")
#input = open("advent13_test_input2.txt", "r")
#input = open("advent13_test_input3.txt", "r")


def get_val(string):
    string_array = ["-", "|", "/", "\\", "+", " ", ">", "<", "v", "^", "X"]
    return string_array.index(string)


def get_string(val):
    string_array = ["-", "|", "/", "\\", "+", " ", ">", "<", "v", "^", "X"]
    return string_array[val]


def print_grid(current_grid):
    # loop
    for j in range(len(current_grid)):
        grid_string = ''
        for i in range(len(current_grid[j])):
            grid_string += get_string(current_grid[j][i])

        print(grid_string)

    # add a blank line at the end
    print(' ')


initial_grid = []
current_grid = []
cart_coords = []
intersections = []
corner_fwd = []
corner_back = []

max_line_length = 0
# read string into array
for line in input:
    data = []
    initial_data = []
    #
    if (len(line) > max_line_length):
        max_line_length = len(line)
    # is there a cart on this line?
    # remember the last character of each line except the last is a newline
    for i in range(len(line)):
        if ((line[i] == ">") or (line[i] == "<")):
            # mark coordinate
            cart_coords.append([i,len(current_grid),line[i],"l"])
            # replace the value with a -
            initial_data.append(get_val("-"))
        elif ((line[i] == "^") or (line[i] == "v")):
            # mark coordinate
            cart_coords.append([i,len(current_grid),line[i],"l"])
            # replace the value with a |
            initial_data.append(get_val("|"))
        elif (line[i] == "+"):
            # intersection
            intersections.append([i,len(current_grid)])
            initial_data.append(get_val("+"))
        elif (line[i] == "/"):
            # corner forward
            corner_fwd.append([i,len(current_grid)])
            initial_data.append(get_val("/"))
        elif (line[i] == "\\"):
            # corner forward
            corner_back.append([i,len(current_grid)])
            initial_data.append(get_val("\\"))
        else:
            if (line[i] != "\n"):
               initial_data.append(get_val(line[i]))

        if (line[i] != "\n"):
            data.append(get_val(line[i]))

    current_grid.append(data)
    initial_grid.append(initial_data)


print_grid(initial_grid)
print_grid(current_grid)
print(cart_coords)

print(current_grid)

time = 0
#collision = False
end = False
# while (not collision):  # part 1
while (not end):  # part 2
    time += 1
    collision = False
    if (len(cart_coords) <= 1):
        end = True
    # loop over carts
    collision_list = []
    for n in range(len(cart_coords)):
        # update the grid accordingly
        x = cart_coords[n][0]
        y = cart_coords[n][1]
        type = cart_coords[n][2]
        next_turn = cart_coords[n][3]

        old_type = type
        # I'm sure this can be simplified but it's not easy to see how
        if (type == ">"):
            # replace with -
            current_grid[y][x] = get_val("-")
            x += 1
            if (current_grid[y][x] == get_val("/")):
                # left turn, so new cart direction is ^
                type = "^"
            elif (current_grid[y][x] == get_val("\\")):
                # right turn, so new cart direction is v
                type = "v"
            elif (current_grid[y][x] == get_val("+")):
                # turn depending on the value of next_turn
                if (next_turn == "l"):
                    type = "^"
                    next_turn = "s"
                elif (next_turn == "r"):
                    type = "v"
                    next_turn = "l"
                else:
                    # next_turn goes from s to r, type doesn't change
                    next_turn = "r"
        elif (type == "<"):
            # replace with -
            current_grid[y][x] = get_val("-")
            x -= 1
            if (current_grid[y][x] == get_val("/")):
                # left turn, so new cart direction is v
                type = "v"
            elif (current_grid[y][x] == get_val("\\")):
                # right turn, so new cart direction is ^
                type = "^"
            elif (current_grid[y][x] == get_val("+")):
                # turn depending on the value of next_turn
                if (next_turn == "l"):
                    type = "v"
                    next_turn = "s"
                elif (next_turn == "r"):
                    type = "^"
                    next_turn = "l"
                else:
                    # next_turn goes from s to r, type doesn't change
                    next_turn = "r"
        elif (type == "^"):
            # replace with |
            current_grid[y][x] = get_val("|")
            y -= 1
            if (current_grid[y][x] == get_val("/")):
                # right turn, so new cart direction is >
                type = ">"
            elif (current_grid[y][x] == get_val("\\")):
                # left turn, so new cart direction is <
                type = "<"
            elif (current_grid[y][x] == get_val("+")):
                # turn depending on the value of next_turn
                if (next_turn == "l"):
                    type = "<"
                    next_turn = "s"
                elif (next_turn == "r"):
                    type = ">"
                    next_turn = "l"
                else:
                    # next_turn goes from s to r, type doesn't change
                    next_turn = "r"
        elif (type == "v"):
            # replace with |
            current_grid[y][x] = get_val("|")
            y += 1
            if (current_grid[y][x] == get_val("/")):
                # right turn, so new cart direction is <
                type = "<"
            elif (current_grid[y][x] == get_val("\\")):
                # left turn, so new cart direction is >
                type = ">"
            elif (current_grid[y][x] == get_val("+")):
                # turn depending on the value of next_turn
#                print('next_turn: ', next_turn)
                if (next_turn == "l"):
                    type = ">"
                    next_turn = "s"
                elif (next_turn == "r"):
                    type = "<"
                    next_turn = "l"
                else:
                    # next_turn goes from s to r, type doesn't change
                    next_turn = "r"

        # nothing else changes
        current_grid[y][x] = get_val(type)

        cart_coords[n][0] = x
        cart_coords[n][1] = y
        cart_coords[n][2] = type
        cart_coords[n][3] = next_turn

        # loop over other coordinates to check for collision
        for l in range(len(cart_coords)):
            if ((l < n) and (x == cart_coords[l][0]) and (y == cart_coords[l][1])):
                collision = True
                coll_x = x
                coll_y = y
                collision_list.append(l)
                collision_list.append(n)
                print('collision at ', coll_x, coll_y)
                print('types: ', cart_coords[n][2], cart_coords[l][2])

    # loop over intersections, then corners
    for m in range(len(intersections)):
        inter_x = intersections[m][0]
        inter_y = intersections[m][1]
        if ((current_grid[inter_y][inter_x] != get_val("<")) and
            (current_grid[inter_y][inter_x] != get_val(">")) and
            (current_grid[inter_y][inter_x] != get_val("^")) and
            (current_grid[inter_y][inter_x] != get_val("v"))):
            current_grid[inter_y][inter_x] = get_val("+")

    for m in range(len(corner_fwd)):
        cf_x = corner_fwd[m][0]
        cf_y = corner_fwd[m][1]
        if ((current_grid[cf_y][cf_x] != get_val("<")) and
            (current_grid[cf_y][cf_x] != get_val(">")) and
            (current_grid[cf_y][cf_x] != get_val("^")) and
            (current_grid[cf_y][cf_x] != get_val("v"))):
            current_grid[cf_y][cf_x] = get_val("/")

    for m in range(len(corner_back)):
        cb_x = corner_back[m][0]
        cb_y = corner_back[m][1]
        if ((current_grid[cb_y][cb_x] != get_val("<")) and
            (current_grid[cb_y][cb_x] != get_val(">")) and
            (current_grid[cb_y][cb_x] != get_val("^")) and
            (current_grid[cb_y][cb_x] != get_val("v"))):
            current_grid[cb_y][cb_x] = get_val("\\")

    if (collision):
        # remove the coordinates that collided
        #print(collision_list)
        collision_set = sorted(set(collision_list))
        #print(collision_set)
        print('time: ', time)
        for k in range(len(collision_set)):
            x = cart_coords[collision_set[k]-k][0]
            y = cart_coords[collision_set[k]-k][1]
            print(x,y)
            current_grid[y][x] = initial_grid[y][x]
            cart_coords.pop(collision_set[k]-k)
            # we need to replace the value here with
            # whatever it was previously
#        if (coll1 < coll2):
#            cart_coords.pop(coll1)
#            cart_coords.pop(coll2-1)
#        else:
#            cart_coords.pop(coll2)
#            cart_coords.pop(coll1)

#        current_grid[coll_y][coll_x] = get_val("X") # part 1

#    print('time: ', time)
#    print_grid(current_grid)
#    print(cart_coords)

    if (time > 10):
        no_collision = False
