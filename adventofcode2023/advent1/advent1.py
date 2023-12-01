# Advent of code 2023, day 1

# open file
input = open("advent1_input.txt", "r")
# input = open("advent1_input_test.txt", "r")
# input = open("advent1_input_test2.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
digits_names = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

digits_dict = {}
for digit, digit_name in zip(digits, digits_names):
    digits_dict[digit_name] = int(digit)

print(digits_dict)

def part1():

    sum = 0
    for input in input_array:
        digits_line = []
        for char in input:
            if char in digits:
                digits_line.append(int(char))

        if len(digits_line):
            sum += digits_line[0]*10 + digits_line[-1]

    answer = sum

    return answer

def part2():

    sum = 0
    for input in input_array:
        digits_line = []
        n_input = len(input)
        for n in range(n_input):
            if input[n] in digits:
                digits_line.append(int(input[n]))
            # inputs can be three, four or five letters long
            elif input[n:n+3] in digits_names:
                digits_line.append(digits_dict[input[n:n+3]])
            elif input[n:n+4] in digits_names:
                digits_line.append(digits_dict[input[n:n+4]])
            elif input[n:n+5] in digits_names:
                digits_line.append(digits_dict[input[n:n+5]])

        sum += digits_line[0]*10 + digits_line[-1]

    answer = sum
    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
