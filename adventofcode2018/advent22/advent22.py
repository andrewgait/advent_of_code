# Advent of code, day 22

# open file
input = open("advent22_input.txt", "r")
#input = open("advent22_test_input.txt", "r")


def char_from_val(val):
    characters = ['.', '=', '|', 'M', 'T']
    return characters[val]


def val_from_char(char):
    characters = ['.', '=', '|', 'M', 'T']
    return characters.index(char)


def render_map(grid):
    for j in range(len(grid)):
        render_line = ''
        for i in range(len(grid[j])):
            render_line += char_from_val(grid[j][i])

        print(render_line)

    print(' ')


# read string into array
ll = 0
depth = 0
xtarget = 0
ytarget = 0
for line in input:
    if (ll == 0):
        depth = int(line.rsplit(' ', 1)[1])
        ll += 1
    else:
        data1 = line.rsplit(' ', 1)[1]
        data2 = data1.rsplit(',', 1)
        xtarget = int(data2[0])
        ytarget = int(data2[1])


print(depth, xtarget, ytarget)

y_mul = 16807
x_mul = 48271
erosion_mod = 20183
type_mod = 3

geologic_index_map = []
erosion_level_map = []
type_map = []
distance_map = []
equip1 = []
equip2 = []

for j in range(ytarget*10):
    geologic_index = []
    erosion_level = []
    type = []
    distance = []
    equip = []
    for i in range(xtarget*100):
        if ((i==0) and (j==0)):
            geologic = 0
            geologic_index.append(geologic)
            erosion = (geologic + depth) % erosion_mod
            erosion_level.append(erosion)
            type.append(erosion % type_mod)
        elif ((i==xtarget) and (j==ytarget)):
            geologic = 0
            geologic_index.append(geologic)
            erosion = (geologic + depth) % erosion_mod
            erosion_level.append(erosion)
            type.append(erosion % type_mod)
        elif (j==0):
            geologic = i * y_mul
            geologic_index.append(geologic)
            erosion = (geologic + depth) % erosion_mod
            erosion_level.append(erosion)
            type.append(erosion % type_mod)
        elif (i==0):
            geologic = j * x_mul
            geologic_index.append(geologic)
            erosion = (geologic + depth) % erosion_mod
            erosion_level.append(erosion)
            type.append(erosion % type_mod)
        else:
            geologic = erosion_level_map[j-1][i] * erosion_level[i-1]
            geologic_index.append(geologic)
            erosion = (geologic + depth) % erosion_mod
            erosion_level.append(erosion)
            type.append(erosion % type_mod)
        distance.append(0)
        equip.append(0)

    geologic_index_map.append(geologic_index)
    erosion_level_map.append(erosion_level)
    type_map.append(type)
    distance_map.append(distance)
    equip1.append(equip)
    equip2.append(equip)

render_map(type_map)

sum_risk = 0
for j in range(ytarget+1):
    for i in range(xtarget+1):
        sum_risk += type_map[j][i]

print('risk level is ', sum_risk)

# part 2: start from the target and work out route values from it?
# You have to have a torch equipped at the rocky target.
# no torch in wet
# no climbing gear in narrow
# no neither in rock

import heapq
queue = [(0, 0, 0, 1)]  # minutes, x, y, cannot
best = dict()  # (x, y, cannot) : minutes

target = (xtarget, ytarget, 1)
while queue:
    minutes, x, y, cannot = heapq.heappop(queue)
    best_key = (x, y, cannot)
    if best_key in best and best[best_key] <= minutes:
        continue
    best[best_key] = minutes
    if best_key == target:
        print(minutes, ' minutes')
        break
    for i in range(3):  # rocky:neither, wet:torch, narrow:climb
        if ((i != cannot) and (i != type_map[y][x])):
            heapq.heappush(queue, (minutes + 7, x, y, i))

#    print(x,y)
    # up down left right
    for dx, dy in [[-1,0], [1,0], [0,-1], [0,1]]:
        newx = x + dx
        newy = y + dy
        if (newx < 0):
            continue
        if (newy < 0):
            continue
        if (type_map[newy][newx] == cannot):
            continue
        heapq.heappush(queue, (minutes + 1, newx, newy, cannot))


