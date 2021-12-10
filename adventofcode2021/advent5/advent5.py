# Advent of code, day 5

# open file
input = open("advent5_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    answer = 0

    x1 = []
    y1 = []
    x2 = []
    y2 = []
    n_inputs = len(input_array)
    for n in range(n_inputs):
        splitcomma = input_array[n].split(",")
        x1.append(int(splitcomma[0]))
        y2.append(int(splitcomma[-1])) # ends with \n
        splitspace = splitcomma[1].split(" ")
        y1.append(int(splitspace[0]))
        x2.append(int(splitspace[-1]))

    print(x1, y1, x2, y2)

    max_x = max(max(x1), max(x2))
    max_y = max(max(y1), max(y2))
    print(max_x, max_y)

    grid = []
    for i in range(max_x+1):
        line = []
        for j in range(max_y+1):
            line.append(0)
        grid.append(line)

    # print(grid)

    for n in range(n_inputs):
        if (x1[n] == x2[n]):
            if (y1[n] > y2[n]):
                for y in range(y2[n], y1[n]+1):
                    grid[x1[n]][y] += 1
            else:
                for y in range(y1[n], y2[n]+1):
                    grid[x1[n]][y] += 1

        if (y1[n] == y2[n]):
            if (x1[n] > x2[n]):
                for x in range(x2[n], x1[n]+1):
                    grid[x][y1[n]] += 1
            else:
                for x in range(x1[n], x2[n]+1):
                    grid[x][y1[n]] += 1

    # print(grid)

    for i in range(max_x+1):
        for j in range(max_y+1):
            if grid[i][j] > 1:
                answer += 1

    return answer

def part2():

    answer = 0

    x1 = []
    y1 = []
    x2 = []
    y2 = []
    n_inputs = len(input_array)
    for n in range(n_inputs):
        splitcomma = input_array[n].split(",")
        x1.append(int(splitcomma[0]))
        y2.append(int(splitcomma[-1])) # ends with \n
        splitspace = splitcomma[1].split(" ")
        y1.append(int(splitspace[0]))
        x2.append(int(splitspace[-1]))

    print(x1, y1, x2, y2)

    max_x = max(max(x1), max(x2))
    max_y = max(max(y1), max(y2))
    print(max_x, max_y)

    grid = []
    for i in range(max_x+1):
        line = []
        for j in range(max_y+1):
            line.append(0)
        grid.append(line)

    # print(grid)

    for n in range(n_inputs):
        if (x1[n] == x2[n]):
            if (y1[n] > y2[n]):
                for y in range(y2[n], y1[n]+1):
                    grid[x1[n]][y] += 1
            else:
                for y in range(y1[n], y2[n]+1):
                    grid[x1[n]][y] += 1
        elif (y1[n] == y2[n]):
            if (x1[n] > x2[n]):
                for x in range(x2[n], x1[n]+1):
                    grid[x][y1[n]] += 1
            else:
                for x in range(x1[n], x2[n]+1):
                    grid[x][y1[n]] += 1
        else:
            # must be a diagonal at 45 degrees
            # print("diagonal")
            if (x1[n] > x2[n]):
                if (y1[n] > y2[n]):
                    low_y = y2[n]
                    for x in range(x2[n], x1[n]+1):
                        # print(x, low_y)
                        grid[x][low_y] += 1
                        low_y += 1
                else:
                    high_y = y2[n]
                    for x in range(x2[n], x1[n]+1):
                        # print(x, high_y)
                        grid[x][high_y] += 1
                        high_y -= 1
            else:
                if (y1[n] > y2[n]):
                    high_y = y1[n]
                    for x in range(x1[n], x2[n]+1):
                        # print(x, high_y)
                        grid[x][high_y] += 1
                        high_y -= 1
                else:
                    low_y = y1[n]
                    for x in range(x1[n], x2[n]+1):
                        # print(x, low_y)
                        grid[x][low_y] += 1
                        low_y += 1

    # print(grid)

    for i in range(max_x+1):
        for j in range(max_y+1):
            if grid[i][j] > 1:
                answer += 1

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
