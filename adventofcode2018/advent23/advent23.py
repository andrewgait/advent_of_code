# Advent of code, day 23

# open file
input = open("advent23_input.txt", "r")
#input = open("advent23_test_input.txt", "r")
#input = open("advent23_test_input2.txt", "r")

nanobots = []
max_radius = 0
max_bot = 0
# read string into array
for line in input:
    splitspace = line.rsplit(' ', 1)
    pos = splitspace[0]
    radius = int(splitspace[1][2:])
    xyz = pos.rsplit(',', 3)
    x = int(xyz[0][5:])
    y = int(xyz[1])
    z = int(xyz[2][:-1])
    nanobots.append([x,y,z,radius])
    if (radius > max_radius):
        max_radius = radius
        max_bot = len(nanobots)-1

print('max_radius is ', max_radius, ' at nanobot ', max_bot)
#print(nanobots)
x_bot = nanobots[max_bot][0]
y_bot = nanobots[max_bot][1]
z_bot = nanobots[max_bot][2]


def in_range(x,y,z,radius,xb,yb,zb):
    distance = abs(x-xb) + abs(y-yb) + abs(z-zb)
    return distance <= radius


count_within = 0
for n in range(len(nanobots)):
    if (in_range(nanobots[n][0],nanobots[n][1],nanobots[n][2],max_radius,x_bot,y_bot,z_bot)):
        count_within += 1

# part 1
print('there are ', count_within, ' bots within ', max_radius, ' of bot ', max_bot)

# part 2
# is there a clever search technique available here?
nbots = len(nanobots)
mult = 10000000
max_in_range = 0
coord_at_max = []
for x in range(-10,10):
    for y in range(-10,10):
        for z in range(-10,10):
            sum_in_range = 0
            xt = x * mult
            yt = y * mult
            zt = z * mult
            for n in range(nbots):
                xb = nanobots[n][0]
                yb = nanobots[n][1]
                zb = nanobots[n][2]
                radius = nanobots[n][3]
                if (in_range(xt,yt,zt,radius,xb,yb,zb)):
                    sum_in_range += 1

            if (sum_in_range > max_in_range):
                max_in_range = sum_in_range
                coord_at_max = [[xt,yt,zt]]
            elif (sum_in_range == max_in_range):
                coord_at_max.append([xt,yt,zt])


print('coord ', coord_at_max, ' in range of max bots: ', max_in_range)

while (mult > 1):
    next_coord = [coord_at_max[0][0], coord_at_max[0][1], coord_at_max[0][2]]
    mult = mult // 10
    coords_at_max = []
    for x in range(-20,20):
        for y in range(-20,20):
            for z in range(-20,20):
                sum_in_range = 0
                xt = x * mult + next_coord[0]
                yt = y * mult + next_coord[1]
                zt = z * mult + next_coord[2]
                for n in range(nbots):
                    xb = nanobots[n][0]
                    yb = nanobots[n][1]
                    zb = nanobots[n][2]
                    radius = nanobots[n][3]
                    if (in_range(xt,yt,zt,radius,xb,yb,zb)):
                        sum_in_range += 1

                if (sum_in_range > max_in_range):
                    max_in_range = sum_in_range
                    coords_at_max = [[xt,yt,zt]]
                elif (sum_in_range == max_in_range):
                    coords_at_max.append([xt,yt,zt])


    # in this list, which is closest to [0,0,0] ?
#    print(coords_at_max)
    min_dist = 10000000000000
    coord_at_max = []
    for m in range(len(coords_at_max)):
        dist = 0
        for l in range(3):
            dist += abs(coords_at_max[m][l])
        if (dist < min_dist):
            coord_at_max = [[coords_at_max[m][0],coords_at_max[m][1],coords_at_max[m][2]]]
            min_dist = dist

    print('coord ', coord_at_max, ' in range of max bots: ', max_in_range, ' (mult = ', mult, ')')
    print('distance from (0,0,0) is ', abs(coord_at_max[0][0])+abs(coord_at_max[0][1])+abs(coord_at_max[0][2]))

