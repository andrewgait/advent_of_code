# Advent of code, day 14

# open file
# input = open("advent14_input.txt", "r")
input = open("advent14_test_input.txt", "r")
# input = open("advent14_test_input2.txt", "r")
# input = open("advent14_test_input3.txt", "r")
# input = open("advent14_test_input4.txt", "r")
# input = open("advent14_test_input5.txt", "r")

required_dict = dict()
rhs_dict = dict()

# read string into array
for line in input:
    input_line = line[:-1].split(" => ")
    required_dict[input_line[1]] = input_line[0]
    rhs_line = input_line[1].split(" ")
    rhs_dict[rhs_line[1]] = int(rhs_line[0])

print(required_dict)
print(rhs_dict)
print(required_dict["1 FUEL"])

# really not sure how to do this.  not awake enough.  make another dict which determines which ids depend on others?

def get_list(str):
    return str.split(", ")

def get_id(element):
    split = element.split(" ")
    return split[1]

def get_value(element):
    split = element.split(" ")
    return int(split[0])

# some sort of recursive function is needed to do this
def get_stuff(id, value, total, required_dict, rhs_dict):
    keystr = str(value)+" "+id
    list = get_list(required_dict[keystr])
    for n in range(len(list)):
        acc_value = get_value(list[n])
        id = get_id(list[n])
        if (id=="ORE"):
            print("reached ORE, ", acc_value, value, id)
            total += acc_value 
        else:
            new_value = rhs_dict[id]
            print("ID acc_value value new_value ", id, acc_value, value, new_value)
            total = get_stuff(id, new_value, total, required_dict, rhs_dict)

    return total

def part1(required_dict, rhs_dict):

    id = "FUEL"
    value = 1
    total = 0

    total += get_stuff(id, value, total, required_dict, rhs_dict)

    return total

def part2():

    answer = 0

    return answer

print("Part 1 answer: ", part1(required_dict, rhs_dict))
print("Part 2 answer: ", part2())
