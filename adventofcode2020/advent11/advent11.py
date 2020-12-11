# Advent of code, day 11
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.rc('animation', ffmpeg_path='/opt/local/bin/ffmpeg')

# open file
input = open("advent11_input.txt", "r")
# input = open("advent11_test_input.txt", "r")

# key_dict = {".": 0, "L": 1, "#":2}

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def print_seating_array(seating_array):
    n = len(seating_array)
    print(" ")
    for i in range(n):
        seating_str = ""
        for j in range(len(seating_array[i])):
            seating_str += seating_array[i][j]
        print(seating_str)

def number_adjacent_occupied(seating_array, i, j, height, width):
    occupied = 0
    for ii in range(i-1,i+2):
        for jj in range(j-1,j+2):
            # ignore current seat!
            if (ii == i) and (jj == j):
                occupied += 0
            elif ((jj >= 0) and (ii >= 0) and (jj < width) and (ii < height) and
                    (seating_array[ii][jj] == "#")):
                occupied += 1

    return occupied

def get_new_value(seating_array, i, j, height, width):

    seat = seating_array[i][j]
    new_seat = "."
    if (seat == "L"):
        # look at values around it
        occupied = number_adjacent_occupied(seating_array, i, j, height, width)
        if (occupied == 0):
            new_seat = "#"
        else:
            new_seat = "L"
    elif (seat == "#"):
        occupied = number_adjacent_occupied(seating_array, i, j, height, width)
        if (occupied >= 4):
            new_seat = "L"
        else:
            new_seat = "#"

    return new_seat


def occupied_p2(seating_array, i, j, height, width):
    occupied = 0

    # test in 8 directions

    for move_i in range(-1,2):
        for move_j in range(-1,2):
            ii = i
            jj = j
            if (move_i == 0) and (move_j == 0):
                # Do nothing!
                occupied += 0
            else:
                ii += move_i
                jj += move_j
                reached_seat = False
                while ((ii >= 0) and (jj >= 0) and (ii < height) and
                       (jj < width) and (not reached_seat)):
                    if (seating_array[ii][jj] == "."):
                        ii += move_i
                        jj += move_j
                    elif (seating_array[ii][jj] == "#"):
                        occupied += 1
                        reached_seat = True
                    else:
                        # "L" i.e. empty so break without adding
                        reached_seat = True

    return occupied


def get_new_value_p2(seating_array, i, j, height, width):

    seat = seating_array[i][j]
    new_seat = "."
    if (seat == "L"):
        # look at values around it
        occupied = occupied_p2(seating_array, i, j, height, width)
        if (occupied == 0):
            new_seat = "#"
        else:
            new_seat = "L"
    elif (seat == "#"):
        occupied = occupied_p2(seating_array, i, j, height, width)
        if (occupied >= 5):
            new_seat = "L"
        else:
            new_seat = "#"

    return new_seat

def convert_str_to_number(seating_array, height, width):
    grid = np.zeros((height, width), dtype=np.int64)

    for i in range(height):
        for j in range(width):
            grid[i][j] = 0
            if (seating_array[i][j] == "L"):
                grid[i][j] = 1
            if (seating_array[i][j] == "#"):
                grid[i][j] = 2

    return grid

def part1():

    answer = 0
    grids = []

    height = len(input_array)
    width = len(input_array[0])-1
    # build the seating array
    seating_array = []
    for i in range(height):
        seating_line = []
        for j in range(width):
            seating_line.append(input_array[i][j])
#         print(seating_line)
        seating_array.append(seating_line)

#     print_seating_array(seating_array)
    grids.append(convert_str_to_number(seating_array, height, width))

    new_seating_array = []
    changed = True
    n = 0
    while changed:
        # loop over current seating array, build new one
        new_seating_array = []
        for i in range(height):
            new_seating_line = []
            for j in range(width):
                new_seating_line.append(get_new_value(
                    seating_array, i, j, height, width))
            new_seating_array.append(new_seating_line)

#         print_seating_array(new_seating_array)

        grids.append(convert_str_to_number(new_seating_array, height, width))

        # compare new_seating array to old one
        if (new_seating_array == seating_array):
            changed = False

        seating_array = new_seating_array

        n += 1

    # count number of occupied seats
    answer = 0
    for i in range(height):
        for j in range(width):
            if (seating_array[i][j] == "#"):
                answer += 1

    return answer, grids

def part2():

    answer = 0
    grids = []

    height = len(input_array)
    width = len(input_array[0])-1
    # build the seating array
    seating_array = []
    for i in range(height):
        seating_line = []
        for j in range(width):
            seating_line.append(input_array[i][j])
#         print(seating_line)
        seating_array.append(seating_line)

#     print_seating_array(seating_array)
    grids.append(convert_str_to_number(seating_array, height, width))

    new_seating_array = []
    changed = True
    n = 0
    while changed:
        # loop over current seating array, build new one
        new_seating_array = []
        for i in range(height):
            new_seating_line = []
            for j in range(width):
                new_seating_line.append(get_new_value_p2(
                    seating_array, i, j, height, width))
            new_seating_array.append(new_seating_line)

#         print_seating_array(new_seating_array)
        grids.append(convert_str_to_number(new_seating_array, height, width))

        # compare new_seating array to old one
        if (new_seating_array == seating_array):
            changed = False

        seating_array = new_seating_array

        n += 1

    # count number of occupied seats
    answer = 0
    for i in range(height):
        for j in range(width):
            if (seating_array[i][j] == "#"):
                answer += 1

    return answer, grids

answer1, gridsp1 = part1()
print("Part 1 answer: ", answer1)
answer2, gridsp2 = part2()
print("Part 2 answer: ", answer2)

x = np.linspace(0, 1, len(gridsp1[0][0])+1)
y = np.linspace(0, 1, len(gridsp1[0])+1)
xmesh, ymesh = np.meshgrid(x,y)

fig = plt.figure()
ims = []
print("Animating ", len(gridsp1), " grids for part 1")
for n in range(len(gridsp1)):
# for n in range(100):
    if n % 20 == 0:
        print(n)
    array = np.flipud(np.array(gridsp1[n]))
# print(array)
    ims.append((plt.pcolor(xmesh, ymesh, array),))

im_ani = animation.ArtistAnimation(fig, ims, interval=100, repeat_delay=3000,
                                   blit=True)
my_writer = animation.FFMpegWriter(metadata={'code':'andrewgait'})
im_ani.save('advent11_2020_seating_p1.mp4', writer=my_writer)

plt.show()

x = np.linspace(0, 1, len(gridsp2[0][0])+1)
y = np.linspace(0, 1, len(gridsp2[0])+1)
xmesh, ymesh = np.meshgrid(x,y)

fig = plt.figure()
ims = []
print("Animating ", len(gridsp2), " grids for part 2")
for n in range(len(gridsp2)):
# for n in range(100):
    if n % 20 == 0:
        print(n)
    array = np.flipud(np.array(gridsp2[n]))
# print(array)
    ims.append((plt.pcolor(xmesh, ymesh, array),))

im_ani = animation.ArtistAnimation(fig, ims, interval=100, repeat_delay=3000,
                                   blit=True)
my_writer = animation.FFMpegWriter(metadata={'code':'andrewgait'})
im_ani.save('advent11_2020_seating_p2.mp4', writer=my_writer)

plt.show()

