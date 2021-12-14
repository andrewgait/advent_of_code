# Advent of code, day 14

# open file
input = open("advent14_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    answer = 0

    polymer = input_array[0][0:-1]

    print(polymer)

    # make rules dictionary
    rules = {}
    n_inputs = len(input_array)
    for n in range(2, n_inputs):
        splitspace = input_array[n].split(" ")
        rules[splitspace[0]] = splitspace[2][0:-1]

    print(rules)

    n_steps = 10
    length = len(polymer)

    # update polymer for 10 steps via insertion from rule
    # brute force method: just keep extending the polymer array
    for n in range(n_steps):
        new_polymer = ""
        for nn in range(length-1):
            pair = polymer[nn] + polymer[nn+1]
            insert = rules[pair]
            new_polymer += polymer[nn] + insert
            if (nn == length-2):
                new_polymer += polymer[nn+1]

        polymer = new_polymer
        length = len(polymer)

    print("After ", n_steps, " steps polymer has length ", length)
    # calculate number of each element
    elements = {}
    for nn in range(length):
        if polymer[nn] in elements.keys():
            elements[polymer[nn]] += 1
        else:
            elements[polymer[nn]] = 1

    print(elements)
    max = 0
    min = 99999999999999999999
    for value in elements.values():
        if value > max:
            max = value
        if value < min:
            min = value

    answer = max - min

    return answer

def part2():

    answer = 0
    polymer = input_array[0][0:-1]

    print(polymer)

    # make rules dictionary
    rules = {}
    n_inputs = len(input_array)
    for n in range(2, n_inputs):
        splitspace = input_array[n].split(" ")
        rules[splitspace[0]] = splitspace[2][0:-1]

    print(rules)

    n_steps = 40

    # brute force method of extending polymer will now take ages
    # instead, keep track of pairs and elements; elements just update,
    # and the pairs change each step i.e. NN -> B makes an NB and a BN; if
    # there are 5 NNs then this makes 5 NBs and 5 BNs
    polymer_pairs = {}
    polymer_elements = {}
    for n in range(len(polymer)):

        if polymer[n] in polymer_elements.keys():
            polymer_elements[polymer[n]] += 1
        else:
            polymer_elements[polymer[n]] = 1

        if (n < len(polymer) - 1):
            polymer_pair = polymer[n] + polymer[n+1]
            if polymer_pair in polymer_pairs.keys():
                polymer_pairs[polymer_pair] += 1
            else:
                polymer_pairs[polymer_pair] = 1

    print(polymer_elements)
    print(polymer_pairs)

    for n in range(n_steps):
        new_polymer_pairs = {}
        for key in polymer_pairs.keys():
            # add another value from the rules to the polymer_elements
            value = rules[key]
            if value in polymer_elements.keys():
                polymer_elements[value] += polymer_pairs[key]
            else:
                polymer_elements[value] = polymer_pairs[key]

            # add the number of two new pairs that there were of the old pair
            new_polymer_pair1 = key[0] + value
            new_polymer_pair2 = value + key[1]
            if new_polymer_pair1 in new_polymer_pairs.keys():
                new_polymer_pairs[new_polymer_pair1] += polymer_pairs[key]
            else:
                new_polymer_pairs[new_polymer_pair1] = polymer_pairs[key]
            if new_polymer_pair2 in new_polymer_pairs.keys():
                new_polymer_pairs[new_polymer_pair2] += polymer_pairs[key]
            else:
                new_polymer_pairs[new_polymer_pair2] = polymer_pairs[key]

        polymer_pairs = new_polymer_pairs

    print(polymer_elements)
    max = 0
    min = 99999999999999999999999
    for value in polymer_elements.values():
        if value > max:
            max = value
        if value < min:
            min = value

    answer = max - min

    return answer

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
