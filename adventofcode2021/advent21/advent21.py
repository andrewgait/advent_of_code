# Advent of code, day 21

# open file
input = open("advent21_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)


def part1():

    answer = 0

    player1at = int(input_array[0].split(" ")[-1])
    player2at = int(input_array[1].split(" ")[-1])
    print(player1at, player2at)
    player1score = 0
    player2score = 0
    die100 = 1
    total_die_rolls = 0
    losing_score = 0
    winscore = 1000

    game_continuing = True
    while game_continuing:
        turnscore1 = 0
        for n in range(3):
            turnscore1 += die100
            die100 += 1
            if die100 > 100:
                die100 -= 100

        player1at = (player1at + turnscore1)
        if player1at > 10:
            player1at = player1at % 10
            if player1at == 0:
                player1at = 10
        player1score += player1at
        total_die_rolls += 3
        if (player1score >= winscore):
            losing_score = player2score
            break

        turnscore2 = 0
        for n in range(3):
            turnscore2 += die100
            die100 += 1
            if die100 > 100:
                die100 -= 100

        player2at = player2at + turnscore2
        if player2at > 10:
            player2at = player2at % 10
            if player2at == 0:
                player2at = 10
        player2score += player2at
        total_die_rolls += 3
        if (player2score >= winscore):
            losing_score = player1score
            break

        # print("die100, player1, player2, total rolls ",
        #       die100, player1score, player2score, total_die_rolls)

    answer = losing_score * total_die_rolls

    return answer


def part2():

    answer = 0

    player1at = int(input_array[0].split(" ")[-1])
    player2at = int(input_array[1].split(" ")[-1])
    print(player1at, player2at)

    # Tried something with recursion to start off with, but that goes a bit
    # crazy with recursion depth (and I don't want to kill my computer...)

    # How many ways can 3 dice sum to each number?
    ways = [0, 0, 0, 1, 3, 6, 7, 6, 3, 1]
    # Dict to hold "current" universes
    universes = { # (p1_pos, p2_pos, p1_score, p2_score, next_player) -> n_worlds
        (player1at, player2at, 0, 0, 0): 1,
    }
    wins0 = wins1 = 0
    # end when there are no more universes to investigate
    while universes:
        new_universes = {}
        for (p0, p1, s0, s1, turn), n in universes.items():
            for roll in range(3, 10):
                if turn == 0:
                    new_p0 = (p0 + roll) % 10
                    new_s0 = s0 + (new_p0 or 10)
                    if new_s0 >= 21:
                        wins0 += n * ways[roll]
                    else:
                        state = (new_p0, p1, new_s0, s1, 1)
                        new_universes[state] = new_universes.get(
                            state, 0) + n * ways[roll]
                else:
                    new_p1 = (p1 + roll) % 10
                    new_s1 = s1 + (new_p1 or 10)
                    if new_s1 >= 21:
                        wins1 += n * ways[roll]
                    else:
                        state = (p0, new_p1, s0, new_s1, 0)
                        new_universes[state] = new_universes.get(
                            state, 0) + n * ways[roll]
        universes = new_universes

    answer = max(wins0, wins1)

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
