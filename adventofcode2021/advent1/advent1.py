# Advent of code, day 1

# open file
input = open("advent1_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(int(line))

def part1():

    answer = 0

    n_inputs = len(input_array)
    print(n_inputs)
    for n in range(n_inputs):
        if n > 0:
            if input_array[n] > input_array[n-1]:
                answer += 1

    return answer

def part2():

    answer = 0

    n_inputs = len(input_array)
    print(n_inputs)
    sum_array = []
    for n in range(n_inputs):
        if n < (n_inputs-2):
            sum_array.append(input_array[n]+input_array[n+1]+input_array[n+2])


    for n in range(len(sum_array)):
        if n > 0:
            if sum_array[n] > sum_array[n-1]:
                answer += 1

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
