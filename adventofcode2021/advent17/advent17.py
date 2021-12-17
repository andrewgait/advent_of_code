# Advent of code, day 17

# open file
input = open("advent17_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    answer = 0

    splitspace = input_array[0].split(" ")
    splitx = splitspace[2].split("..")
    splity = splitspace[3].split("..")
    x_min = int(splitx[0][2:])
    x_max = int(splitx[1][:-1])
    y_min = int(splity[0][2:])
    y_max = int(splity[1])

    print(x_min, x_max, y_min, y_max)

    successful = {}
    for start_xv in range(x_max+1):
        for start_yv in range(y_min, abs(y_min)):
            x = 0
            y = 0
            high_y = 0
            xv = start_xv
            yv = start_yv
            while (x <= x_max) and (y >= y_min):
                x += xv
                y += yv
                if xv > 0:
                    xv -= 1
                elif xv < 0:
                    xv += 1
                yv -= 1
                if y > high_y:
                    high_y = y

                if (x >= x_min) and (x <= x_max) and (y >= y_min) and (y <= y_max):
                    successful[(start_xv, start_yv)] = high_y

    print(successful)

    answer = max(successful.values())

    return answer

def part2():

    answer = 0

    splitspace = input_array[0].split(" ")
    splitx = splitspace[2].split("..")
    splity = splitspace[3].split("..")
    x_min = int(splitx[0][2:])
    x_max = int(splitx[1][:-1])
    y_min = int(splity[0][2:])
    y_max = int(splity[1])

    print(x_min, x_max, y_min, y_max)

    successful = {}
    for start_xv in range(x_max+1):
        for start_yv in range(y_min, abs(y_min)):
            x = 0
            y = 0
            high_y = 0
            xv = start_xv
            yv = start_yv
            while (x <= x_max) and (y >= y_min):
                x += xv
                y += yv
                if xv > 0:
                    xv -= 1
                elif xv < 0:
                    xv += 1
                yv -= 1
                if y > high_y:
                    high_y = y

                if (x >= x_min) and (x <= x_max) and (y >= y_min) and (y <= y_max):
                    successful[(start_xv, start_yv)] = high_y

    print(successful)

    answer = len(successful)

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
