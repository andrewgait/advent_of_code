# Advent of code, day 11

# open file
input = open("advent11_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)


def print_grid(inputs):
    n_inputs = len(inputs)
    n_line = len(inputs[0])
    for j in range(n_inputs):
        line_print = ""
        for i in range(n_line):
            line_print += str(inputs[j][i])
        print(line_print)

    print(" ")


def update_inputs(new_inputs, flashed, i, j, n_i, n_j):
    lo_j = j - 1
    hi_j = j + 1
    lo_i = i - 1
    hi_i = i + 1
    if (i == 0) and (j == 0):
        lo_i = 0
        lo_j = 0
    elif (i == 0) and (j == n_j - 1):
        lo_i = 0
        hi_j = n_j - 1
    elif (i == n_i - 1) and (j == 0):
        hi_i = n_i - 1
        lo_j = 0
    elif (i == n_i - 1) and (j == n_j - 1):
        hi_i = n_i - 1
        hi_j = n_j - 1
    elif (i == 0):
        lo_i = 0
    elif (j == 0):
        lo_j = 0
    elif (i == n_i - 1):
        hi_i = n_i - 1
    elif (j == n_j - 1):
        hi_j = n_j - 1

    for jj in range(lo_j,hi_j+1):
        for ii in range(lo_i,hi_i+1):
            if (jj == j) and (ii == i):
                test = 1
            else:
                if (flashed[jj][ii] == 1):
                    new_inputs[j][i] += 1


def part1():

    answer = 0

    inputs = []
    flashed = []
    all_flashed = []
    n_inputs = len(input_array)
    n_line = len(input_array[0]) - 1
    for j in range(n_inputs):
        input_line = []
        flashed_line = []
        all_flashed_line = []
        for i in range(n_line):
            input_line.append(int(input_array[j][i]))
            flashed_line.append(0)
            all_flashed_line.append(0)
        inputs.append(input_line)
        flashed.append(flashed_line)
        all_flashed.append(all_flashed_line)

    print(inputs)
    print_grid(inputs)

    n_steps = 100
    total_flashes = 0

    for n in range(n_steps):
        # print("Step ", n)
        # print(" ")
        new_inputs = []

        n_flashes = 0

        # Add 1 to every input, count flashes
        for j in range(n_inputs):
            new_line = []
            for i in range(n_line):
                new_line.append(inputs[j][i] + 1)
                if ((inputs[j][i] + 1) > 9):
                    n_flashes += 1
                    flashed[j][i] = 1
                    all_flashed[j][i] = 1

            new_inputs.append(new_line)

        total_flashes += n_flashes

        # print_grid(flashed)
        while n_flashes > 0:
        # for n in range(4):
            # print("n_flashes ", n_flashes)
            n_flashes = 0
            prev_flashed = [[0 for j in range(n_inputs)] for i in range(n_line)]
            for j in range(n_inputs):
                for i in range(n_line):
                    if all_flashed[j][i] == 0:
                        # update based on nearby octopus
                        update_inputs(new_inputs, flashed, i, j, n_line, n_inputs)
                        if new_inputs[j][i] > 9:
                            prev_flashed[j][i] = 1
                            all_flashed[j][i] = 1
                            n_flashes += 1
                            # print_grid(new_inputs)

            # print_grid(new_inputs)
            flashed = prev_flashed
            # print_grid(flashed)

            total_flashes += n_flashes

            for j in range(n_inputs):
                for i in range(n_line):
                    if new_inputs[j][i] > 9:
                        new_inputs[j][i] = 0


        inputs = new_inputs
        flashed = [[0 for jj in range(n_inputs)] for ii in range(n_line)]
        all_flashed = [[0 for jj in range(n_inputs)] for ii in range(n_line)]
        # print_grid(inputs)

    answer = total_flashes

    return answer

def part2():

    answer = 0

    inputs = []
    flashed = []
    all_flashed = []
    n_inputs = len(input_array)
    n_line = len(input_array[0]) - 1
    for j in range(n_inputs):
        input_line = []
        flashed_line = []
        all_flashed_line = []
        for i in range(n_line):
            input_line.append(int(input_array[j][i]))
            flashed_line.append(0)
            all_flashed_line.append(0)
        inputs.append(input_line)
        flashed.append(flashed_line)
        all_flashed.append(all_flashed_line)

    print(inputs)
    print_grid(inputs)

    steps = 0
    step_flashes = 0

    grid_size = n_inputs * n_line

    while step_flashes != grid_size:
        # print("Step ", steps)
        # print(" ")
        new_inputs = []

        n_flashes = 0
        step_flashes = 0

        # Add 1 to every input, count flashes
        for j in range(n_inputs):
            new_line = []
            for i in range(n_line):
                new_line.append(inputs[j][i] + 1)
                if ((inputs[j][i] + 1) > 9):
                    n_flashes += 1
                    flashed[j][i] = 1
                    all_flashed[j][i] = 1

            new_inputs.append(new_line)

        step_flashes += n_flashes

        # print_grid(flashed)
        while n_flashes > 0:
        # for n in range(4):
            # print("n_flashes ", n_flashes)
            n_flashes = 0
            prev_flashed = [[0 for j in range(n_inputs)] for i in range(n_line)]
            for j in range(n_inputs):
                for i in range(n_line):
                    if all_flashed[j][i] == 0:
                        # update based on nearby octopus
                        update_inputs(new_inputs, flashed, i, j, n_line, n_inputs)
                        if new_inputs[j][i] > 9:
                            prev_flashed[j][i] = 1
                            all_flashed[j][i] = 1
                            n_flashes += 1
                            # print_grid(new_inputs)

            # print_grid(new_inputs)
            flashed = prev_flashed
            # print_grid(flashed)

            step_flashes += n_flashes

            for j in range(n_inputs):
                for i in range(n_line):
                    if new_inputs[j][i] > 9:
                        new_inputs[j][i] = 0


        inputs = new_inputs
        flashed = [[0 for jj in range(n_inputs)] for ii in range(n_line)]
        all_flashed = [[0 for jj in range(n_inputs)] for ii in range(n_line)]
        # print_grid(inputs)

        # print("step flashes: ", step_flashes)
        steps += 1

    answer = steps

    return answer

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
