# Advent of code, day 22
from functools import reduce

# open file
input = open("advent22_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    answer = 0

    # make grid going from -50 to 50 in each x,y,z dimension
    # (so add 50 to all coordinates)
    nx = ny = nz = 101
    grid = []
    for z in range(nz):
        grid_square = []
        for y in range(ny):
            grid_line = []
            for x in range(nx):
                grid_line.append(0)

            grid_square.append(grid_line)
        grid.append(grid_square)

    n_inputs = len(input_array)
    for n in range(n_inputs):
        splitspace = input_array[n].split(" ")
        state = 0
        if splitspace[0] == "on":
            state = 1
        splitcomma = splitspace[1].split(",")
        coords_min = []
        coords_max = []
        for nn in range(3):
            splitdots = splitcomma[nn].split("..")
            coords_min.append(int(splitdots[0][2:]))
            coords_max.append(int(splitdots[1]))

        print(coords_min, coords_max)

        coords_min = [coords_min[i] + 50 for i in range(3)]
        coords_max = [coords_max[i] + 50 for i in range(3)]

        print(coords_min, coords_max)

        if ((coords_min[2] >= 0) and (coords_max[2] < 102) and
            (coords_min[1] >= 0) and (coords_max[1] < 102) and
            (coords_min[0] >= 0) and (coords_max[0] < 102)):
            for z in range(coords_min[2], coords_max[2]+1):
                for y in range(coords_min[1], coords_max[1]+1):
                    for x in range(coords_min[0], coords_max[0]+1):
                        grid[z][y][x] = state

    for z in range(nz):
        for y in range(ny):
            for x in range(nx):
                answer += grid[z][y][x]

    return answer

def part2():

    answer = 0

    # Well there must be a clever way of doing this... is it possible to make
    # a dict somehow of coords that were turned on?
    ops = []

    n_inputs = len(input_array)
    for n in range(n_inputs):
        splitspace = input_array[n].split(" ")
        state = 0
        if splitspace[0] == "on":
            state = 1
        splitcomma = splitspace[1].split(",")
        coords_min = []
        coords_max = []
        for nn in range(3):
            splitdots = splitcomma[nn].split("..")
            coords_min.append(int(splitdots[0][2:]))
            coords_max.append(int(splitdots[1]))

        # print(coords_min, coords_max)
        # coords = coords_min + coords_max
        # print(coords)

        ops.append((state == 1, ((coords_min[0], coords_max[0]+1),
                                 (coords_min[1], coords_max[1]+1),
                                 (coords_min[2], coords_max[2]+1))))

    cubes = [op[1] for op in ops]
    # Make a full state grid
    xs = sorted(reduce(lambda a, b: a + b, [list(c[0]) for c in cubes]))
    ys = sorted(reduce(lambda a, b: a + b, [list(c[1]) for c in cubes]))
    zs = sorted(reduce(lambda a, b: a + b, [list(c[2]) for c in cubes]))
    print(f"The state size is {len(xs) * len(ys) * len(zs)}")
    state = [[[False
               for _ in range(len(zs))]
              for _ in range(len(ys))]
             for _ in range(len(xs))]
    print(f"Made the state!")

    x2i = {x: i for i, x in enumerate(xs)}
    y2i = {y: i for i, y in enumerate(ys)}
    z2i = {z: i for i, z in enumerate(zs)}

    n_lit = 0
    for turn_on, box in ops:
        # This is still slow (and somewhat borrowed) but seems faster
        # than my original idea of making a dict with "on" elements
        print(turn_on, box, n_lit)
        for xi in range(x2i[box[0][0]], x2i[box[0][1]]):
            for yi in range(y2i[box[1][0]], y2i[box[1][1]]):
                for zi in range(z2i[box[2][0]], z2i[box[2][1]]):
                    region_size = (xs[xi + 1] - xs[xi]) \
                        * (ys[yi + 1] - ys[yi]) \
                        * (zs[zi + 1] - zs[zi])
                    if turn_on and not state[xi][yi][zi]:
                        n_lit += region_size
                        state[xi][yi][zi] = True
                    elif (not turn_on) and state[xi][yi][zi]:
                        n_lit -= region_size
                        state[xi][yi][zi] = False

        # left some notes below on what might work if an "intersection" method is tried

        # We know (obviously) how many locations get turned on / off each time
        # - is there a way of telling whether something is already on / off?

        # Ohhh... so an on-on coincidence could:
        # - create 9 new on "blocks" (old one plus 8 new, rules dependent on
        #   which of the 6 corners of the new is within the old, ouch)
        # - if it intersects fully along a plane, then the new plus the bit of
        #   the old that's still relevant

        # An off-on coincidence could:
        # - slice a current block into two pieces in one of three planes
        # - turn 1 block into 7 blocks

        # If a new block doesn't intersect with any then it just gets added

        # What happens if an off is entirely within an on, though?  That's nasty...

        # if state == 1:
        #     if len(on_blocks) == 0:
        #         on_blocks.append(coords)
        #     else:
        #         # Loop over other grids
        #         for nn in range(len(on_blocks)):
        #             # Find coincidences
        #             if ((coords[0] >= on_coords[0]) and (coords[1] >= on_coords[1]) and
        #                 (coords[2] >= on_coords[2]) and (coords[0] <= on_coords[3]) and
        #                 (coords[1] >= on_coords[4]) and (coords[2] <= on_coords[5])):
        #
        #
        #             elif ((coords[3] >= on_coords[0]) and (coords[4] >= on_coords[1]) and
        #                 (coords[5] >= on_coords[2]) and (coords[3] <= on_coords[3]) and
        #                 (coords[4] >= on_coords[4]) and (coords[5] <= on_coords[5])):

    answer = n_lit

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
