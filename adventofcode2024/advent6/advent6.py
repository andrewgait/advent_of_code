# Advent of code 2024, day 6

# open file
input = open("advent6_input.txt", "r")
# input = open("advent6_test_input1.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def get_guard_path(guard_loc, guard_dirn, lab_map, height, width):

    # Set a variable for if the guard gets stuck
    stuck = False

    # height = len(lab_map)
    # width = len(lab_map[0])-1

    guard_visits = set()
    guard_visits_n = {}

    guard_visits.add((guard_loc[0],guard_loc[1]))

    answer = 0
    on_map = True
    while on_map:
        # answer += 1
        gh = guard_loc[0]
        gw = guard_loc[1]
        if (gh,gw) in guard_visits_n.keys():
            guard_visits_n[(gh,gw)] += 1
            # I think if you've gone through somewhere 4 times then you're guaranteed to be stuck?
            # (Remembering that when you get somewhere and turn that uses 2 steps)
            if guard_visits_n[(gh,gw)] == 8:
                stuck = True
                on_map = False
        else:
            guard_visits_n[(gh,gw)] = 1

        if guard_dirn == "up":
            if gh == 0:
                on_map = False
            elif lab_map[gh-1][gw] == "#":
                guard_dirn = "right"
            else:
                guard_loc[0] = gh - 1
                guard_visits.add((guard_loc[0],guard_loc[1]))
        elif guard_dirn == "right":
            if gw == width-1:
                on_map = False
            elif lab_map[gh][gw+1] == "#":
                guard_dirn = "down"
            else:
                guard_loc[1] = gw + 1
                guard_visits.add((guard_loc[0],guard_loc[1]))
        elif guard_dirn == "down":
            if gh == height-1:
                on_map = False
            elif lab_map[gh+1][gw] == "#":
                guard_dirn = "left"
            else:
                guard_loc[0] = gh + 1
                guard_visits.add((guard_loc[0],guard_loc[1]))
        elif guard_dirn == "left":
            if gw == 0:
                on_map = False
            elif lab_map[gh][gw-1] == "#":
                guard_dirn = "up"
            else:
                guard_loc[1] = gw - 1
                guard_visits.add((guard_loc[0],guard_loc[1]))

    return guard_visits, stuck


def part1():

    lab_map = input_array

    height = len(lab_map)
    width = len(lab_map[0])-1

    guard_loc = []
    guard_dirn = "up"

    for h in range(height):
        for w in range(width):
            if lab_map[h][w] == "^":
                guard_loc = [h,w]

    print(guard_loc)

    guard_visits, stuck = get_guard_path(guard_loc, guard_dirn, lab_map, height, width)

    print(stuck)
    answer = len(guard_visits)

    return answer

def part2():

    #
    lab_map = []

    for input in input_array:
        lab_map_line = []
        for n in range(len(input)-1):
            lab_map_line.append(input[n])
        lab_map.append(lab_map_line)

    print(lab_map)

    height = len(lab_map)
    width = len(lab_map[0])

    guard_loc = []
    guard_dirn = "up"

    for hh in range(height):
        for ww in range(width):
            if lab_map[hh][ww] == "^":
                guard_loc = [hh,ww]

    print(guard_loc)

    answer = 0

    # This is quite slow (roughly a minute to run) but it works
    for h in range(height):
        for w in range(width):
            if lab_map[h][w] == ".":
                # Make sure guard position and direction are correct at the start of each check
                guard_dirn = "up"
                for hh in range(height):
                    for ww in range(width):
                        if lab_map[hh][ww] == "^":
                            guard_loc = [hh,ww]
                lab_map[h][w] = "#"
                guard_visits, stuck = get_guard_path(guard_loc, guard_dirn, lab_map, height, width)
                if stuck:
                    answer += 1
                lab_map[h][w] = "."


    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
