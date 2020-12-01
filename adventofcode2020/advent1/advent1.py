# Advent of code, day 1

# open file
input = open("advent1_input.txt", "r")
# input = open("advent1_test_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(int(line))

print(input_array)

def part1():

    n = len(input_array)

    answer = 0

    for i in range(n):
        for j in range(i+1, n):
            if (input_array[i]+input_array[j] == 2020):
                answer = input_array[i] * input_array[j]
                break

    return answer

def part2():

    n = len(input_array)

    answer = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                ia = input_array[i]
                ja = input_array[j]
                ka = input_array[k]
                if (ia + ja + ka == 2020):
                    print(ia, ja, ka, i, j, k)
                    answer = ia * ja * ka

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
