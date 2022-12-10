# Advent of code 2022, day 9

# open file
input = open("advent9_input.txt", "r")
# input = open("advent9_test_input1.txt", "r")
# input = open("advent9_test_input2.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def manhattanX(H,T):
    return H[0]-T[0]

def manhattanY(H,T):
    return H[1]-T[1]

def move_tail(currentH, currentT):
    if ((abs(manhattanX(currentH, currentT)) > 1) or
        (abs(manhattanY(currentH, currentT)) > 1)):

        # It's also possible for both manhattans to simultaneously be 2 (or -2)
        if manhattanX(currentH, currentT) == 2 and manhattanY(currentH, currentT) == 2:
            # In this case the tail moves to diagonally below the head
            currentT[0] = currentH[0] - 1
            currentT[1] = currentH[1] - 1
        elif manhattanX(currentH, currentT) == 2 and manhattanY(currentH, currentT) == -2:
            # In this case the tail moves to diagonally below the head
            currentT[0] = currentH[0] - 1
            currentT[1] = currentH[1] + 1
        elif manhattanX(currentH, currentT) == -2 and manhattanY(currentH, currentT) == 2:
            # In this case the tail moves to diagonally below the head
            currentT[0] = currentH[0] + 1
            currentT[1] = currentH[1] - 1
        elif manhattanX(currentH, currentT) == -2 and manhattanY(currentH, currentT) == -2:
            # In this case the tail moves to diagonally below the head
            currentT[0] = currentH[0] + 1
            currentT[1] = currentH[1] + 1
        elif manhattanX(currentH, currentT) == 2:
            currentT[0] = currentH[0] - 1
            currentT[1] = currentH[1]
        elif manhattanX(currentH, currentT) == -2:
            currentT[0] = currentH[0] + 1
            currentT[1] = currentH[1]
        elif manhattanY(currentH, currentT) == 2:
            currentT[0] = currentH[0]
            currentT[1] = currentH[1] - 1
        elif manhattanY(currentH, currentT) == -2:
            currentT[0] = currentH[0]
            currentT[1] = currentH[1] + 1
        else:
            print("don't think this is possible", manhattanX(currentH, currentT),
                  manhattanY(currentH, currentT), currentH, currentT)

    return currentT

def print_rope(knots, nx, ny):
    # Make a big image
    rope_print_array = []
    for y in range(ny):
        rope_print_line = []
        for x in range(nx):
            rope_print_line.append(0)
        rope_print_array.append(rope_print_line)

    rope_length = len(knots)
    for n in range(rope_length-1, -1, -1):
        if n == 0:
            rope_print_array[knots[n][1]+int(0.4*ny)][knots[n][0]+int(0.4*nx)] = 10
        else:
            rope_print_array[knots[n][1]+int(0.4*ny)][knots[n][0]+int(0.4*nx)] = n

    return rope_print_array
    # for y in range(ny-1,-1,-1):
    #     rope_line = ""
    #     for x in range(nx):
    #         if rope_print_array[y][x] == 0:
    #             rope_line += "."
    #         elif rope_print_array[y][x] == 10:
    #             rope_line += "H"
    #         else:
    #             rope_line += str(rope_print_array[y][x])
    #     print(rope_line)

def part1():

    # Call the start point [0,0]
    currentH = [0,0]
    currentT = [0,0]

    Tvisited = set()

    print(Tvisited)

    for input_line in input_array:
        direction = input_line[0]
        distance = int(input_line[2:-1])

        for n in range(distance):
            if direction == "U":
                currentH[1] += 1
            elif direction == "D":
                currentH[1] -= 1
            elif direction == "R":
                currentH[0] += 1
            elif direction == "L":
                currentH[0] -= 1
            else:
                print("direction not recognised")

            # If T touches H then don't move it
            currentT = move_tail(currentH, currentT)

            Tvisited.add(tuple(currentT))


    print(Tvisited)
    answer = len(Tvisited)

    return answer

def part2():

    rope_length = 10
    knots = []
    visitedsets = []
    for mm in range(rope_length):
        knots.append([0,0])
        visitedsets.append(set())

    plot_arrays = []

    for input_line in input_array:
        direction = input_line[0]
        distance = int(input_line[2:-1])

        # print(input_line)
        for n in range(distance):
            if direction == "U":
                knots[0][1] += 1
            elif direction == "D":
                knots[0][1] -= 1
            elif direction == "R":
                knots[0][0] += 1
            elif direction == "L":
                knots[0][0] -= 1
            else:
                print("direction not recognised")

            visitedsets[0].add(tuple(knots[0]))
            for m in range(1,rope_length):
                # If T touches H then don't move it
                knots[m] = move_tail(knots[m-1], knots[m])
                visitedsets[m].add(tuple(knots[m]))

            # print_rope(knots)
            # print(" ")
        plot_arrays.append(print_rope(knots, 600, 600))


    print(visitedsets[-1])
    answer = len(visitedsets[-1])

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())

