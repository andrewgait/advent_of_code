# Advent of code, day 12

# open file
input = open("advent12_input.txt", "r")
#input = open("advent12_test_input.txt", "r")

# read string into array
initial_data = []
# append some zeroes for the negative numbered pots
num_negative = 3
for i in range(num_negative):
    initial_data.append(0)

# the pot numbered 0 is at this location in the data array
zero_pot_location = num_negative

create_patterns = []
count_lines = 0
for line in input:
    if (count_lines == 0):
        # create the initial data array from the input
        for i in range(0,len(line)):
            if (line[i] == "#"):
                initial_data.append(1)
            elif (line[i] == "."):
                initial_data.append(0)
        # pad this initial_data with 4 zeroes?
        pad = 4
        for i in range(pad):
            initial_data.append(0)
    elif (count_lines > 1):
        print(len(line), line[9])
        create_line = []
        # if the last value is # then add to note
        if (line[9] == "#"):
            for i in range(5):
                if (line[i] == "#"):
                    create_line.append(1)
                else:
                    create_line.append(0)

            create_patterns.append(create_line)

    count_lines += 1

print('zero location: ', zero_pot_location, ' generation ', 0, ' data: ', initial_data)

data = initial_data
num_patterns = len(create_patterns)

# for part 2, can we test to see if the pattern repeats, then we don't need
# to run it for 50 billion generations ;-)
generations_array = []

# go through the initial data and populate as necessary
n_generations = 500 # 20
for n in range(n_generations):
    new_data = []
    for i in range(len(data)):
        # make a length 5 array of the nearby pots
        new_data.append(0)
        local_pots = []
        for j in range(i-2,i+3):
            if ((j < 0) or (j >= len(data))):
                local_pots.append(0)
            else:
                local_pots.append(data[j])

        # compare this to all the patterns we have
        for m in range(num_patterns):
            sum = 0
            for j in range(5):
                if (local_pots[j] == create_patterns[m][j]):
                    sum += 1

            # if the sum is 5, then the pattern has been found,
            # change the value in new_data and break
            if (sum == 5):
                new_data[i] = 1
                break

    # make data the same as new_data for the next loop
    data = []
    # if any of the final five pots have a plant, then append some extra zeroes
    plant_at_end = False
    for i in range(len(new_data)):
        data.append(new_data[i])
        if (i >= len(new_data)-5):
            if (new_data[i]==1):
                plant_at_end = True

    # I'm not sure but we may need to append more zeroes on the end to make this work
    if (plant_at_end):
        for i in range(4):
            data.append(0)

    # if any of the first five pots have a plant, then we need to append stuff to the front
    plant_at_start = False
    for i in range(5):
        if (new_data[i] == 1):
            plant_at_start = True

    if (plant_at_start):
        zero_pot_location += 4
        for i in range(4):
            data = [0] + data

    # observing the data, what happens is that after an initial period,
    # the values process by 1 upwards each time, which increments the sum by 63
    # I imagine that this sum increment is different depending upon the initial input :-)

    # this is an unnecessary bit of code for the actual problem, as I thought
    # what might happen would be that it would repeat and stabilise in a location
    # (as I was assuming there weren't a nassive number of plant pots...!)
    for m in range(len(generations_array)):
        # compare data with the generations_array
        sum = 0
        for i in range(len(generations_array[m])):
            if (data[i] == generations_array[m][i]):
                sum += 1

        if (sum == len(data)):
            print('generation ', m , ' matches current_generation ', n)

    generations_array.append(data)

    # after 20 generations, do a sum of the "pot values"
    sum_pots = 0
    for i in range(len(data)):
        if (data[i] == 1):
            sum_pots += (i-zero_pot_location)

    print('zero location: ', zero_pot_location, ' generation ', n+1,
          ' len(data) ', len(data), ' sum ', sum_pots, ' data: ', data)

    # so there is a pattern: the sum settles at going up by 63 each generation
    # after a while

    #print('sum total after 20 generations is ', sum_pots)

# so I know the incremental sum each generation (after 500 gens, at least) is 63,
# so I'm going to guess that this is the answer (and it is :-)):
print('value after 50 billion gens is ', sum_pots + ((50000000000-500)*63))

# this problem is evil if the left hand side grows as well, surely... :-(
