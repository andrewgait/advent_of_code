# Advent of code 2024, day 3
import re

# open file
input = open("advent3_input.txt", "r")
# input = open("advent3_test_input1.txt", "r")
# input = open("advent3_test_input2.txt", "r")

input_string = ""
# read string into array
for line in input:
    input_string += line

def part1():

    answer = 0

    print(input_string)

    # print(int("]"))

    # Find all instances of "mul("
    mulstart = [m.start() for m in re.finditer('mul', input_string)]
    print(mulstart)

    for start in mulstart:
        if input_string[start+3] == "(":
            splitcomma = input_string[start+4:].split(",")
            if splitcomma[0].isnumeric():
                splitrbracket = splitcomma[1].split(")")
                if splitrbracket[0].isnumeric():
                    # Need to check there is actually a right bracket after this number
                    if input_string[start+3+len(splitcomma[0])+1+len(splitrbracket[0])+1] == ")":
                        # print(splitcomma[0], splitrbracket[0], input_string[start:start+20])
                        answer += int(splitcomma[0]) * int(splitrbracket[0])

    return answer

def part2():

    answer = 0

    print(input_string)

    # print(int("]"))

    # Find all instances of "mul("
    mulstart = [m.start() for m in re.finditer('mul', input_string)]
    print(mulstart)

    # Find all instances of don't() and do()
    dostart = [0] + [m.start() for m in re.finditer('do\(\)', input_string)]
    dontstart = [m.start() for m in re.finditer("don't\(\)", input_string)]
    print(dostart, "length", len(dostart))
    print(dontstart, "length", len(dontstart))

    # Make a list of locations which are under "do()"
    do_locations = []
    while len(dostart) > 0 and len(dontstart) > 0:
        do_locations += [n for n in range(dostart[0], dontstart[0])]
        # remove any locations in do that were before the first don't
        if len(dontstart) > 0:
            remove = -1
            for mm in range(len(dostart)):
                if dostart[mm] < dontstart[0]:
                    remove = mm
            if remove >= 0:
                dostart = dostart[remove+1:]
        # Now remove any locations in don't that are before the next do
        if len(dostart) > 0:
            remove = -1
            for mm in range(len(dontstart)):
                if dontstart[mm] < dostart[0]:
                    remove = mm
            if remove >= 0:
                dontstart = dontstart[remove+1:]

        # print(len(dostart), dostart)
        # print(len(dontstart), dontstart)
        # print(do_locations)

    # If do list max was larger than don't list, need to add the remaining dos
    if len(dostart) > 0:
        do_locations += [n for n in range(dostart[0],len(input_string))]

    # Remove all mulstart values not in the list of locations
    for start in mulstart:
        if start in do_locations:
            if input_string[start+3] == "(":
                splitcomma = input_string[start+4:].split(",")
                if splitcomma[0].isnumeric():
                    splitrbracket = splitcomma[1].split(")")
                    if splitrbracket[0].isnumeric():
                        # Need to check there is actually a right bracket after this number
                        if input_string[start+3+len(splitcomma[0])+1+len(splitrbracket[0])+1] == ")":
                            # print(splitcomma[0], splitrbracket[0], input_string[start:start+20])
                            answer += int(splitcomma[0]) * int(splitrbracket[0])

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
