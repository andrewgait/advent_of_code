# Advent of code 2024, day 7

# open file
input = open("advent7_input.txt", "r")
# input = open("advent7_test_input1.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    answer = 0

    for input in input_array:
        splitcolon = input.split(":")
        result = int(splitcolon[0])

        splitspace = splitcolon[1].split(" ")

        possible_results = []
        for nn in range(1,len(splitspace)):
            value = int(splitspace[nn])
            if nn == 1:
                new_possible_results = [value]
            else:
                new_possible_results = []
                for possible in possible_results:
                    new_possible_results.append(value + possible)
                    new_possible_results.append(value * possible)

            possible_results = []
            for new_possible in new_possible_results:
                possible_results.append(new_possible)

        if result in possible_results:
            answer += result

    return answer

def part2():

    answer = 0

    for input in input_array:
        splitcolon = input.split(":")
        result = int(splitcolon[0])

        splitspace = splitcolon[1].split(" ")

        possible_results = []
        for nn in range(1,len(splitspace)):
            value = int(splitspace[nn])
            if nn == 1:
                new_possible_results = [value]
            else:
                new_possible_results = []
                for possible in possible_results:
                    new_possible_results.append(value + possible)
                    new_possible_results.append(value * possible)
                    # concatenate is (possible * 10^n+digits_p) + value
                    n_digits_v = len(str(value))
                    new_possible_results.append((possible * (10**n_digits_v)) + value)

            possible_results = []
            for new_possible in new_possible_results:
                possible_results.append(new_possible)

        if result in possible_results:
            answer += result

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
