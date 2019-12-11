# Advent of code 2019, day 11
import numpy as np

# open file
input = open("advent11_input.txt", "r")
# input = open("advent11_test_input.txt", "r")
# input = open("advent11_test_input2.txt", "r")
# input = open("advent11_test_input3.txt", "r")

# read string into array
for line in input:
    input_string = line

input_list = input_string.split(",")
input_data = []
for i in range(len(input_list)):
    input_data.append(int(input_list[i]))

print(len(input_data))
codelen = len(input_data)

# extra memory space needed?
for i in range(500):
    input_data.append(0)

# make a separate copy for part2
part2_input_data = []
for i in range(len(input_data)):
    part2_input_data.append(input_data[i])
# print(input_data)

def get_operating_values(input_data, op_pos, par1, par2, par3, relative_base):
    if par1 == 2:
        loc1 = input_data[op_pos+1]+relative_base
    else:
        loc1 = input_data[op_pos+1]
    if par2 == 2:
        loc2 = input_data[op_pos+2]+relative_base
    else:
        loc2 = input_data[op_pos+2]

#     print(op_pos, par1, par2)
#     print(loc1, loc2)

    if par1 == 1:
        val1 = loc1
    else:
        val1 = input_data[loc1]
    if par2 == 1:
        val2 = loc2
    else:
        val2 = input_data[loc2]

    if par3 == 2:
        val3 = input_data[op_pos+3] + relative_base
    else:
        val3 = input_data[op_pos+3]

    return val1, val2, val3

def get_value(base_input_data, input, op_pos, relative_base):
    input_data = []
    for i in range(len(base_input_data)):
        input_data.append(base_input_data[i])

    outputs = []

    while op_pos < len(input_data):

        opcode = input_data[op_pos]
        par3 = (opcode // 10**4)
        next = opcode - (par3 * 10**4)
        par2 = (next // 10**3)
        next = next - (par2 * 10**3)
        par1 = (next // 10**2)
        next = next - (par1 * 10**2)
        instruction = next

        if (instruction==1):
            # add
            val1, val2, val3 = get_operating_values(
                input_data, op_pos, par1, par2, par3, relative_base)

            store_at = val3


            value = val1 + val2
            input_data[store_at] = value
            op_pos += 4
        elif (instruction==2):
            # multiply
            val1, val2, val3 = get_operating_values(
                input_data, op_pos, par1, par2, par3, relative_base)

            store_at = val3

            value = val1 * val2
            input_data[store_at] = value
            op_pos += 4
        elif (instruction==3):
            # input value
            store_at = input_data[op_pos+1]
            if par1 == 2:
                store_at = relative_base + input_data[op_pos+1]
            input_data[store_at] = input
            op_pos += 2
        elif (instruction==4):
            # output value
            value_at = input_data[op_pos+1]
            if par1 == 0:
                output = input_data[value_at]
            elif par1 == 2:
                output = input_data[value_at+relative_base]
            else:
                output = value_at
            op_pos += 2
            # in this case the output needs to be returned, not appended ?
            outputs.append(output)
            # when it gets to two outputs, send it
            if len(outputs)==2:
                return outputs, op_pos, relative_base, input_data
        elif (instruction==5):
            # jump if non-zero
            val1, val2, val3 = get_operating_values(
                input_data, op_pos, par1, par2, par3, relative_base)

            if val1 != 0:
                op_pos = val2
            else:  # "Do nothing" i.e. move on to the next instruction
                op_pos += 3
        elif (instruction==6):
            # jump if zero
            val1, val2, val3 = get_operating_values(
                input_data, op_pos, par1, par2, par3, relative_base)

            if val1 == 0:
                op_pos = val2
            else:  # "Do nothing" i.e. move on to the next instruction
                op_pos += 3
        elif (instruction==7):
            # if 1 less than 2
            val1, val2, val3 = get_operating_values(
                input_data, op_pos, par1, par2, par3, relative_base)
            store_at = val3

            if (val1 < val2):
                input_data[store_at] = 1
            else:
                input_data[store_at] = 0
            op_pos += 4
        elif (instruction==8):
            # if equals
            val1, val2, val3 = get_operating_values(
                input_data, op_pos, par1, par2, par3, relative_base)

            store_at = val3

            if (val1 == val2):
                input_data[store_at] = 1
            else:
                input_data[store_at] = 0
            op_pos += 4
        elif (instruction==9):
            # adjust the relative base
            if par1 == 1:
                relative_base += input_data[op_pos+1]
            elif par1 == 0:
                relative_base += input_data[input_data[op_pos+1]]
            else:
                relative_base += input_data[input_data[op_pos+1]+relative_base]

            op_pos += 2
        else:
            break

    return outputs, op_pos, relative_base, input_data

def draw_hull(hull):
    print("\n")
    for j in range(len(hull)):
        str = ""
        for i in range(len(hull[j])):
            if hull[j][i] == 0:
                str = str+"."
            elif hull[j][i] == 1:
                str = str+"#"
            else:
                str = str+"O"
        print(str)
    print("\n")

def test_robot():

    hull = np.zeros((5,5), dtype=np.int32)
    was_painted = np.zeros((5,5), dtype=np.int32)
#     draw_hull(hull)
    instructions = [0, (1,0), 0, (0,0), 0, (1,0), 0, (1,0), 1, (0,1), 0, (1,0),
                    0, (1,0)]

    current = [2, 2]
    dirn = 'up'
    # up 0, left 1, down 2, right 3 ?

    for i in range(len(instructions)//2):
        # ignore the input instruction in this instance
        outputs = instructions[(i*2)+1]
        print('outputs: ', outputs)
        hull[current[1]][current[0]] = outputs[0]
        was_painted[current[1]][current[0]] = 1
        if dirn == 'up':
            if outputs[1] == 0:
                dirn = 'left'
                current[0] -= 1
            else:
                dirn = 'right'
                current[0] += 1
        elif dirn == 'down':
            if outputs[1] == 0:
                dirn = 'right'
                current[0] += 1
            else:
                dirn = 'left'
                current[0] -= 1
        elif dirn == 'left':
            if outputs[1] == 0:
                dirn = 'down'
                current[1] += 1
            else:
                dirn = 'up'
                current[1] -= 1
        elif dirn == 'right':
            if outputs[1] == 0:
                dirn = 'up'
                current[1] -= 1
            else:
                dirn = 'down'
                current[1] += 1

    draw_hull(hull)

    answer = 0
    for j in range(len(hull)):
        for i in range(len(hull[j])):
            if was_painted[j][i]:
                answer += 1

    return answer

def do_painting(input_data, relative_base, op_pos,
                hull, was_painted, current, dirn):

    while True:

        input = hull[current[1]][current[0]]

        outputs, op_pos, relative_base, input_data = get_value(
            input_data, input, op_pos, relative_base)

        if outputs == []:
            break

        hull[current[1]][current[0]] = outputs[0]
        was_painted[current[1]][current[0]] = 1
        if dirn == 'up':
            if outputs[1] == 0:
                dirn = 'left'
                current[0] -= 1
            else:
                dirn = 'right'
                current[0] += 1
        elif dirn == 'down':
            if outputs[1] == 0:
                dirn = 'right'
                current[0] += 1
            else:
                dirn = 'left'
                current[0] -= 1
        elif dirn == 'left':
            if outputs[1] == 0:
                dirn = 'down'
                current[1] += 1
            else:
                dirn = 'up'
                current[1] -= 1
        elif dirn == 'right':
            if outputs[1] == 0:
                dirn = 'up'
                current[1] -= 1
            else:
                dirn = 'down'
                current[1] += 1

    return hull, was_painted

def part1(input_data, relative_base):
    # in this instance output should always be a set of two instructions
    # which tell the robot what to do at the current square
    op_pos = 0
    hull = np.zeros((101,101), dtype=np.int32)
    was_painted = np.zeros((101,101), dtype=np.int32)
    current = [50, 50]
    dirn = 'up'

#     draw_hull(hull)

    hull, was_painted = do_painting(input_data, relative_base, op_pos,
                                    hull, was_painted, current, dirn)

    draw_hull(hull)

    answer = 0
    for j in range(len(hull)):
        for i in range(len(hull[j])):
            if was_painted[j][i]:
                answer += 1

    return answer


def part2(input_data, relative_base):
    # in this instance output should always be a set of two instructions
    # which tell the robot what to do at the current square
    op_pos = 0
    hull = np.zeros((101,101), dtype=np.int32)
    was_painted = np.zeros((101,101), dtype=np.int32)
    current = [50, 50]
    dirn = 'up'

    # set the initial position to 1 rather than 0
    hull[current[1]][current[0]] = 1

#     draw_hull(hull)

    hull, was_painted = do_painting(input_data, relative_base, op_pos,
                                    hull, was_painted, current, dirn)

    draw_hull(hull)

    answer = 0
    for j in range(len(hull)):
        for i in range(len(hull[j])):
            if was_painted[j][i]:
                answer += 1

    return answer

answer = test_robot()

print("Test robot: answer ", answer)

relative_base = 0
print(input_data)
print('Part1: ', part1(input_data, relative_base))

relative_base = 0
print(part2_input_data)
print('Part2: ', part2(part2_input_data, relative_base))