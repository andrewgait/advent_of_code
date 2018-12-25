# Advent of code, day 25

# Note: I have no idea why, but this code takes forever on the main input.
#       I guessed the answer of 420 based on the output I was getting!
#       There's something wrong inside the while loop which appears to currently
#       exponentially increase the time spent per "iteration" whicb I can't be
#       bothered to find right now.

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
    constellation = []
    for i in range(4):
        constellation.append(int(data[i]))

    n_cons = len(constellations)
    if (n_cons == 0):
        constellations.append([constellation])
    else:
        within = False
        for n in range(n_cons):
            in_cons = False
            for m in range(len(constellations[n])):
                 if (distance(constellation, constellations[n][m]) <= 3):
                     in_cons = True
                     break

            if (in_cons):
                constellations[n].append(constellation)
                within = True
                break

        if (not within):
            constellations.append([constellation])

#    print(constellations)

n_cons = len(constellations)
print('there are ', n_cons, ' constellations')

fully_merged = False
while (not fully_merged):

    join_together = []
    merged = []
    for n in range(n_cons-1):
        join_set = set()
        for m in range(n+1, n_cons):
            constellation1 = constellations[n]
            constellation2 = constellations[m]
            for i in range(len(constellation1)):
                for j in range(len(constellation2)):
                    if (distance(constellation1[i], constellation2[j]) <= 3):
                        join_set.add(n)
                        join_set.add(m)

        join_together.append(join_set)
        merged.append(0)

    merged.append(0)
    print('join_together: ', join_together)

    new_constellations = []
    for n in range(len(join_together)):
        join_list = list(join_together[n])
        if (len(join_list) > 0):
            constellation = []
            for i in range(len(join_list)):
                constel = constellations[join_list[i]]
                merged[join_list[i]] = 1
                for j in range(len(constel)):
                    constellation.append(constel[j])

            new_constellations.append(constellation)

    for n in range(len(merged)):
        if (merged[n] == 0):
            new_constellations.append(constellations[n])

#    print('new_constellations: ', new_constellations)

    n_new_cons = len(new_constellations)
    print('now there are ', n_new_cons, ' constellations')

    if (n_new_cons == n_cons):
        fully_merged = True
    else:
        constellations = []
        for n in range(n_new_cons):
            constellations.append(new_constellations[n])
#            print(len(new_constellations[n]))

        n_cons = n_new_cons
