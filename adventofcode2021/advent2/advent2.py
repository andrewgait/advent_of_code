# Advent of code, day 2

# open file
input = open("advent2_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    answer = 0
    horizontal = 0
    depth = 0
    n_inputs = len(input_array)
    for n in range(n_inputs):
        commands = input_array[n].split(" ")
        if commands[0] == "forward":
            horizontal += int(commands[1])
        elif commands[0] == "down":
            depth += int(commands[1])
        elif commands[0] == "up":
            depth -= int(commands[1])

    print(horizontal, depth)
    answer = horizontal * depth

    return answer

def part2():

    answer = 0
    horizontal = 0
    depth = 0
    aim = 0
    n_inputs = len(input_array)
    for n in range(n_inputs):
        commands = input_array[n].split(" ")
        if commands[0] == "forward":
            horizontal += int(commands[1])
            depth += aim * int(commands[1])
        elif commands[0] == "down":
            aim += int(commands[1])
        elif commands[0] == "up":
            aim -= int(commands[1])

    print(horizontal, depth)
    answer = horizontal * depth

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
