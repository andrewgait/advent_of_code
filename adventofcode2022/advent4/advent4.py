# Advent of code 2022, day 4

# open file
input = open("advent4_input.txt", "r")
# input = open("advent4_test_input1.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    total = 0

    for input_line in input_array:
        splitcomma = input_line.split(",")

        firstsplitdash = splitcomma[0].split("-")
        first = []
        firstbegin = int(firstsplitdash[0])
        firstend = int(firstsplitdash[1])+1
        for n in range(firstbegin, firstend):
            first.append(n)
        secondsplitdash = splitcomma[1].split("-")
        second = []
        secondbegin = int(secondsplitdash[0])
        secondend = int(secondsplitdash[1])+1
        for n in range(secondbegin, secondend):
            second.append(n)

        if (set(first).issubset(set(second)) or set(second).issubset(set(first))):
            total += 1

    answer = total

    return answer

def part2():

    total = 0

    for input_line in input_array:
        splitcomma = input_line.split(",")

        firstsplitdash = splitcomma[0].split("-")
        first = []
        firstbegin = int(firstsplitdash[0])
        firstend = int(firstsplitdash[1])+1
        for n in range(firstbegin, firstend):
            first.append(n)
        secondsplitdash = splitcomma[1].split("-")
        second = []
        secondbegin = int(secondsplitdash[0])
        secondend = int(secondsplitdash[1])+1
        for n in range(secondbegin, secondend):
            second.append(n)

        for mm in range(len(second)):
            if second[mm] in first:
                total += 1
                break

    answer = total

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
