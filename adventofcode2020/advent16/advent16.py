# Advent of code 2020, day 16

# open file
input = open("advent16_input.txt", "r")
# input = open("advent16_test_input.txt", "r")
# input = open("advent16_test_input2.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def get_information(input_array):
#     n = len(input_array)
    # read the valid ticket info
    # make an array which is [first_lo, first_hi, second_lo, second_hi]
    valid_tickets_info = dict()
    i = 0
    while input_array[i] != "\n":
#         valid_ticket_info = []
        splitcolon = input_array[i].split(":")
        splitspace = splitcolon[1].split(" ")

        splitdash1 = splitspace[1].split("-")
        valid_tickets_info[splitcolon[0]] = []
        valid_tickets_info[splitcolon[0]].append(int(splitdash1[0]))
        valid_tickets_info[splitcolon[0]].append(int(splitdash1[1]))

        splitdash2 = splitspace[3].split("-")
        valid_tickets_info[splitcolon[0]].append(int(splitdash2[0]))
        valid_tickets_info[splitcolon[0]].append(int(splitdash2[1]))

#         valid_tickets_info.append(valid_ticket_info)

        i += 1

    # Next line is "your ticket", so skip it
    i += 2
    # split following line by commas
    splitcomma = input_array[i].split(",")
    your_ticket = []
    for j in range(len(splitcomma)):
        your_ticket.append(int(splitcomma[j]))

    # Next line is blank, line after is "nearby tickets"
    i += 3
    nearby_tickets = []
    while input_array[i] != "\n":
        splitcomma = input_array[i].split(",")
        nearby_ticket = []
        for j in range(len(splitcomma)):
            nearby_ticket.append(int(splitcomma[j]))

        nearby_tickets.append(nearby_ticket)
        i += 1

    return valid_tickets_info, your_ticket, nearby_tickets

def part1():

    valid_tickets_info, your_ticket, nearby_tickets = get_information(input_array)

    print(valid_tickets_info)
    print(your_ticket)
    print(nearby_tickets)

    # answer is the sum of invalid values found
    answer = 0
    for i in range(len(nearby_tickets)):
        for j in range(len(nearby_tickets[i])):
            value = nearby_tickets[i][j]
            valid = False
            for info in valid_tickets_info.values():
                if (((value >= info[0]) and (value <= info[1])) or
                    ((value >= info[2]) and (value <= info[3]))):
                    valid = True

            if not valid:
                answer += value


    return answer

def part2():

    valid_tickets_info, your_ticket, nearby_tickets = get_information(input_array)

    invalid_tickets = []
    for i in range(len(nearby_tickets)):
        for j in range(len(nearby_tickets[i])):
            value = nearby_tickets[i][j]
            valid = False
            for info in valid_tickets_info.values():
                if (((value >= info[0]) and (value <= info[1])) or
                    ((value >= info[2]) and (value <= info[3]))):
                    valid = True

            if not valid:
                invalid_tickets.append(i)

    print(nearby_tickets)

    for n in range(len(invalid_tickets)-1, -1, -1):
        nearby_tickets.pop(invalid_tickets[n])

    print(nearby_tickets)
    print(valid_tickets_info)

    # Now we have a list of valid tickets...
    # ... so we get information by "column"
    n_columns = len(nearby_tickets[0])
    column_desc = [[] for i in range(n_columns)]
#     print(column_desc)
    for j in range(n_columns):
        column_vals = []
        for i in range(len(nearby_tickets)):
            column_vals.append(nearby_tickets[i][j])

#         print(column_vals)

        # work out from this which part of the dict we are in
        for key, info in valid_tickets_info.items():
            n_found = 0
            for n in range(len(column_vals)):
                value = column_vals[n]
                if (((value >= info[0]) and (value <= info[1])) or
                    ((value >= info[2]) and (value <= info[3]))):
                    n_found += 1

#             print(key, info, n_found)

            if n_found == len(column_vals):
                # append the key value
                column_desc[j].append(key)

    print(column_desc)
    # This is now a list of all possibles...
    n_possibles = 0
    for j in range(n_columns):
        n_possibles += len(column_desc[j])

    desc_done = []
    while (n_possibles > n_columns):
        # Find the column with one descriptor
        single_desc = ""
        location = 0
        for j in range(n_columns):
            if ((column_desc[j][0] not in desc_done) and (len(column_desc[j]) == 1)):
                single_desc = column_desc[j][0]
                location = j

        desc_done.append(single_desc)

        # loop over all others and remove value from column desc
        for j in range(n_columns):
            if ((j != location) and (single_desc in column_desc[j])):
                column_desc[j].remove(single_desc)

        n_possibles = 0
        for j in range(n_columns):
            n_possibles += len(column_desc[j])

    print(column_desc)
    # Finally work out answer = mult of things that say departure
    answer = 1
    for j in range(n_columns):
        if column_desc[j][0][0:9] == "departure":
            answer *= your_ticket[j]

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
