# Advent of code 2022, day 20

# open file
input = open("advent20_input.txt", "r")
# input = open("advent20_test_input.txt", "r")
# input = open("advent20_test_input2.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    print("-2 % 7 is ", -2 % 7)
    print("-7 % 7 is ", -7 % 7)

    original_list = []
    current_list = []

    for input_line in input_array:
        original_list.append(int(input_line[:-1]))
        current_list.append(int(input_line[:-1]))

    print(current_list)
    n_original = len(original_list)
    print(n_original)

    for n in range(n_original):
        n_orig_index = n % n_original
        original_num = original_list[n_orig_index]

        # Find the number in the list
        current_index = current_list.index(original_num)

        new_index = (current_index + (original_num % n_original)) % n_original
        print(new_index, current_index, original_num)

        # delete from current_list
        del current_list[current_index]

        # Now what happens depends on whether the new index lands
        # before or after the index that was just deleted?
        if original_num < 0:
            current_list.insert(new_index-1, original_num)
        else:
            current_list.insert(new_index, original_num)

        print(current_list)


    print(current_list)
    zero_index = current_list.index(0)
    groves = []
    for nn in range(1000,4000,1000):
        after_index = (zero_index + nn) % n_original
        print(nn, after_index, zero_index)
        groves.append(current_list[after_index])

    print(groves)
    answer = sum(groves)

    return answer

def part2():

    answer = 0

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
