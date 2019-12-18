# Advent of code, day 14
import math

# open file
# input = open("advent14_input.txt", "r")
# input = open("advent14_test_input.txt", "r")
input = open("advent14_test_input2.txt", "r")
# input = open("advent14_test_input3.txt", "r")
# input = open("advent14_test_input4.txt", "r")
# input = open("advent14_test_input5.txt", "r")

required_dict = dict()
rhs_dict = dict()
rhs_amount = dict()

# read string into array
for line in input:
    input_line = line[:-1].split(" => ")
    required_dict[input_line[1]] = input_line[0]
    rhs_line = input_line[1].split(" ")
    rhs_dict[rhs_line[1]] = int(rhs_line[0])
    rhs_amount[rhs_line[1]] = 0

print(required_dict)
print(rhs_dict)
print(required_dict["1 FUEL"])

def get_list(str):
    return str.split(", ")

def get_id(element):
    split = element.split(" ")
    return split[1]

def get_value(element):
    split = element.split(" ")
    return int(split[0])

# some sort of recursive function is needed to do this
def get_stuff(id, value, req_value, total,
              required_dict, rhs_dict, rhs_amount):
    keystr = str(value)+" "+id
    list = get_list(required_dict[keystr])
    for n in range(len(list)):
        new_value = get_value(list[n])
        new_id = get_id(list[n])
        if (new_id=="ORE"):
            total += int(math.ceil(req_value / new_value)) * value
            print("reached ORE, ", req_value, value, new_value, new_id, total)
        else:
            # If e.g. in test 2 I am at AB, I need 2 (new_value) ABs
            # so this needs to go into the next layer

            value = rhs_dict[new_id] # // value) * acc_value * mult
#             mult = acc_value
#             value = int(math.ceil(req_value / value)) * new_value
            print("ID req_value value new_value",
                  new_id, req_value, value, new_value)
#             new_value = req_value * new_value
            rhs_amount[new_id] += new_value - int(math.ceil(new_value/req_value))
            print(rhs_amount)
            # I think at this point we need to work out whether we need to get stuff or not
            if rhs_amount[new_id] < value:
                total = get_stuff(new_id, value, new_value, total,
                                  required_dict, rhs_dict, rhs_amount)
            else:
                print('reduce amount in storage of ', new_id)
                rhs_amount[new_id] -= value

    return total

def part1(required_dict, rhs_dict, rhs_amount):

    id = "FUEL"
    value = 1
    mult = 1
#     v = 1
    total = 0

    total += get_stuff(id, value, mult, total,
                       required_dict, rhs_dict, rhs_amount)

    return total

def part2():

    answer = 0

    return answer

print("Part 1 answer: ", part1(required_dict, rhs_dict, rhs_amount))
print("Part 2 answer: ", part2())
