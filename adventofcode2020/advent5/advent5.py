# Advent of code, day 5
import numpy

# open file
input = open("advent5_input.txt", "r")
# input = open("advent5_test_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    answer = 0
    # This is a binary problem where F=0 B=1 for rows and L=0 R=1 for columns
    n = len(input_array)
    for i in range(n):
        row_str = input_array[i][0:7]
        column_str = input_array[i][7:10]
        row_bin_str = ""
        for j in range(7):
            if row_str[j] == "F":
                row_bin_str += "0"
            else:
                row_bin_str += "1"
        col_bin_str = ""
        for j in range(3):
            if column_str[j] == "L":
                col_bin_str += "0"
            else:
                col_bin_str += "1"
        row_int = int(row_bin_str, 2)
        col_int = int(col_bin_str, 2)
        seat_id = (row_int * 8) + col_int

        if (seat_id > answer):
            answer = seat_id

    return answer

def part2():

    answer = 0
    # This is a binary problem where F=0 B=1 for rows and L=0 R=1 for columns

    # In this part make a list of the seat IDs?
    seat_id_array = []

    n = len(input_array)
    for i in range(n):
        row_str = input_array[i][0:7]
        column_str = input_array[i][7:10]
        row_bin_str = ""
        for j in range(7):
            if row_str[j] == "F":
                row_bin_str += "0"
            else:
                row_bin_str += "1"
        col_bin_str = ""
        for j in range(3):
            if column_str[j] == "L":
                col_bin_str += "0"
            else:
                col_bin_str += "1"
        row_int = int(row_bin_str, 2)
        col_int = int(col_bin_str, 2)
        seat_id = (row_int * 8) + col_int
        seat_id_array.append(seat_id)

    # Now sort this array...
    sorted_seats = numpy.sort(numpy.array(seat_id_array))
    m = len(sorted_seats)
    for i in range(m):
        if (sorted_seats[i] != (sorted_seats[i+1]-1)):
            answer = sorted_seats[i+1]-1
            break

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
