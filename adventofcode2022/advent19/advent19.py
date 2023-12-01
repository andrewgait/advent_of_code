# Advent of code 2022, day 19

# open file
input = open("advent19_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    blueprint_ID = []
    ore_robot_cost = [] # ore
    clay_robot_cost = [] # ore
    obsidian_robot_costs = [] # ore, clay
    geode_robot_costs = [] # ore, obsidian

    for input_line in input_array:
        splitspace = input_line.split(" ")
        blueprint_ID.append(int(splitspace[1][:-1]))
        ore_robot_cost.append(int(splitspace[6]))
        clay_robot_cost.append(int(splitspace[12]))
        obsidian_robot_costs.append([int(splitspace[18]),
                                     int(splitspace[21])])
        geode_robot_costs.append([int(splitspace[27]),
                                  int(splitspace[30])])

    max_geode = 0
    ore = 0
    clay = 0
    obsidian = 0
    geode = 0
    n_ore_robot = 1
    n_clay_robot = 0
    n_obisidian_robot = 0
    n_geode_robot = 0

    answer = max_geode

    return answer

def part2():

    answer = 0

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
