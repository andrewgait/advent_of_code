# Advent of code 2022, day 14
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.rc('animation', ffmpeg_path='/opt/local/bin/ffmpeg')

# open file
input = open("advent14_input.txt", "r")
# input = open("advent14_test_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def print_grid(grid, nx, ny):
    for y in range(ny):
        grid_line = ""
        for x in range(nx):
            if grid[x][y] == 0:
                grid_line += "."
            elif grid[x][y] == 1:
                grid_line += "#"
            elif grid[x][y] == 2:
                grid_line += "o"
            elif grid[x][y] == 3:
                grid_line += "+"

        print(grid_line)
    print (" ")


def part1():

    # Get the lines and work out the max depth
    max_depth = 0
    max_x = 500
    min_x = 500

    # lines to draw is a list where each element is a list of coord1 then coord2
    lines_to_draw = []

    for input_line in input_array:
        splitline = input_line.split(" -> ")
        for n in range(len(splitline)-1):
            splitn = splitline[n].split(",")
            splitn1 = splitline[n+1].split(",")
            x0 = int(splitn[0])
            y0 = int(splitn[1])
            x1 = int(splitn1[0])
            y1 = int(splitn1[1])
            lines_to_draw.append([x0, y0, x1, y1])
            if y0 > max_depth:
                max_depth = y0
            if y1 > max_depth:
                max_depth = y1
            if x0 < min_x:
                min_x = x0
            if x1 < min_x:
                min_x = x1
            if x0 > max_x:
                max_x = x0
            if x1 > max_x:
                max_x = x1

    # Make a halo around the outside just to be safe
    max_depth += 1
    max_x += 1
    min_x -= 1

    print(max_depth, min_x, max_x)
    print(lines_to_draw)

    nx = max_x+1-min_x
    ny = max_depth+1
    grid = np.zeros(shape=(nx, ny), dtype=int)
    start_x = 500 - min_x
    start_y = 0

    grid[start_x][start_y] = 3
    # Subtract min_x off every x coordinate!
    for line in lines_to_draw:
        x0 = line[0] - min_x
        x1 = line[2] - min_x
        y0 = line[1]
        y1 = line[3]
        if x0 == x1:
            # x coords are the same
            if y1 > y0:
                for y in range(y1, y0-1, -1):
                    grid[x0][y] = 1
            else:
                for y in range(y1, y0+1):
                    grid[x0][y] = 1
        elif y0 == y1:
            # x coords are the same
            # print(" y same, ", y0, " x0, x1 ", x0, x1)
            if x1 > x0:
                for x in range(x1, x0-1, -1):
                    grid[x][y0] = 1
            else:
                for x in range(x1, x0+1):
                    grid[x][y0] = 1
        else:
            print("weird coords for line ", line)


    # Draw the grid
    print_grid(grid, nx, ny)
    grids = []

    # Now
    sand_y = 0
    sand_x = start_x
    while sand_y < max_depth:
        if (grid[sand_x][sand_y+1] == 0):
            sand_y += 1
        elif (grid[sand_x-1][sand_y+1] == 0):
            sand_y += 1
            sand_x -= 1
        elif (grid[sand_x+1][sand_y+1] == 0):
            sand_y += 1
            sand_x += 1
        else:
            grid[sand_x][sand_y] = 2
            # and reset
            sand_x = start_x
            sand_y = 0

            copy_grid = np.copy(grid)

            grids.append(np.transpose(copy_grid))

        # print_grid(grid, nx, ny)

    count_sand = 0
    for y in range(ny):
        for x in range(nx):
            if grid[x][y] == 2:
                count_sand += 1

    answer = count_sand
    print_grid(grid, nx, ny)

    return answer, grids

def part2():

    # Get the lines and work out the max depth
    max_depth = 0
    max_x = 500
    min_x = 500

    # lines to draw is a list where each element is a list of coord1 then coord2
    lines_to_draw = []

    for input_line in input_array:
        splitline = input_line.split(" -> ")
        for n in range(len(splitline)-1):
            splitn = splitline[n].split(",")
            splitn1 = splitline[n+1].split(",")
            x0 = int(splitn[0])
            y0 = int(splitn[1])
            x1 = int(splitn1[0])
            y1 = int(splitn1[1])
            lines_to_draw.append([x0, y0, x1, y1])
            if y0 > max_depth:
                max_depth = y0
            if y1 > max_depth:
                max_depth = y1
            if x0 < min_x:
                min_x = x0
            if x1 < min_x:
                min_x = x1
            if x0 > max_x:
                max_x = x0
            if x1 > max_x:
                max_x = x1

    # Make a halo around the outside just to be safe
    max_depth += 2
    # How far do we need to go in each direction?
    max_x += max_depth
    min_x -= max_depth

    print(max_depth, min_x, max_x)
    print(lines_to_draw)

    nx = max_x+1-min_x
    ny = max_depth+1
    grid = np.zeros(shape=(nx, ny), dtype=int)
    start_x = 500 - min_x
    start_y = 0

    grid[start_x][start_y] = 3
    # Subtract min_x off every x coordinate!
    for line in lines_to_draw:
        x0 = line[0] - min_x
        x1 = line[2] - min_x
        y0 = line[1]
        y1 = line[3]
        if x0 == x1:
            # x coords are the same
            if y1 > y0:
                for y in range(y1, y0-1, -1):
                    grid[x0][y] = 1
            else:
                for y in range(y1, y0+1):
                    grid[x0][y] = 1
        elif y0 == y1:
            # x coords are the same
            # print(" y same, ", y0, " x0, x1 ", x0, x1)
            if x1 > x0:
                for x in range(x1, x0-1, -1):
                    grid[x][y0] = 1
            else:
                for x in range(x1, x0+1):
                    grid[x][y0] = 1
        else:
            print("weird coords for line ", line)

    # Draw a line at max_depth (which had 2 added already)
    for x in range(1,nx-1):
        grid[x][max_depth] = 1

    # Draw the grid
    # print_grid(grid, nx, ny)

    grids = []
    # Now is the stopping condition different?
    sand_y = 0
    sand_x = start_x
    sand_stopped = False
    while not sand_stopped:
        if (grid[sand_x][sand_y+1] == 0):
            sand_y += 1
        elif (grid[sand_x-1][sand_y+1] == 0):
            sand_y += 1
            sand_x -= 1
        elif (grid[sand_x+1][sand_y+1] == 0):
            sand_y += 1
            sand_x += 1
        else:
            grid[sand_x][sand_y] = 2
            # If the point being filled is the start point
            # then no more sand can flow through I think
            if sand_x == start_x and sand_y == 0:
                sand_stopped = True
                grid[sand_x][sand_y] = 3

            # and reset
            sand_x = start_x
            sand_y = 0

            # append current grid for animation?
            copy_grid = np.copy(grid)

            grids.append(np.transpose(copy_grid))

        # print_grid(grid, nx, ny)

    count_sand = 1 # includes the start point, lol
    for y in range(ny):
        for x in range(nx):
            if grid[x][y] == 2:
                count_sand += 1

    answer = count_sand
    # print_grid(grid, nx, ny)
    plt.imshow(np.transpose(grid), cmap='hot')
    plt.colorbar()
    plt.show()

    return answer, grids

part1, gridsp1 = part1()
print("Part 1 answer: ", part1)
part2, gridsp2 = part2()
print("Part 2 answer: ", part2)

x = np.linspace(0, 1, len(gridsp1[0][0])+1)
y = np.linspace(0, 1, len(gridsp1[0])+1)
xmesh, ymesh = np.meshgrid(x,y)

fig = plt.figure()
ims = []
print("Animating ", len(gridsp1), " grids for part 1")
for n in range(len(gridsp1)):
# for n in range(100):
    if n % 200 == 0:
        print(n)
    array = np.flipud(np.array(gridsp1[n]))
# print(array)
    ims.append((plt.pcolormesh(xmesh, ymesh, array, cmap="hot"),))

im_ani = animation.ArtistAnimation(fig, ims, interval=10, repeat_delay=3000,
                                   blit=True)
my_writer = animation.FFMpegWriter(fps=60, metadata={'code':'andrewgait'})
im_ani.save('advent14_2022_sand_p1.mp4', writer=my_writer)

# plt.show()

x = np.linspace(0, 2, len(gridsp2[0][0])+1)
y = np.linspace(0, 1, len(gridsp2[0])+1)
xmesh, ymesh = np.meshgrid(x,y)

fig = plt.figure()
ims = []
print("Animating ", len(gridsp2), " grids for part 2")
for n in range(len(gridsp2)):
# for n in range(100):
    if n % 2000 == 0:
        print(n)
    if n % 10 == 0:
        array = np.flipud(np.array(gridsp2[n]))
    # print(array)
        ims.append((plt.pcolormesh(xmesh, ymesh, array, cmap="hot"),))

array = np.flipud(np.array(gridsp2[-1]))
ims.append((plt.pcolormesh(xmesh, ymesh, array, cmap="hot"),))

im_ani = animation.ArtistAnimation(fig, ims, interval=10, repeat_delay=3000,
                                   blit=True)
my_writer = animation.FFMpegWriter(fps=100, metadata={'code':'andrewgait'})
im_ani.save('advent14_2022_sand_p2.mp4', writer=my_writer)

plt.show()


