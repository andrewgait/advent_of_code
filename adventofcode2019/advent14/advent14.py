# Advent of code, day 14

# open file
# input = open("advent14_input.txt", "r")
input = open("advent14_test_input.txt", "r")
# input = open("advent14_test_input2.txt", "r")
# input = open("advent14_test_input3.txt", "r")
# input = open("advent14_test_input4.txt", "r")
# input = open("advent14_test_input5.txt", "r")

required_dict = dict()

# read string into array
for line in input:
    input_line = line[:-1].split(" => ")
    required_dict[input_line[1]] = input_line[0]

print(required_dict)
print(required_dict["1 FUEL"])

# really not sure how to do this.  not awake enough.  make another dict which determines which ids depend on others?

def get_list(str):
    return str.split(", ")

def get_id_and_value(element):
    split = element.split(" ")
    return int(split[0]), split[1]

def part1(required_dict):

    id = "FUEL"
    value = 1

    list = get_list(required_dict["1 FUEL"])

    print(list)
    for n in range(len(list)):
#         print(list[n])
        value, id = get_id_and_value(list[n])
        print(value, id)



    answer = 0

    return answer

def part2():

    answer = 0

    return answer

print("Part 1 answer: ", part1(required_dict))
print("Part 2 answer: ", part2())
