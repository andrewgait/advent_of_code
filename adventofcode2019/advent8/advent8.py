# Advent of code, day 8
import numpy as np

# open file
input = open("advent8_input.txt", "r")
# input = open("advent8_test_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

width = 25
height = 6
# width = 3
# height = 2

n_layers = int(len(input_array[0]) / (width * height))

print(len(input_array[0]))
print(n_layers)

layers = []
count = 0

for n in range(n_layers):
    layer = np.zeros((width, height), dtype=np.int32)

    for j in range(height):
        for i in range(width):
            layer[i][j] = input_array[0][count]
            count += 1

    layers.append(layer)

# print(layers)


def part1(layers):

    min_zeros = height * width
    print(height, width, n_layers)
    min_layer = None
    for n in range(n_layers):
        count_zeros = 0
        for j in range(height):
            for i in range(width):
                if (layers[n][i][j] == 0):
                    count_zeros += 1

        print('layer ', n, ' zeros ', count_zeros)
        if count_zeros < min_zeros:
            min_zeros = count_zeros
            min_layer = n

    print(layers[min_layer])

    # in this layer count the 1s and 2s
    count_ones = 0
    count_twos = 0
    for j in range(height):
        for i in range(width):
            if (layers[min_layer][i][j] == 1):
                count_ones += 1
            elif (layers[min_layer][i][j] == 2):
                count_twos += 1

    print(count_ones, count_twos)
    answer = count_ones * count_twos

    return answer

def part2(layers):

    black = 0
    white = 1
    answer = np.zeros((width, height), dtype=np.int32)
    for j in range(height):
        for i in range(width):
            layer = 0
            while layers[layer][i][j] == 2:
                layer += 1
            if layers[layer][i][j] == white:
                answer[i][j] = white
            elif layers[layer][i][j] == black:
                answer[i][j] = black

    return np.transpose(answer)  # in order to read it better off the screen :)

print("Part 1 answer: ", part1(layers))
p2 = part2(layers)
print("Part 2 answer: \n")
for j in range(height):
    print(p2[j])
