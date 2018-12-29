# Advent of code, day 25

# Trying this again with a slightly different idea

# open file
input = open("advent25_input.txt", "r")
#input = open("advent25_test_input3.txt", "r")


def distance(coordA, coordB):
    sum = 0
    for i in range(4):
        sum += abs(coordA[i]-coordB[i])

    return sum


constellations = []
# read string into array
for line in input:
    data = line.rsplit(',', 3)
    point = []
    for i in range(4):
        point.append(int(data[i]))

    n_cons = len(constellations)
    if (n_cons == 0):
        constellations.append([point])
    else:
        within = False
        # instead of breaking from the outer loop, record each constellation
        # it is part of and then join multiple matches together
        for n in range(n_cons):
            in_cons = False
            for m in range(len(constellations[n])):
                 if (distance(point, constellations[n][m]) <= 3):
                     in_cons = True
                     break

            if (in_cons):
                within = True

        if (not within):
            constellations.append([constellation])

#    print(constellations)

n_cons = len(constellations)
print('there are ', n_cons, ' constellations')
