# Advent of code, day 5
from _threading_local import local

# open file
input = open("advent5_input.txt", "r")
# input = open("advent5_test1.txt", "r")

def part2(input):
    # read string into array
    insts = []
    for line in input:
        insts.append(int(line))

    print(insts)

    count = 1
    loc = 0
    N = len(insts)
    print(N)
    loc = insts[loc] + loc
    insts[loc] += 1

    print(insts, loc)
    while loc >= 0 and loc < N:
        count += 1
        new_loc = loc + insts[loc]
        if (insts[loc] > 2):  # just edit this bit to go back to part 1
            insts[loc] -= 1
        else:
            insts[loc] += 1
        loc = new_loc
#         print(insts, loc)



    return count

print(part2(input))
