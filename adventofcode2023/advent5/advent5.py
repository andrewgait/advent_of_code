# Advent of code 2023, day 5

# open file
input = open("advent5_input.txt", "r")
# input = open("advent5_input_test.txt", "r")

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

    # seeds[0] = 89

    # # brute force loop for comparing test answers
    # for n in range(len(seeds)//2):
    #     start_seed = seeds[2*n]
    #     range_seed = seeds[2*n+1]
    #     # print(start_seed, range_seed)
    #     # print(map_seed(seed, maps[0]), " from ",  seed, maps[0])
    #     for seed in range(start_seed, start_seed+range_seed):
    #         for map in maps:
    #             seed = map_seed(seed, map)
    #
    #             # if (new_seed - start_seed) == range_seed:
    #             #     # no need to do anything
    #             #     start_seed = new_seed
    #             # else:
    #             #     # some point between start_seed and (start_seed + range_seed)
    #             #     # add a map to the end of maps...
    #             #     start_seed = new_seed
    #
    #         if seed < min_location:
    #             min_location = seed
    #
    # print("CHECK part 2 answer using brute force loop ", min_location)

    min_location = 999999999999999999999999

    # well this works with the test data but not the actual data
    # (one of the answers is suspiciously some orders of magnitude smaller than the others)

    for n in range(len(seeds)//2):
        start_seed = seeds[2*n]
        range_seed = seeds[2*n+1]
        # print(" ")
        # print(start_seed, range_seed)
        # print(map_seed(seed, maps[0]), " from ",  seed, maps[0])

        ranges = [[start_seed, range_seed]]
        for map in maps:

            # print("map ", map)
            # print("ranges ", ranges)

            # does the
            new_ranges = set()

            for my_range in ranges:
                new_seed = map_seed(my_range[0], map)
                new_seed_top = map_seed(my_range[0]+my_range[1]-1, map)
                if new_seed_top - new_seed == my_range[1]-1:
                    new_ranges.add((new_seed, new_seed_top-new_seed+1))
                    # print("new ranges: ", new_ranges)
                else:
                    # print("new seeds ", new_seed, new_seed_top)
                    # work out where the old range needs to split
                    for key, values in map.items():
                        # print(key, values)

                        # there are 4 scenarios:
                        # 1; the current key-values pair doesn't change the
                        #    range in which case we can just ignore it
                        #    (basically this was covered above)
                        # 2; the old seed (my_range[0]) falls between the
                        #    key and key + range (i.e. key + values[1])
                        if (my_range[0] >= key) and (my_range[0] < key + values[1]):
                            # the new ranges are therefore from
                            # new_seed to new_seed + (key+values[1]-my_range[0])
                            new_val_low = new_seed
                            new_val_midlow = new_seed + (key+values[1]-my_range[0]-1)

                            new_val_midtop = new_seed_top - ((my_range[0]+my_range[1])-(key+values[1])-1)
                            new_val_top = new_seed_top
                            # print("seed in range, low mid, mid top", new_val_low, new_val_midlow,
                            #       new_val_midtop, new_val_top)
                            new_ranges.add((new_val_low, new_val_midlow-new_val_low+1))
                            # and from new_seed + (key+values[1]-my_range[0]) to new_seed_top
                            new_ranges.add((new_val_midtop, new_val_top-new_val_midtop+1))
                        # 3; the old seed plus range (my_range[0] + my_range[1]) falls between
                        #    the key and key + range
                        elif (my_range[0]+my_range[1] >= key) and (my_range[0]+my_range[1] < key + values[1]):
                            # so the new ranges are from
                            # new_seed to key
                            new_val_low = new_seed
                            new_val_midlow = new_seed + (key-my_range[0]-1)
                            new_val_midtop = new_seed_top - (my_range[0]+my_range[1]-key-1)
                            new_val_top = new_seed_top
                            # print("top seed in range low mid, mid top", new_val_low, new_val_midlow,
                            #       new_val_midtop, new_val_top)
                            new_ranges.add((new_val_low, new_val_midlow-new_val_low+1))
                            # and key to my_range[0]+my_range[1]
                            new_ranges.add((new_val_midtop, new_val_top-new_val_midtop+1))
                        # 4; the new range is entirely contained in the old range
                        #    in which instance it splits into three pieces?
                        elif (my_range[0] < key) and (my_range[0]+my_range[1] >= key + values[1]):
                            # this splits into three bits, ouch
                            new_val_low = new_seed
                            new_val_high = new_seed_top
                            new_val_mid1low = map_seed(key-1, map)
                            new_val_mid1up = map_seed(key, map)
                            new_val_mid2low = map_seed(key+values[1]-1, map)
                            new_val_mid2up = map_seed(key+values[1], map)
                            new_ranges.add((new_val_low, new_val_mid1low-new_val_low+1))
                            new_ranges.add((new_val_mid1up, new_val_mid2low-new_val_mid1up+1))
                            new_ranges.add((new_val_mid2up, new_val_high-new_val_mid2up+1))

                    # new_ranges = list(new_ranges)
                    # print(new_ranges)

            ranges = list(new_ranges)

        print("test ranges ", ranges)

        # the answer is now (I think) the minimum of the start values in the ranges
        for my_range in ranges:
            if my_range[0] < min_location:
                min_location = my_range[0]

    answer = min_location

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())

# Code below works: credit to https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/5.py
# I might revisit my code above in light of this but not yet...

import sys
import re
from collections import defaultdict
D = open("advent5_input.txt").read().strip()
L = D.split('\n')

parts = D.split('\n\n')
seed, *others = parts
seed = [int(x) for x in seed.split(':')[1].split()]

class Function:
  def __init__(self, S):
    lines = S.split('\n')[1:] # throw away name
    # dst src sz
    self.tuples: list[tuple[int,int,int]] = [[int(x) for x in line.split()] for line in lines]
    #print(self.tuples)
  def apply_one(self, x: int) -> int:
    for (dst, src, sz) in self.tuples:
      if src<=x<src+sz:
        return x+dst-src
    return x

  # list of [start, end) ranges
  def apply_range(self, R):
    A = []
    for (dest, src, sz) in self.tuples:
      src_end = src+sz
      NR = []
      while R:
        # [st                                     ed)
        #          [src       src_end]
        # [BEFORE ][INTER            ][AFTER        )
        (st,ed) = R.pop()
        # (src,sz) might cut (st,ed)
        before = (st,min(ed,src))
        inter = (max(st, src), min(src_end, ed))
        after = (max(src_end, st), ed)
        if before[1]>before[0]:
          NR.append(before)
        if inter[1]>inter[0]:
          A.append((inter[0]-src+dest, inter[1]-src+dest))
        if after[1]>after[0]:
          NR.append(after)
      R = NR
    return A+R

Fs = [Function(s) for s in others]

def f(R, o):
  A = []
  for line in o:
    dest,src,sz = [int(x) for x in line.split()]
    src_end = src+sz

P1 = []
for x in seed:
  for f in Fs:
    x = f.apply_one(x)
  P1.append(x)
print(min(P1))

P2 = []
pairs = list(zip(seed[::2], seed[1::2]))
for st, sz in pairs:
  # inclusive on the left, exclusive on the right
  # e.g. [1,3) = [1,2]
  # length of [a,b) = b-a
  # [a,b) + [b,c) = [a,c)
  R = [(st, st+sz)]
  for f in Fs:
    R = f.apply_range(R)
  #print(len(R))
  P2.append(min(R)[0])
print("Part 2 again answer: ", min(P2))
