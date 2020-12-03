# Advent of code, day 3

# open file
input = open("advent3_input.txt", "r")
# input = open("advent3_test_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def input_to_binary_array(input_array):
    binary_array = []

    n = len(input_array)
    for i in range(n):
        binary_line = []
        m = len(input_array[i])-1  # carriage return
        for j in range(m):
            if input_array[i][j] == '#':
                binary_line.append(1)
            else:
                binary_line.append(0)

        binary_array.append(binary_line)

    return binary_array

def count_trees_for_slopes(binary_array, right, down):
    n_rows = len(binary_array)
    n_columns = len(binary_array[0])

    inc_right = 0
    inc_down = 0
    count_trees = 0

    while inc_down < n_rows:
        right_loc = inc_right % n_columns
        if binary_array[inc_down][right_loc] == 1:
            count_trees += 1
        inc_down += down
        inc_right += right

    return count_trees

def part1():

    binary_array = input_to_binary_array(input_array)

    count_trees = count_trees_for_slopes(binary_array, 3, 1)

    return count_trees

def part2():

    binary_array = input_to_binary_array(input_array)

    count_trees1 = count_trees_for_slopes(binary_array, 1, 1)
    count_trees2 = count_trees_for_slopes(binary_array, 3, 1)
    count_trees3 = count_trees_for_slopes(binary_array, 5, 1)
    count_trees4 = count_trees_for_slopes(binary_array, 7, 1)
    count_trees5 = count_trees_for_slopes(binary_array, 1, 2)

    return count_trees1 * count_trees2 * count_trees3 * count_trees4 * count_trees5

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
