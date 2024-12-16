# Advent of code 2024, day 11

# open file
input = open("advent11_input.txt", "r")
# input = open("advent11_input_test1.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    stones = input_array[0][:-1].split(" ")

    print(stones)

    n_blinks = 25

    for nb in range(n_blinks):
        new_stones = []
        for stone in stones:
            stone_val = int(stone)
            if stone_val == 0:
                new_stones.append(str(1))
            elif len(stone) % 2 == 0:
                new_stones.append(str(stone_val//(10**(len(stone)//2))))
                new_stones.append(str(stone_val % (10**(len(stone)//2))))
            else:
                new_stones.append(str(stone_val*2024))

        print(nb, new_stones)
        stones = []
        for new_stone in new_stones:
            stones.append(new_stone)

    answer = len(new_stones)

    return answer

def part2():

    stones = input_array[0][:-1].split(" ")

    print(stones)

    n_blinks = 75

    stone_dict = {}
    for stone in stones:
        stone_dict[stone] = 1

    for nb in range(n_blinks):

        # print(stone_dict)
        new_stone_dict = {}
        for stone in stone_dict.keys():
            stone_val = int(stone)
            if stone_val == 0:
                if "1" in new_stone_dict.keys():
                    new_stone_dict["1"] += stone_dict[stone]
                else:
                    new_stone_dict["1"] = stone_dict[stone]
            elif len(stone) % 2 == 0:
                stone1 = str(stone_val//(10**(len(stone)//2)))
                if stone1 in new_stone_dict.keys():
                    new_stone_dict[stone1] += stone_dict[stone]
                else:
                    new_stone_dict[stone1] = stone_dict[stone]
                stone2 = str(stone_val % (10**(len(stone)//2)))
                if stone2 in new_stone_dict.keys():
                    new_stone_dict[stone2] += stone_dict[stone]
                else:
                    new_stone_dict[stone2] = stone_dict[stone]
            else:
                new_stone = str(stone_val * 2024)
                if new_stone in new_stone_dict.keys():
                    new_stone_dict[new_stone] += stone_dict[stone]
                else:
                    new_stone_dict[new_stone] = stone_dict[stone]

        # print(new_stone_dict)
        stone_dict = new_stone_dict

    answer = 0
    for key in stone_dict.keys():
        answer += stone_dict[key]

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
