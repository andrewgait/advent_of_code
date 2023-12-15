# Advent of code 2023, day 12

# open file
input = open("advent12_input.txt", "r")
input = open("advent12_input_test.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    answer = 0

    for input in input_array:
        splitspace = input[:-1].split(" ")
        splitcomma = splitspace[1].split(",")
        broken_springs = [int(splitcom) for splitcom in splitcomma]

        print(broken_springs)

        condition_record = splitspace[0]

        possible_conditions = [""]

        for n in range(len(condition_record)):
            new_possible_conditions = []
            if condition_record[n] == "?":
                for possible_condition in possible_conditions:
                    # Add a . to the end of all of them
                    new_possible_conditions.append(possible_condition+".")
                    # Add a new array to the end of possible_conditions
                    new_possible_conditions.append(possible_condition+"#")
            else:
                # it's a . or # already so just add it to the current possible conditions
                for possible_condition in possible_conditions:
                    new_possible_conditions.append(possible_condition+condition_record[n])

            possible_conditions = new_possible_conditions

        # Loop over the possible conditions and work out if they are legitimate
        for possible_condition in possible_conditions:

            # work out the array
            n_poss = 0
            while possible_condition[n_poss] == ".":
                n_poss += 1
                if n_poss >= len(possible_condition):
                    break

            possible_broken_springs = [0]
            for nn in range(n_poss, len(possible_condition)):
                if possible_condition[nn] == "#":
                    possible_broken_springs[-1] += 1
                else:
                    possible_broken_springs.append(0)

            possible_broken_springs = [p for p in possible_broken_springs if p != 0]

            if possible_broken_springs == broken_springs:
                # print(possible_condition)
                answer += 1

    return answer

def part2():

    answer = 0

    for input in input_array:
        splitspace = input[:-1].split(" ")
        splitcomma = splitspace[1].split(",")
        broken_springs = [int(splitcom) for splitcom in splitcomma]

        broken_springs *= 5
        print(broken_springs)

        condition_record = splitspace[0]

        condition_record = condition_record + "?"
        condition_record *= 5
        condition_record = condition_record[:-1]

        print(condition_record)

        # Obviously making a list of possible conditions is now out of the question?
        possible_conditions = [""]

        for n in range(len(condition_record)):
            new_possible_conditions = []
            if condition_record[n] == "?":
                for possible_condition in possible_conditions:
                    # Add a . to the end of all of them
                    new_possible_conditions.append(possible_condition+".")
                    # Add a new array to the end of possible_conditions
                    new_possible_conditions.append(possible_condition+"#")
            else:
                # it's a . or # already so just add it to the current possible conditions
                for possible_condition in possible_conditions:
                    new_possible_conditions.append(possible_condition+condition_record[n])

            possible_conditions = new_possible_conditions

        print("possible conditions listed")
        # Loop over the possible conditions and work out if they are legitimate
        for possible_condition in possible_conditions:

            # work out the array
            n_poss = 0
            while possible_condition[n_poss] == ".":
                n_poss += 1
                if n_poss >= len(possible_condition):
                    break

            possible_broken_springs = [0]
            for nn in range(n_poss, len(possible_condition)):
                if possible_condition[nn] == "#":
                    possible_broken_springs[-1] += 1
                else:
                    possible_broken_springs.append(0)

            possible_broken_springs = [p for p in possible_broken_springs if p != 0]

            if possible_broken_springs == broken_springs:
                # print(possible_condition)
                answer += 1

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
