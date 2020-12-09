# Advent of code, day 9

# open file
input = open("advent9_input.txt", "r")
# input = open("advent9_test_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(int(line))

def find_invalid_number(input_array, n_to_consider):
    answer = 0
    location = n_to_consider
    n = len(input_array)
    for i in range(n_to_consider, n):

        sum_found = False

        test_value = input_array[i]

        # Loop over previous n_to_consider numbers
        for j in range(i-n_to_consider, i):
            for k in range(j, i):
                sum = input_array[j] + input_array[k]
                if sum == test_value:
                    sum_found = True

        if not sum_found:
            answer = test_value
            location = i
            break

    return answer, location


def part1():

#     n_to_consider = 5  # test data
    n_to_consider = 25  # real data

    answer, location = find_invalid_number(input_array, n_to_consider)

    print(answer, location)

    return answer


def part2():

#     n_to_consider = 5  # test data
    n_to_consider = 25  # real data

    inv_number, location = find_invalid_number(input_array, n_to_consider)

    array_found = []

    print(inv_number, location)

    # the contiguous set of numbers must be before the calculated location
    # (and it must be at least 3 in length)
    for length in range(3, location):
        sum_found = False

        # start from location and search backwards
        for i in range(location-1, length, -1):
            sum = 0
            for j in range(length):
                sum += input_array[i-j]

            if sum == inv_number:
                array_found = input_array[i-length+1:i+1]
                sum_found = True
                break

        if sum_found:
            break

    print(array_found)
    answer = max(array_found) + min(array_found)

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
