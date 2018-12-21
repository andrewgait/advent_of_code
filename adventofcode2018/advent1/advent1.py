# Advent of code, day 1

# open file
input = open("advent1_input.txt", "r")

# data file has + or - as first character

# running totals
total = 0
rec_freq = []
total_array = []
freq_diff = True
for line in input:
    # print(line[0], len(line))
    # add or subtract depending on whether the first character is + or -
    # store in an array to avoid opening and closing files a lot (part 2)
    if (line[0] == "+"):
        add = int(line[1:])
        total += add
        total_array.append([1, add])
    elif (line[0] == "-"):
        sub = int(line[1:])
        total -= sub
        total_array.append([0, sub])

    # test whether the value appears in the recorded frequencies
    for i in range(len(rec_freq)):
        if (total == rec_freq[i]):
            print('reached frequency: ', rec_freq[i], ' again ', i)
            freq_diff = False

    rec_freq.append(total)

# output to check I'm not going crazy
print('the total is ', total)

# loop to try and find frequency value
while freq_diff:
    for j in range(len(total_array)):
        if (total_array[j][0] == 1):
            total += total_array[j][1]
        elif (total_array[j][0] == 0):
            total -= total_array[j][1]

        for i in range(len(rec_freq)):
            if (total == rec_freq[i]):
                print('reached frequency: ', rec_freq[i], ' again ', i)
                freq_diff = False
                # there should probably have been a break here

        rec_freq.append(total)

    print('the total is ', total)

input.close()

