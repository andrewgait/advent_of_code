# Advent of code, day 1

# open file
input = open("advent1_input.txt", "r")
#input = open("advent1_test_input1.txt", "r")
#input = open("advent1_test_input2.txt", "r")
#input = open("advent1_test_input3.txt", "r")
#input = open("advent1_test_input4.txt", "r")

# read string into array
for line in input:
    data = line

print('data', data, len(data))

# loop along said string for part 1
sum = 0
total = len(data)-1
for i in range(total):
    if (data[i] == data[(i-1) % total]):
        sum += int(data[i])

print('sum is ', sum)

# part 2
sum2 = 0
for i in range(total):
#    print(i, (i+(total/2)) % total)
    if (data[i] == data[(i+(total/2)) % total]):
        sum2 += int(data[i])

print('sum2 is ', sum2)
