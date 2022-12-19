# Advent of code 2022, day 18
import numpy as np

# open file
input = open("advent18_input.txt", "r")
# input = open("advent18_test_input.txt", "r")
# input = open("advent18_test_input2.txt", "r")
# input = open("advent18_test_input3.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

# input_array = []
# for x in range(11):
#     for y in range(11):
#         for z in range(11):
#             if x != 0 and x != 10 and y != 0 and y != 10 and z != 0 and z != 10:
#                 if x == 1 or y == 1 or z == 1:
#                     input_array.append(str(x)+","+str(y)+","+str(z)+"\n")
#                 elif x != 2 and x != 8 and y != 2 and y != 8 and z != 2 and z != 8:
#                     if x == 3 or y == 3 or z == 3:
#                         input_array.append(str(x)+","+str(y)+","+str(z)+"\n")
#
#
# print(input_array)

def calc_area(cubes, grid_3d, side_test):
    # now loop over all cubes again and test against six neighbours
    open_faces = 0

    for cube in cubes:

        if grid_3d[cube[0]-1][cube[1]][cube[2]] == side_test:
            open_faces += 1
        if grid_3d[cube[0]+1][cube[1]][cube[2]] == side_test:
            open_faces += 1
        if grid_3d[cube[0]][cube[1]-1][cube[2]] == side_test:
            open_faces += 1
        if grid_3d[cube[0]][cube[1]+1][cube[2]] == side_test:
            open_faces += 1
        if grid_3d[cube[0]][cube[1]][cube[2]-1] == side_test:
            open_faces += 1
        if grid_3d[cube[0]][cube[1]][cube[2]+1] == side_test:
            open_faces += 1

    return open_faces

def part1():

    cubes = []
    max_x = 0
    max_y = 0
    max_z = 0
    for input_line in input_array:
        splitcomma = input_line.split(",")
        x = int(splitcomma[0])
        y = int(splitcomma[1])
        z = int(splitcomma[2][:-1])
        cubes.append([x,y,z])
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        if z > max_z:
            max_z = z

    nx = max_x + 2
    ny = max_y + 2
    nz = max_z + 2
    print("grid_3d size: ", nx, ny, nz)
    grid_3d = np.zeros(shape=(nx,ny,nz), dtype=int)

    # Loop to add cubes to grid
    for cube in cubes:
        grid_3d[cube[0]][cube[1]][cube[2]] = 1

    open_faces = calc_area(cubes, grid_3d, 0)

    answer = open_faces

    return answer

def trapped(x,y,z,grid_3d,nx,ny,nz,visited,not_trapped,test_side):
    # If we are at an edge or indeed next to one (?) then we can't be trapped
    if x == 0 or y == 0 or z == 0 or x == (nx-1) or y == (ny-1) or z == (nz-1):
        return False
    elif [x,y,z] in not_trapped:
        return False
    else:
        visited.append([x,y,z])
        # We don't want to go round in circles so also check whether visited
        if grid_3d[x][y][z+1] == test_side and [x,y,z+1] not in visited:
            return trapped(x,y,z+1,grid_3d,nx,ny,nz,visited,not_trapped,test_side)
        if grid_3d[x][y][z-1] == test_side and [x,y,z-1] not in visited:
            return trapped(x,y,z-1,grid_3d,nx,ny,nz,visited,not_trapped,test_side)
        if grid_3d[x][y+1][z] == test_side and [x,y+1,z] not in visited:
            return trapped(x,y+1,z,grid_3d,nx,ny,nz,visited,not_trapped,test_side)
        if grid_3d[x][y-1][z] == test_side and [x,y-1,z] not in visited:
            return trapped(x,y-1,z,grid_3d,nx,ny,nz,visited,not_trapped,test_side)
        if grid_3d[x+1][y][z] == test_side and [x+1,y,z] not in visited:
            return trapped(x+1,y,z,grid_3d,nx,ny,nz,visited,not_trapped,test_side)
        if grid_3d[x-1][y][z] == test_side and [x-1,y,z] not in visited:
            return trapped(x-1,y,z,grid_3d,nx,ny,nz,visited,not_trapped,test_side)

        return True

def calc_trapped(nx,ny,nz,grid_3d,test_side):
    print("test side ", test_side)
    not_trapped = []
    interior_trapped = []
    # Speculating that starting this loop from the edges doesn't help; could even be
    # best to start from the centre and go out...
    for z in range(nz//2, nz):
        for y in range(ny//2, ny):
            for x in range(nx//2, nx):
                if grid_3d[x][y][z] == test_side:
                    visited = []
                    if trapped(x,y,z,grid_3d,nx,ny,nz,visited,not_trapped,test_side):
                        interior_trapped.append([x,y,z])
                    else:
                        not_trapped.append([x,y,z])
                    # print("check ", x, y, z)
                else:
                    not_trapped.append([x,y,z])
            for x in range((nx//2)-1,-1,-1):
                if grid_3d[x][y][z] == test_side:
                    visited = []
                    if trapped(x,y,z,grid_3d,nx,ny,nz,visited,not_trapped,test_side):
                        interior_trapped.append([x,y,z])
                    else:
                        not_trapped.append([x,y,z])
                    # print("check ", x, y, z)
                else:
                    not_trapped.append([x,y,z])
        for y in range((ny//2)-1,-1,-1):
            for x in range(nx//2, nx):
                if grid_3d[x][y][z] == test_side:
                    visited = []
                    if trapped(x,y,z,grid_3d,nx,ny,nz,visited,not_trapped,test_side):
                        interior_trapped.append([x,y,z])
                    else:
                        not_trapped.append([x,y,z])
                    # print("check ", x, y, z)
                else:
                    not_trapped.append([x,y,z])
            for x in range((nx//2)-1,-1,-1):
                if grid_3d[x][y][z] == test_side:
                    visited = []
                    if trapped(x,y,z,grid_3d,nx,ny,nz,visited,not_trapped,test_side):
                        interior_trapped.append([x,y,z])
                    else:
                        not_trapped.append([x,y,z])
                    # print("check ", x, y, z)
                else:
                    not_trapped.append([x,y,z])
    for z in range((nz//2)-1,-1,-1):
        for y in range(ny//2, ny):
            for x in range(nx//2, nx):
                if grid_3d[x][y][z] == test_side:
                    visited = []
                    if trapped(x,y,z,grid_3d,nx,ny,nz,visited,not_trapped,test_side):
                        interior_trapped.append([x,y,z])
                    else:
                        not_trapped.append([x,y,z])
                    # print("check ", x, y, z)
                else:
                    not_trapped.append([x,y,z])
            for x in range((nx//2)-1,-1,-1):
                if grid_3d[x][y][z] == test_side:
                    visited = []
                    if trapped(x,y,z,grid_3d,nx,ny,nz,visited,not_trapped,test_side):
                        interior_trapped.append([x,y,z])
                    else:
                        not_trapped.append([x,y,z])
                    # print("check ", x, y, z)
                else:
                    not_trapped.append([x,y,z])
        for y in range((ny//2)-1,-1,-1):
            for x in range(nx//2, nx):
                if grid_3d[x][y][z] == test_side:
                    visited = []
                    if trapped(x,y,z,grid_3d,nx,ny,nz,visited,not_trapped,test_side):
                        interior_trapped.append([x,y,z])
                    else:
                        not_trapped.append([x,y,z])
                    # print("check ", x, y, z)
                else:
                    not_trapped.append([x,y,z])
            for x in range((nx//2)-1,-1,-1):
                if grid_3d[x][y][z] == test_side:
                    visited = []
                    if trapped(x,y,z,grid_3d,nx,ny,nz,visited,not_trapped,test_side):
                        interior_trapped.append([x,y,z])
                    else:
                        not_trapped.append([x,y,z])
                    # print("check ", x, y, z)
                else:
                    not_trapped.append([x,y,z])

    return interior_trapped

def part2():

    cubes = []
    max_x = 0
    max_y = 0
    max_z = 0
    for input_line in input_array:
        splitcomma = input_line.split(",")
        x = int(splitcomma[0])
        y = int(splitcomma[1])
        z = int(splitcomma[2][:-1])
        cubes.append([x,y,z])
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        if z > max_z:
            max_z = z

    nx = max_x + 2
    ny = max_y + 2
    nz = max_z + 2
    print("grid_3d size: ", nx, ny, nz)
    grid_3d = np.zeros(shape=(nx,ny,nz), dtype=int)

    # Loop to add cubes to grid
    for cube in cubes:
        grid_3d[cube[0]][cube[1]][cube[2]] = 1


    # Work out the surface area from the initial calculation
    open_faces = calc_area(cubes, grid_3d, 0)

    # So the question seems to be to work out how many cubes of air (0)
    # are trapped inside the lava cubes (1).  So for every 0 test
    # whether there's a way out to the edge through other 0s

    # Ooh but also 1s could then be trapped inside the zeros... bloody hell.

    interior_trapped_areas = []

    finished = False
    count = 0

    while not finished:
        interior_trapped = calc_trapped(nx,ny,nz,grid_3d,0)

        if len(interior_trapped) == 0:
            finished = True
        else:
            # interior_area = calc_area(interior_trapped, grid_3d, 1)
            # print(interior_area)
            # interior_trapped_areas.append(interior_area)
            # Make a new grid from the trapped cubes!
            new_cubes = []
            max_x = 0
            max_y = 0
            max_z = 0
            for cube in interior_trapped:
                new_cubes.append(cube)
                if cube[0] > max_x:
                    max_x = cube[0]
                if cube[1] > max_y:
                    max_y = cube[1]
                if cube[2] > max_z:
                    max_z = cube[2]

            nx = max_x + 2
            ny = max_y + 2
            nz = max_z + 2
            print("next grid 3d size is ", nx, ny, nz)
            grid_3d = np.zeros(shape=(nx,ny,nz), dtype=int)

            for cube in new_cubes:
                grid_3d[cube[0]][cube[1]][cube[2]] = 1

            interior_area = calc_area(new_cubes, grid_3d, 0)
            print(interior_area, len(new_cubes), len(interior_trapped))
            print(new_cubes)
            interior_trapped_areas.append(interior_area)
            count += 1


    print(open_faces, interior_trapped_areas)

    # I think the answer is alternating minus plus along the trapped areas

    answer = open_faces

    for n in range(len(interior_trapped_areas)):
        if n % 2 == 0:
            answer -= interior_trapped_areas[n]
        else:
            answer += interior_trapped_areas[n]

    # Dammit, so the answer is somewhere in between open_faces - in_a[0] (2497) and
    # open_faces - in_a[0] + in_a[1] (2649)

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
