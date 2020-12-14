# Advent of code, day 13
from functools import reduce

# open file
input = open("advent13_input.txt", "r")
# input = open("advent13_test_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def part1():

    answer = 0
    my_depart = int(input_array[0][:-1])
    busIDs = input_array[1][:-1].split(",")
    n = len(busIDs)
    closest_bus = 999999999
    closest_busID = 0
    for i in range(n):
        if busIDs[i] != "x":
            busID = int(busIDs[i])
            bus_dist = (((my_depart // busID)+1)*busID) - my_depart
            if bus_dist < closest_bus:
                closest_bus = bus_dist
                closest_busID = busID
                print(closest_bus, closest_busID)

    answer = closest_bus * closest_busID

    return answer

def part2():

    # worked out eventually that this is the chinese remainder theorem,
    # and borrowed some code from
    # https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
    # to do this

    print("[17,x,13,19] is ", chinese_remainder([17,13,19],[0,11,16]))

    busIDs = input_array[1][:-1].split(",")
    n = len(busIDs)

    buses = []
    remainders = []
    for i in range(n):
        if i == 0:
            buses.append(int(busIDs[0]))
            remainders.append(0)
        else:
            if (busIDs[i] != "x"):
                buses.append(int(busIDs[i]))
                remainders.append(int(busIDs[i])-i)

    print(buses)
    print(remainders)

    answer = chinese_remainder(buses, remainders)

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
