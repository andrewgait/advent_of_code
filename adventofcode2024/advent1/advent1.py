# Advent of code 2024, day 1

# open file
input = open("advent1_input.txt", "r")
# input = open("advent1_test_input1.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)


def part1():

    list1 = []
    list2 = []
    for input in input_array:
        splitspace = input.split("   ")
        list1.append(int(splitspace[0]))
        list2.append(int(splitspace[1]))

    # sort separately
    sorted1 = sorted(list1)
    sorted2 = sorted(list2)

    answer = 0
    for n in range(len(sorted1)):
        answer += abs(sorted2[n]-sorted1[n])

    return answer

def part2():

    list1 = []
    list2 = []
    for input in input_array:
        splitspace = input.split("   ")
        list1.append(int(splitspace[0]))
        list2.append(int(splitspace[1]))

    answer = 0
    for n in range(len(list1)):
        # Count value from list 1 in list 2
        value1 = list1[n]
        count2 = list2.count(value1)
        answer += value1 * count2

    return answer

    answer = 0

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
