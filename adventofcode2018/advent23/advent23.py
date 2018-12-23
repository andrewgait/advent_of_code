# Advent of code, day 23

# open file
#input = open("advent23_input.txt", "r")
input = open("advent23_test_input.txt", "r")

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

count_within = 0
for n in range(len(nanobots)):
    distance = abs(nanobots[n][0]-x_bot) + abs(nanobots[n][1]-y_bot) + abs(nanobots[n][2]-z_bot)
    if (distance <= max_radius):
        count_within += 1

# part 1
print('there are ', count_within, ' bots within ', max_radius, ' of bot ', max_bot)

# part 2
