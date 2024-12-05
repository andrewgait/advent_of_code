# Advent of code 2024, day 2

# open file
input = open("advent2_input.txt", "r")
# input = open("advent2_test_input1.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)


def test_safe(test_array):
    check_test = []
    for n in range(len(test_array)-1):
        check_test.append(test_array[n+1] - test_array[n])
    safe = True
    # print(check_test)
    for nn in range(len(check_test)):
        if check_test[nn] == 0:
            safe = False
        if abs(check_test[nn]) > 3:
            safe = False
    if not all(x < 0 for x in check_test) and not all(x > 0 for x in check_test):
        safe = False
    return safe

def part1():

    answer = 0

    for input in input_array:
        splitspace = input.split(" ")
        test_array = []
        for ss in splitspace:
            test_array.append(int(ss))

        safe = test_safe(test_array)

        if safe:
            answer += 1


    return answer

def part2():

    answer = 0

    for input in input_array:
        splitspace = input.split(" ")
        test_array = []
        for ss in splitspace:
            test_array.append(int(ss))

        # Test every instance of test_array with a level removed
        # and if any are safe then that's good
        safe = False
        test_len = len(test_array)
        for n in range(test_len):
            test_this = test_array[0:n] + test_array[n+1:]
            safe_test = test_safe(test_this)
            if safe_test:
                safe = True

        if safe:
            answer += 1

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
