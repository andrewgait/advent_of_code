# part 1 was pretty naive, there must be a better way
# this was a solution on the Reddit thread

from collections import deque, defaultdict

def game(n_players, last_marble):
    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(1, last_marble + 1):
        # div by 23, counter-clockwise 7
        if ((marble % 23) == 0):
            circle.rotate(7)
            scores[marble % n_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values()) if scores else 0

print('players last_marble max_score')
print(9, 25, game(9, 25))
print(10, 1618, game(10, 1618))
print(13, 7999, game(13, 7999))
print(17, 1104, game(17, 1104))
print(21, 6111, game(21, 6111))
print(30, 5807, game(30, 5807))
print(462, 71938, game(462, 71938))
print(462, 7193800, game(462, 7193800))

