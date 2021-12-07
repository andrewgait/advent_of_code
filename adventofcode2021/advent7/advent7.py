# Advent of code, day 7

# open file
input = open("advent7_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    answer = 0

    input = input_array[0].split(",")
    n_inputs = len(input)
    for n in range(n_inputs):
        input[n] = int(input[n])

    max_input = max(input)

    sum_distances = []
    min_sum_d = 99999999999999999
    min_location = 0
    for i in range(max_input):
        sum_d = 0
        for n in range(n_inputs):
            sum_d += abs(i - input[n])
        sum_distances.append(sum_d)
        if sum_d < min_sum_d:
            min_sum_d = sum_d
            min_location = i

    print(min_location)
    answer = min_sum_d

    return answer

def part2():

    answer = 0

    input = input_array[0].split(",")
    n_inputs = len(input)
    for n in range(n_inputs):
        input[n] = int(input[n])

    max_input = max(input)

    sum_distances = []
    min_sum_d = 99999999999999999
    min_location = 0
    for i in range(max_input):
        sum_d = 0
        for n in range(n_inputs):
            distance = abs(i - input[n])
            sum_d += distance * (distance + 1) // 2
        sum_distances.append(sum_d)
        if sum_d < min_sum_d:
            min_sum_d = sum_d
            min_location = i

    print(min_location)
    answer = min_sum_d

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
