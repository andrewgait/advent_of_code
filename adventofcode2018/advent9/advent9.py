# Advent of code, day 9

# my input is n_players=426, last_marble=71938

n_players = 462 # 9
last_marble = 7193800 # 25

change_at = 23

# score array
score_array = []
for i in range(n_players):
    score_array.append(0)

# read string into array
first_marble = 0

# place this marble
game_data = []
game_data.append(first_marble)
current_player = 1
current_marble = 1
current_location = 0
while (current_marble <= last_marble):
#    print('current_marble: ', current_marble)
#    print('current_player: ', current_player)
#    print('current_location: ', current_location)

    new_game_data = []

    if ((current_marble % 23) == 0):
        # go left 7 in the array from current location
        if ((current_location - 7) >= 0):
            new_location = current_location - 7
        else:
            print('current location went past the left end of the array! ', current_marble)
            new_location = len(game_data) + (current_location - 7)
        score_left_7 = game_data[new_location]
        score_array[current_player-1] += current_marble + score_left_7
#        print('score_left_7: ', score_left_7)
        new_game_data = game_data[0:new_location]
        for j in range(new_location+1, len(game_data)):
            new_game_data.append(game_data[j])
        current_location = new_location
    else:
        if ((current_location + 1) >= len(game_data)):
            new_game_data.append(game_data[0])
            new_game_data.append(current_marble)
            current_location = 1
            if (len(game_data) > 1):
                for j in range(len(game_data)-1):
                    new_game_data.append(game_data[j+1])
        else:
            for j in range(current_location+2):
                new_game_data.append(game_data[j])
            new_game_data.append(current_marble)
            for j in range(len(game_data)-(current_location+2)):
                new_game_data.append(game_data[current_location+2+j])
            current_location += 2

#    print('new_game_data: ', new_game_data)

    game_data = new_game_data
    current_marble += 1
    current_player = (current_marble % n_players) + 1


print('score_array: ', score_array)
max_score = 0
winner = 0
for i in range(len(score_array)):
    if (score_array[i] > max_score):
        max_score = score_array[i]
        winner = i+1

print('max_score: ', max_score, ' by player ', winner)
