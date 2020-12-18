# Advent of code, day 18

# borrowed solution using classes
class Infix:
    def __init__(self, function):
        self.function = function
    def __ror__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))
    def __or__(self, other):
        return self.function(other)
    def __rlshift__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))
    def __rshift__(self, other):
        return self.function(other)
    def __call__(self, value1, value2):
        return self.function(value1, value2)


# open file
input = open("advent18_input.txt", "r")
# input = open("advent18_test_input.txt", "r")
# input = open("advent18_test_input2.txt", "r")
# input = open("advent18_test_input3.txt", "r")
# input = open("advent18_test_input4.txt", "r")
# input = open("advent18_test_input5.txt", "r")
# input = open("advent18_test_input6.txt", "r")
# input = open("advent18_test_input7.txt", "r")
# input = open("advent18_test_input8.txt", "r")
# input = open("advent18_test_input9.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

globals()['plus'] = Infix(lambda x, y: x + y)
globals()['mul'] = Infix(lambda x, y: x * y)

p1 = sum(eval(expr) for expr in
        [expr.replace('+', '|plus|').replace('*', '|mul|') for expr in input_array])

p2 = sum(eval(expr) for expr in
      [expr.replace('+', '<<plus>>').replace('*', '|mul|') for expr in input_array])

print("part1, part2: ", p1, p2)

# Rest of this is my attempt at a solution: part1 works, but can't get part2 right
# for all cases (trying to do it by inserting brackets to enforce operation order)

def evaluate_expression(expression_array, n, j, add):
#     print(expression_array)
    row_total = 0
    bracket_level = 0
    while j < n:
#         print("j is ", j)
        if expression_array[j][0] == "(":
            # get the new expression to be evaluated: search
            # forward until the number of ) is the same as the number of (
            n_left_bracket = 1
            if expression_array[j][1] == "(":
                n_left_bracket = 2
            n_right_bracket = 0
            # first element is the value but without the bracket
            new_expression = [expression_array[j]]
            size = 1
            while n_left_bracket != n_right_bracket:
                j += 1
                size += 1
                new_expression.append(expression_array[j])
                if (expression_array[j][-2:] == "))"):
                    n_right_bracket += 2
                elif (expression_array[j][-1] == ")"):
                    n_right_bracket += 1
                elif (expression_array[j][0] == "("):
                    n_left_bracket += 1

#                 print(j, n_left_bracket, n_right_bracket, new_expression, add)


            # I think at this point the array should be the correct size...
            # but there will be an extra brackets at the beginning and end
            new_expression[0] = new_expression[0][1:]
            new_expression[-1] = new_expression[-1][:-1]

            if add:
                row_total += evaluate_expression(new_expression, size, 0, add)
            else:
                # this seems like a fudge but it seems to work
                if (row_total == 0):
                    row_total = 1
                row_total *= evaluate_expression(new_expression, size, 0, add)


        else:
            if j == 0:
                row_total = int(expression_array[j])
            elif expression_array[j] == "+":
                add = True
#                 print(j, add)
            elif expression_array[j] == "*":
                add = False
#                 print(j, add)
            else:
                # it's a number, update accordingly:
                if add:
                    row_total += int(expression_array[j])
                else:
                    row_total *= int(expression_array[j])


#         print(j, row_total, expression_array)
        j += 1

    return row_total

def part1():

    answer = 0

    for i in range(len(input_array)):
        splitspace = input_array[i].split(" ")
        splitspace[-1] = splitspace[-1][:-1]

        n = len(splitspace)
        row_total = evaluate_expression(splitspace, n, 0, True)
        print(row_total)

        answer += row_total

    return answer

def part2():

    answer = 0

    # my feeling is you can do this using the previous idea with added
    # brackets... e.g. do
    # 1 + 2 * 3 + 4 * 5 + 6 -> (1 + 2) * (3 + 4) * (5 + 6) = 231
    # 2 * 3 + (4 * 5) -> 2 * (3 + (4 * 5)) = 46
    # 5 + (8 * 3 + 9 + 3 * 4 * 3) -> 5 + (8 * (3 + 9 + 3) * 4 * 3) = 1445

    # I've made this work for some cases but not all.  Not quite sure
    # exactly where it's going wrong.

    for i in range(len(input_array)):
        splitspace = input_array[i].split(" ")
        splitspace[-1] = splitspace[-1][:-1]  # remove trailing \n

        print(splitspace)
        j = 0

        while j < len(splitspace):
            # if there's a "+"
            if splitspace[j] == "+":
                # Add a bracket to the start of the previous entry...
                splitspace[j-1] = "("+splitspace[j-1]

                # how many brackets are on this entry?

                # now move forwards, and add another bracket if brackets balance
                # and you find a multiply
                n_left_bracket = 1
                n_right_bracket = 0

#                 k = j
                while n_left_bracket != n_right_bracket:
                    j += 1
                    if j < len(splitspace):
                        if splitspace[j] == "*":
                            if (splitspace[j-1][0] == "("):
                                n_left_bracket += 1
                                if (splitspace[j-1][1] == "("):
                                    n_left_bracket += 1
                            elif (splitspace[j-1][-1] == ")"):
                                n_right_bracket += 1
                                if (splitspace[j-1][-2] == ")"):
                                    n_right_bracket += 1
                            else:
                                splitspace[j-1] = splitspace[j-1]+")"
                                n_right_bracket += 1
                        elif splitspace[j] == "+":
                            if splitspace[j-1][0] != "(":
                                splitspace[j-1] = splitspace[j-1]+")"
                                n_right_bracket += 1
                    else:
                        n_right_bracket += 1
                        if splitspace[j-1][-1] != ")":
                            splitspace[j-1] = splitspace[j-1]+")"

                    print(j, n_left_bracket, n_right_bracket)

#                 splitspace[-1] = splitspace[-1]+")"
            else:
                j += 1


            print(j, splitspace)

        print(splitspace)

        n = len(splitspace)
        row_total = evaluate_expression(splitspace, n, 0, True)
        print(row_total)

        answer += row_total

    print(sys.maxsize)


    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
