# Advent of code 2023, day 5

# open file
# input = open("advent5_input.txt", "r")
input = open("advent5_input_test.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def map_seed(seed, map):
    return_seed = seed
    for key, value in map.items():
        source_start = key
        dest_start = value[0]
        value_range = value[1]
        if seed >= source_start and seed < source_start + value_range:
            return_seed = dest_start + (seed - source_start)

    return return_seed


def part1():

    # first line contains the starting seeds
    seedsplit = input_array[0][:-1].split(" ")
    seeds = []
    for n in range(1, len(seedsplit)):
        seeds.append(int(seedsplit[n]))

    print(seeds)

    maps = []
    n = 1
    for input in input_array[2:]:
        if input != "\n":
            # Do stuff to make map
            if input[-5:-1] == "map:":
                # print("Starting map for ", input)
                map_dict = {}
                # maps.append(map_dict)
            else:
                # read in numbers
                key_values = input[:-1].split(" ")
                map_dict[int(key_values[1])] = [int(key_values[0]),
                                                int(key_values[2])]

        else:
            maps.append(map_dict)


    print(maps)

    test_seed = 49
    print("seed ", test_seed, " map 0 ", map_seed(test_seed, maps[0]))

    print(len(maps))

    min_location = 99999999999999999999999
    for seed in seeds:
        # print(map_seed(seed, maps[0]), " from ",  seed, maps[0])
        for map in maps:
            seed = map_seed(seed, map)

        if seed < min_location:
            min_location = seed

    answer = min_location

    return answer


def part2():

    # first line contains the starting seeds
    seedsplit = input_array[0][:-1].split(" ")
    seeds = []
    for n in range(1, len(seedsplit)):
        seeds.append(int(seedsplit[n]))

    print(seeds)

    maps = []
    n = 1
    for input in input_array[2:]:
        if input != "\n":
            # Do stuff to make map
            if input[-5:-1] == "map:":
                # print("Starting map for ", input)
                map_dict = {}
                # maps.append(map_dict)
            else:
                # read in numbers
                key_values = input[:-1].split(" ")
                map_dict[int(key_values[1])] = [int(key_values[0]),
                                                int(key_values[2])]

        else:
            maps.append(map_dict)


    print(maps)

    test_seed = 49
    print("seed ", test_seed, " map 0 ", map_seed(test_seed, maps[0]))

    print(len(maps))

    min_location = 9999999999999999999
    # In this case the seeds array also has ranges
    # Given the puzzle input it clearly isn't practical to loop
    # over every single seed that can be calculated from these ranges,
    # but the starting seed for the minimum of location could come
    # from any of them

    # So I suppose the answer must lie in calculating where the two endpoints
    # go each time and then bifurcating if the endpoints aren't separated by
    # by the range between the two initial endpoints?

    for n in range(len(seeds)//2):
        start_seed = seeds[2*n]
        range_seed = seeds[2*n+1]
        # print(start_seed, range_seed)
        # print(map_seed(seed, maps[0]), " from ",  seed, maps[0])
        for map in maps:
            seed = map_seed(start_seed, map)

            if (seed - start_seed) == range_seed:
                start_seed = seed

        if seed < min_location:
            min_location = seed

    answer = min_location

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
