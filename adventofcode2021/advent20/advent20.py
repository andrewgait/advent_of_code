# Advent of code, day 20
from distlib.util import OR

# open file
input = open("advent20_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)


def print_image(image, border_size):
    n_j = len(image)
    n_i = len(image[0])
    lit_pixels = 0
    print("image_size: ", n_i, n_j)
    for j in range(n_j):
        strline = ""
        for i in range(n_i):
            if image[j][i] == 1:
                strline += "#"
                if ((i > border_size) and (i < n_i - border_size) and
                    (j > border_size) and (j < n_j - border_size)):
                    lit_pixels += 1
            else:
                strline += "."
        print(strline)
    print(" ")

    return lit_pixels


def add_border(input_image, border_size, flip=False):
    # add a border to the input_image
    n_j = len(input_image)
    n_i = len(input_image)
    new_input_image = []
    for j in range(n_j+border_size):
        new_input_line = []
        for i in range(n_i+border_size):
            # if ((i == 0) or (j == 0) or (i == n_i+3) or (j == n_j+3) or
            #     (i == 1) or (j == 1) or (i == n_i+2) or (j == n_j+2)):
            ii = i-((border_size//2))
            jj = j-((border_size//2))
            if ((ii < 0) or (jj < 0) or (ii > n_i-1) or (jj > n_j-1)):
                if flip:
                    new_input_line.append(1)
                else:
                    new_input_line.append(0)
            elif (input_image[j-5][i-5] == 1):
                new_input_line.append(1)
            else:
                new_input_line.append(0)

        new_input_image.append(new_input_line)

    return new_input_image


def part1():

    answer = 0

    enhancement = []

    enh_len = 512
    for n in range(enh_len):
        if input_array[0][n] == "#":
            enhancement.append(1)
        else:
            enhancement.append(0)

    input_image = []
    n_inputs = len(input_array)
    n_line = len(input_array[2]) - 1
    for j in range(2, n_inputs):
        input_line = []
        for i in range(n_line):
            if input_array[j][i] == "#":
                input_line.append(1)
            else:
                input_line.append(0)
        input_image.append(input_line)

    border_size = 10
    input_image = add_border(input_image, border_size)
    print_image(input_image, border_size)

    n_steps = 2
    for n in range(n_steps):
        # add a border to the input_image
        n_j = len(input_image)
        n_i = len(input_image)
        # new_input_image = []
        # for j in range(n_j+2):
        #     new_input_line = []
        #     for i in range(n_i+2):
        #         # if ((i == 0) or (j == 0) or (i == n_i+3) or (j == n_j+3) or
        #         #     (i == 1) or (j == 1) or (i == n_i+2) or (j == n_j+2)):
        #         if ((i == 0) or (j == 0) or (i == n_i+1) or (j == n_j+1)):
        #             new_input_line.append(0)
        #         elif (input_image[j-2][i-2] == 1):
        #             new_input_line.append(1)
        #         else:
        #             new_input_line.append(0)
        #
        #     new_input_image.append(new_input_line)

        new_input_image = add_border(input_image, border_size)

        # print("new input")
        # print_image(new_input_image, border_size)

        # make output image
        output_image = []
        for j in range(n_j+10):
            output_line = []
            for i in range(n_i+10):
                binary_str = ""
                # if (i == 0) or (j == 0) or (i == n_i+1) or (j == n_j+1):
                #     output_line.append(0)
                # else:
                for jj in range(j-1, j+2):
                    for ii in range(i-1, i+2):
                        if (jj < 0) or (ii < 0):
                            binary_str += "0"
                        elif (ii > n_i+1) or (jj > n_j+1):
                            binary_str += "0"
                        elif new_input_image[jj][ii] == 1:
                            binary_str += "1"
                        else:
                            binary_str += "0"

                # convert binary_str to integer
                e_index = int(binary_str, 2)
                # print(i, j, binary_str, e_index, enhancement[e_index])
                output_line.append(enhancement[e_index])

            output_image.append(output_line)

        # print("output")
        # answer = print_image(output_image, border_size)

        input_image = output_image

    answer = print_image(output_image, border_size)

    return answer

def part2():

    answer = 0

    enhancement = []

    enh_len = 512
    for n in range(enh_len):
        if input_array[0][n] == "#":
            enhancement.append(1)
        else:
            enhancement.append(0)

    input_image = []
    n_inputs = len(input_array)
    n_line = len(input_array[2]) - 1
    for j in range(2, n_inputs):
        input_line = []
        for i in range(n_line):
            if input_array[j][i] == "#":
                input_line.append(1)
            else:
                input_line.append(0)
        input_image.append(input_line)

    border_size = 10
    flip = False
    input_image = add_border(input_image, border_size, flip)
    print_image(input_image, border_size)

    n_steps = 50
    for n in range(n_steps):
        # add a border to the input_image
        n_j = len(input_image)
        n_i = len(input_image)
        # new_input_image = []
        # for j in range(n_j+2):
        #     new_input_line = []
        #     for i in range(n_i+2):
        #         # if ((i == 0) or (j == 0) or (i == n_i+3) or (j == n_j+3) or
        #         #     (i == 1) or (j == 1) or (i == n_i+2) or (j == n_j+2)):
        #         if ((i == 0) or (j == 0) or (i == n_i+1) or (j == n_j+1)):
        #             new_input_line.append(0)
        #         elif (input_image[j-2][i-2] == 1):
        #             new_input_line.append(1)
        #         else:
        #             new_input_line.append(0)
        #
        #     new_input_image.append(new_input_line)

        flip = (n % 2) == 1
        new_input_image = add_border(input_image, border_size, flip)

        # print("new input")
        # print_image(new_input_image, border_size)

        # make output image
        output_image = []
        for j in range(n_j+10):
            output_line = []
            for i in range(n_i+10):
                binary_str = ""
                # if (i == 0) or (j == 0) or (i == n_i+1) or (j == n_j+1):
                #     output_line.append(0)
                # else:
                for jj in range(j-1, j+2):
                    for ii in range(i-1, i+2):
                        if (jj < 0) or (ii < 0):
                            if flip:
                                binary_str += "1"
                            else:
                                binary_str += "0"
                        elif (ii > n_i+1) or (jj > n_j+1):
                            if flip:
                                binary_str += "1"
                            else:
                                binary_str += "0"
                        elif new_input_image[jj][ii] == 1:
                            binary_str += "1"
                        else:
                            binary_str += "0"

                # convert binary_str to integer
                e_index = int(binary_str, 2)
                # print(i, j, binary_str, e_index, enhancement[e_index])
                output_line.append(enhancement[e_index])

            output_image.append(output_line)


        input_image = output_image

    print("output")
    answer = print_image(output_image, border_size)

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
