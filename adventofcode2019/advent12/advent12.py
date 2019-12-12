# Advent of code, day 12
import numpy as np
import matplotlib.pyplot as plt
import math
from itertools import combinations

# open file
input = open("advent12_input.txt", "r")
# input = open("advent12_test_input.txt", "r")
# input = open("advent12_test_input2.txt", "r")

# there are 4 moons
moons = np.zeros((4,3), dtype=np.int64)
part2_moons = np.zeros((4,3), dtype=np.int64)
count = 0
# read string into array
for line in input:
    # string is of form <x=a, y=b, z=c> where we want to get a, b, c, (integers)
    # split by spaces
    input_split = line.split(' ')
    x = int(input_split[0][3:-1])
    y = int(input_split[1][2:-1])
    z = int(input_split[2][2:-2])
    moons[count][0] = x
    moons[count][1] = y
    moons[count][2] = z
    part2_moons[count][0] = x
    part2_moons[count][1] = y
    part2_moons[count][2] = z
    count += 1

print(moons)

def get_velocities(moons, velocities):

    new_velocities = np.zeros((len(moons),3), dtype=np.int64)
    for n in range(len(moons)):
        for coord in range(3):
            new_velocities[n][coord] = velocities[n][coord]
    # loop over all moons and apply 'gravity'
    for n in range(len(moons)):
        # get other moons
        for m in range(len(moons)):
            # a moon can't move itself
            if n != m:
                for coord in range(3):
                    if moons[n][coord] < moons[m][coord]:
                        new_velocities[n][coord] += 1
                    elif moons[n][coord] > moons[m][coord]:
                        new_velocities[n][coord] -= 1

    return new_velocities

def calculate_energy(moons, velocities):
#     total_energy = 0
    energy = np.zeros(len(moons), dtype=np.int64)
    for n in range(len(moons)):
        potential_energy = abs(moons[n][0]) + abs(moons[n][1]) + abs(moons[n][2])
        kinetic_energy = abs(velocities[n][0]) + abs(velocities[n][1]) + abs(velocities[n][2])
        energy[n] += potential_energy * kinetic_energy

    return energy

def test_equality(moons, velocities, initial_moons, initial_velocities, timestep,
                  found0, found1, found2, found3):
    # loop over all
    m0 = m1 = m2 = m3 = -1

    if not found0:
        if (np.array_equal(moons[0], initial_moons[0]) and
            np.array_equal(velocities[0], initial_velocities[0])):
            print("moon 0 repeat at ", timestep)
            found0 = True

    if not found1:
        if (np.array_equal(moons[1], initial_moons[1]) and
            np.array_equal(velocities[1], initial_velocities[1])):
            print("moon 1 repeat at ", timestep)
            found1 = True

    if not found2:
        if (np.array_equal(moons[2], initial_moons[2]) and
            np.array_equal(velocities[2], initial_velocities[2])):
            print("moon 2 repeat at ", timestep)
            found2 = True

    if not found3:
        if (np.array_equal(moons[3], initial_moons[3]) and
            np.array_equal(velocities[3], initial_velocities[3])):
            print("moon 3 repeat at ", timestep)
            found3 = True

    return found0, found1, found2, found3

def lcm(x, y):
    return abs(x*y) // math.gcd(x, y)

def part1(moons, timesteps):
    timestep = 0
    velocities = np.zeros((len(moons),3), dtype=np.int64)
    while timestep < timesteps:
        velocities = get_velocities(moons, velocities)

        # update the moon positions
        for n in range(len(moons)):
            for coord in range(3):
                moons[n][coord] += velocities[n][coord]

        timestep += 1

#         print(timestep)
#         print(moons)
#         print(velocities)


    total_energy = calculate_energy(moons, velocities)

    return sum(total_energy)

def my_compare(x, y):
    if (x > y):
        a = 1
    else:
        a = 0

    if (x < y):
        b = 1
    else:
        b = 0

    return a - b

def part2(moons):

    repeat_at = np.zeros(3, dtype=np.int64)

    # the planes are independent, so they can be done separately
    for coord in range(3):
        timestep = 0
        orig_plane = [x[coord] for x in moons]
        orig_velocities = [0 for _ in moons]

        plane = [x[coord] for x in moons]
        velocities = [0 for _ in moons]

        while True:
            # borrowed from solutions browsed on reddit
            for i, j in combinations(range(len(plane)), 2):
                pull = my_compare(plane[i], plane[j])
                velocities[i] -= pull
                velocities[j] += pull

            for pos, vel in enumerate(velocities):
                plane[pos] += velocities[pos]

            timestep += 1

            # are we at original plane and velocities yet?
            if plane == orig_plane and velocities == orig_velocities:
                break

        repeat_at[coord] = timestep

    print(repeat_at)

    # simply do an lcm across the repeat_at array at this point
    answer = repeat_at[0]
    for n in range(1,len(repeat_at)):
        answer = lcm(answer, repeat_at[n])

    print(answer)

    return answer

print("Part 1 answer: ", part1(moons, 1000))
timestep = part2(part2_moons)
print("Part 2 answer: ", timestep)
