# Advent of code, day 10

# open file
input = open("advent10_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    answer = 0

    # open_brackets = []
    syntax_error_score = 0
    n_inputs = len(input_array)
    for n in range(n_inputs):
        open_brackets = []
        for m in range(len(input_array[n])-1):
            if ((input_array[n][m] == "(") or (input_array[n][m] == "[") or
                (input_array[n][m] == "{") or (input_array[n][m] == "<")):
                open_brackets.append(input_array[n][m])
            elif (input_array[n][m] == ")"):
                current_open = open_brackets.pop(-1)
                if (current_open != "("):
                    syntax_error_score += 3
                    break
            elif (input_array[n][m] == "]"):
                current_open = open_brackets.pop(-1)
                if (current_open != "["):
                    syntax_error_score += 57
                    break
            elif (input_array[n][m] == "}"):
                current_open = open_brackets.pop(-1)
                if (current_open != "{"):
                    syntax_error_score += 1197
                    break
            elif (input_array[n][m] == ">"):
                current_open = open_brackets.pop(-1)
                if (current_open != "<"):
                    syntax_error_score += 25137
                    break

    answer = syntax_error_score

    return answer

def part2():

    answer = 0

    syntax_error_score = 0
    n_inputs = len(input_array)
    incomplete_scores = []
    for n in range(n_inputs):
        corrupted = False
        open_brackets = []
        for m in range(len(input_array[n])-1):
            if ((input_array[n][m] == "(") or (input_array[n][m] == "[") or
                (input_array[n][m] == "{") or (input_array[n][m] == "<")):
                open_brackets.append(input_array[n][m])
            elif (input_array[n][m] == ")"):
                current_open = open_brackets.pop(-1)
                if (current_open != "("):
                    corrupted = True
                    break
            elif (input_array[n][m] == "]"):
                current_open = open_brackets.pop(-1)
                if (current_open != "["):
                    corrupted = True
                    break
            elif (input_array[n][m] == "}"):
                current_open = open_brackets.pop(-1)
                if (current_open != "{"):
                    corrupted = True
                    break
            elif (input_array[n][m] == ">"):
                current_open = open_brackets.pop(-1)
                if (current_open != "<"):
                    corrupted = True
                    break

        if not corrupted:
            # The array needed to close is the opposite of the open_brackets
            n_open = len(open_brackets)
            closed_brackets = []
            total_score = 0
            for n in range(n_open):
                end_open = open_brackets.pop(-1)
                if (end_open == "("):
                    closed_brackets.append(")")
                    total_score = (total_score*5) + 1
                elif (end_open == "["):
                    closed_brackets.append("]")
                    total_score = (total_score*5) + 2
                elif (end_open == "{"):
                    closed_brackets.append("}")
                    total_score = (total_score*5) + 3
                elif (end_open == "<"):
                    closed_brackets.append(">")
                    total_score = (total_score*5) + 4

            incomplete_scores.append(total_score)

    # Answer is the middle score of all calculated incomplete scores
    sort_scores = sorted(incomplete_scores)
    n_incomplete = len(incomplete_scores)
    answer = sort_scores[(n_incomplete - 1) // 2]

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
