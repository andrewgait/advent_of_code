# Advent of code 2023, day 8
import math

# open file
input = open("advent8_input.txt", "r")
# input = open("advent8_input_test.txt", "r")
# input = open("advent8_input_test2.txt", "r")
# input = open("advent8_input_test_part2.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    # First line is instructions
    lr_instructions = input_array[0][:-1]
    n_inst = len(lr_instructions)

    direction_dict = {}
    # This dictionary has key given by the left value of the input, then (left, right)

    for input in input_array[2:]:
        direction_dict[input[0:3]] = [input[7:10], input[12:15]]

    print(direction_dict)

    # Start at AAA
    inst = "AAA"

    n = 0
    while inst != "ZZZ":
        lr = lr_instructions[n % n_inst]

        if lr == "L":
            inst = direction_dict[inst][0]
        else:
            inst = direction_dict[inst][1]
        n += 1

    answer = n

    return answer

    # return 0


def part2():

    # First line is instructions
    lr_instructions = input_array[0][:-1]
    n_inst = len(lr_instructions)

    direction_dict = {}
    # This dictionary has key given by the left value of the input, then (left, right)

    for input in input_array[2:]:
        direction_dict[input[0:3]] = [input[7:10], input[12:15]]

    print(direction_dict)

    # Start at every instruction that ends in an A
    insts = []
    for key in direction_dict.keys():
        if key[2] == "A":
            insts.append(key)

    n_insts = len(insts)
    print(n_insts, insts)

    # Do each case from the instructions individually and then multiply
    count_insts = []

    for inst in insts:
        n = 0

        end_in_Z = False
        while (inst[2] != "Z"):
            lr = lr_instructions[n % n_inst]

            if lr == "L":
                inst = direction_dict[inst][0]
            else:
                inst = direction_dict[inst][1]

            n += 1

        count_insts.append(n)

    print(count_insts)
    # Bit of a cheat because I know I have 6 ending in A
    answer = math.lcm(count_insts[0], count_insts[1], count_insts[2], count_insts[3],
                      count_insts[4], count_insts[5])

    print(answer)

    # Oh wait, LCM is commutative...
    answer = 1
    for count_inst in count_insts:
        answer = math.lcm(answer, count_inst)

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
