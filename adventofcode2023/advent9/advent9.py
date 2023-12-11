# Advent of code 2023, day 9

# open file
input = open("advent9_input.txt", "r")
# input = open("advent9_input_test.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    answer = 0

    for input in input_array:
        splitspace = input[:-1].split(" ")
        sequences = []
        sequences.append([int(splitspace[n]) for n in range(len(splitspace))])

        print(sequences)

        all_zeros = False
        while all_zeros is False:
            new_sequence = []
            for n in range(len(sequences[-1])-1):
                new_sequence.append(sequences[-1][n+1]-sequences[-1][n])

            sequences.append(new_sequence)

            all_zeros = True
            for nn in range(len(new_sequence)):
                if new_sequence[nn] != 0:
                    all_zeros = False

        # print(sequences)

        # Add a zero to the final sequence and traverse back up...
        sequences[-1].append(0)

        for n in range(len(sequences)-2, -1, -1):
            sequences[n].append(sequences[n][-1]+sequences[n+1][-1])

        print(sequences[0])

        answer += sequences[0][-1]

    return answer

def part2():

    answer = 0

    for input in input_array:
        splitspace = input[:-1].split(" ")
        sequences = []
        sequences.append([int(splitspace[n]) for n in range(len(splitspace))])

        print(sequences)

        all_zeros = False
        while all_zeros is False:
            new_sequence = []
            for n in range(len(sequences[-1])-1):
                new_sequence.append(sequences[-1][n+1]-sequences[-1][n])

            sequences.append(new_sequence)

            all_zeros = True
            for nn in range(len(new_sequence)):
                if new_sequence[nn] != 0:
                    all_zeros = False

        # print(sequences)

        # Add a zero to the final sequence and traverse back up...
        sequences[-1].append(0)

        for n in range(len(sequences)-2, -1, -1):
            sequences[n].insert(0, sequences[n][0]-sequences[n+1][0])

        print(sequences[0])

        answer += sequences[0][0]

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
