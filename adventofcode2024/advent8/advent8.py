# Advent of code 2024, day 8

# open file
input = open("advent8_input.txt", "r")
# input = open("advent8_test_input1.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    antennas = {}

    width = len(input_array[0])-1
    height = 0
    for input in input_array:
        for n in range(width):
            val = input[n]
            if val != ".":
                if val not in antennas.keys():
                    antennas[val] = [(n,height)]
                else:
                    antennas[val].append((n,height))

        height += 1

    print(width, height)

    print(antennas)

    # Use a set to prevent duplications
    antinodes = set()

    # For each key in dict, make antinodes from pairs

    for antenna_key in antennas.keys():
        ant = antennas[antenna_key]
        n_antennas = len(ant)
        if n_antennas > 1:
            for na in range(n_antennas):
                for nb in range(n_antennas):
                    # Don't use the same antenna for comparison
                    if na != nb:
                        ant1 = ant[na]
                        ant2 = ant[nb]
                        diff = (ant2[0] - ant1[0], ant2[1]-ant1[1])
                        # print(ant1, ant2, diff)
                        test_up = (ant2[0] + diff[0], ant2[1] + diff[1])
                        if (0 <= test_up[0] < width) and (0 <= test_up[1] < height):
                            antinodes.add(test_up)
                        test_down = (ant1[0] - diff[0], ant1[1] - diff[1])
                        if (0 <= test_down[0] < width) and (0 <= test_down[1] < height):
                            antinodes.add(test_down)


    print(antinodes)

    answer = len(antinodes)

    return answer

def part2():

    antennas = {}

    width = len(input_array[0])-1
    height = 0
    for input in input_array:
        for n in range(width):
            val = input[n]
            if val != ".":
                if val not in antennas.keys():
                    antennas[val] = [(n,height)]
                else:
                    antennas[val].append((n,height))

        height += 1

    print(width, height)

    print(antennas)

    # Use a set to prevent duplications
    antinodes = set()

    # For each key in dict, make antinodes from pairs

    for antenna_key in antennas.keys():
        ant = antennas[antenna_key]
        n_antennas = len(ant)
        if n_antennas > 1:
            for na in range(n_antennas):
                for nb in range(n_antennas):
                    # Don't use the same antenna for comparison
                    if na != nb:
                        ant1 = ant[na]
                        ant2 = ant[nb]
                        diff = (ant2[0] - ant1[0], ant2[1]-ant1[1])
                        # print(ant1, ant2, diff)
                        antinodes.add(ant1)
                        antinodes.add(ant2)
                        # keep adding nodes until you get past the height / width
                        test_up = (ant2[0] + diff[0], ant2[1] + diff[1])
                        while (0 <= test_up[0] < width) and (0 <= test_up[1] < height):
                            antinodes.add(test_up)
                            test_up = (test_up[0] + diff[0], test_up[1] + diff[1])

                        test_down = (ant1[0] - diff[0], ant1[1] - diff[1])
                        while (0 <= test_down[0] < width) and (0 <= test_down[1] < height):
                            antinodes.add(test_down)
                            test_down = (test_down[0] - diff[0], test_down[1] - diff[1])


    print(antinodes)

    for w in range(width):
        for h in range(height):
            line = ""
            if (w,h) in antinodes:
                line += "#"
            else:
                line += "."

    answer = len(antinodes)

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
