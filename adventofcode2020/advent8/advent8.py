# Advent of code, day 8

# open file
input = open("advent8_input.txt", "r")
# input = open("advent8_test_input.txt", "r")
# input = open("advent8_test_input2.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def get_accumulated_value(input_array):

    answer = 0
    terminated = False
    n = len(input_array)

    instruction_visited = []
    for i in range(n):
        instruction_visited.append(False)

    readline = 0
    repeated = False

    while (not repeated or terminated):
        splitspace = input_array[readline].split(" ")
        value = int(splitspace[1][:-1])
        if splitspace[0] == "acc":
            answer += value
            readline += 1
        elif splitspace[0] == "jmp":
            readline += value
        elif splitspace[0] == "nop":
            readline += 1

        if readline >= n:
            terminated = True
            break

        if instruction_visited[readline]:
            repeated = True
        else:
            instruction_visited[readline] = True


    return answer, terminated

def part1():

    answer, terminated = get_accumulated_value(input_array)

    return answer

def part2():

    answer = 0
    terminated = False

    # Loop over the size of the full array
    n = len(input_array)
    for i in range(n):
        # Make a copy of the input array
        input_array_copy = []
        for j in range(n):
            input_array_copy.append(input_array[j])

        # Change the current line if it's nop or jmp
        splitspace = input_array[i].split(" ")
        if splitspace[0] == "jmp":
            input_array_copy[i] = input_array[i].replace("jmp", "nop")
        elif splitspace[0] == "nop":
            input_array_copy[i] = input_array[i].replace("nop", "jmp")

        # run the instructions with this set
        answer, terminated = get_accumulated_value(input_array_copy)

        # break when a program terminates correctly
        if terminated:
            break


    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
