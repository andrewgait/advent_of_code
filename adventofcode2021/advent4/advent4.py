# Advent of code, day 4

# open file
input = open("advent4_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    answer = 0

    # Read in input numbers
    input_numbers = input_array[0].split(",")
    input_numbers[-1] = input_numbers[-1][:-1]
    print(input_numbers)

    # Read in bingo boards - work out number of boards first
    board_first_lines = []
    for n in range(len(input_array)):
        if ((n - 2) % 6) == 0:  # 5x5 board with a space
            board_first_lines.append(n)

    print(board_first_lines)
    bingo_boards = []
    marked_boards = []
    for bfl in board_first_lines:
        board = []
        marked_board = []
        for n in range(bfl, bfl+5):
            board_line = []
            for m in range(5):
                board_line.append(int(input_array[n][3*m:3*m+2]))
            marked_line = [0, 0, 0, 0, 0]
            board.append(board_line)
            marked_board.append(marked_line)

        bingo_boards.append(board)
        marked_boards.append(marked_board)

    print(bingo_boards)
    print(marked_boards)

    n_boards = len(bingo_boards)
    print(n_boards)

    winning_board = 0
    number_at_win = 0
    win = False
    # Loop over input numbers
    for input_number in input_numbers:
        number = int(input_number)
        # print("input_number is ", input_number)

        # mark boards
        for n in range(n_boards):
            for i in range(5):
                for j in range(5):
                    if bingo_boards[n][i][j] == number:
                        marked_boards[n][i][j] = 1

        # now test if any horizontal or vertical lines
        for n in range(n_boards):
            for i in range(5):
                sum_j = 0
                for j in range(5):
                    sum_j += marked_boards[n][i][j]
                if sum_j == 5:
                    winning_board = n
                    number_at_win = number
                    win = True
                    break

            for j in range(5):
                sum_i = 0
                for i in range(5):
                    sum_i += marked_boards[n][i][j]
                if sum_i == 5:
                    winning_board = n
                    number_at_win = number
                    win = True
                    break

            if win:
                break

        if win:
            break

    print("winning board ", winning_board, bingo_boards[winning_board])
    print("marked board ", winning_board, marked_boards[winning_board])
    print("number_at_win ", number_at_win)

    sum_win = 0
    for i in range(5):
        for j in range(5):
            if marked_boards[winning_board][i][j] == 0:
                sum_win += bingo_boards[winning_board][i][j]

    answer = sum_win * number_at_win

    return answer

def part2():

    answer = 0

    # Read in input numbers
    input_numbers = input_array[0].split(",")
    input_numbers[-1] = input_numbers[-1][:-1]
    print(input_numbers)

    # Read in bingo boards - work out number of boards first
    board_first_lines = []
    for n in range(len(input_array)):
        if ((n - 2) % 6) == 0:  # 5x5 board with a space
            board_first_lines.append(n)

    print(board_first_lines)
    bingo_boards = []
    marked_boards = []
    for bfl in board_first_lines:
        board = []
        marked_board = []
        for n in range(bfl, bfl+5):
            board_line = []
            for m in range(5):
                board_line.append(int(input_array[n][3*m:3*m+2]))
            marked_line = [0, 0, 0, 0, 0]
            board.append(board_line)
            marked_board.append(marked_line)

        bingo_boards.append(board)
        marked_boards.append(marked_board)

    print(bingo_boards)
    print(marked_boards)

    n_boards = len(bingo_boards)
    print(n_boards)

    winning_board = 0
    number_at_win = 0
    win = [0 for n in range(n_boards)]
    # Loop over input numbers
    for input_number in input_numbers:
        number = int(input_number)
        # print("input_number is ", input_number)

        # mark boards
        for n in range(n_boards):
            for i in range(5):
                for j in range(5):
                    if bingo_boards[n][i][j] == number:
                        marked_boards[n][i][j] = 1

        # now test if any horizontal or vertical lines
        for n in range(n_boards):
            for i in range(5):
                sum_j = 0
                for j in range(5):
                    sum_j += marked_boards[n][i][j]
                if sum_j == 5:
                    winning_board = n
                    number_at_win = number
                    win[n] = 1
                    sum_win = 0
                    for nn in range(n_boards):
                        if win[nn] == 1:
                            sum_win += 1
                    if sum_win == n_boards:
                        break

            for j in range(5):
                sum_i = 0
                for i in range(5):
                    sum_i += marked_boards[n][i][j]
                if sum_i == 5:
                    winning_board = n
                    number_at_win = number
                    win[n] = 1
                    sum_win = 0
                    for nn in range(n_boards):
                        if win[nn] == 1:
                            sum_win += 1
                    if sum_win == n_boards:
                        break

            sum_win = 0
            for nn in range(n_boards):
                if win[nn] == 1:
                    sum_win += 1
            if sum_win == n_boards:
                break

        sum_win = 0
        for nn in range(n_boards):
            if win[nn] == 1:
                sum_win += 1
        if sum_win == n_boards:
            break

    print("losing board ", winning_board, bingo_boards[winning_board])
    print("marked board ", winning_board, marked_boards[winning_board])
    print("number_at_win ", number_at_win)

    sum_win = 0
    for i in range(5):
        for j in range(5):
            if marked_boards[winning_board][i][j] == 0:
                sum_win += bingo_boards[winning_board][i][j]

    answer = sum_win * number_at_win

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
