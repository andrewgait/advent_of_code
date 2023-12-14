# Advent of code 2023, day 14
import numpy as np

# open file
input = open("advent14_input.txt", "r")
# input = open("advent14_input_test.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

rocks_dict = {".": 0, "#": 1, "O": 2}
rocks_back_dict = {0: ".", 1: "#", 2: "O"}


def display_rock_map(rock_map):
    print(" ")
    n_rows = len(rock_map)
    n_cols = len(rock_map[0])
    for row in range(n_rows):
        print_rocks = ""
        for col in range(n_cols):
            print_rocks += rocks_back_dict[rock_map[row][col]]
        print(print_rocks)
    print(" ")


def roll_north(rock_map):
    n_cols = len(rock_map[0])
    n_rows = len(rock_map)

    unchanged = False

    while not unchanged:
        new_rock_map = np.zeros((n_rows, n_cols))
        # don't need to edit the first row
        for col in range(n_cols):
            new_rock_map[0][col] = rock_map[0][col]
        # new_rock_map.append(new_rock_line)
        for row in range(1,n_rows):
            # new_rock_line = []
            for col in range(n_cols):
                if rock_map[row][col] == rocks_dict["O"]:
                    if rock_map[row-1][col] == rocks_dict["."]:
                        new_rock_map[row-1][col] = rocks_dict["O"]
                        new_rock_map[row][col] = rocks_dict["."]
                    else:
                        new_rock_map[row][col] = rocks_dict["O"]
                else:
                    new_rock_map[row][col] = rock_map[row][col]

        if np.array_equal(new_rock_map, rock_map):
            unchanged = True

        rock_map = np.copy(new_rock_map)

    return rock_map


def roll_south(rock_map):
    n_cols = len(rock_map[0])
    n_rows = len(rock_map)

    unchanged = False

    while not unchanged:
        new_rock_map = np.zeros((n_rows, n_cols))
        modified = []
        for row in range(n_rows-2,-1,-1):
            for col in range(n_cols):
                if rock_map[row][col] == rocks_dict["O"] and [row,col] not in modified:
                    if rock_map[row+1][col] == rocks_dict["."]:
                        new_rock_map[row+1][col] = rocks_dict["O"]
                        modified.append([row+1, col])
                        new_rock_map[row][col] = rocks_dict["."]
                    else:
                        new_rock_map[row][col] = rocks_dict["O"]
                else:
                    if [row,col] not in modified:
                        new_rock_map[row][col] = rock_map[row][col]


        # don't need to edit the final row
        for col in range(n_cols):
            if [n_rows-1,col] not in modified:
                new_rock_map[n_rows-1][col] = rock_map[n_rows-1][col]

        if np.array_equal(new_rock_map, rock_map):
            unchanged = True

        rock_map = np.copy(new_rock_map)

    return rock_map


def roll_west(rock_map):
    n_cols = len(rock_map[0])
    n_rows = len(rock_map)

    unchanged = False

    while not unchanged:
        new_rock_map = np.zeros((n_rows, n_cols))
        for row in range(n_rows):
            # Don't edit the first column
            new_rock_map[row][0] = rock_map[row][0]
            for col in range(1,n_cols):
                if rock_map[row][col] == rocks_dict["O"]:
                    if rock_map[row][col-1] == rocks_dict["."]:
                        new_rock_map[row][col-1] = rocks_dict["O"]
                        new_rock_map[row][col] = rocks_dict["."]
                    else:
                        new_rock_map[row][col] = rocks_dict["O"]
                else:
                    new_rock_map[row][col] = rock_map[row][col]

        if np.array_equal(new_rock_map, rock_map):
            unchanged = True

        rock_map = np.copy(new_rock_map)

    return rock_map


def roll_east(rock_map):
    n_cols = len(rock_map[0])
    n_rows = len(rock_map)

    unchanged = False

    while not unchanged:
        new_rock_map = np.zeros((n_rows, n_cols))
        modified = []
        for row in range(n_rows):
            for col in range(n_cols-2, -1, -1):
                if rock_map[row][col] == rocks_dict["O"] and [row,col] not in modified:
                    if rock_map[row][col+1] == rocks_dict["."]:
                        new_rock_map[row][col+1] = rocks_dict["O"]
                        modified.append([row,col+1])
                        new_rock_map[row][col] = rocks_dict["."]
                    else:
                        new_rock_map[row][col] = rocks_dict["O"]
                else:
                    if [row,col] not in modified:
                        new_rock_map[row][col] = rock_map[row][col]
            # Don't edit the final column
            if [row,n_cols-1] not in modified:
                new_rock_map[row][n_cols-1] = rock_map[row][n_cols-1]

        if np.array_equal(new_rock_map, rock_map):
            unchanged = True

        rock_map = np.copy(new_rock_map)

    return rock_map


def calculate_load_north(rock_map):
    answer = 0
    n_rows = len(rock_map)
    n_cols = len(rock_map[0])
    for row in range(n_rows):
        for col in range(n_cols):
            if rock_map[row][col] == rocks_dict["O"]:
                answer += n_rows-row

    return answer


def part1():

    rock_map = []

    for input in input_array:
        rock_row = []
        for n in range(len(input[:-1])):
            rock_row.append(rocks_dict[input[n]])

        rock_map.append(rock_row)

    rock_map = np.array(rock_map)

    n_rows = len(rock_map)
    n_cols = len(rock_map[0])
    display_rock_map(rock_map)

    rock_map = roll_north(rock_map)

    display_rock_map(rock_map)

    answer = calculate_load_north(rock_map)

    return answer

def part2():

    rock_map = []

    for input in input_array:
        rock_row = []
        for n in range(len(input[:-1])):
            rock_row.append(rocks_dict[input[n]])

        rock_map.append(rock_row)

    rock_map = np.array(rock_map)

    n_rows = len(rock_map)
    n_cols = len(rock_map[0])
    display_rock_map(rock_map)

    # At a guess, this goes through cycles so work out the length of a cycle...
    found = False
    n = 0
    calculated_loads = []
    rock_maps = []
    index = 0
    while not found:
        rock_map = roll_north(rock_map)
        # display_rock_map(rock_map)
        rock_map = roll_west(rock_map)
        # display_rock_map(rock_map)
        rock_map = roll_south(rock_map)
        # display_rock_map(rock_map)
        rock_map = roll_east(rock_map)
        n += 1
        calculated_loads.append(calculate_load_north(rock_map))

        for m in range(len(rock_maps)):
            if np.array_equal(rock_map, rock_maps[m]):
                found = True
                index = m

        rock_maps.append(rock_map)

        print(n)

    print(n, index, calculated_loads)

    display_rock_map(rock_map)

    test_val = 1000000000 - index

    print(test_val % (n-index-1), test_val / (n-index-1))

    answer = calculated_loads[index + (test_val % (n-index-1)) - 1]

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
