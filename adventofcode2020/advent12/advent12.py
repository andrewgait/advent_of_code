# Advent of code, day 12

# open file
input = open("advent12_input.txt", "r")
# input = open("advent12_test_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def go_east(coords, value):
    coords[0] += value
    return coords

def go_west(coords, value):
    coords[0] -= value
    return coords

def go_north(coords, value):
    coords[1] += value
    return coords

def go_south(coords, value):
    coords[1] -= value
    return coords

def part1():

    answer = 0
    compass = ["N", "E", "S", "W"]

    coords = [0, 0]
    facing = "E"
    facing_deg = 90
    n = len(input_array)
    for i in range(n):
        action = input_array[i][0]
        value = int(input_array[i][1:-1])
        if action == "N":
            go_north(coords, value)
        elif action == "S":
            go_south(coords, value)
        elif action == "E":
            go_east(coords, value)
        elif action == "W":
            go_west(coords, value)
        elif action == "F":
            if facing == "N":
                go_north(coords, value)
            elif facing == "S":
                go_south(coords, value)
            elif facing == "W":
                go_west(coords, value)
            elif facing == "E":
                go_east(coords, value)
        elif action == "R":
            facing_deg += value
            facing_deg = facing_deg % 360
            facing = compass[facing_deg // 90]
        elif action == "L":
            facing_deg -= value
            facing_deg = facing_deg % 360
            facing = compass[facing_deg // 90]

#         print(action, value, facing, coords)


    answer = abs(coords[0]) + abs(coords[1])

    return answer

def part2():

    answer = 0

    n = len(input_array)
    waypoint_coords = [10, 1]
    ship_coords = [0, 0]
    for i in range(n):
        action = input_array[i][0]
        value = int(input_array[i][1:-1])
        if action == "N":
            go_north(waypoint_coords, value)
        elif action == "S":
            go_south(waypoint_coords, value)
        elif action == "E":
            go_east(waypoint_coords, value)
        elif action == "W":
            go_west(waypoint_coords, value)
        elif action == "F":
            ship_coords[0] += waypoint_coords[0] * value
            ship_coords[1] += waypoint_coords[1] * value
        elif action == "R":
            orig_coords = []
            orig_coords.append(waypoint_coords[0])
            orig_coords.append(waypoint_coords[1])
            if value == 90:
                waypoint_coords[0] = orig_coords[1]
                waypoint_coords[1] = -orig_coords[0]
            elif value == 180:
                waypoint_coords[0] = -orig_coords[0]
                waypoint_coords[1] = -orig_coords[1]
            elif value == 270:
                waypoint_coords[0] = -orig_coords[1]
                waypoint_coords[1] = orig_coords[0]
            else:
                print("unexpected value when turning R")
        elif action == "L":
            orig_coords = []
            orig_coords.append(waypoint_coords[0])
            orig_coords.append(waypoint_coords[1])
            if value == 90:
                waypoint_coords[0] = -orig_coords[1]
                waypoint_coords[1] = orig_coords[0]
            elif value == 180:
                waypoint_coords[0] = -orig_coords[0]
                waypoint_coords[1] = -orig_coords[1]
            elif value == 270:
                waypoint_coords[0] = orig_coords[1]
                waypoint_coords[1] = -orig_coords[0]
            else:
                print("unexpected value when turning L")

#         print(action, value, ship_coords, waypoint_coords)

    answer = abs(ship_coords[0]) + abs(ship_coords[1])

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
