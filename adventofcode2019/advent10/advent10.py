# Advent of code, day 10
import math

# open file
input = open("advent10_input.txt", "r")
# input = open("advent10_test_input.txt", "r")
# input = open("advent10_test_input2.txt", "r")
# input = open("advent10_test_input3.txt", "r")
# input = open("advent10_test_input4.txt", "r")
# input = open("advent10_test_input5.txt", "r")

input_map = []
# read string into array
for line in input:
    input_line = []
    for i in range(len(line)-1): # -1 due to \n
        # . is 0, # is 1
        if line[i] == ".":
            input_line.append(0)
        elif line[i] == "#":
            input_line.append(1)

    input_map.append(input_line)

def print_map(input_map):
    print("\n")
    for j in range(len(input_map)):
        str = ""
        for i in range(len(input_map[j])):
            if input_map[j][i] == 0:
                str = str+"."
            elif input_map[j][i] == 1:
                str = str+"#"
        print(str)
    print("\n")

def get_factors(number):
    factors = []
    for i in range(1, number+1):
        if (number % i == 0):
            factors.append(i)
    return factors

def lowest_factor(x, y):
    if x == y:
        return x

    x_factors = get_factors(x)
    y_factors = get_factors(y)

    possible_factors = []
    for i in range(len(x_factors)):
        for j in range(len(y_factors)):
            if x_factors[i] == y_factors[j]:
                possible_factors.append(x_factors[i])

    return max(possible_factors)

def visible_from(input_map, base_x, base_y, x, y):
    # is (x,y) visible from (base_x,base_y)
    rel_x = x-base_x
    rel_y = y-base_y

    if rel_x == 0:
        # check all points between rel_y and base_y
        if y < base_y:
            for j in range(y+1, base_y):
                if input_map[j][x] == 1:
                    return False
            return True
        else:
            for j in range(base_y+1, y):
                if input_map[j][x] == 1:
                    return False
            return True
    elif rel_y == 0:
        # check all points between rel_x and base_x
        if x < base_x:
            for i in range(x+1, base_x):
                if input_map[y][i] == 1:
                    return False
            return True
        else:
            for i in range(base_x+1, x):
                if input_map[y][i] == 1:
                    return False
            return True
    else:
        # work out the lowest common factor of rel_x and rel_y
        factor = lowest_factor(abs(rel_x), abs(rel_y))
        if factor == 1:
            return True
        else:
            coords_to_test = []
            n_coords = factor
            for n in range(1, n_coords):
                x_coord = base_x + (rel_x//factor)*n
                y_coord = base_y + (rel_y//factor)*n
                coords_to_test.append([x_coord, y_coord])

            for n in range(len(coords_to_test)):
                j = coords_to_test[n][1]
                i = coords_to_test[n][0]
                if input_map[j][i] == 1:
                    return False

            return True

    # if somehow you're out here then return True?
    return True

def get_asteroids(input_map, i, j):
    # loop over all other positions in map
    asteroids = []
    count_asteroids = 0
    for n in range(len(input_map)):
        for m in range(len(input_map[n])):
            # don't look where you currently are
            if ((n==i) and (m==j)):
                dummy = True
            else:
                if (input_map[m][n] == 1):
                    if visible_from(input_map, i, j, n, m):
                        count_asteroids += 1
                        asteroids.append([n, m])

    return count_asteroids, asteroids

def part1(input_map):

    max_asteroids = 0
    for j in range(len(input_map)):
        for i in range(len(input_map[j])):
            # if at an asteroid
            count_asteroids = 0
            if (input_map[j][i]==1):

                count_asteroids, _asteroids = get_asteroids(input_map, i, j)

            if count_asteroids > max_asteroids:
                max_asteroids = count_asteroids
                answer = [max_asteroids, (i, j)]

    return answer

def part2(input_map, laser_station):

    count_asteroids, asteroids = get_asteroids(
        input_map, laser_station[0], laser_station[1])

    # 200 is less than the size of the asteroids viewed from the laser
    # (in both big cases), so we don't need to worry about what happens
    # on later spins; the way to do it, though, would just be to update
    # the map to remove an asteroid when it counts it, and then to
    # call get_asteroids again if you reach the end of the first list

    # Reorder the array to match what the laser will see using angles!
    first_asteroid = 0
    angles = []
    for a in range(len(asteroids)):
        adj = asteroids[a][0] - laser_station[0]
        opp = laser_station[1] - asteroids[a][1]
        angle = math.atan2(adj, opp)
        if angle < 0.0:
            angle = angle + 2*math.pi
        angles.append([angle, asteroids[a], a])

    angles_sorted = sorted(angles, key=lambda x: x[0])

#     print(angles_sorted)
#     print(angles_sorted[1])
#     print(angles_sorted[2])
#     print(angles_sorted[9])
#     print(angles_sorted[49])
#     print(angles_sorted[99])
#     print(angles_sorted[199])
    answer = angles_sorted[199][1][0]*100 + angles_sorted[199][1][1]

    return answer

print_map(input_map)

part1_answer = part1(input_map)
print("Part 1 answer: ", part1_answer)
print("Part 2 answer: ", part2(input_map, part1_answer[1]))
