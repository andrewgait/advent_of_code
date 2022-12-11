# Advent of code 2022, day 11
from collections import deque

# open file
input = open("advent11_input.txt", "r")
# input = open("advent11_test_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

# hugeint = 10 ** 500000
# print(hugeint)

def part1():

    monkey_items = []
    monkey_operations = []
    monkey_test_divisible = []
    monkey_true = []
    monkey_false = []

    new_monkey_items = []

    monkey_inspections = []

    current_line = 0
    for input_line in input_array:
        if input_line[0] == "M":
            monkey_inspections.append(0)
            new_monkey_items.append([])
            # read in data from following lines
            for n in range(1,6,1):
                splitspace1 = input_array[current_line+1].split(" ")
                items = []
                for m in range(4,len(splitspace1)):
                    items.append(int(splitspace1[m][:-1]))
            monkey_items.append(items)

            splitspace2 = input_array[current_line+2].split(" ")
            monkey_operations.append([splitspace2[5], splitspace2[6], splitspace2[7][:-1]])

            splitspace3 = input_array[current_line+3].split(" ")
            monkey_test_divisible.append(int(splitspace3[-1][:-1]))

            splitspace4 = input_array[current_line+4].split(" ")
            monkey_true.append(int(splitspace4[-1][:-1]))
            splitspace5 = input_array[current_line+5].split(" ")
            monkey_false.append(int(splitspace5[-1][:-1]))

            current_line += 7

    print(monkey_items)
    print(monkey_operations)
    print(monkey_test_divisible)
    print(monkey_true)
    print(monkey_false)
    print(monkey_inspections)

    print(new_monkey_items)

    n_monkeys = len(monkey_items)

    for round in range(20):

        for monkey in range(n_monkeys):
            # print("monkey_items: ", monkey_items)
            items = monkey_items[monkey]
            item_list = []
            for item in items:
                item_list.append(item)
            for item in item_list:
                monkey_inspections[monkey] += 1
                old = item
                # print("item ", item)
                new_item = 0
                if monkey_operations[monkey][1] == "*":
                    if monkey_operations[monkey][2] == "old":
                        new_item = old * old
                    else:
                        new_item = old * int(monkey_operations[monkey][2])
                else:
                    # operations are only + or *
                    if monkey_operations[monkey][2] == "old":
                        new_item = old + old
                    else:
                        new_item = old + int(monkey_operations[monkey][2])

                # Divide by 3
                new_item = new_item // 3

                if ((new_item % monkey_test_divisible[monkey]) == 0):
                    # print("new_item ", new_item, " to ", monkey_true[monkey])
                    monkey_items[monkey_true[monkey]].append(new_item)
                else:
                    # print("new_item ", new_item, " to ", monkey_false[monkey])
                    monkey_items[monkey_false[monkey]].append(new_item)

                monkey_items[monkey].pop(0)

        for monkey in range(n_monkeys):
            print("round ", round, " monkey ", monkey, " items ", monkey_items[monkey])

    print(monkey_inspections)

    max1 = max(monkey_inspections)
    monkey_inspections.pop(monkey_inspections.index(max1))
    max2 = max(monkey_inspections)

    answer = max1 * max2

    return answer


def add_new_item(monkey_deques, monkey, monkey_inspections, monkey_test_divisible,
                 monkey_true, monkey_false, old):
    for item in monkey_deques[monkey]:
        monkey_inspections[monkey] += 1

        new_item = item + old

        # new_item = new_item // 3

        if ((new_item % monkey_test_divisible[monkey]) == 0):
            # print("new_item ", new_item, " to ", monkey_true[monkey])
            monkey_deques[monkey_true[monkey]].append(new_item)
        else:
            # print("new_item ", new_item, " to ", monkey_false[monkey])
            monkey_deques[monkey_false[monkey]].append(new_item)

    monkey_deques[monkey] = deque([])

    return monkey_inspections, monkey_deques

def mult_new_item(monkey_deques, monkey, monkey_inspections, monkey_test_divisible,
                  monkey_true, monkey_false, old):
    for item in monkey_deques[monkey]:
        monkey_inspections[monkey] += 1

        new_item = item * old

        # new_item = new_item // 3

        if ((new_item % monkey_test_divisible[monkey]) == 0):
            # print("new_item ", new_item, " to ", monkey_true[monkey])
            monkey_deques[monkey_true[monkey]].append(new_item)
        else:
            # print("new_item ", new_item, " to ", monkey_false[monkey])
            monkey_deques[monkey_false[monkey]].append(new_item)

    # monkey_deques[monkey] = deque([])

    return monkey_inspections, monkey_deques

def add_new_item_self(monkey_deques, monkey, monkey_inspections, monkey_test_divisible,
                      monkey_true, monkey_false):
    for item in monkey_deques[monkey]:
        monkey_inspections[monkey] += 1

        new_item = item + item

        # new_item = new_item // 3

        if ((new_item % monkey_test_divisible[monkey]) == 0):
            # print("new_item ", new_item, " to ", monkey_true[monkey])
            monkey_deques[monkey_true[monkey]].append(new_item)
        else:
            # print("new_item ", new_item, " to ", monkey_false[monkey])
            monkey_deques[monkey_false[monkey]].append(new_item)

    # monkey_deques[monkey] = deque([])

    return monkey_inspections, monkey_deques


def mult_new_item_self(monkey_deques, monkey, monkey_inspections, monkey_test_divisible,
                       monkey_true, monkey_false, total_modulo):
    for item in monkey_deques[monkey]:
        monkey_inspections[monkey] += 1

        test_item = pow(item, 2, monkey_test_divisible[monkey])
        # new_item = pow(item, 2, hugeint)
        # new_item = squared[item]
        # for add in range(item):
        #     new_item += item

        # new_item = new_item // 3

        if (test_item == 0):
            # print("new_item ", new_item, " to ", monkey_true[monkey])
            monkey_deques[monkey_true[monkey]].append(
                pow(item, 2, total_modulo))
        else:
            # print("new_item ", new_item, " to ", monkey_false[monkey])
            monkey_deques[monkey_false[monkey]].append(
                pow(item, 2, total_modulo))

    # monkey_deques[monkey] = deque([])

    return monkey_inspections, monkey_deques

def part2():

    monkey_items = []
    monkey_operations = []
    monkey_test_divisible = []
    monkey_true = []
    monkey_false = []

    monkey_deques = []

    new_monkey_items = []

    monkey_inspections = []

    current_line = 0
    total_modulo = 1
    for input_line in input_array:
        if input_line[0] == "M":
            monkey_inspections.append(0)
            new_monkey_items.append([])
            # read in data from following lines
            for n in range(1,6,1):
                splitspace1 = input_array[current_line+1].split(" ")
                items = []
                for m in range(4,len(splitspace1)):
                    items.append(int(splitspace1[m][:-1]))
            monkey_items.append(items)
            monkey_deques.append(deque(items))

            splitspace2 = input_array[current_line+2].split(" ")
            if splitspace2[7][:-1] == "old":
                monkey_operations.append([splitspace2[5], splitspace2[6], 0])
            else:
                monkey_operations.append([splitspace2[5], splitspace2[6],
                                          int(splitspace2[7][:-1])])


            splitspace3 = input_array[current_line+3].split(" ")
            monkey_test_divisible.append(int(splitspace3[-1][:-1]))
            total_modulo *= int(splitspace3[-1][:-1])

            splitspace4 = input_array[current_line+4].split(" ")
            monkey_true.append(int(splitspace4[-1][:-1]))
            splitspace5 = input_array[current_line+5].split(" ")
            monkey_false.append(int(splitspace5[-1][:-1]))

            current_line += 7

    print(monkey_items)
    print(monkey_operations)
    print(monkey_test_divisible)
    print(monkey_true)
    print(monkey_false)
    print(monkey_inspections)

    print(new_monkey_items)

    n_monkeys = len(monkey_items)

    for round in range(10000):

        for monkey in range(n_monkeys):
            new_item = 0
            if monkey_operations[monkey][1] == "*":
                if monkey_operations[monkey][2] == 0:
                    monkey_inspections, monkey_deques = mult_new_item_self(
                        monkey_deques, monkey, monkey_inspections,
                        monkey_test_divisible, monkey_true, monkey_false,
                        total_modulo)
                else:
                    monkey_inspections, monkey_deques = mult_new_item(
                        monkey_deques, monkey, monkey_inspections,
                        monkey_test_divisible, monkey_true, monkey_false,
                        monkey_operations[monkey][2])
            else:
                # operations are only + or *
                if monkey_operations[monkey][2] == 0:
                    monkey_inspections, monkey_deques = add_new_item_self(
                        monkey_deques, monkey, monkey_inspections,
                        monkey_test_divisible, monkey_true, monkey_false)
                else:
                    monkey_inspections, monkey_deques = add_new_item(
                        monkey_deques, monkey, monkey_inspections,
                        monkey_test_divisible, monkey_true, monkey_false,
                        monkey_operations[monkey][2])

            monkey_deques[monkey] = deque([])

        if (round == 0) or (round == 19) or (round % 1000 == 0):
            print("round ", round)
            print(monkey_inspections)

        # for monkey in range(n_monkeys):
        #     print("round ", round, " monkey ", monkey, " items ", monkey_items[monkey])

    print(monkey_inspections)

    max1 = max(monkey_inspections)
    monkey_inspections.pop(monkey_inspections.index(max1))
    max2 = max(monkey_inspections)

    answer = max1 * max2

    return answer

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
