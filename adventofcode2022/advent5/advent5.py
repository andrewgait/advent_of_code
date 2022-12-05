# Advent of code 2022, day 5

# open file
input = open("advent5_input.txt", "r")
# input = open("advent5_test_input1.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    cratespic = []
    movelist = []

    pic = True
    for input_line in input_array:
        if input_line == "\n":
            pic = False
            continue

        if pic:
            cratespic.append(input_line)
        else:
            movelist.append(input_line)

    n_stack = int(cratespic[-1][-2])
    # print(n_stack)

    cratestacks = []
    for n in range(n_stack):
        cratestacks.append([])
    for crates in cratespic:
        for n in range(len(crates)//4):
            if crates[n*4] != " ":
                cratestacks[n].append(crates[n*4+1])

    # print(cratestacks)

    # max_stack_size = 0
    for move in movelist:
        splitspace = move.split(" ")
        n_to_move = int(splitspace[1])
        move_from = int(splitspace[3])
        move_to = int(splitspace[5])
        # print(n_to_move, move_from, move_to)

        for n in range(n_to_move):
            move_crate = cratestacks[move_from-1].pop(0)
            cratestacks[move_to-1].insert(0, move_crate)

        # print(cratestacks)
    #     for n in range(n_stack):
    #         if len(cratestacks[n]) > max_stack_size:
    #                max_stack_size = len(cratestacks[n])

    # print("max stack ", max_stack_size)
    answer = ""

    for n in range(n_stack):
        answer += cratestacks[n][0]

    return answer

def part2():

    cratespic = []
    movelist = []

    pic = True
    for input_line in input_array:
        if input_line == "\n":
            pic = False
            continue

        if pic:
            cratespic.append(input_line)
        else:
            movelist.append(input_line)

    n_stack = int(cratespic[-1][-2])
    # print(n_stack)

    cratestacks = []
    for n in range(n_stack):
        cratestacks.append([])
    for crates in cratespic:
        for n in range(len(crates)//4):
            if crates[n*4] != " ":
                cratestacks[n].append(crates[n*4+1])

    # print(cratestacks)

    # max_stack_size = 0
    for move in movelist:
        splitspace = move.split(" ")
        n_to_move = int(splitspace[1])
        move_from = int(splitspace[3])
        move_to = int(splitspace[5])
        # print(n_to_move, move_from, move_to)

        move_crates = []
        for n in range(n_to_move):
            move_crate = cratestacks[move_from-1].pop(0)
            move_crates.append(move_crate)

        cratestacks[move_to-1][0:0] = move_crates

        # print(cratestacks)
        # for n in range(n_stack):
        #     if len(cratestacks[n]) > max_stack_size:
        #            max_stack_size = len(cratestacks[n])

    # print("max stack ", max_stack_size)

    answer = ""

    for n in range(n_stack):
        answer += cratestacks[n][0]

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
