# Advent of code 2022, day 15
import numpy as np

# open file
input = open("advent15_input.txt", "r")
# input = open("advent15_test_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def manhattan_dist(A, B):
    return abs(A[0]-B[0]) + abs(A[1]-B[1])


def make_arrays(input_array):
    sensors = []
    beacons = []
    manhattans = []

    for input_line in input_array:
        splitspace = input_line.split(" ")
        sensor = [int(splitspace[2][2:-1]), int(splitspace[3][2:-1])]
        beacon = [int(splitspace[8][2:-1]), int(splitspace[9][2:-1])]

        sensors.append(sensor)
        beacons.append(beacon)
        manhattans.append(manhattan_dist(sensor, beacon))

    return sensors, beacons, manhattans

def test_row(y, sensors, beacons, manhattans, include_beacons):

    set_x = set()

    for n in range(len(sensors)):
        # print(sensors[n], beacons[n], manhattans[n])
        for x in range(sensors[n][0]-manhattans[n],sensors[n][0]+manhattans[n]+1):
            if (manhattan_dist(
                [x,y], [sensors[n][0],sensors[n][1]]) <= manhattans[n]):
                set_x.add(x)

    if not include_beacons:
        for n in range(len(beacons)):
            # print("beacon ", beacons[n])
            if (beacons[n][1] == y) and (beacons[n][0] in set_x):
                set_x.remove(beacons[n][0])
                # row_y[beacons[n][0]-min_x-10000000] = 0

    return len(set_x), set_x

def test_row_p2(y, coord_size, sensors, beacons, manhattans, include_beacons):

    set_x = set()

    for x in range(coord_size):
        for n in range(len(sensors)):
            if (manhattan_dist(
                [x,y], [sensors[n][0],sensors[n][1]]) <= manhattans[n]):
                set_x.add(x)

    if not include_beacons:
        for n in range(len(beacons)):
            # print("beacon ", beacons[n])
            if (beacons[n][1] == y) and (beacons[n][0] in set_x):
                set_x.remove(beacons[n][0])
                # row_y[beacons[n][0]-min_x-10000000] = 0

    return len(set_x), set_x

def part1():

    print("test manhattan (0,2) (3,1)", manhattan_dist([0,2], [3,1]))

    sensors, beacons, manhattans = make_arrays(input_array)

    include_beacons = True # False
    # answer, set_x = test_row(10, sensors, beacons, manhattans, include_beacons)
    answer, set_x = test_row(2000000, sensors, beacons, manhattans, include_beacons)

    return answer

def part2():

    sensors, beacons, manhattans = make_arrays(input_array)

    # After reading the solution thread for some hints, it seems that
    # searching sensor areas, and then if inside moving to the next x
    # point outside the sensor area that you are currently inside;
    # or moving to the next row if going beyond the search coordinate
    # this is still quite slow but it gets the right answer.
    # I'm guessing that there might be some way of doing a y search too.
    coord_size = 4000000
    # coord_size = 20

    x = 0
    y = 0
    inside = True
    while inside:
        # print("x, y is ", x, y)
        inside = False
        for n in range(len(sensors)):
            sensor_x = sensors[n][0]
            sensor_y = sensors[n][1]
            manh = manhattans[n]

            if manhattan_dist([x,y], [sensor_x,sensor_y]) <= manh:
                inside = True

                # move the coordinate to the next x position
                if x <= sensor_x:
                    x += (sensor_x-x) + (manh-abs(sensor_y-y)) + 1
                else:
                    x += (manh - abs(sensor_y-y) - (x - sensor_x)) + 1

                if x >= coord_size:
                    y += 1
                    x = 0


    answer = (x * 4000000) + y

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
