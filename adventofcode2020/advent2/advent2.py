# Advent of code, day 2

# open file
input = open("advent2_input.txt", "r")
# input = open("advent2_test_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

#     answer = 0
    n = len(input_array)
    print('Number of passwords is ', n)
    n_valid = 0
    for i in range(n):
        # format is N-M *: password
        this_line = input_array[i]
        splitcolon = this_line[:-1].split(":")
        password = splitcolon[1][1:]
        splitspace = splitcolon[0].split(" ")
        letter = splitspace[1]
        splitdash = splitspace[0].split("-")
        low = int(splitdash[0])
        high = int(splitdash[1])
        n_letters = 0
        for j in range(len(password)):
            if password[j] == letter:
                n_letters += 1

#         print(letter, ' appears ', n_letters, ' times in ', password)

        if (n_letters >= low) and (n_letters <= high):
            n_valid += 1

    return n_valid

def part2():

    answer = 0
    n = len(input_array)
    print('Number of passwords is ', n)
    n_valid = 0
    n_invalid = 0
    for i in range(n):
        # format is N-M *: password
        this_line = input_array[i]
        splitcolon = this_line[:-1].split(":")
        password = splitcolon[1][1:]
        splitspace = splitcolon[0].split(" ")
        letter = splitspace[1]
        splitdash = splitspace[0].split("-")
        low = int(splitdash[0])
        high = int(splitdash[1])
        n_letters = 0
        if ((password[low-1] == letter) and (password[high-1] == letter)):
            n_invalid += 1
        elif ((password[low-1] == letter) or (password[high-1] == letter)):
            n_valid += 1
        else:
            n_invalid += 1

    print(n_valid, n_invalid)
    return n_valid

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
