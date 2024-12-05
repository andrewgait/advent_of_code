# Advent of code 2024, day 5

# open file
input = open("advent5_input.txt", "r")
input = open("advent5_test_input1.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    # Create dict where value goes before key
    rules_dict = {}
    n = 0
    input = input_array[n]
    while input != "\n":
        splitline = input.split("|")
        if int(splitline[1]) in rules_dict.keys():
            rules_dict[int(splitline[1])].append(int(splitline[0]))
        else:
            rules_dict[int(splitline[1])] = [int(splitline[0])]

        n += 1
        input = input_array[n]

    print(rules_dict)
    answer = 0

    for nn in range(n+1,len(input_array)):
        instructions = input_array[nn]
        splitcomma = instructions.split(",")
        len_instr = len(splitcomma)
        passes = True
        for mm in range(len_instr):
            if int(splitcomma[mm]) in rules_dict.keys():
                test_these = rules_dict[int(splitcomma[mm])]
                for mmm in range(mm,len_instr):
                    if int(splitcomma[mmm]) in test_these:
                        passes = False
        if passes:
            answer += int(splitcomma[len_instr//2])

    return answer

def sort_pages(pages, inverse_rules_dict):
    for i in range(len(pages)):
        for j in range(i + 1, len(pages)):
            if pages[i] in inverse_rules_dict.keys():
                if pages[j] not in inverse_rules_dict[pages[i]]:
                    pages.insert(i, pages.pop(j))
    return pages

def part2():

    # Create dict where value goes before key
    rules_dict = {}
    inverse_rules_dict = {}
    rules_list = []
    n = 0
    input = input_array[n]
    while input != "\n":
        splitline = input.split("|")
        if int(splitline[1]) in rules_dict.keys():
            rules_dict[int(splitline[1])].append(int(splitline[0]))
        else:
            rules_dict[int(splitline[1])] = [int(splitline[0])]
        if int(splitline[0]) in inverse_rules_dict.keys():
            inverse_rules_dict[int(splitline[0])].append(int(splitline[1]))
        else:
            inverse_rules_dict[int(splitline[0])] = [int(splitline[1])]

        n += 1
        input = input_array[n]

    print(rules_dict)
    print(inverse_rules_dict)
    for key in rules_dict.keys():
        if key not in inverse_rules_dict.keys():
            inverse_rules_dict[key] = []
    answer = 0

    for nn in range(n+1,len(input_array)):
        instructions = input_array[nn]
        splitcomma = instructions.split(",")
        len_instr = len(splitcomma)
        passes = True
        for mm in range(len_instr):
            if int(splitcomma[mm]) in rules_dict.keys():
                test_these = rules_dict[int(splitcomma[mm])]
                for mmm in range(mm,len_instr):
                    if int(splitcomma[mmm]) in test_these:
                        passes = False
        if not passes:
            # need to reorder the instructions correctly...
            # I have "noticed" that the number of instructions is a triangular number
            # so this means each number must be repeated the number of times it is above/below a number

            # So the first number is the one that is in the keys of inverse_rules_dict but not the keys
            # of rules_dict

            # rules_dict[first_key] = []
            # for key in rules_dict.keys():
            #     print("hello ", key, len(rules_dict[key]))
            # # The remaining keys of rules_dict go into this array in the order
            # unordered = [int(splitcomma[mm]) for mm in range(len_instr)]
            # print("unordered ", unordered)
            # reordered = sorted(unordered, key=lambda x: len(rules_dict[x]))
            # print("reordered ", reordered)

            # answer += int(reordered[len_instr//2])

            # OK so the above was true for my test input but it's not true in general, sadly
            # So we need to decide a method for working out how to sort based on a different set of criteria

            # print("first ", first_key)

            # Loop over the instructions
            unordered = [int(splitcomma[mm]) for mm in range(len_instr)]
            # Sort them
            ordered = sort_pages(unordered, inverse_rules_dict)
            # for mm in range(1, len_instr):
            #     left = unordered[mm-1]
            #     right = unordered[mm]
            answer += int(ordered[len_instr//2])

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
