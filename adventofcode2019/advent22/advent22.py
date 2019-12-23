# Advent of code, day 22
import numpy as np

# open file
input = open("advent22_input.txt", "r")
# input = open("advent22_test_input.txt", "r")
# input = open("advent22_test_input2.txt", "r")
# input = open("advent22_test_input3.txt", "r")
# input = open("advent22_test_input4.txt", "r")

input_instructions = []
# read string into array
for line in input:
    input_instructions.append(line)

def cut(deck, cut_at):
    new_deck = np.concatenate((deck[cut_at:], deck[:cut_at]), axis=None)

    return new_deck

def deal_increment(deck, N):
    position = 0
    deck_size = len(deck)
    new_deck = np.zeros(deck_size, dtype=np.int32)
    for i in range(deck_size):
        new_deck[position] = deck[i]
        position = (position + N) % deck_size

    return new_deck

def part1(input_instructions):
    print(input_instructions)

    deck_size = 10
    deck = np.arange(deck_size)
    print(deck)

    print(cut(deck, 3))
    print(np.flip(deck))
    print(deal_increment(deck, 3))
    print(cut(deck, -4))

    deck_size = 10007
    deck = np.arange(deck_size)

    for n in range(len(input_instructions)):
        if (input_instructions[n][:3] == "cut"):
            value = int(input_instructions[n].split(" ")[1])
            deck = cut(deck, value)
        elif (input_instructions[n][5:9] == "into"):
            deck = np.flip(deck)
        elif (input_instructions[n][5:9] == "with"):
            value = int(input_instructions[n].split(" ")[3])
            deck = deal_increment(deck, value)

    print(deck)
    answer = 0
    for m in range(deck_size):
         if (deck[m] == 2019):
             answer = m
             break

    return answer

def part2():

    answer = 0

    return answer

print("Part 1 answer: ", part1(input_instructions))
print("Part 2 answer: ", part2())
