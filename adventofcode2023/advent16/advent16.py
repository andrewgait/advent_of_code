# Advent of code 2023, day 16

# open file
input = open("advent16_input.txt", "r")
# input = open("advent16_input_test.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

type_dict = {".": 0, "/": 1, "\\": 2, "|": 3, "-": 4, "#": 5}
type_rev_dict = {0: ".", 1: "/", 2: "\\", 3: "|", 4: "-", 5: "#"}

print(type_dict)

start = [0,0]

def part1(start):

    answer = 0
    input_nums = []

    for input in input_array:
        input_line = []
        for n in range(len(input[:-1])):
            input_line.append(type_dict[input[n]])

        input_nums.append(input_line)

    # print(input_nums)

    paths = set()
    paths.add((start[0],start[1]))

    move = []
    nx = len(input_nums[0])
    ny = len(input_nums)

    if start[1] == 0:
        if (type_rev_dict[input_nums[start[1]][start[0]]] == ".") or (
            type_rev_dict[input_nums[start[1]][start[0]]] == "|"):
            move = [[start, "down"]]
        else:
            if (type_rev_dict[input_nums[start[1]][start[0]]] == "-"):
                move = [[start, "right"], [start, "left"]]
            elif (type_rev_dict[input_nums[start[1]][start[0]]] == "\\"):
                move = [[start, "right"]]
            elif (type_rev_dict[input_nums[start[1]][start[0]]] == "/"):
                move = [[start, "left"]]
    elif start[1] == ny - 1:
        if (type_rev_dict[input_nums[start[1]][start[0]]] == ".") or (
            type_rev_dict[input_nums[start[1]][start[0]]] == "|"):
            move = [[start, "up"]]
        else:
            if (type_rev_dict[input_nums[start[1]][start[0]]] == "-"):
                move = [[start, "right"], [start, "left"]]
            elif (type_rev_dict[input_nums[start[1]][start[0]]] == "\\"):
                move = [[start, "left"]]
            elif (type_rev_dict[input_nums[start[1]][start[0]]] == "/"):
                move = [[start, "right"]]

    if start[0] == 0:
        if (type_rev_dict[input_nums[start[1]][start[0]]] == ".") or (
            type_rev_dict[input_nums[start[1]][start[0]]] == "-"):
            move = [[start, "right"]]
        else:
            if (type_rev_dict[input_nums[start[1]][start[0]]] == "|"):
                move = [[start, "down"], [start, "up"]]
            elif (type_rev_dict[input_nums[start[1]][start[0]]] == "\\"):
                move = [[start, "down"]]
            elif (type_rev_dict[input_nums[start[1]][start[0]]] == "/"):
                move = [[start, "up"]]
    elif start[0] == nx - 1:
        if (type_rev_dict[input_nums[start[1]][start[0]]] == ".") or (
            type_rev_dict[input_nums[start[1]][start[0]]] == "-"):
            move = [[start, "left"]]
        else:
            if (type_rev_dict[input_nums[start[1]][start[0]]] == "|"):
                move = [[start, "down"], [start, "up"]]
            elif (type_rev_dict[input_nums[start[1]][start[0]]] == "\\"):
                move = [[start, "up"]]
            elif (type_rev_dict[input_nums[start[1]][start[0]]] == "/"):
                move = [[start, "down"]]


    # print(move)

    old_len = 0
    new_len = len(paths)

    n = 0
    while n < 800:  # new_len != old_len:
        old_len = new_len
        new_move = []
        for move_item in move:
            current = move_item[0]
            dirn = move_item[1]
            # print(current, dirn)
            if dirn == "right":
                if current[0] + 1 < nx:
                    new_x = current[0] + 1
                    new_y = current[1]
                    paths.add((new_x, new_y))
                    if type_rev_dict[input_nums[new_y][new_x]] == ".":
                        new_move.append([[new_x, new_y], "right"])
                    elif type_rev_dict[input_nums[new_y][new_x]] == "/":
                        new_move.append([[new_x, new_y], "up"])
                    elif type_rev_dict[input_nums[new_y][new_x]] == "\\":
                        new_move.append([[new_x, new_y], "down"])
                    elif type_rev_dict[input_nums[new_y][new_x]] == "|":
                        new_move.append([[new_x, new_y], "up"])
                        new_move.append([[new_x, new_y], "down"])
                    elif type_rev_dict[input_nums[new_y][new_x]] == "-":
                        new_move.append([[new_x, new_y], "right"])
            if dirn == "left":
                if current[0] - 1 >= 0:
                    new_x = current[0] - 1
                    new_y = current[1]
                    paths.add((new_x, new_y))
                    if type_rev_dict[input_nums[new_y][new_x]] == ".":
                        new_move.append([[new_x, new_y], "left"])
                    elif type_rev_dict[input_nums[new_y][new_x]] == "/":
                        new_move.append([[new_x, new_y], "down"])
                    elif type_rev_dict[input_nums[new_y][new_x]] == "\\":
                        new_move.append([[new_x, new_y], "up"])
                    elif type_rev_dict[input_nums[new_y][new_x]] == "|":
                        new_move.append([[new_x, new_y], "up"])
                        new_move.append([[new_x, new_y], "down"])
                    elif type_rev_dict[input_nums[new_y][new_x]] == "-":
                        new_move.append([[new_x, new_y], "left"])
            if dirn == "up":
                if current[1] - 1 >= 0:
                    new_x = current[0]
                    new_y = current[1] - 1
                    paths.add((new_x, new_y))
                    if type_rev_dict[input_nums[new_y][new_x]] == ".":
                        new_move.append([[new_x, new_y], "up"])
                    elif type_rev_dict[input_nums[new_y][new_x]] == "/":
                        new_move.append([[new_x, new_y], "right"])
                    elif type_rev_dict[input_nums[new_y][new_x]] == "\\":
                        new_move.append([[new_x, new_y], "left"])
                    elif type_rev_dict[input_nums[new_y][new_x]] == "|":
                        new_move.append([[new_x, new_y], "up"])
                    elif type_rev_dict[input_nums[new_y][new_x]] == "-":
                        new_move.append([[new_x, new_y], "left"])
                        new_move.append([[new_x, new_y], "right"])
            if dirn == "down":
                if current[1] + 1 < ny:
                    new_x = current[0]
                    new_y = current[1] + 1
                    paths.add((new_x, new_y))
                    if type_rev_dict[input_nums[new_y][new_x]] == ".":
                        new_move.append([[new_x, new_y], "down"])
                    elif type_rev_dict[input_nums[new_y][new_x]] == "/":
                        new_move.append([[new_x, new_y], "left"])
                    elif type_rev_dict[input_nums[new_y][new_x]] == "\\":
                        new_move.append([[new_x, new_y], "right"])
                    elif type_rev_dict[input_nums[new_y][new_x]] == "|":
                        new_move.append([[new_x, new_y], "down"])
                    elif type_rev_dict[input_nums[new_y][new_x]] == "-":
                        new_move.append([[new_x, new_y], "left"])
                        new_move.append([[new_x, new_y], "right"])

        # print(paths)
        move = new_move
        new_len = len(paths)
        n += 1


    answer = len(paths)

    # for y in range(ny):
    #     print_line = ""
    #     for x in range(nx):
    #         if (x,y) in paths:
    #             print_line += "#"
    #         else:
    #             print_line += "."
    #     print(print_line)
    # print(" ")



    return answer

def part2():


    answer = 0

    ny = len(input_array)
    nx = len(input_array[0][:-1])

    location = [0,0]
    for y in range(ny):
        for x in range(nx):
            if x == 0 or y == 0 or x == nx-1 or y == ny-1:
                get_val = part1([x, y])
                print(x, y)
                if get_val > answer:
                    answer = get_val
                    location = [x,y]
                    print(answer, " at ", location)

    print(location)
    return answer

print("Part 1 answer: ", part1(start))
# Running it short for every case and picking the largest of these, then running that to the limit
print('[0,72] answer: ', part1([0,72]))
print("Part 2 answer: ", part2())

