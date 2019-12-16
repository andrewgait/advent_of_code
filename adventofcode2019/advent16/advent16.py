# Advent of code, day 16
import numpy as np

# open file
input = open("advent16_input.txt", "r")
# input = open("advent16_test_input.txt", "r")
# input = open("advent16_test_input2.txt", "r")
# input = open("advent16_test_input3.txt", "r")
# input = open("advent16_test_input4.txt", "r")
# input = open("advent16_test_input5.txt", "r")
# input = open("advent16_test_input6.txt", "r")
# input = open("advent16_test_input7.txt", "r")

input_array = None
# read string into array
for line in input:
    input_array = np.zeros(len(line), dtype=np.int32)
    for i in range(len(line)):
        input_array[i] = int(line[i])

print(input_array)

def create_repeating_pattern(n_inputs, output_at):
    pattern = np.zeros((n_inputs-output_at, n_inputs-output_at), dtype=np.int32)
    base_pattern = [0, 1, 0, -1]

    for n in range(n_inputs-output_at):
        # the row is output_at-1 zeros, then output_at 1s, output_at 0s, output_at -1s
        for m in range(n, n_inputs-output_at):
            pattern[n][m] = base_pattern[
                (((m+output_at)+1) // ((n+output_at)+1)) % 4]

    return pattern

def create_repeating_pattern_from(n_inputs, output_at):

    # This works quite nicely for the test examples, but sadly this array
    # is too big for my input :( must be a different way of doing it
    pattern = np.transpose(np.tri(
        n_inputs-output_at, n_inputs-output_at, 0, dtype=np.int32))

    return pattern


def multiply_by_pattern(input_array, pattern):
    n_inputs = len(input_array)
    output_array = np.zeros(n_inputs, dtype=np.int32)
    # note: we know by default that this is an upper-triangular matrix!

    # this is a matrix multiplication, right?  so find a numpy function to do it
    output_array = np.matmul(np.triu(pattern), input_array)

    for n in range(n_inputs):
        output_array[n] = abs(output_array[n]) % 10

    return output_array

# It's an upper triangular matrix, so the final value doesn't change,
# and the other values going backwards from that only change based on the
# previous value

def update_signal(input_array):  # , output_at):
    n_inputs = len(input_array)

    for n in reversed(range(1, n_inputs)):
        input_array[n-1] += input_array[n]

    for n in range(n_inputs):
        input_array[n] = abs(input_array[n]) % 10

    return input_array

def part1(input_array):

    n_inputs = len(input_array)
    big_pattern = create_repeating_pattern(n_inputs, 0)

    phases = 100

    for p in range(phases):
        print('phase ', p)
        input_array = multiply_by_pattern(input_array, big_pattern)

    answer = 0
    for n in range(8):
        answer += input_array[n] * (10**(7-n))

    return answer

def part2(input_array):

    repeat = 10000
    orig_size = len(input_array)
    large_input_array = np.zeros(repeat*len(input_array), dtype=np.int32)
    for n in range(len(large_input_array)):
        large_input_array[n] = input_array[n % orig_size]

    print(large_input_array)
    n_inputs = len(large_input_array)

    # the first seven digits of the original input array tell us
    # where to look to get the output
    output_at = 0
    for n in range(7):
        output_at += input_array[n] * (10**(6-n))

    print(' get output at, n_inputs ', output_at, n_inputs)

    # anything before this point doesn't matter (upper triangular matrix!)
    # so make a new input array from here

    new_input_array = large_input_array[output_at:]

    # This works for the test input, but creates an array that's too big otherwise
#     required_pattern = create_repeating_pattern_from(n_inputs, output_at)

    phases = 100

    for p in range(phases):
        print('phase ', p)
#         new_input_array = multiply_by_pattern(new_input_array, required_pattern)
        new_input_array = update_signal(new_input_array)

    print(new_input_array[:8])

    answer = 0
    for n in range(8):
        answer += new_input_array[n] * (10**(7-n))

    return answer

print("Part 1 answer: ", part1(input_array))
print("Part 2 answer: ", part2(input_array))
