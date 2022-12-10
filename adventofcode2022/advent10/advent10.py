# Advent of code 2022, day 10

# open file
input = open("advent10_input.txt", "r")
# input = open("advent10_test_input1.txt", "r")
# input = open("advent10_test_input2.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    X = 1
    Xarray = [1]
    for input_line in input_array:
        splitspace = input_line[:-1].split(" ")
        if splitspace[0] == "noop":
            Xarray.append(X)
        elif splitspace[0] == "addx":
            Xarray.append(X)
            Xarray.append(X)
            X += int(splitspace[1])

    print(len(input_array), len(Xarray), Xarray)

    answer = 0
    for value in range(20,260,40):
        print(value, Xarray[value])
        answer += Xarray[value] * value

    return answer

def part2():

    X = 1
    Xarray = [1]
    CRT = ""
    crtpos = 0
    for input_line in input_array:
        crtpos = crtpos % 40
        splitspace = input_line[:-1].split(" ")
        if splitspace[0] == "noop":
            Xarray.append(X)
            if (crtpos == X-1) or (crtpos == X) or (crtpos == X+1):
                CRT += "#"
            else:
                CRT += "."
            crtpos += 1
        elif splitspace[0] == "addx":
            Xarray.append(X)
            if (crtpos == X-1) or (crtpos == X) or (crtpos == X+1):
                CRT += "#"
            else:
                CRT += "."
            crtpos += 1
            Xarray.append(X)
            if (crtpos == X-1) or (crtpos == X) or (crtpos == X+1):
                CRT += "#"
            else:
                CRT += "."
            crtpos += 1
            X += int(splitspace[1])
        # print(CRT)

    print(CRT[:40])
    print(CRT[40:80])
    print(CRT[80:120])
    print(CRT[120:160])
    print(CRT[160:200])
    print(CRT[200:240])

    answer = 0
    for value in range(20,260,40):
        answer += Xarray[value] * value

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer should be above, the calculation is still: ", part2())
