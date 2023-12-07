# Advent of code 2023, day 7
from _ast import Or
from distlib.util import OR

# open file
input = open("advent7_input.txt", "r")
# input = open("advent7_input_test.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)


card_rank_order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
card_rank_joker_order = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

card_rank_dict = {}
card_rank_joker_dict = {}
for n in range(len(card_rank_order)):
    card_rank_dict[card_rank_order[n]] = n
    card_rank_joker_dict[card_rank_joker_order[n]] = n

hand_rank_order = {"high card": 0, "one pair": 1, "two pair": 2, "three of a kind": 3,
                   "full house": 4, "four of a kind": 5, "five of a kind": 6}

print(card_rank_dict)

def part1():

    n_cards = 5

    hands_bids = {}

    for input in input_array:
        splitspace = input[:-1].split(" ")
        hands_bids[splitspace[0]] = int(splitspace[1])
        # hands_ranks[splitspace[0]] = 0

    # print(hands_bids)

    hands_type = {}

    for hand in hands_bids.keys():
        n_card_type = {}
        for card_rank in card_rank_order:
            n_card_type[card_rank] = 0
        for n in range(n_cards):
            n_card_type[hand[n]] += 1

        max_key = max(zip(n_card_type.values(), n_card_type.keys()))[1]
        max_value = max(n_card_type.values())

        if max_value == 5:
            hands_type[hand] = "five of a kind"
        elif max_value == 4:
            hands_type[hand] = "four of a kind"
        elif max_value == 1:
            hands_type[hand] = "high card"
        elif max_value == 3:
            # could be full house or three of a kind
            hands_type[hand] = "three of a kind"
            # if the remaining two cards are the same
            rem_cards = str.replace(hand, max_key, "")
            if rem_cards[0] == rem_cards[1]:
                hands_type[hand] = "full house"
        elif max_value == 2:
            # could be one pair or two pair
            hands_type[hand] = "one pair"
            # if two of the remaining three cards are the same
            rem_cards = str.replace(hand, max_key, "")
            if ((rem_cards[0] == rem_cards[1]) or
                (rem_cards[1] == rem_cards[2]) or
                (rem_cards[0] == rem_cards[2])):
                hands_type[hand] = "two pair"

    # print(hands_type)

    # now make an array of [hand, bid, hand_rank_value, first_in_hand_value, second_in_hand_value, ...]
    hand_array = []
    for hand in hands_bids.keys():
        hand_array.append([hand, hands_bids[hand], hand_rank_order[hands_type[hand]],
                          card_rank_dict[hand[0]], card_rank_dict[hand[1]],
                          card_rank_dict[hand[2]], card_rank_dict[hand[3]],
                          card_rank_dict[hand[4]]])

    # print(hand_array)

    sorted_hand_array = sorted(hand_array, key = lambda x: (x[2], x[3], x[4], x[5], x[6], x[7]))

    # print(sorted_hand_array)

    answer = 0
    for n in range(len(sorted_hand_array)):
        answer += (n+1)*sorted_hand_array[n][1]

    return answer

def part2():

    print(card_rank_joker_dict)
    n_cards = 5

    hands_bids = {}

    for input in input_array:
        splitspace = input[:-1].split(" ")
        hands_bids[splitspace[0]] = int(splitspace[1])
        # hands_ranks[splitspace[0]] = 0

    # print(hands_bids)

    hands_type = {}

    for hand in hands_bids.keys():
        n_card_type = {}
        for card_rank in card_rank_joker_order:
            n_card_type[card_rank] = 0
        for n in range(n_cards):
            n_card_type[hand[n]] += 1

        max_key = max(zip(n_card_type.values(), n_card_type.keys()))[1]
        max_value = max(n_card_type.values())

        if max_key != "J":
            if max_value == 5:
                hands_type[hand] = "five of a kind"
            elif max_value == 4:
                hands_type[hand] = "four of a kind"
                # If the remaining card is a J...
                rem_card = str.replace(hand, max_key, "")
                if rem_card[0] == "J":
                    hands_type[hand] = "five of a kind"
            elif max_value == 1:
                hands_type[hand] = "high card"
                # if one of the (remaining) cards is a J
                # this can only increase the answer to one pair
                # (there can't be more than one J as max_value=1)
                if "J" in hand:
                    hands_type[hand] = "one pair"
            elif max_value == 3:
                # could be full house or three of a kind
                hands_type[hand] = "three of a kind"
                # if the remaining two cards are the same
                rem_cards = str.replace(hand, max_key, "")
                if (rem_cards[0] == "J") and (rem_cards[1] == "J"):
                    hands_type[hand] = "five of a kind"
                elif (rem_cards[0] == "J") or (rem_cards[1] == "J"):
                    hands_type[hand] = "four of a kind"
                elif rem_cards[0] == rem_cards[1]:
                    hands_type[hand] = "full house"
            elif max_value == 2:
                # could be one pair or two pair
                hands_type[hand] = "one pair"
                # if two of the remaining three cards are the same
                rem_cards = str.replace(hand, max_key, "")

                # if there's a J in the remaining cards...
                if "J" in rem_cards:
                    # If there are two Js (there can't be three...)
                    rem_cards_noJ = str.replace(rem_cards, "J", "")
                    if len(rem_cards_noJ) == 1:
                        # two Js were removed
                        hands_type[hand] = "four of a kind"
                    else:
                        if rem_cards_noJ[0] == rem_cards_noJ[1]:
                            hands_type[hand] = "full house"
                        else:
                            hands_type[hand] = "three of a kind"
                else:
                    # no J
                    if ((rem_cards[0] == rem_cards[1]) or
                        (rem_cards[1] == rem_cards[2]) or
                        (rem_cards[0] == rem_cards[2])):
                        hands_type[hand] = "two pair"
        else:
            # max_key is a joker, so in each case we need to pick the next hand up
            # as it matches with anything else
            if max_value == 5:
                # Could be 5 Js I guess
                hands_type[hand] = "five of a kind"
            elif max_value == 4:
                # If there are 4 Js then this makes five of a kind too
                hands_type[hand] = "five of a kind"
            elif max_value == 1:
                # If there's one J then everything else must be distinct too
                hands_type[hand] = "one pair"
            elif max_value == 3:
                # 3 jokers, so could be five of a kind or four of a kind
                hands_type[hand] = "four of a kind"
                # if the remaining two cards are the same
                rem_cards = str.replace(hand, max_key, "")
                if rem_cards[0] == rem_cards[1]:
                    hands_type[hand] = "five of a kind"
            elif max_value == 2:
                #  2 jokers so min 3 of a kind
                hands_type[hand] = "three of a kind"
                # if two of the remaining three cards are the same
                rem_cards = str.replace(hand, max_key, "")
                if ((rem_cards[0] == rem_cards[1]) or
                    (rem_cards[1] == rem_cards[2]) or
                    (rem_cards[0] == rem_cards[2])):
                    hands_type[hand] = "four of a kind"

    # now make an array of [hand, bid, hand_rank_value, first_in_hand_value, second_in_hand_value, ...]
    hand_array = []
    for hand in hands_bids.keys():
        hand_array.append([hand, hands_bids[hand], hand_rank_order[hands_type[hand]],
                          card_rank_joker_dict[hand[0]], card_rank_joker_dict[hand[1]],
                          card_rank_joker_dict[hand[2]], card_rank_joker_dict[hand[3]],
                          card_rank_joker_dict[hand[4]]])

    sorted_hand_array = sorted(hand_array, key = lambda x: (x[2], x[3], x[4], x[5], x[6], x[7]))

    answer = 0
    for n in range(len(sorted_hand_array)):
        answer += (n+1)*sorted_hand_array[n][1]

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
