# Advent of code, day 6

# open file
input = open("advent6_input.txt", "r")
# input = open("advent6_test_input.txt", "r")
# input = open("advent6_test_input2.txt", "r")

orbits = dict()
objects = set()
# read string into array
for line in input:
    # split
    inputs = line[:-1].split(")")
    objects.add(inputs[0])
    objects.add(inputs[1])
    orbits[inputs[1]] = inputs[0]

print(objects)
print(orbits)

def get_orbit_list(object, orbits):
    test = object
    obj_list = []
    test = orbits[test]
    while test in orbits:
        obj_list.append(test)
        test = orbits[test]

    return obj_list

def part1(objects, orbits):
    total = 0
    for obj in objects:
        test = obj
        count = 0
        while test in orbits:
            count += 1
            test = orbits[test]

        total += count

    return total

def part2(orbits):
    you = 'YOU'
    san = 'SAN'

    you_orbit = get_orbit_list(you, orbits)
    san_orbit = get_orbit_list(san, orbits)

    you_excl = [x for x in you_orbit if x not in san_orbit]
    san_excl = [x for x in san_orbit if x not in you_orbit]

    answer = len(you_excl) + len(san_excl)

    return answer

print("Part 1 answer: ", part1(objects, orbits))
print("Part 2 answer: ", part2(orbits))
