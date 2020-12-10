# Advent of code, day 10
import numpy

# open file
input = open("advent10_input.txt", "r")
# input = open("advent10_test_input.txt", "r")
# input = open("advent10_test_input2.txt", "r")

# charging socket at the start is 0
input_array = [0]
# read string into array
for line in input:
    input_array.append(int(line))

def part1():

    # Find the maximum of the adapters in the bag (input) and add it to the array
    max_bag = max(input_array)
    input_array.append(max_bag+3)

    # Sort the adapters
    adapters = numpy.array(input_array)
    sorted_adapters = numpy.sort(adapters)

    # Now they are sorted simply count the 1-diffs and 3-diffs
    n = len(input_array)
    diff1 = 0
    diff3 = 0
    for i in range(n-1):
        diff = sorted_adapters[i+1] - sorted_adapters[i]
        if (diff == 1):
            diff1 += 1
        elif (diff == 3):
            diff3 += 1

    answer = diff1 * diff3

    return answer

def part2():

    # input_array was already modified by part 1

    # Sort the adapters
    adapters = numpy.array(input_array)
    sorted_adapters = numpy.sort(adapters)

    n = len(input_array)
    connect_array = [1]
    # use dynamic programming and update the sum whilst heading along the sorted array
    for i in range(1,n-1):
        connect_array.append(0)
        j = i-1
#         print(connect_array)
        # at each point check whether values below can be included too
        while (sorted_adapters[i] - sorted_adapters[j] <= 3) and (j >= 0):
            connect_array[i] += connect_array[j]
            j -= 1

    answer = connect_array[len(connect_array)-1]

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
