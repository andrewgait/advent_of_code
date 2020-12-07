# Advent of code, day 6
from collections import OrderedDict

# open file
input = open("advent6_input.txt", "r")
# input = open("advent6_test_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)


def create_array(input_array):
    # full array of all answers
    answers_array = []

    # answers for this group
    answer_array = []

    n = len(input_array)

    for i in range(n):
        # make an array and add valuees until we hit a blank line
        if input_array[i][0] == "\n":
            answers_array.append(answer_array)
            answer_array = []
        else:
            answer_array.append(input_array[i])

    return answers_array

def part1():

    answer = 0

    full_array = create_array(input_array)

    n = len(full_array)
    for i in range(n):
        m = len(full_array[i])
        this_str = ""
        for j in range(m):
            this_str += full_array[i][j][:-1]  # remove \n from end

        # now remove all duplicate letters from this_str
        no_duplicates = "".join(OrderedDict.fromkeys(this_str))

        answer += len(no_duplicates)
        # Noted that this is the same as doing the union of all the strings

    return answer

def part2():

    answer = 0

    full_array = create_array(input_array)

    n = len(full_array)
    for i in range(n):
        m = len(full_array[i])

        # Now I need to do the intersection of all of the strings in this bit
        this_str = full_array[i][0][:-1]  # remove \n from end
        if m==1:
            answer += len(this_str)
        else:
            for j in range(1, m):
                current_str = full_array[i][j][:-1]
                # this_str becomes intersection of this_str and current_str
                this_str = set(this_str).intersection(current_str)

            answer += len(this_str)

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
