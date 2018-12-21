# Advent of code, day 2

# open file
input = open("advent2_input.txt", "r")

# array of characters
char_array = []


twice = 0
thrice = 0

# loop over input
for line in input:
    char_same = []
    char_array.append(line)
    for i in range(len(line)):
        for j in range(len(line)):
            if (i != j):
                if (line[i]==line[j]):
                    if (len(char_same)==0):
                        char_same.append([line[i], 1])
                    else:
                        # is it in char_same already?
                        notfound = True
                        for k in range(len(char_same)):
                            if (char_same[k][0]==line[i]):
                                notfound = False
                                char_same[k][1] += 1
                        if notfound:
                            char_same.append([line[i], 1])

    find6 = False
    find2 = False
    for n in range(len(char_same)):
        if (char_same[n][1] == 6):
            find6 = True
        elif (char_same[n][1] == 2):
            find2 = True

    if find6:
        thrice += 1
    if find2:
        twice += 1

    print('char_same is ', char_same)

print('twice: ', twice, 'thrice: ', thrice, ' twice * thrice', twice*thrice)

print('PART TWO')
input.close()

input = open("advent2_input.txt", "r")

num_same_max = 0
for n in range(len(char_array)):
    for m in range(len(char_array)):
        if (n!=m):
            num_same = 0
            for i in range(len(char_array[n])):
                if (char_array[n][i] == char_array[m][i]):
                    num_same += 1

            if num_same > num_same_max:
                print('n m num_same', n, m, num_same)
                print('line n ', char_array[n])
                print('line m ', char_array[m])
                num_same_max = num_same
