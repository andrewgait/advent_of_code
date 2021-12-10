# Advent of code, day 9

# open file
input = open("advent9_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    answer = 0

    input_map = []
    n_inputs = len(input_array)
    n_line = len(input_array[0]) - 1
    for n in range(n_inputs):
        input_line = []
        for nn in range(n_line):
            input_line.append(int(input_array[n][nn]))

        input_map.append(input_line)

    print(input_map)
    n_low_points = 0
    risk_level = 0

    for j in range(n_inputs):
        for i in range(n_line):
            low_point = False
            if (i > 0) and (j > 0) and (i < n_line-1) and (j < n_inputs-1):
                if ((input_map[j][i] < input_map[j][i-1]) and
                    (input_map[j][i] < input_map[j][i+1]) and
                    (input_map[j][i] < input_map[j-1][i]) and
                    (input_map[j][i] < input_map[j+1][i])):
                    low_point = True
                    n_low_points += 1
                    risk_level += (input_map[j][i] + 1)
            elif (i == 0) and (j == 0):
                if ((input_map[j][i] < input_map[j][i+1]) and
                    (input_map[j][i] < input_map[j+1][i])):
                    low_point = True
                    n_low_points += 1
                    risk_level += (input_map[j][i] + 1)
            elif (i == 0) and (j == n_inputs-1):
                if ((input_map[j][i] < input_map[j][i+1]) and
                    (input_map[j][i] < input_map[j-1][i])):
                    low_point = True
                    n_low_points += 1
                    risk_level += (input_map[j][i] + 1)
            elif (i == n_line-1) and (j == 0):
                if ((input_map[j][i] < input_map[j][i-1]) and
                    (input_map[j][i] < input_map[j+1][i])):
                    low_point = True
                    n_low_points += 1
                    risk_level += (input_map[j][i] + 1)
            elif (i == n_line-1) and (j == n_inputs-1):
                if ((input_map[j][i] < input_map[j][i-1]) and
                    (input_map[j][i] < input_map[j-1][i])):
                    low_point = True
                    n_low_points += 1
                    risk_level += (input_map[j][i] + 1)
            elif (i == 0):
                if ((input_map[j][i] < input_map[j][i+1]) and
                    (input_map[j][i] < input_map[j-1][i]) and
                    (input_map[j][i] < input_map[j+1][i])):
                    low_point = True
                    n_low_points += 1
                    risk_level += (input_map[j][i] + 1)
            elif (j == 0):
                if ((input_map[j][i] < input_map[j][i+1]) and
                    (input_map[j][i] < input_map[j][i-1]) and
                    (input_map[j][i] < input_map[j+1][i])):
                    low_point = True
                    n_low_points += 1
                    risk_level += (input_map[j][i] + 1)
            elif (i == n_line-1):
                if ((input_map[j][i] < input_map[j][i-1]) and
                    (input_map[j][i] < input_map[j-1][i]) and
                    (input_map[j][i] < input_map[j+1][i])):
                    low_point = True
                    n_low_points += 1
                    risk_level += (input_map[j][i] + 1)
            elif (j == n_inputs-1):
                if ((input_map[j][i] < input_map[j][i+1]) and
                    (input_map[j][i] < input_map[j][i-1]) and
                    (input_map[j][i] < input_map[j-1][i])):
                    low_point = True
                    n_low_points += 1
                    risk_level += (input_map[j][i] + 1)


    print(n_low_points, risk_level)
    answer = risk_level


    return answer


def get_basin_size(input_map, basin_done, i, j, current_basin, current_size):
    n_inputs = len(input_map)
    n_line = len(input_map[0])

    basin_done[j][i] = current_basin
    current_size = 1
    if (i > 0) and (j > 0) and (i < n_line-1) and (j < n_inputs-1):
        if (input_map[j][i-1] != 9) and (basin_done[j][i-1] == 0):
            current_size += get_basin_size(
                input_map, basin_done, i-1, j, current_basin, current_size)
        if (input_map[j][i+1] != 9) and (basin_done[j][i+1] == 0):
            current_size += get_basin_size(
                input_map, basin_done, i+1, j, current_basin, current_size)
        if (input_map[j-1][i] != 9) and (basin_done[j-1][i] == 0):
            current_size += get_basin_size(
                input_map, basin_done, i, j-1, current_basin, current_size)
        if (input_map[j+1][i] != 9) and (basin_done[j+1][i] == 0):
            current_size += get_basin_size(
                input_map, basin_done, i, j+1, current_basin, current_size)
        return current_size
    elif (i == 0) and (j == 0):
        if (input_map[j][i+1] != 9) and (basin_done[j][i+1] == 0):
            current_size += get_basin_size(
                input_map, basin_done, i+1, j, current_basin, current_size)
        if (input_map[j+1][i] != 9) and (basin_done[j+1][i] == 0):
            current_size += get_basin_size(
                input_map, basin_done, i, j+1, current_basin, current_size)
        return current_size
    elif (i == 0) and (j == n_inputs-1):
        if (input_map[j][i+1] != 9) and (basin_done[j][i+1] == 0):
            current_size += get_basin_size(
                input_map, basin_done, i+1, j, current_basin, current_size)
        if (input_map[j-1][i] != 9) and (basin_done[j-1][i] == 0):
            current_size += 1
            current_size += get_basin_size(
                input_map, basin_done, i, j-1, current_basin, current_size)
        return current_size
    elif (i == n_line-1) and (j == 0):
        if (input_map[j][i-1] != 9) and (basin_done[j][i-1] == 0):
            current_size += get_basin_size(
                input_map, basin_done, i-1, j, current_basin, current_size)
        if (input_map[j+1][i] != 9) and (basin_done[j+1][i] == 0):
            current_size += get_basin_size(
                input_map, basin_done, i, j+1, current_basin, current_size)
        return current_size
    elif (i == n_line-1) and (j == n_inputs-1):
        if (input_map[j][i-1] != 9) and (basin_done[j][i-1] == 0):
            current_size += get_basin_size(
                input_map, basin_done, i-1, j, current_basin, current_size)
        if (input_map[j-1][i] != 9) and (basin_done[j-1][i] == 0):
            current_size += get_basin_size(
                input_map, basin_done, i, j-1, current_basin, current_size)
        return current_size
    elif (i == 0):
        if (input_map[j][i+1] != 9) and (basin_done[j][i+1] == 0):
            current_size += get_basin_size(
                input_map, basin_done, i+1, j, current_basin, current_size)
        if (input_map[j-1][i] != 9) and (basin_done[j-1][i] == 0):
            current_size += get_basin_size(
                input_map, basin_done, i, j-1, current_basin, current_size)
        if (input_map[j+1][i] != 9) and (basin_done[j+1][i] == 0):
            current_size += get_basin_size(
                input_map, basin_done, i, j+1, current_basin, current_size)
        return current_size
    elif (j == 0):
        if (input_map[j][i-1] != 9) and (basin_done[j][i-1] == 0):
            current_size += get_basin_size(
                input_map, basin_done, i-1, j, current_basin, current_size)
        if (input_map[j][i+1] != 9) and (basin_done[j][i+1] == 0):
            current_size += get_basin_size(
                input_map, basin_done, i+1, j, current_basin, current_size)
        if (input_map[j+1][i] != 9) and (basin_done[j+1][i] == 0):
            current_size += get_basin_size(
                input_map, basin_done, i, j+1, current_basin, current_size)
        return current_size
    elif (i == n_line-1):
        if (input_map[j][i-1] != 9) and (basin_done[j][i-1] == 0):
            current_size += get_basin_size(
                input_map, basin_done, i-1, j, current_basin, current_size)
        if (input_map[j-1][i] != 9) and (basin_done[j-1][i] == 0):
            current_size += get_basin_size(
                input_map, basin_done, i, j-1, current_basin, current_size)
        if (input_map[j+1][i] != 9) and (basin_done[j+1][i] == 0):
            current_size += get_basin_size(
                input_map, basin_done, i, j+1, current_basin, current_size)
        return current_size
    elif (j == n_inputs-1):
        if (input_map[j][i-1] != 9) and (basin_done[j][i-1] == 0):
            current_size += get_basin_size(
                input_map, basin_done, i-1, j, current_basin, current_size)
        if (input_map[j][i+1] != 9) and (basin_done[j][i+1] == 0):
            current_size += get_basin_size(
                input_map, basin_done, i+1, j, current_basin, current_size)
        if (input_map[j-1][i] != 9) and (basin_done[j-1][i] == 0):
            current_size += get_basin_size(
                input_map, basin_done, i, j-1, current_basin, current_size)
        return current_size


def part2():

    answer = 1

    input_map = []
    basin_done = []
    n_inputs = len(input_array)
    n_line = len(input_array[0]) - 1
    for n in range(n_inputs):
        input_line = []
        basin_line = []
        for nn in range(n_line):
            input_line.append(int(input_array[n][nn]))
            basin_line.append(0)

        input_map.append(input_line)
        basin_done.append(basin_line)

    print(input_map)
    n_low_points = 0

    current_basin = 1
    basin_sizes = []
    for j in range(n_inputs):
        for i in range(n_line):
            low_point = False
            if (i > 0) and (j > 0) and (i < n_line-1) and (j < n_inputs-1):
                if ((input_map[j][i] < input_map[j][i-1]) and
                    (input_map[j][i] < input_map[j][i+1]) and
                    (input_map[j][i] < input_map[j-1][i]) and
                    (input_map[j][i] < input_map[j+1][i])):
                    low_point = True
                    n_low_points += 1
            elif (i == 0) and (j == 0):
                if ((input_map[j][i] < input_map[j][i+1]) and
                    (input_map[j][i] < input_map[j+1][i])):
                    low_point = True
                    n_low_points += 1
            elif (i == 0) and (j == n_inputs-1):
                if ((input_map[j][i] < input_map[j][i+1]) and
                    (input_map[j][i] < input_map[j-1][i])):
                    low_point = True
                    n_low_points += 1
            elif (i == n_line-1) and (j == 0):
                if ((input_map[j][i] < input_map[j][i-1]) and
                    (input_map[j][i] < input_map[j+1][i])):
                    low_point = True
                    n_low_points += 1
            elif (i == n_line-1) and (j == n_inputs-1):
                if ((input_map[j][i] < input_map[j][i-1]) and
                    (input_map[j][i] < input_map[j-1][i])):
                    low_point = True
                    n_low_points += 1
            elif (i == 0):
                if ((input_map[j][i] < input_map[j][i+1]) and
                    (input_map[j][i] < input_map[j-1][i]) and
                    (input_map[j][i] < input_map[j+1][i])):
                    low_point = True
                    n_low_points += 1
            elif (j == 0):
                if ((input_map[j][i] < input_map[j][i+1]) and
                    (input_map[j][i] < input_map[j][i-1]) and
                    (input_map[j][i] < input_map[j+1][i])):
                    low_point = True
                    n_low_points += 1
            elif (i == n_line-1):
                if ((input_map[j][i] < input_map[j][i-1]) and
                    (input_map[j][i] < input_map[j-1][i]) and
                    (input_map[j][i] < input_map[j+1][i])):
                    low_point = True
                    n_low_points += 1
            elif (j == n_inputs-1):
                if ((input_map[j][i] < input_map[j][i+1]) and
                    (input_map[j][i] < input_map[j][i-1]) and
                    (input_map[j][i] < input_map[j-1][i])):
                    low_point = True
                    n_low_points += 1

            if (low_point):
                # work out the size of the basin around this low point (j,i)
                current_size = 0
                basin_size = get_basin_size(
                    input_map, basin_done, i, j, current_basin, current_size)

                print("basin at ", i, j, basin_size)
                basin_sizes.append(basin_size)
                current_basin += 1

    print(basin_sizes)

    for nn in range(3):
        max_val = 0
        max_loc = -1
        n_basins = len(basin_sizes)
        for n in range(n_basins):
            if max_val < basin_sizes[n]:
                max_val = basin_sizes[n]
                max_loc = n

        print(max_val)
        answer *= max_val
        del basin_sizes[max_loc]

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
