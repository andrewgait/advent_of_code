# Advent of code, day 12
import copy

# open file
input = open("advent12_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)


def get_path(caves, current, path, paths):
    for cave in caves[current]:
        new_path = copy.deepcopy(path)
        if cave == "end":
            new_path.append(cave)
            paths.append(new_path)
        elif cave.islower():
            if cave in path:
                paths.append(new_path)
            else:
                new_path.append(cave)
                get_path(caves, cave, new_path, paths)
        else:
            new_path.append(cave)
            get_path(caves, cave, new_path, paths)


def get_path_part2(caves, current, path, paths):
    for cave in caves[current]:
        new_path = copy.deepcopy(path)
        if cave == "end":
            new_path.append(cave)
            paths.append(new_path)
        elif cave.islower():
            if cave in path:
                if cave == "start":
                    paths.append(new_path)
                else:
                    # count how many times a lower-case cave is in path
                    n_count = 0
                    twice = False
                    # list lower-case caves
                    lc_caves = []
                    for cave2 in path:
                        if cave2.islower():
                            lc_caves.append(cave2)
                    for lc_cave in lc_caves:
                        n_count = 0
                        for cave3 in path:
                            if lc_cave == cave3:
                                n_count += 1
                        if n_count > 1:
                            twice = True
                    if twice:
                        paths.append(new_path)
                    else:
                        new_path.append(cave)
                        get_path_part2(caves, cave, new_path, paths)
            else:
                new_path.append(cave)
                get_path_part2(caves, cave, new_path, paths)
        else:
            new_path.append(cave)
            get_path_part2(caves, cave, new_path, paths)

def part1():

    answer = 0

    # make a dict for each cave where the key is the cave and the value(s)
    # the cave(s) it connects to
    caves = {}

    for n in range(len(input_array)):
        splitdash = input_array[n].split("-")
        first = splitdash[0]
        second = splitdash[1][0:-1]
        print(first, second)
        if first in caves.keys():
            caves[first].append(second)
        else:
            caves[first] = [second]
        if second in caves.keys():
            caves[second].append(first)
        else:
            caves[second] = [first]

    print(caves)

    path = ["start"]

    current = "start"

    paths = []
    get_path(caves, current, path, paths)

    pathset = set(tuple(path) for path in paths)

    n_end = 0
    for path in pathset:
        if path[-1] == "end":
            # print(path)
            n_end += 1


    answer = n_end

    return answer

def part2():

    answer = 0

    # make a dict for each cave where the key is the cave and the value(s)
    # the cave(s) it connects to
    caves = {}

    for n in range(len(input_array)):
        splitdash = input_array[n].split("-")
        first = splitdash[0]
        second = splitdash[1][0:-1]
        print(first, second)
        if first in caves.keys():
            caves[first].append(second)
        else:
            caves[first] = [second]
        if second in caves.keys():
            caves[second].append(first)
        else:
            caves[second] = [first]

    print(caves)

    path = ["start"]

    current = "start"

    paths = []
    get_path_part2(caves, current, path, paths)

    pathset = set(tuple(path) for path in paths)

    n_end = 0
    for path in pathset:
        if path[-1] == "end":
            # print(path)
            n_end += 1


    answer = n_end

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
