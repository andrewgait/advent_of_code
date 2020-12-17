# Advent of code, day 17
import numpy

# open file
input = open("advent17_input.txt", "r")
# input = open("advent17_test_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def print_slice(z, cube, cube_side):

    for i in range(cube_side):
        line_str = ""
        for j in range(cube_side):
            if (cube[i][j][z] == 0):
                line_str += "."
            else:
                line_str += "#"

        print(line_str)

def count_active(cube, i, j, k, cube_side):
    n_active = 0
    for ii in range(i-1, i+2):
        for jj in range(j-1, j+2):
            for kk in range(k-1, k+2):
                # first check in array bounds
                if ((ii >= 0) and (jj >= 0) and (kk >= 0) and
                    (ii < cube_side) and (jj < cube_side) and (kk < cube_side)):
                    if (ii == i) and (jj == j) and (kk == k):
                        n_active += 0
                    else:
                        n_active += cube[ii][jj][kk]

    return n_active

def get_new_value(cube, i, j, k, cube_side):
    new_value = 0

    if (cube[i][j][k] == 1):
        # active
        n_active = count_active(cube, i, j, k, cube_side)
        if (n_active == 2) or (n_active == 3):
            new_value = 1

    else:
        # inactive
        n_active = count_active(cube, i, j, k, cube_side)
        if (n_active == 3):
            new_value = 1

    return new_value

def count_total_active(cube, cube_side):
    total = 0
    for i in range(cube_side):
        for j in range(cube_side):
            for k in range(cube_side):
                total += cube[i][j][k]

    return total

def print_slice_4d(z, w, cube, cube_side):

    for i in range(cube_side):
        line_str = ""
        for j in range(cube_side):
            if (cube[i][j][z][w] == 0):
                line_str += "."
            else:
                line_str += "#"

        print(line_str)

def count_active_4d(cube, i, j, k, w, cube_side):
    n_active = 0
    for ii in range(i-1, i+2):
        for jj in range(j-1, j+2):
            for kk in range(k-1, k+2):
                for ww in range(w-1, w+2):
                    # first check in array bounds
                    if ((ii >= 0) and (jj >= 0) and (kk >= 0) and (ww >= 0) and
                        (ii < cube_side) and (jj < cube_side) and (kk < cube_side) and (ww < cube_side)):
                        if (ii == i) and (jj == j) and (kk == k) and (ww == w):
                            n_active += 0
                        else:
                            n_active += cube[ii][jj][kk][ww]

    return n_active

def get_new_value_4d(cube, i, j, k, w, cube_side):
    new_value = 0

    if (cube[i][j][k][w] == 1):
        # active
        n_active = count_active_4d(cube, i, j, k, w, cube_side)
        if (n_active == 2) or (n_active == 3):
            new_value = 1

    else:
        # inactive
        n_active = count_active_4d(cube, i, j, k, w, cube_side)
        if (n_active == 3):
            new_value = 1

    return new_value

def count_total_active_4d(cube, cube_side):
    total = 0
    for i in range(cube_side):
        for j in range(cube_side):
            for k in range(cube_side):
                for w in range(cube_side):
                    total += cube[i][j][k][w]

    return total


def part1():

    answer = 0

    cycles = 6

    # build a 3D array to hold the values: 2*cycles + len(input_array)
    # in each direction
    input_size = len(input_array)
    cube_side = (2 * cycles) + input_size

    cube = numpy.zeros((cube_side, cube_side, cube_side), dtype=numpy.int32)

    # For initial state z = 0 is at cube index cycles + input_size // 2
    z_index = cycles + input_size // 2

    # loop over the input array and add what's in it to the relevant place
    # in the full cube
    for i in range(input_size):
        for j in range(input_size):
            if input_array[i][j] == "#":
                cube[cycles+i][cycles+j][z_index] = 1

    print("At z=0, cycle 0")
    print_slice(z_index, cube, cube_side)

    for n in range(cycles):

        new_cube = numpy.zeros((cube_side, cube_side, cube_side), dtype=numpy.int32)
        for i in range(cube_side):
            for j in range(cube_side):
                for k in range(cube_side):
                    new_cube[i][j][k] = get_new_value(cube, i, j, k, cube_side)

        cube = new_cube
        print("At z=0, cycle ", n+1)
        print_slice(z_index, cube, cube_side)

        answer = count_total_active(cube, cube_side)
        print("number of active: ", answer)


    return answer

def part2():

    cycles = 6

    # build a 4D array to hold the values: 2*cycles + len(input_array)
    # in each direction
    input_size = len(input_array)
    cube_side = (2 * cycles) + input_size

    cube = numpy.zeros((cube_side, cube_side, cube_side, cube_side), dtype=numpy.int32)

    # For initial state z = 0 is at cube index cycles + input_size // 2
    z_index = cycles + input_size // 2
    w_index = cycles + input_size // 2

    # loop over the input array and add what's in it to the relevant place
    # in the full cube
    for i in range(input_size):
        for j in range(input_size):
            if input_array[i][j] == "#":
                cube[cycles+i][cycles+j][z_index][w_index] = 1

    print("At z=0, w=0, cycle 0")
    print_slice_4d(z_index, w_index, cube, cube_side)

    for n in range(cycles):

        new_cube = numpy.zeros((cube_side, cube_side, cube_side, cube_side), dtype=numpy.int32)
        for i in range(cube_side):
            for j in range(cube_side):
                for k in range(cube_side):
                    for w in range(cube_side):
                        new_cube[i][j][k][w] = get_new_value_4d(cube, i, j, k, w, cube_side)

        cube = new_cube
        print("At z=0, w=0 cycle ", n+1)
        print_slice_4d(z_index, w_index, cube, cube_side)

        answer = count_total_active_4d(cube, cube_side)
        print("number of active: ", answer)

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
