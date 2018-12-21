# Advent of code, day 14

# part 2 isn't worded that well, I was confused what it was asking for initially

# open file
# input = open("advent14_input.txt", "r")

# input is the number of recipes to run for
input = '765071'  # my input is 765071  # int in part 1, string in part 2

digits = [int(digit) for digit in str(input)]  # part 2

n_elves = 2
elves_current = [3, 7]
elves_locations = [0, 1]

recipe_list = [3, 7]

# while (len(recipe_list)<10+input): # part 1
while ((recipe_list[-len(digits):] != digits) and
       (recipe_list[-len(digits)-1:-1] != digits)):  # part 2
    # sum the current recipes
    sum_current = 0
    for n in range(n_elves):
        sum_current += elves_current[n]

    if (sum_current < 10):
        # append the value to the array
        recipe_list.append(sum_current)
    else:
        # there are only two elves, so the sum will be between 10 and 18
        recipe_list.append(1)
        recipe_list.append(sum_current-((sum_current//10)*10))

    elves_locations = [(elves_locations[0]+1+elves_current[0]) % len(recipe_list),
                       (elves_locations[1]+1+elves_current[1]) % len(recipe_list)]

    elves_current = [recipe_list[elves_locations[0]], recipe_list[elves_locations[1]]]
#    print('elves_locations: ', elves_locations)
#    print('elves_current: ', elves_current)
#    print(recipe_list)

#print(recipe_list[input:input+10]) # part 1

print(len(recipe_list) - len(digits) -
      (0 if recipe_list[-len(digits):] == digits else 1)) # part 2
