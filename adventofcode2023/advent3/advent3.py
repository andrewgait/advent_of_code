# Advent of code 2023, day 3

# open file
input = open("advent3_input.txt", "r")
# input = open("advent3_input_test.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def part1():

    number_coords_match = []
    engine_schematic = []
    y = 0
    for input in input_array:
        engine_line = []
        x = 0
        number_coords = []
        number = ""
        for inp in input:
            if inp != "\n":
                engine_line.append(inp)
            if inp in digits:
                number_coords.append((x,y))
                number += inp
            elif number != "":
                number_coords_match.append([int(number), number_coords])
                number_coords = []
                number = ""

            x += 1

        engine_schematic.append(engine_line)
        y += 1

    # print(number_coords_match)
    n_y = len(engine_schematic)
    n_x = len(engine_line)

    sum = 0

    for number_coord in number_coords_match:
        coords = number_coord[1]
        symbol_found = False

        # loop around coordinates listed
        for coord in coords:
            x = coord[0]
            y = coord[1]
            for yy in range(y-1,y+2):
                for xx in range(x-1,x+2):
                    if xx >= 0 and xx < n_x and yy >= 0 and yy < n_y:
                        schematic = engine_schematic[yy][xx]
                        if schematic != "." and schematic not in digits:
                            symbol_found = True
                            break
                if symbol_found:
                    break

            if symbol_found:
                break

        if symbol_found:
            # print(number_coord)
            sum += number_coord[0]

    answer = sum

    return answer

def part2():

    number_coords_match = []
    engine_schematic = []
    y = 0
    for input in input_array:
        engine_line = []
        x = 0
        number_coords = []
        number = ""
        for inp in input:
            if inp != "\n":
                engine_line.append(inp)
            if inp in digits:
                number_coords.append((x,y))
                number += inp
            elif number != "":
                number_coords_match.append([int(number), number_coords])
                number_coords = []
                number = ""

            x += 1

        engine_schematic.append(engine_line)
        y += 1

    n_y = len(engine_schematic)
    n_x = len(engine_line)

    sum = 0

    # Loop through the engine_schematic
    # This does assume that none of the numbers surrounding the gear (*)
    # are the same (if they are then this would need a rethink)
    # As it is with my input, this works
    for y in range(n_y):
        for x in range(n_x):
            if engine_schematic[y][x] == "*":
                # print("coords ", x, y)
                numbers = set()
                gear_surround = []
                for xx in range(x-1,x+2):
                    for yy in range(y-1,y+2):
                        # gear_surround.append((x,y))
                        for number_coords in number_coords_match:
                            if (xx, yy) in number_coords[1]:
                                numbers.add(number_coords[0])

                # print(numbers)
                numbers = list(numbers)
                if len(numbers) == 2:
                    sum += numbers[0] * numbers[1]

    answer = sum

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
