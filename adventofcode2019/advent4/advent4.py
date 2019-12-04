# Advent of code, day 4
import numpy as np

# open file
input = open("advent4_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

low = int(input_array[0][0:6])
high = int(input_array[0][7:13])

print("low, high: ", low, high)

def test_ascending(digits):
    # next digit up is either the same or bigger
    if ((digits[1] >= digits[0]) and (digits[2] >= digits[1]) and
        (digits[3] >= digits[2]) and (digits[4] >= digits[3]) and
        (digits[5] >= digits[4])):
        return True
    else:
        return False

def test_doubles1(digits):
    # if any consecutive digits are the same
    if ((digits[0] == digits[1]) or (digits[1] == digits[2]) or
        (digits[2] == digits[3]) or (digits[3] == digits[4]) or
        (digits[4] == digits[5])):
        return True
    else:
        return False

def test_doubles2(digits):
    # if any two consecutive digits are the same and not part of a larger run
    if (((digits[0] == digits[1]) and (digits[1] != digits[2])) or
        ((digits[1] == digits[2]) and
         ((digits[2] != digits[3]) and (digits[0] != digits[1]))) or
        ((digits[2] == digits[3]) and
         ((digits[3] != digits[4]) and (digits[1] != digits[2]))) or
        ((digits[3] == digits[4]) and
         ((digits[4] != digits[5]) and (digits[2] != digits[3]))) or
        ((digits[4] == digits[5]) and
         (digits[3] != digits[4]))):
        return True
    else:
        return False

def test_number(number):
    password = False
    digits = np.zeros(6)
    for i in range(6):
        digits[i] = number // (10**(5-i))
        number = number - (digits[i]*(10**(5-i)))

#     print(digits)
    double = test_doubles1(digits)
    ascending = test_ascending(digits)

    if double and ascending:
        password = True

    return password

def test_number2(number):
    password = False
    digits = np.zeros(6)
    for i in range(6):
        digits[i] = number // (10**(5-i))
        number = number - (digits[i]*(10**(5-i)))

#     print(digits)
    double = test_doubles2(digits)
    ascending = test_ascending(digits)

    if double and ascending:
        password = True

    return password

def part1(low, high):
    count = 0
    for i in range(low, high+1):
        if test_number(i):
            count += 1

    return count

def part2(low, high):
    count = 0
    for i in range(low, high+1):
        if test_number2(i):
            count += 1

    return count

print("Testing part 1 criteria")
print(122345, test_number(122345))
print(111123, test_number(111123))
print(135679, test_number(135769))
print(111111, test_number(111111))
print(223450, test_number(223450))
print(123789, test_number(123789))
print("Testing part 2 criteria")
print(112233, test_number2(112233))
print(123444, test_number2(123444))
print(111122, test_number2(111122))
print(111111, test_number2(111111))
print("Part 1 answer: ", part1(low, high))
print("Part 2 answer: ", part2(low, high))
