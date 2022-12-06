# Advent of code 2022, day 6

# open file
input = open("advent6_input.txt", "r")
# input = open("advent6_test_input5.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    index = 0
    distinct = False

    while distinct == False:
        fourchars = input_array[0][index:index+4]
        fourset = set(fourchars)

        if len(fourset) == len(fourchars):
            distinct = True
        else:
            index += 1

    answer = index + 4

    return answer

def part2():

    index = 0
    distinct = False

    while distinct == False:
        fourteenchars = input_array[0][index:index+14]
        fourteenset = set(fourteenchars)

        if len(fourteenset) == len(fourteenchars):
            distinct = True
        else:
            index += 1

    answer = index + 14

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
