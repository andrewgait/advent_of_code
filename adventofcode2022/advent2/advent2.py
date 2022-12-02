# Advent of code 2022, day 2

# open file
input = open("advent2_input.txt", "r")
# input = open("advent2_test_input1.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

opprock = "A"
opppaper = "B"
oppscissors = "C"

def game1(input_array, myrock, mypaper, myscissors):
    total_score = 0
    for input_line in input_array:
        oppplay = input_line[0]
        myplay = input_line[2]

        if myplay == myrock:
            total_score += 1
        if myplay == mypaper:
            total_score += 2
        if myplay == myscissors:
            total_score += 3

        if myplay == myrock:
            if oppplay == opprock:
                total_score += 3
            elif oppplay == oppscissors:
                total_score += 6
        elif myplay == mypaper:
            if oppplay == opppaper:
                total_score += 3
            elif oppplay == opprock:
                total_score += 6
        elif myplay == myscissors:
            if oppplay == oppscissors:
                total_score += 3
            elif oppplay == opppaper:
                total_score += 6

    return total_score

def part1():

    answer = game1(input_array, "X", "Y", "Z")

    return answer

def part2():

    total_score = 0
    for input_line in input_array:
        if input_line[2] == "Y":
            total_score += 3
        elif input_line[2] == "Z":
            total_score += 6

        if input_line[2] == "X":
            if input_line[0] == opprock:
                total_score += 3
            elif input_line[0] == opppaper:
                total_score += 1
            elif input_line[0] == oppscissors:
                total_score += 2
        elif input_line[2] == "Y":
            if input_line[0] == opprock:
                total_score += 1
            elif input_line[0] == opppaper:
                total_score += 2
            elif input_line[0] == oppscissors:
                total_score += 3
        elif input_line[2] == "Z":
            if input_line[0] == opprock:
                total_score += 2
            elif input_line[0] == opppaper:
                total_score += 3
            elif input_line[0] == oppscissors:
                total_score += 1

    answer = total_score

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
