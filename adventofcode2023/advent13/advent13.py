# Advent of code 2023, day 13

# open file
input = open("advent13_input.txt", "r")
# input = open("advent13_input_test.txt", "r")
# input = open("advent13_input_test2.txt", "r")
# input = open("advent13_input_test3.txt", "r")
# input = open("advent13_input_test4.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def get_patterns():
    patterns = []
    pattern = []
    for input in input_array:
        if input != "\n":
            pattern.append(input[:-1])
        else:
            patterns.append(pattern)
            pattern = []

    return patterns


def search_rows(pattern, previous_val=-1):
    n_rows = len(pattern)
    found_row_mirror=False
    # Search for a pair of matching rows
    for n_prow in range(1,n_rows):
        if pattern[n_prow-1] == pattern[n_prow]:
            # Loop backwards from n_prow-1 and forwards from n_prow
            up = n_prow-1
            down = n_prow
            found_row_mirror = True
            move = 1
            while (up-move) >= 0 and (down+move) < n_rows:
                if pattern[up-move] == pattern[down+move]:
                    found_row_mirror = True
                else:
                    found_row_mirror = False
                    break

                move += 1

            if found_row_mirror and (100 * n_prow) != previous_val:
                return 100 * n_prow, found_row_mirror

    return -1, found_row_mirror


def search_columns(pattern, previous_val=-1):
    # print("search columns ", previous_val)
    n_rows = len(pattern)
    found_column_mirror = False
    for n_pcol in range(1,len(pattern[0])):
        found_column_mirror = False
        # Make the two columns and test
        leftcolumn = ""
        rightcolumn = ""
        for n in range(n_rows):
            leftcolumn += pattern[n][n_pcol-1]
            rightcolumn += pattern[n][n_pcol]

        if leftcolumn == rightcolumn:
            left = n_pcol-1
            right = n_pcol
            found_column_mirror = True
            move = 1
            while (left-move) >= 0 and (right+move) < len(pattern[0]):
                nextleftcolumn = ""
                nextrightcolumn = ""
                for n in range(n_rows):
                    nextleftcolumn += pattern[n][left-move]
                    nextrightcolumn += pattern[n][right+move]

                if nextleftcolumn == nextrightcolumn:
                    found_column_mirror = True
                else:
                    found_column_mirror = False
                    break

                move += 1

            # if found_column_mirror:
            # print(found_column_mirror, n_pcol, " previous ", previous_val)
            if found_column_mirror and n_pcol != previous_val:
                return n_pcol, found_column_mirror
                # break

    return -1, found_column_mirror

def part1():

    patterns = get_patterns()

    answer = 0

    for pattern in patterns:
        row_val, found_row_mirror = search_rows(pattern)
        if row_val != -1:
            answer += row_val

        if not found_row_mirror:
            col_val, found_column_mirror = search_columns(pattern)
            if col_val != -1:
                answer += col_val

    return answer

def print_pattern(pattern):
    for n in range(len(pattern)):
        print(pattern[n])
    print(" ")

def part2():

    patterns = get_patterns()

    answer = 0

    for pattern in patterns:
        # print("pattern")
        # print_pattern(pattern)
        n_rows = len(pattern)
        n_cols = len(pattern[0])
        # print(n_rows, n_cols)
        row_val, found_row_mirror = search_rows(pattern)
        this_pattern_val = row_val

        if not found_row_mirror:
            col_val, found_column_mirror = search_columns(pattern)
            this_pattern_val = col_val

        new_pattern_val = this_pattern_val
        # Change one value in the pattern and run again
        row = 0
        col = 0
        while new_pattern_val == this_pattern_val:
            new_pattern = pattern.copy()
            if pattern[row][col] == "#":
                new_pattern[row] = str(pattern[row][:col])+"."+str(pattern[row][col+1:])
            else:
                new_pattern[row] = str(pattern[row][:col])+"#"+str(pattern[row][col+1:])

            # print("old pattern")
            # print_pattern(pattern)
            # print("new pattern ", row, col, this_pattern_val)
            # print_pattern(new_pattern)

            row_val, found_row_mirror = search_rows(new_pattern, this_pattern_val)
            if row_val != -1:
                new_pattern_val = row_val
                # print("new pattern val: ", new_pattern_val)

            if row_val != this_pattern_val:
                col_val, found_column_mirror = search_columns(new_pattern, this_pattern_val)
                if col_val != -1:
                    new_pattern_val = col_val
                    # print("new pattern val: ", new_pattern_val)

            row += 1
            if row == n_rows:
                row = 0
                col += 1
                # print(row, col)

        answer += new_pattern_val
        # print(answer)


    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
