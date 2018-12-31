# Advent of code, day 25

# Trying this again with a slightly different idea
# This is a lot faster than the other one but it doesn't get quite the right answer yet...
# ... still not quite right even with the extra attempts to combine neighbours.  For some
# reason it now goes below the correct answer of 420.

# open file
input = open("advent25_input.txt", "r")
#input = open("advent25_test_input4.txt", "r")


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
        add_to_set = set()
        for n in range(n_cons):
            in_cons = False
            for m in range(len(constellations[n])):
                 if (distance(point, constellations[n][m]) <= 3):
                     in_cons = True
                     add_to_set.add(n)

            if (in_cons):
                within = True

        if (not within):
            constellations.append([point])
        else:
            add_to = list(add_to_set)
#            print('add_to ', add_to)
            for j in range(len(add_to)):
                if (j==0):
                    constellations[add_to[0]].append(point)
                else:
                    for k in range(len(constellations[add_to[j]])):
#                        print('add ',  k, constellations[add_to[j]][k])
                        constellations[add_to[0]].append(constellations[add_to[j]][k])

            if (len(add_to) > 0):
                for j in range(1, len(add_to)):
#                    print('delete ', j)
                    del constellations[add_to[j]-(j-1)]

print(constellations)

n_cons = len(constellations)
print('there are ', n_cons, ' constellations')

join_together = set()
for n in range(n_cons-1):
    for m in range(n+1, n_cons):
        if (n != m):
            for i in range(len(constellations[n])):
                for j in range(len(constellations[m])):
                    if (distance(constellations[n][i], constellations[m][j]) <= 3):
                        join_together.add((n,m))

print(join_together)
join_list = list(join_together)

while (len(join_list) > 0):
    for n in range(len(join_list)):
        for i in range(len(constellations[join_list[n][1]])):
            constellations[join_list[n][0]].append(constellations[join_list[n][1]][i])

    for n in range(len(join_list)):
        del constellations[join_list[n][1]-n]

    n_cons = len(constellations)
    print('there are ', n_cons, ' constellations')

    join_together = set()
    for n in range(n_cons-1):
        for m in range(n+1, n_cons):
            if (n != m):
                for i in range(len(constellations[n])):
                    for j in range(len(constellations[m])):
                        if (distance(constellations[n][i], constellations[m][j]) <= 3):
                            join_together.add((n,m))

    print(join_together)
    join_list = list(join_together)
