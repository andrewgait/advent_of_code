# Advent of code, day 2

# open file
input = open("advent2_input.txt", "r")
#input = open("advent2_test_input1.txt", "r")
#input = open("advent2_test_input2.txt", "r")

# read string into array
checksum = 0  # part 1
checksum2 = 0  # part 2
for line in input:
    data = line.split('\t')
#    print(data, int(data[-1]))

    size = len(data)
    min = 999999
    max = 0
    for i in range(size):
        if (int(data[i]) > max):
            max = int(data[i])
        if (int(data[i]) < min):
            min = int(data[i])

    checksum += (max-min)

    for i in range(size):
        finddivisors = False
        for j in range(i+1, size):
            if ((int(data[i]) % int(data[j])) == 0):
                finddivisors = True
                checksum2 += int(data[i])/int(data[j])
                break
            if ((int(data[j]) % int(data[i])) == 0):
                finddivisors = True
                checksum2 += int(data[j])/int(data[i])
                break

        if (finddivisors):
            break

print('checksum ', checksum)
print('checksum2 ', checksum2)