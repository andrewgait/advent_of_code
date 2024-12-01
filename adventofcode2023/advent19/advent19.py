# Advent of code 2023, day 19

# open file
input = open("advent19_input.txt", "r")
input = open("advent19_input_test.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    is_input_data = False
    workflows = {}
    input_dicts = []
    for input in input_array:
        if input == "\n":
            is_input_data = True
            continue

        if is_input_data:
            # Form of {x ,m, a, s}
            splitcomma = input.split(",")
            input_vals = {splitcomma[0][1]: int(splitcomma[0][3:]),
                          splitcomma[1][0]: int(splitcomma[1][2:]),
                          splitcomma[2][0]: int(splitcomma[2][2:]),
                          splitcomma[3][0]: int(splitcomma[3][2:-2])}
            input_dicts.append(input_vals)
        else:
            splitbrace = input.split("{")
            workflow_inst = splitbrace[0]
            splitcomma = splitbrace[1][:-2].split(",")
            len_comma = len(splitcomma)
            workflows[workflow_inst] = [splitcomma[n] for n in range(len_comma)]

    print(workflows)
    answer = 0

    for input_dict in input_dicts:
        instruction = "in"
        print(input_dict)

        while instruction not in ["A", "R"]:
            workflow = workflows[instruction]
            # print(workflow, instruction)
            for work in workflow:
                if ":" in work:
                    splitcolon = work.split(":")
                    resultiftrue = splitcolon[1]
                    valtest = splitcolon[0][0]
                    test = splitcolon[0][1]
                    number = int(splitcolon[0][2:])

                    if test == ">":
                        if input_dict[valtest] > number:
                            instruction = resultiftrue
                            break
                        # else carry on to next instruction
                    elif test == "<":
                        if input_dict[valtest] < number:
                            instruction = resultiftrue
                            break
                        # else carry on to next instruction

                else:
                    instruction = work
                    break

        if instruction == "A":
            answer += sum(input_dict.values())

    return answer

def part2():

    is_input_data = False
    workflows = {}
    input_dicts = []
    for input in input_array:
        if input == "\n":
            is_input_data = True
            continue

        if is_input_data:
            # Form of {x ,m, a, s}
            splitcomma = input.split(",")
            input_vals = {splitcomma[0][1]: int(splitcomma[0][3:]),
                          splitcomma[1][0]: int(splitcomma[1][2:]),
                          splitcomma[2][0]: int(splitcomma[2][2:]),
                          splitcomma[3][0]: int(splitcomma[3][2:-2])}
            input_dicts.append(input_vals)
        else:
            splitbrace = input.split("{")
            workflow_inst = splitbrace[0]
            splitcomma = splitbrace[1][:-2].split(",")
            len_comma = len(splitcomma)
            workflows[workflow_inst] = [splitcomma[n] for n in range(len_comma)]

    print(workflows)
    answer = 0

    instruction = "in"

    answer = 1
    input_dict_lists = {}
    for valletter in ["x", "m", "a", "s"]:
        input_dict_lists[valletter] = [[[n for n in range(1,4001)], "in"]]

    # for key, input_dict_list in input_dict_lists.items():
    #     print(key)
    #     for input in input_dict_list:
    #         print(input)

    all_inst_A_or_R = False
    # print(valletter)

    nnn = 0
    while nnn < 2: #not all_inst_A_or_R:
        nnn += 1
        new_input_dict_lists = {}
        for valletter in ["x", "m", "a", "s"]:
            new_input_dict_lists[valletter] = []
        # print(" ")
        for valkey, input_dict_listed in input_dict_lists.items():
            for input_dict_list in input_dict_listed:
                instruction = input_dict_list[1]
                # print(instruction, valkey, input_dict_list[0])
                if ":" in instruction:
                    instruction = instruction.split(":")[1]
                if instruction not in ["A", "R"]:
                    workflow = workflows[instruction]
                    # print(workflow, instruction)
                    n_works = len(workflow)
                    for n_work in range(n_works):
                        if ":" in workflow[n_work]:
                            splitcolon = workflow[n_work].split(":")
                            resultiftrue = splitcolon[1]
                            valtest = splitcolon[0][0]
                            test = splitcolon[0][1]
                            number = int(splitcolon[0][2:])

                            if valtest != valkey:
                                new_input_dict_lists[valkey].append(
                                    [input_dict_list[0], workflow[n_work+1]])
                            else:
                                if test == ">":
                                    new_above_list = []
                                    new_below_list = []
                                    for nn in range(len(input_dict_list[0])):
                                        if input_dict_list[0][nn] > number:
                                            new_above_list.append(input_dict_list[0][nn])
                                        else:
                                            new_below_list.append(input_dict_list[0][nn])

                                    new_input_dict_lists[valkey].append(
                                        [new_below_list, workflow[n_work+1]])
                                    if resultiftrue != "R":
                                        new_input_dict_lists[valkey].append(
                                            [new_above_list, resultiftrue])
                                elif test == "<":
                                    new_above_list = []
                                    new_below_list = []
                                    for nn in range(len(input_dict_list[0])):
                                        if input_dict_list[0][nn] < number:
                                            new_below_list.append(input_dict_list[0][nn])
                                        else:
                                            new_above_list.append(input_dict_list[0][nn])

                                    new_input_dict_lists[valkey].append(
                                        [new_above_list, workflow[n_work+1]])
                                    if resultiftrue != "R":
                                        new_input_dict_lists[valkey].append(
                                            [new_below_list, resultiftrue])

                        # else:
                        #     new_input_dict_lists[valkey].append([input_dict_list[0], workflow[n_work]])
                else: # instruction is A or R, just copy it
                    if instruction == "A":
                        new_input_dict_lists[valkey].append(
                            [input_dict_list[0], input_dict_list[1][-1]])
                    # elif instruction == "R":


        input_dict_lists = new_input_dict_lists.copy()
        print("check instructions")
        for key, input_dict_list in input_dict_lists.items():
            print(key)
            for input in input_dict_list:
                print(input)

        all_inst_A_or_R = True
        for _, new_inputs in new_input_dict_lists.items():
            for new_input in new_inputs:
                if new_input[1] not in ["A", "R"]:
                    all_inst_A_or_R = False
                    break

    # print("final dict list for ", valletter)

    final_set = set()
    # print(input_dict_lists)
    for _, input_dict_listed in input_dict_lists.items():
        # print(input_dict_listed)
        for input_dict_list in input_dict_listed[0]:
            for n in range(len(input_dict_list)):
                final_set.add(input_dict_list[n])
    # print(final_set)

    answer *= len(final_set)

    answer = (4000-2662)*(4000-(2090-1801))*(1716)*(2770-1351)

    return answer

    return input_dict_lists

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
