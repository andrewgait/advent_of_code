# Advent of code 2023, day 10

# open file
input = open("advent10_input.txt", "r")
# input = open("advent10_input_test.txt", "r")
# input = open("advent10_input_test2.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def find_connecting_pipes(nx, ny, x, y, start=False):
    connected_pipes = []
    possible_s_values = ["-", "|", "F", "7", "L", "J"]
    if start:
        if x-1 >= 0:
            if ((input_array[y][x-1] == "-") or
                (input_array[y][x-1] == "F") or
                (input_array[y][x-1] == "L")):
                connected_pipes.append((x-1, y))
                if "|" in possible_s_values: { possible_s_values.remove("|") }
                if "F" in possible_s_values: { possible_s_values.remove("F") }
                if "L" in possible_s_values: { possible_s_values.remove("L") }
        if x+1 < nx:
            if ((input_array[y][x+1] == "-") or
                (input_array[y][x+1] == "J") or
                (input_array[y][x+1] == "7")):
                connected_pipes.append((x+1, y))
                if "|" in possible_s_values: { possible_s_values.remove("|") }
                if "J" in possible_s_values: { possible_s_values.remove("J") }
                if "7" in possible_s_values: { possible_s_values.remove("7") }
        if y-1 >= 0:
            if ((input_array[y-1][x] == "|") or
                (input_array[y-1][x] == "7") or
                (input_array[y-1][x] == "F")):
                connected_pipes.append((x, y-1))
                if "-" in possible_s_values: { possible_s_values.remove("-") }
                if "F" in possible_s_values: { possible_s_values.remove("F") }
                if "7" in possible_s_values: { possible_s_values.remove("7") }
        if y+1 < ny:
            if ((input_array[y+1][x] == "|") or
                (input_array[y+1][x] == "L") or
                (input_array[y+1][x] == "J")):
                connected_pipes.append((x, y+1))
                if "-" in possible_s_values: { possible_s_values.remove("-") }
                if "J" in possible_s_values: { possible_s_values.remove("J") }
                if "L" in possible_s_values: { possible_s_values.remove("L") }
    else:
        if x-1 >= 0:
            if ((input_array[y][x] == "-") or
                (input_array[y][x] == "J") or
                (input_array[y][x] == "7")):
                if ((input_array[y][x-1] == "-") or
                    (input_array[y][x-1] == "F") or
                    (input_array[y][x-1] == "L")):
                    connected_pipes.append((x-1, y))
        if x+1 < nx:
            if ((input_array[y][x] == "-") or
                (input_array[y][x] == "F") or
                (input_array[y][x] == "L")):
                if ((input_array[y][x+1] == "-") or
                    (input_array[y][x+1] == "J") or
                    (input_array[y][x+1] == "7")):
                    connected_pipes.append((x+1, y))
        if y-1 >= 0:
            if ((input_array[y][x] == "|") or
                (input_array[y][x] == "J") or
                (input_array[y][x] == "L")):
                if ((input_array[y-1][x] == "|") or
                    (input_array[y-1][x] == "7") or
                    (input_array[y-1][x] == "F")):
                    connected_pipes.append((x, y-1))
        if y+1 < ny:
            if ((input_array[y][x] == "|") or
                (input_array[y][x] == "7") or
                (input_array[y][x] == "F")):
                if ((input_array[y+1][x] == "|") or
                    (input_array[y+1][x] == "L") or
                    (input_array[y+1][x] == "J")):
                    connected_pipes.append((x, y+1))

    return connected_pipes, possible_s_values

def part1():

    # Find S location
    y = 0
    x = 0
    ny = 0
    nx = len(input_array[0][:-1])  # don't include the \n
    for input in input_array:
        if "S" in input:
            y = ny
            for n in range(nx):
                if input[n] == "S":
                    x = n

        ny += 1

    print(x, y, nx, ny)

    # Start from S and find two paths to follow
    path1 = [(x,y)]
    path2 = [(x,y)]

    start = True
    connected_to_S, _ = find_connecting_pipes(nx, ny, x, y, start)

    path1.append(connected_to_S[0])
    path2.append(connected_to_S[1])

    print("from S path1 ", path1)
    print("from S path2 ", path2)

    end_reached = False
    while not end_reached:

        path1_connects = find_connecting_pipes(nx, ny, path1[-1][0], path1[-1][1])
        path2_connects = find_connecting_pipes(nx, ny, path2[-1][0], path2[-1][1])

        for path1_con in path1_connects:
            if path1_con not in path1:
                path1.append(path1_con)
        for path2_con in path2_connects:
            if path2_con not in path2:
                path2.append(path2_con)

        # print("path1 ", path1)
        # print("path2 ", path2)

        if path1[-1] == path2[-1]:
            end_reached = True


    print(path1)
    print(path2)
    answer = len(path1)-1

    return answer


def part2():

    # Same as part 1 as we need the path to work out anything inside it

    # Find S location
    y = 0
    x = 0
    ny = 0
    nx = len(input_array[0][:-1])  # don't include the \n
    for input in input_array:
        if "S" in input:
            y = ny
            for n in range(nx):
                if input[n] == "S":
                    x = n

        ny += 1

    print(x, y, nx, ny)

    # Start from S and find two paths to follow
    full_path = {}
    path1 = [(x,y)]
    path2 = [(x,y)]

    start = True
    connected_to_S, S_value = find_connecting_pipes(nx, ny, x, y, start)

    full_path[(x,y)] = S_value[0]

    print(full_path)

    path1.append(connected_to_S[0])
    path2.append(connected_to_S[1])

    full_path[(path1[-1][0], path1[-1][1])] = input_array[path1[-1][1]][path1[-1][0]]
    full_path[(path2[-1][0], path2[-1][1])] = input_array[path2[-1][1]][path2[-1][0]]

    print(full_path)

    print("from S path1 ", path1)
    print("from S path2 ", path2)

    end_reached = False
    while not end_reached:

        path1_connects, _ = find_connecting_pipes(nx, ny, path1[-1][0], path1[-1][1])
        path2_connects, _ = find_connecting_pipes(nx, ny, path2[-1][0], path2[-1][1])

        for path1_con in path1_connects:
            if path1_con not in path1:
                path1.append(path1_con)
        for path2_con in path2_connects:
            if path2_con not in path2:
                path2.append(path2_con)

        # print("path1 ", path1)
        # print("path2 ", path2)

        full_path[(path1[-1][0], path1[-1][1])] = input_array[path1[-1][1]][path1[-1][0]]
        full_path[(path2[-1][0], path2[-1][1])] = input_array[path2[-1][1]][path2[-1][0]]

        if path1[-1] == path2[-1]:
            end_reached = True

    # Make an array with just the enclosed loop in it (and dots everywhere else)
    closed_loop = [["." for j in range(ny)] for i in range(nx)]

    print(closed_loop)

    for key, value in full_path.items():
        closed_loop[key[1]][key[0]] = value

    for j in range(ny):
        print_row = ""
        for i in range(nx):
            print_row += closed_loop[j][i]
        print(print_row)
    print(" ")

    # Now loop over each row; if you cross a vertical pipe
    # (which in this case I think would be either | or J or L ?)
    count_in = 0
    for j in range(ny):
        inside = False
        for i in range(nx):
            if closed_loop[j][i] in ["|", "J", "L"]:
                inside = not inside
            elif closed_loop[j][i] == "." and inside:
                closed_loop[j][i] = "I"
                count_in += 1

    for j in range(ny):
        print_row = ""
        for i in range(nx):
            print_row += closed_loop[j][i]
        print(print_row)
    print(" ")

    answer = count_in

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
