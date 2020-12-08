# Advent of code, day 7

# open file
input = open("advent7_input.txt", "r")
# input = open("advent7_test_input.txt", "r")
# input = open("advent7_test_input2.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)


def make_bag_tree_dict(input_array):
    n = len(input_array)
    bag_tree_dict = dict()
    for i in range(n):
        splitcontain = input_array[i].split(" contain ")
        # first two words of first entry is key value
        split_first_space = splitcontain[0].split(" ")
        key_val = split_first_space[0] + " " + split_first_space[1]
        if splitcontain[1][0:2] == "no":
            bag_tree_dict[key_val] = 0
        else:
            # this contains a dict too
            splitcomma = splitcontain[1][:-1].split(", ")
            m = len(splitcomma)
            node_dict = dict()
            node_list = []
            for j in range(m):
                split_spaces = splitcomma[j].split(" ")
                val_key = split_spaces[1] + " " + split_spaces[2]
                val_dict = dict()
                val_dict[val_key] = split_spaces[0]
                node_list.append(val_dict)

            bag_tree_dict[key_val] = node_list

    return bag_tree_dict



def get_key_set_for_bag_with_key(bag_tree_dict, key_value, key_set):
    keys = list(bag_tree_dict.keys())
    if key_value not in keys:
        key_set.add(key_value)
    else:
        for key in keys:
            this_dict_list = bag_tree_dict[key]
            if (this_dict_list != 0):
                for j in range(len(this_dict_list)):
                    next_keys = list(this_dict_list[j].keys())
                    for next_key in next_keys:
                        if (next_key == key_value):
                            key_set = get_key_set_for_bag_with_key(
                                bag_tree_dict, key, key_set)
                            key_set.add(key)

    return key_set


# this function goes in the opposite direction to what it should do...
def get_total_bags_from_key(bag_tree_dict, key_value, value, get_val=0):
    dict_val = bag_tree_dict[key_value]
    if (dict_val != 0):
        m = len(dict_val)
        get_val += int(value)
        for j in range(m):
            keys = list(dict_val[j].keys())
            values = list(dict_val[j].values())
            get_val += int(value) * get_total_bags_from_key(bag_tree_dict, keys[0], values[0])
    else:
        get_val = int(value)

    return get_val


def part1():

    bag_tree_dict = make_bag_tree_dict(input_array)

    # Traverse the list to find "shiny gold"

#     print(get_val_from_list(bag_tree_dict, "dark olive", 0))
    key_set = set()
    get_key_set_for_bag_with_key(bag_tree_dict, "shiny gold", key_set)

    answer = len(key_set)

    return answer

def part2():

    print("============ START PART 2 ===============")
    bag_tree_dict = make_bag_tree_dict(input_array)

    answer = get_total_bags_from_key(bag_tree_dict, "shiny gold", 1)

    print(answer)
    # I think this counts the original bag, so subtract that from the answer

    return answer - 1

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
