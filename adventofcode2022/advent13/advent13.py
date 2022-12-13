# Advent of code 2022, day 13
import ast
from functools import cmp_to_key

# open file
input = open("advent13_input.txt", "r")
# input = open("advent13_test_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

# this function was me trying to do it using one recursive function
def compare_pairs(left, right):
    print("left, right ", left, right)
    if isinstance(left, int) and not isinstance(right, int):
        return compare_pairs([left], right)
    elif isinstance(right, int) and not isinstance(left, int):
        return compare_pairs(left, [right])
    elif not isinstance(left, int) and not isinstance(right, int):
        # Both are lists
        print("lengths ", len(left), len(right))
        if len(left) < len(right):
            return -1
        else:
            n_left = len(left)
            print("n_left ", n_left)
            for n in range(n_left):
                print("n of n_left ", n, n_left, left)
                if isinstance(left[n], int) and isinstance(right[n], int):
                    print("both ints, compare n", n, left[n], right[n])
                    result = compare_pairs(left[n], right[n])
                    if result != 0:
                        return result
                else:
                    # at least one is still a list
                    print("compare two 'lists' still ", left[n], right[n])
                    return compare_pairs(left[n], right[n])

            # we have gone through all of the list... return true?
            # return True
            # return compare_pairs(left[1:], right[1:])

    else:
        # both integers!
        if left < right:
            return 1
        if right > left:
            return -1
        if right == left:
            return 0

        # I think if we somehow got all the way through here then it's true?
        # return True

    print("how did I get here")


# Looking at actual solutions it seems as though two recursive functions are better
def compare_one_index(first, second):
    if type(first) is int and type(second) is int:
        comparison_result = 0
        if first > second:
            comparison_result = 1
        elif second > first:
            comparison_result = -1
        return comparison_result
    elif type(first) is list and type(second) is list:
        if len(first) == 0 and len(second) == 0:
            # Both sides ran out of items
            return 0
        elif len(first) == 0:
            # Left side ran out of items
            return -1
        elif len(second) == 0:
            # Right side ran out of items
            return 1
        else:
            # The same so go back and compare all again
            return compare_all_index(first, second)
    elif type(first) is int:
         return compare_one_index([first], second)
    elif type(second) is int:
        return compare_one_index(first, [second])

def compare_all_index(list1, list2):
    for i in range(min(len(list1), len(list2))):
        result = compare_one_index(list1[i], list2[i])

        if result != 0:
            return result

    if len(list1) < len(list2):
        # print("Left side ran out of items")
        return -1
    elif len(list1) == len(list2):
        # print("Same amount of items")
        return 0
    else:
        # print("Right side ran out of items")
        return 1

def part1():

    lefts = []
    rights = []

    n_line = 0

    for input_line in input_array:
        if n_line % 3 == 0:
            lefts.append(ast.literal_eval(input_line[:-1]))
            rights.append(ast.literal_eval(input_array[n_line+1][:-1]))

        n_line += 1


    print(lefts)
    print(rights)

    sum_success = 0
    n_pairs = len(lefts)
    for n in range(n_pairs):
        if compare_all_index(lefts[n], rights[n]) == -1:
            sum_success += (n+1)
        print("--------> n, sum_success ", n, sum_success)

    answer = sum_success

    return answer

def part2():

    # I think this can be done just using functools with the function(s) above
    packets = [[2],[6]]
    for input_line in input_array:
        if input_line != "\n":
            packets.append(ast.literal_eval(input_line[:-1]))

    print(packets)

    packets.sort(key=cmp_to_key(compare_all_index))

    print(packets)

    answer = (packets.index([2]) + 1) * (packets.index([6]) + 1)

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
