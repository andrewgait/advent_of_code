# Advent of code, day 8

# open file
input = open("advent8_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    answer = 0

    count_1478 = 0

    n_inputs = len(input_array)
    for n in range(n_inputs):
        split_space = input_array[n].split(" ")
        split_space[-1] = split_space[-1][:-1]
        entries = len(split_space)
        for m in range(entries-4,entries):
            if ((len(split_space[m]) == 2) or (len(split_space[m]) == 3) or
                (len(split_space[m]) == 4) or (len(split_space[m]) == 7)):
                count_1478 += 1

    answer = count_1478

    return answer

def part2():

    answer = 0

    n_inputs = len(input_array)
    for n in range(n_inputs):
        split_space = input_array[n].split(" ")
        split_space[-1] = split_space[-1][:-1]
        entries = len(split_space)
        sorted_entries = []
        entry_done = []
        for m in range(entries):
            sorted_entries.append("".join(sorted(split_space[m])))
            entry_done.append(0)

        # print(sorted_entries)

        codes = ["b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]

        for m in range(10):
            if len(sorted_entries[m]) == 2:
                codes[1] = sorted_entries[m]
                entry_done[m] = 1
            elif len(sorted_entries[m]) == 3:
                codes[7] = sorted_entries[m]
                entry_done[m] = 1
            elif len(sorted_entries[m]) == 4:
                codes[4] = sorted_entries[m]
                entry_done[m] = 1
            elif len(sorted_entries[m]) == 7:
                codes[8] = sorted_entries[m]
                entry_done[m] = 1

        # print(codes)

        for m in range(10):
            # 6 is the only one that doesn't contain both from 1
            # 9 is the only one that contains all of 4
            if len(sorted_entries[m]) == 6:
                if ((codes[1][0] not in sorted_entries[m]) or
                    (codes[1][1] not in sorted_entries[m])):
                    codes[6] = sorted_entries[m]
                    entry_done[m] = 1
                if ((codes[4][0] in sorted_entries[m]) and
                    (codes[4][1] in sorted_entries[m]) and
                    (codes[4][2] in sorted_entries[m]) and
                    (codes[4][3] in sorted_entries[m])):
                    codes[9] = sorted_entries[m]
                    entry_done[m] = 1

            # 3 is the only one that contains all from 7
            if len(sorted_entries[m]) == 5:
                if ((codes[7][0] in sorted_entries[m]) and
                    (codes[7][1] in sorted_entries[m]) and
                    (codes[7][2] in sorted_entries[m])):
                    codes[3] = sorted_entries[m]
                    entry_done[m] = 1

        for m in range(10):
            # 0 is the only length 6 left
            if (len(sorted_entries[m]) == 6 and entry_done[m] == 0):
                codes[0] = sorted_entries[m]

            # 5 is the intersection of 9 and 6... (?)
            if (len(sorted_entries[m]) == 5 and entry_done[m] == 0):
                inter69 = ""
                for i in codes[6]:
                    if i in codes[9]:
                        inter69 += i
                if (inter69 == sorted_entries[m]):
                    codes[5] = sorted_entries[m]
                else:
                    codes[2] = sorted_entries[m]

        # print(codes)
        thousands = 0
        hundreds = 0
        tens = 0
        ones = 0
        for i in range(10):
            if sorted_entries[entries-4] == codes[i]:
                thousands = i
            if sorted_entries[entries-3] == codes[i]:
                hundreds = i
            if sorted_entries[entries-2] == codes[i]:
                tens = i
            if sorted_entries[entries-1] == codes[i]:
                ones = i

        answer += (thousands*1000 + hundreds*100 + tens*10 + ones)


    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
