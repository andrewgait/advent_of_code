# Advent of code, day 18
import ast

# open file
input = open("advent18_test_input2.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)


class Pair:
    def __init__(self, value1, value2, depth, left=None):
        self.__left = left
        self.__right = None
        self.__depth = depth
        self.__value = [value1, value2]

    def depth(self):
        return self.__depth

    def left(self):
        return self.__left

    def right(self):
        return self.__right

    def set_right(self, right):
        self.__right = right

    def set_left(self, left):
        self.__left = left

    def value(self):
        return self.__value

    def set_value1(self, v1):
        self.__value[0] = v1

    def set_value2(self, v2):
        self.__value[1] = v2

    def __repr__(self):
        return "Pair {} depth {}".format(self.__value, self.__depth,)


def make_list_from_str(list_string):
    this_list = ast.literal_eval(list_string)
    return this_list


def make_dict_from_str(list_string):
    depth_dict = {}
    return depth_dict


def make_pairs(list_string):
    pairs = []
    depth = 0
    parse_loc = 0
    while parse_loc < len(list_string):
        if list_string[parse_loc] == "[":
            depth += 1
            parse_loc += 1
        elif list_string[parse_loc] == "]":
            depth -= 1
            parse_loc += 1
        elif list_string[parse_loc] == ",":
            depth += 0
            parse_loc += 1
        else:
            # this isn't right if the second value is another pair (of pairs etc.)
            splitcomma = list_string[parse_loc:parse_loc+3].split(",")
            v1 = int(splitcomma[0])
            v2 = int(splitcomma[1])
            print(splitcomma)
            if len(pairs) == 0:
                pair = Pair(v1, v2, depth)
            else:
                pair = Pair(v1, v2, depth, pairs[-1])
                pairs[-1].set_right(pair)
            pairs.append(pair)
            parse_loc += 3

        print(parse_loc, pairs)

    return pairs


# def make_str_from_list(string_list):
#     str_list = "["
#
#
#     str_list += "]"
#     return str_list


def part1():

    answer = 0

    full_str_list = input_array[0][:-1]
    print("first input: ", full_str_list)

    pairs = make_pairs(full_str_list)

    print(pairs)

    lists = make_list_from_str(full_str_list)



    print(lists)

    n_inputs = len(input_array)
    for n in range(1, n_inputs):
        str_list = input_array[n][:-1]

        full_str_list = "[" + full_str_list + "," + str_list + "]"

        pairs = make_pairs(full_str_list)

        print(full_str_list)
        print(pairs)

        do_something = True
        while do_something:
            do_something = False
            new_pairs = []
            for n in range(len(pairs)):
                depth = pairs[n].depth()
                if depth > 4:
                    # explode pair
                    do_something = True
                    if pairs[n].left() is not None:
                        right_val = pairs[n].left().value()[1]
                        left_val = pairs[n].value()[0]
                        pairs[n].left().set_value2(right_val+left_val)
                    if pairs[n].right() is not None:
                        left_val = pairs[n].right().value()[0]
                        right_val = pairs[n].value()[1]
                        pairs[n].right().set_value1(left_val+right_val)

                    new_pair = Pair(0, 0, depth-1, pairs[n].left())
                    new_pair.set_right(pairs[n].right())
                    new_pairs.append(new_pair)


                    # add the rest of the pairs array
                    for nn in range(n+1, len(pairs)):
                        if nn == n+1:
                            pairs[nn].set_left(new_pair)
                        new_pairs.append(pairs[nn])

                    break

                else:
                    new_pairs.append(pairs[n])

            pairs = new_pairs
            print(pairs)

        new_list = make_list_from_str(full_str_list)
        print(new_list)

        # there must be an easier way of writing this which doesn't screw my brain up



    print(full_str_list)
    print(new_list)

    return answer

def part2():

    answer = 0

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
