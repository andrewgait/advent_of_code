# Advent of code 2023, day 4

# open file
input = open("advent4_input.txt", "r")
# input = open("advent4_input_test.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    sum = 0

    for input in input_array:
        points = 0
        splitcolon = input.split(":")
        splitnumbers = splitcolon[1].split("|")

        splitmynumbers = splitnumbers[0][1:-1].split(" ")
        splitwinnumbers = splitnumbers[1][1:-1].split(" ")

        win_numbers = []
        for splitwin in splitwinnumbers:
            if splitwin != "":
                win_numbers.append(int(splitwin))

        my_numbers = []
        for splitmy in splitmynumbers:
            if splitmy != "":
                my_numbers.append(int(splitmy))

        print(my_numbers, win_numbers)

        for number in my_numbers:
            if number in win_numbers:
                if points == 0:
                    points = 1
                else:
                    points *= 2

        sum += points

    answer = sum

    return answer

def part2():

    sum_cards = 0

    # start off with one copy of each card
    n_copies = [1 for n in range(len(input_array))]

    n = 0

    for input in input_array:
        matches = 0
        copies = n_copies[n]
        splitcolon = input.split(":")
        splitnumbers = splitcolon[1].split("|")

        splitmynumbers = splitnumbers[0][1:-1].split(" ")
        splitwinnumbers = splitnumbers[1][1:-1].split(" ")

        win_numbers = []
        for splitwin in splitwinnumbers:
            if splitwin != "":
                win_numbers.append(int(splitwin))

        my_numbers = []
        for splitmy in splitmynumbers:
            if splitmy != "":
                my_numbers.append(int(splitmy))

        for number in my_numbers:
            if number in win_numbers:
                matches += 1

        for m in range(n+1, n+matches+1):
            n_copies[m] += copies

        n += 1


    print(n_copies)
    answer = sum(n_copies)

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
