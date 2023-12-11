# Advent of code 2023, day 11

# open file
input = open("advent11_input.txt", "r")
# input = open("advent11_input_test.txt", "r")
# input = open("advent11_input_test2.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    answer = 0

    # Start with assuming full columns and rows
    empty_columns = [n for n in range(len(input_array[0][:-1]))]
    empty_rows = [n for n in range(len(input_array))]

    n_rows = len(empty_rows)
    n_columns = len(empty_columns)

    print(empty_rows)
    print(empty_columns)

    for n_row in range(n_rows):
        print_row = ""
        for n_col in range(n_columns):
            print_row += input_array[n_row][n_col]
        print(print_row)
    print(" ")

    # Work out which rows / columns contain #
    for n in range(n_rows):
        if "#" in input_array[n]:
            empty_rows.remove(n)

        for m in range(n_columns):
            if input_array[n][m] == "#":
                if m in empty_columns:
                    empty_columns.remove(m)

    # Debug: check number of galaxies in original image
    galaxies = []
    for n_row in range(n_rows):
        for n_col in range(n_columns):
            if input_array[n_row][n_col] == "#":
                galaxies.append((n_row, n_col))

    print("There are ", len(galaxies), " galaxies in the original image")


    print(empty_rows)
    print(empty_columns)

    print(n_rows, n_columns)

    # Make a new array of size
    new_n_rows = len(empty_rows) + n_rows
    new_n_columns = len(empty_columns) + n_columns

    new_array = [["." for n_col in range(new_n_columns)] for n_row in range(new_n_rows)]

    column_lims = [0] + empty_columns + [n_columns]
    row_lims = [0] + empty_rows + [n_rows]
    print(column_lims)

    print(len(new_array), len(new_array[0]))

    n_add_row = 0
    for nn in range(len(row_lims[:-2])):
        for n_row in range(row_lims[nn]+n_add_row,row_lims[nn+1]+n_add_row):
            n_add_col = 0
            # Do the interior bits
            for mm in range(len(column_lims[:-2])):
                # Loop from column[0] to column[1]+1
                for n_col in range(column_lims[mm]+n_add_col,column_lims[mm+1]+n_add_col):
                    new_array[n_row][n_col] = input_array[n_row-n_add_row][n_col-n_add_col]

                new_array[n_row][n_add_col+column_lims[mm+1]+1] = "."

                n_add_col += 1

            # And the final loop
            for n_col in range(column_lims[-2]+n_add_col,new_n_columns):
                new_array[n_row][n_col] = input_array[n_row-n_add_row][n_col-n_add_col]

        # Add a new empty row
        for mm in range(new_n_columns):
            new_array[row_lims[nn+1]+n_add_row+1][mm] = "."

        n_add_row += 1

    # Do the remaining rows!
    for n_row in range(row_lims[-2]+n_add_row, new_n_rows):
        n_add_col = 0
        # Do the interior bits
        for nn in range(len(column_lims[:-2])):
            # Loop from column[0] to column[1]+1
            for n_col in range(column_lims[nn]+n_add_col,column_lims[nn+1]+n_add_col):
                new_array[n_row][n_col] = input_array[n_row-n_add_row][n_col-n_add_col]

            new_array[n_row][n_add_col+column_lims[nn+1]+1] = "."

            n_add_col += 1

        # And the final loop
        for n_col in range(column_lims[-2]+n_add_col,new_n_columns):
            new_array[n_row][n_col] = input_array[n_row-n_add_row][n_col-n_add_col]

    for n_row in range(new_n_rows):
        print_row = ""
        for n_col in range(new_n_columns):
            print_row += new_array[n_row][n_col]
        print(print_row)
    print(" ")

    # find all #s and work out distances
    galaxies = []
    for n_row in range(new_n_rows):
        for n_col in range(new_n_columns):
            if new_array[n_row][n_col] == "#":
                galaxies.append((n_row, n_col))

    print("There are ", len(galaxies), " galaxies")

    distance_dict = {}
    for galaxy in galaxies:
        for galaxy2 in galaxies:
            if galaxy != galaxy2:
                distance_dict[(galaxy, galaxy2)] = abs(galaxy2[0]-galaxy[0]) + abs(galaxy2[1]-galaxy[1])

    # print(distance_dict)

    # This will give double the number required
    # print(len(distance_dict), distance_dict)
    print(sum(distance_dict.values()))
    answer = sum(distance_dict.values()) // 2

    return answer

def part2():

    # Start with assuming full columns and rows
    empty_columns = [n for n in range(len(input_array[0][:-1]))]
    empty_rows = [n for n in range(len(input_array))]

    n_rows = len(empty_rows)
    n_columns = len(empty_columns)

    print(empty_rows)
    print(empty_columns)

    for n_row in range(n_rows):
        print_row = ""
        for n_col in range(n_columns):
            print_row += input_array[n_row][n_col]
        print(print_row)
    print(" ")

    # Work out which rows / columns contain #
    for n in range(n_rows):
        if "#" in input_array[n]:
            empty_rows.remove(n)

        for m in range(n_columns):
            if input_array[n][m] == "#":
                if m in empty_columns:
                    empty_columns.remove(m)

    # Debug: check number of galaxies in original image
    galaxies = []
    for n_row in range(n_rows):
        for n_col in range(n_columns):
            if input_array[n_row][n_col] == "#":
                galaxies.append((n_row, n_col))

    print("There are ", len(galaxies), " galaxies in the original image")

    # Part 2 made me go "doh, there's a much easier way of doing this"
    # When traversing between two galaxies, every time you hit an empty row
    # you need to add the "empty row distance" to the distance (you only
    # necessarily cross it once in any manhattan distance measure)

    distance = 1000000
    empty_distance = distance - 1

    distance_dict = {}
    for galaxy in galaxies:
        for galaxy2 in galaxies:
            if galaxy != galaxy2:
                extra_distance = 0
                # the extra distance is the number of empty rows / columns between the galaxies
                if galaxy2[0] > galaxy[0]:
                    for empty_row in empty_rows:
                        if empty_row > galaxy[0] and empty_row < galaxy2[0]:
                            extra_distance += empty_distance
                else:
                    for empty_row in empty_rows:
                        if empty_row > galaxy2[0] and empty_row < galaxy[0]:
                            extra_distance += empty_distance

                if galaxy2[1] > galaxy[1]:
                    for empty_column in empty_columns:
                        if empty_column > galaxy[1] and empty_column < galaxy2[1]:
                            extra_distance += empty_distance
                else:
                    for empty_column in empty_columns:
                        if empty_column > galaxy2[1] and empty_column < galaxy[1]:
                            extra_distance += empty_distance

                distance_dict[(galaxy, galaxy2)] = abs(galaxy2[0]-galaxy[0]) + abs(galaxy2[1]-galaxy[1]) + extra_distance

    # print(distance_dict)

    # This will give double the number required
    # print(len(distance_dict), distance_dict)
    print(sum(distance_dict.values()))
    answer = sum(distance_dict.values()) // 2

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
