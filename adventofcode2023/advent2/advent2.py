# Advent of code 2023, day 2

# open file
input = open("advent2_input.txt", "r")
# input = open("advent2_input_test.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    max_red = 12
    max_green = 13
    max_blue = 14

    sum_id = 0

    for input in input_array:
        game_good = True
        game_string = input.split(":")[0]
        game_instructions = input.split(":")[1]
        game_id = int(game_string.split(" ")[1])
        # print(game_id)
        # Ignore the \n at the end
        games = game_instructions[:-1].split(";")

        for game in games:
            colours_inst = game.split(",")
            for colour_inst in colours_inst:
                colour = colour_inst[1:].split(" ")
                if colour[1] == "red" and int(colour[0]) > max_red:
                    game_good = False
                    break
                if colour[1] == "green" and int(colour[0]) > max_green:
                    game_good = False
                    break
                if colour[1] == "blue" and int(colour[0]) > max_blue:
                    game_good = False
                    break
            if not game_good:
                break

        if game_good:
            sum_id += game_id



    answer = sum_id

    return answer

def part2():

    sum_power = 0

    for input in input_array:
        max_red = 0
        max_green = 0
        max_blue = 0
        game_good = True
        game_string = input.split(":")[0]
        game_instructions = input.split(":")[1]
        game_id = int(game_string.split(" ")[1])
        # print(game_id)
        # Ignore the \n at the end
        games = game_instructions[:-1].split(";")

        for game in games:
            colours_inst = game.split(",")
            for colour_inst in colours_inst:
                colour = colour_inst[1:].split(" ")
                if colour[1] == "red" and int(colour[0]) > max_red:
                    max_red = int(colour[0])
                if colour[1] == "green" and int(colour[0]) > max_green:
                    max_green = int(colour[0])
                if colour[1] == "blue" and int(colour[0]) > max_blue:
                    max_blue = int(colour[0])

        power = max_red * max_green * max_blue
        sum_power += power

    answer = sum_power

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
