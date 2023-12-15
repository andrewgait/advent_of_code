# Advent of code 2023, day 15

# open file
input = open("advent15_input.txt", "r")
# input = open("advent15_input_test.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def hash(instruction):
    current_value = 0
    for char_val in instruction:
        current_value += ord(char_val)
        current_value *= 17
        current_value = current_value % 256

    return current_value


def part1():

    answer = 0

    split_comma = input_array[0][:-1].split(",")

    for instruction in split_comma:
        answer += hash(instruction)

    return answer

def part2():

    answer = 0

    split_comma = input_array[0][:-1].split(",")

    boxes = [[] for n in range(256)]

    for instruction in split_comma:

        if "=" in instruction:
            split_equals = instruction.split("=")
            box_no = hash(split_equals[0])
            found = False
            for lens in boxes[box_no]:
                if split_equals[0] == lens[0]:
                    found = True
                    # remove from this box
                    boxes[box_no][boxes[box_no].index(lens)] = [
                        split_equals[0], int(split_equals[1])]
                    break
            if not found:
                boxes[box_no].append([split_equals[0], int(split_equals[1])])
        elif "-" in instruction:
            split_dash = instruction.split("-")
            box_no = hash(split_dash[0])
            found = False
            for lens in boxes[box_no]:
                if split_dash[0] == lens[0]:
                    found = True
                    # remove from this box
                    boxes[box_no].remove(lens)
                    break

        # print(boxes)

    for n_box in range(len(boxes)):
        box = boxes[n_box]
        for n_lens in range(len(box)):
            focusing_power = (n_box + 1) * (n_lens + 1) * box[n_lens][1]
            answer += focusing_power

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
