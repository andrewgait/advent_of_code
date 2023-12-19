# Advent of code 2023, day 18
import numpy as np
from matplotlib.path import Path
from shapely.geometry import Polygon, Point
import cv2

# open file
input = open("advent18_input.txt", "r")
# input = open("advent18_input_test.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

symbol_dict = {0: ".", 1: "#"}
print(symbol_dict[0])

def print_map(map):
    ny = len(map)
    nx = len(map[0])
    for y in range(ny):
        print_line = ""
        for x in range(nx):
            print_line += symbol_dict[map[y][x]]
        print(print_line)
    print(" ")


def part1():

    path = [[0,0]]
    offset = 0
    xpoints = [0 + offset]
    ypoints = [0 + offset]

    for input in input_array:
        splitspace = input.split(" ")
        direction = splitspace[0]
        n_steps = int(splitspace[1])

        currently_at = path[-1]
        print(currently_at, direction, n_steps)

        for n in range(n_steps):
            if direction == "R":
                path.append([currently_at[0]+1+n, currently_at[1]])
            elif direction == "D":
                path.append([currently_at[0], currently_at[1]+1+n])
            elif direction == "L":
                path.append([currently_at[0]-1-n, currently_at[1]])
            elif direction == "U":
                path.append([currently_at[0], currently_at[1]-1-n])

        xpoints.append(path[-1][0] + offset)
        ypoints.append(path[-1][1] + offset)

    print(path)
    min_x = 100000000
    min_y = 100000000
    max_x = -100000000
    max_y = -100000000
    for p in path:
        if p[0] > max_x:
            max_x = p[0]
        if p[1] > max_y:
            max_y = p[1]
        if p[0] < min_x:
            min_x = p[0]
        if p[1] < min_y:
            min_y = p[1]

    print(max_x, max_y)
    print(min_x, min_y)

    nx = max_x - min_x + 1
    ny = max_y - min_y + 1
    area_map = np.zeros((ny,nx))
    print(area_map)
    new_path = []
    for p in path[1:]:
        area_map[p[1]+abs(min_y)][p[0]+abs(min_x)] = 1
        new_path.append([p[0]+abs(min_x), p[1]+abs(min_y)])

    print_map(area_map)

    test_area_map = np.zeros((ny,nx))

    polygonpath = Path(new_path)

    newpolygonpath = Polygon(new_path)
    # now fill in the map
    # Any . on top or bottom row is outside so just ignore
    for y in range(1,ny-1):
        for x in range(1,nx-1):
            if polygonpath.contains_point([x,y]):
                area_map[y][x] = 1
            if newpolygonpath.contains(Point(x,y)):
                test_area_map[y][x] = 1

    print_map(area_map)

    print(xpoints, ypoints)

    print("test polygon area calculation in part 1: ", polygon_area(np.array(xpoints), np.array(ypoints)))
    # print("test shapely polygon area calculation in part 1: ", Polygon(new_path).area)
    # print("test shapely polygon area calculation in part 1 (old): ", Polygon(path).area)
    print("shoelace direct ", shoelace_formula(path))
    print("shoelace reverse ", shoelace_formula(list(reversed(path))))

    print_map(test_area_map)

    area, perimeter = shoelace_formula(list(reversed(path)))

    answer = area + int(perimeter/2) + 1

    return answer


def polygon_area(x,y):
    x1 = x - x.mean()
    y1 = y - y.mean()
    correction = x1[-1] * y1[0] - y1[-1] * x1[0]
    main_area = np.dot(x1[:-1], y1[1:]) - np.dot(y1[:-1], x1[1:])
    # main_area = np.dot(x1, y1) - np.dot(y1, x1)
    return 0.5*np.abs(main_area + correction)


def shoelace_formula(points):
    area = 0
    perimeter = 0
    q = points[-1]
    for p in points:
        area += p[0]*q[1] - p[1]*q[0]
        perimeter += abs((p[0]-q[0])+(p[1]-q[1])*1j)
        q = p
    return int(area * 0.5), perimeter


def part2():

    path = [[0,0]]
    points = [[0,0]]
    xpoints = [0]
    ypoints = [0]

    for input in input_array:
        splitspace = input.split(" ")
        direction = splitspace[2][-3]
        n_steps = int(splitspace[2][2:-3], 16)

        currently_at = points[-1]
        print(currently_at, direction, n_steps)


        if direction == "0":
            points.append([currently_at[0]+n_steps, currently_at[1]])
        elif direction == "1":
            points.append([currently_at[0], currently_at[1]+n_steps])
        elif direction == "2":
            points.append([currently_at[0]-n_steps, currently_at[1]])
        elif direction == "3":
            points.append([currently_at[0], currently_at[1]-n_steps])
        xpoints.append(points[-1][0])
        ypoints.append(points[-1][1])


    print(len(points))

    area, perimeter = shoelace_formula(list(reversed(points)))

    # Some trial and error based on the test input data suggests
    # that for some reason the answer is area + perimeter/2 + 1, but why?

    answer = area + int(perimeter/2) + 1

    return answer


print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
