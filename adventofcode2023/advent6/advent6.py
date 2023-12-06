# Advent of code 2023, day 6
import math

# open file
input = open("advent6_input.txt", "r")
# input = open("advent6_input_test.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    splittimes = input_array[0][:-1].split(" ")
    splitdistances = input_array[1][:-1].split(" ")
    print(splittimes)

    times = [int(splittimes[n]) for n in range(1,len(splittimes)) if splittimes[n] != ""]
    distances = [int(splitdistances[n]) for n in range(1,len(splitdistances)) if splitdistances[n] != ""]

    print(times, distances)

    n_ways = 1 # multiplicative

    for n in range(len(times)):
        time_race = times[n]
        record_distance = distances[n]

        start_speed = 0
        n_records = 0

        for m in range(time_race):
            distance_covered = (start_speed + m) * (time_race - m)
            if distance_covered > record_distance:
                n_records += 1

        print("time ", time_race, " n_records ", n_records)
        n_ways *= n_records

    answer = n_ways

    return answer

def part2():

    splittimes = input_array[0][:-1].split(" ")
    splitdistances = input_array[1][:-1].split(" ")

    time_str = ""
    for n in range(1,len(splittimes)):
        time_str += splittimes[n]
    time = int(time_str)
    distance_str = ""
    for n in range(1,len(splitdistances)):
        distance_str += splitdistances[n]
    distance = int(distance_str)

    print(time, distance)

    # Obviously looping doesn't work here!
    # But I think this is just the intersection of a curve and a line
    # for the distance and time variables
    # - The curve given by distance = (start + time) * (time_race - time)
    #   which in polynomial form is distance = -time^2 + (start + time_race) * time + (start * time_race)
    # - And the line at distance = max_distance

    # So solve 0 = -time^2 + (start + time_race) * time + (start * time_race) - max_distance
    start = 0  # (start speed)
    time_race = time
    max_distance = distance

    b = (start + time_race)
    a = -1
    c = (start * time_race) - max_distance

    t1 = ((-1 * b) + math.sqrt(b**2 - (4*a*c))) / (2 * a)
    t2 = ((-1 * b) - math.sqrt(b**2 - (4*a*c))) / (2 * a)

    print(t1, t2)
    # The answer is then floor(largest) - ceil(smallest) + 1 (inclusive of both ends)
    answer = math.floor(max([t1,t2])) - math.ceil(min([t1,t2])) + 1

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
