# Advent of code, day 6
import numpy

# open file
input = open("advent6_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    answer = 0

    lanternfish = input_array[0].split(",")
    n_fish = len(lanternfish)
    for n in range(n_fish):
        lanternfish[n] = int(lanternfish[n])

    # obvious way based on the way the question is asked ;)
    days = 80
    for day in range(days):
        n_fish = len(lanternfish)
        new_lanternfish = lanternfish
        for n in range(n_fish):
            if (lanternfish[n] == 0):
                new_lanternfish[n] = 6
                new_lanternfish.append(8)
            else:
                new_lanternfish[n] = lanternfish[n] - 1

        lanternfish = new_lanternfish

        # print(day+1, lanternfish)

    answer = len(lanternfish)

    return answer

def part2():

    answer = 0

    lanternfish = input_array[0].split(",")
    n_total_fish = len(lanternfish)

    # Could not see this at all without looking for hints; list fish by ages
    # and then calculate based on that
    fish_at_age = [0 for n in range(9)]
    for n in range(n_total_fish):
        lanternfish[n] = int(lanternfish[n])
        fish_at_age[lanternfish[n]] += 1

    print(fish_at_age)

    days = 256
    for day in range(days):
        new_fish_at_age = [0] * 9
        for n in range(9):
            if n == 6:
                new_fish_at_age[6] = fish_at_age[0] + fish_at_age[7]
            elif n == 8:
                new_fish_at_age[8] = fish_at_age[0]
            else:
                new_fish_at_age[n] = fish_at_age[n+1]

        fish_at_age = new_fish_at_age

    answer = sum(fish_at_age)

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
