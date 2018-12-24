# Advent of code, day 24

# open file
#input = open("advent24_input.txt", "r")
input = open("advent24_test_input.txt", "r")

fighting_units = []

# array: [type, number, hit points, attack type, attack power, weakness, immunity, initiative] 
# attack types are fire, cold, slashing, bludgeoning, radiation

attack_types = ['fire', 'cold', 'slashing', 'bludgeoning', 'radiation']

boost = 0  # 1570

# read string into array
n = 0
for line in input:
    if (n == 0):
        army = line[:-2]
#        print('army: ', army)
        n += 1
    else:
#        print(line)
        if (line == '\n'):
            n = 0
        else:
            n += 1
            data = line.rsplit(' ', 55)
#            print(data)
            initiative = int(data[-1])
            attack_type = data[-5]
            attack_power = int(data[-6])
            number = int(data[0])
            hitpoints = int(data[4])
            effective_power = number * attack_power
            unit = [army, number, hitpoints, attack_type, attack_power, [''], [''], effective_power, initiative]
            fighting_units.append(unit)
            weaksplit = line.rsplit('weak', 1)
            if (len(weaksplit) > 1):
                weak = weaksplit[1].rsplit(' ', 60)  # could be up to 5 different types here
#                print('weak: ', weak)
                m = 2
                weakness = weak[m][:-1]
                weaknesses = []
                weaknesses.append(weakness)
                next = True
                while (next):
                    m += 1
                    weakness = weak[m][:-1]
                    if (weakness in attack_types):
                        weaknesses.append(weakness)
                    else:
                        next = False

                unit[5] = weaknesses

            immunesplit = line.rsplit('immune', 1)
            if (len(immunesplit) > 1):
                immune = immunesplit[1].rsplit(' ', 60)  # could be up to 5 different types here
#                print('immune: ', immune)
                m = 2
                immunity = immune[m][:-1]
                immunities = []
                immunities.append(immunity)
                next = True
                while (next):
                    m += 1
                    immunity = immune[m][:-1]
                    if (immunity in attack_types):
                        immunities.append(immunity)
                    else:
                        next = False

                unit[6] = immunities

units_sort = sorted(fighting_units, key=lambda fighting_units: (fighting_units[-2], fighting_units[-1]), reverse=True)
print(units_sort)

# reminder, array: [type, number, hit points, attack type, attack power, weakness, immunity, initiative]
battle = True
while (battle):
    # Target selection
    attacks = []
    nunits = len(units_sort)
    for n in range(nunits):
        attack = []
        # attack is [source, target, damage]
        # loop over targets
        max_damage = 0
        for m in range(nunits):
            # don't attack yourself
            if (m != n):
                # don't attack someone on your side
                if (units_sort[m][0] != units_sort[n][0]):
                    # work out whether attack can happen
                    if (units_sort[n][3] in units_sort[m][6]):
                        # unit m is immune
#                        print('unit ', units_sort[m], ', is immune to unit ', units_sort[n])
                        damage = 0
                        mult = 0
                    elif (units_sort[n][3] in units_sort[m][5]):
                        # unit m is weak
#                        print('unit ', units_sort[m], ', is weak to unit ', units_sort[n])
                        damage =  2 * units_sort[n][1] * units_sort[n][4]
                        mult = 2
                    else:
#                        print('unit ', units_sort[m], ', is attacked by unit ', units_sort[n])
                        damage =  units_sort[n][1] * units_sort[n][4]
                        mult = 1

                    if (damage > max_damage):
                        max_damage = damage
                        attack = [units_sort[n][0], n, units_sort[m][0], m, mult, units_sort[n][-1]]

#        print(attack)
        if (len(attack) > 0):
            attacks.append(attack)

    print('len(attacks): ', len(attacks), attacks)
    attack_sort = sorted(attacks, key=lambda attack: attack[5], reverse=True)

    print('attack_sort: ', attack_sort)

    # at this point, two attacks on the same group cannot happen; tie-breaker is initiative
    delete_attacks = set()
    for n in range(len(attack_sort)):
        for m in range(len(attack_sort)):
            if (n != m):
                if (attack_sort[n][3] == attack_sort[m][3]):
                    if (attack_sort[n][5] > attack_sort[m][5]):
                        delete_attacks.add(n)
                    else:
                        delete_attacks.add(m)

    delete_list = list(delete_attacks)
    print('delete_attacks: ', delete_attacks)
    if (len(delete_attacks) > 0):
        for i in range(len(delete_attacks)):
            del attack_sort[delete_list[i]-i]

    # Attacking
    for n in range(len(attack_sort)):
        src = attack_sort[n][1]
        tgt = attack_sort[n][3]
        attack_pow = units_sort[src][-2] * attack_sort[n][-2]
        units_dead = attack_pow // units_sort[tgt][2]
        print('source: ', src, ' attack power: ', attack_pow, ' target: ', tgt, ' units_dead: ', units_dead)
        if (units_dead >= units_sort[tgt][1]):
            units_sort[tgt][1] = 0
            units_sort[tgt][-2] = 0
        else:
            units_sort[tgt][1] -= units_dead
            units_sort[tgt][-2] = units_sort[tgt][1] * units_sort[tgt][4]

#        print('n: ', n, 'units: ', units_sort)

    sum_infect = 0
    sum_immune = 0
    mark_to_delete = []
    for n in range(len(units_sort)):
        if (units_sort[n][1] == 0):
            mark_to_delete.append(n)
        if (units_sort[n][0] == 'Infection'):
            sum_infect += units_sort[n][1]
        else:
            sum_immune += units_sort[n][1]

    print(sum_infect, sum_immune)

    if (len(mark_to_delete) > 0):
        for i in range(len(mark_to_delete)):
            del units_sort[mark_to_delete[i]-i]

    units_sort = sorted(units_sort, key=lambda units_sort: (units_sort[-2], units_sort[-1]), reverse=True)

    print('units_sort: ', units_sort)

    if ((sum_immune == 0) or (sum_infect == 0)):
        battle = False
