# Advent of code 2024, day 9

# open file
input = open("advent9_input.txt", "r")
# input = open("advent9_test_input1.txt", "r")
# input = open("advent9_test_input2.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)


def part1():

    disk_map = []

    ID_number = 0
    for n in range(len(input_array[0])-1):
        n_vals = int(input_array[0][n])
        if n % 2 == 0:
            for n in range(n_vals):
                disk_map.append(ID_number)
            ID_number += 1
        else:
            for n in range(n_vals):
                disk_map.append(".")

    # print(disk_map)
    disk_size = len(disk_map)

    # now compact the disk map
    compacted_disk_map = []
    end_location = disk_size - 1
    for n in range(disk_size):
        if disk_map[n] != ".":
            compacted_disk_map.append(disk_map[n])
        else:
            while disk_map[end_location] == ".":
                end_location -= 1
            if end_location <= n:
                break
            compacted_disk_map.append(disk_map[end_location])
            disk_map[end_location] = "."


    # print(compacted_disk_map)

    answer = 0
    for n in range(len(compacted_disk_map)):
        answer += n * compacted_disk_map[n]

    return answer

def part2():

    disk_map = []

    ID_number = 0
    for n in range(len(input_array[0])-1):
        n_vals = int(input_array[0][n])
        if n % 2 == 0:
            for n in range(n_vals):
                disk_map.append(ID_number)
            ID_number += 1
        else:
            for n in range(n_vals):
                disk_map.append(".")

    print(disk_map)
    disk_size = len(disk_map)

    # now compact the disk map
    compacted_disk_map = []
    end_location = disk_size - 1

    # Go from the end of the current disk_map
    n = end_location
    while n >= 0:
        if disk_map[n] != ".":
            # Get the size of the file
            loc = n
            file_size = 0
            while disk_map[loc] == disk_map[n]:
                loc -= 1
                file_size +=1

            IDval = disk_map[n]
            n -= file_size

            # print("ID ", IDval, " file size ", file_size)
            # print(disk_map)
            # We have the file size, so now look from the front end of disk_map to find a space big enough
            nn = 0
            keep_going = True
            while keep_going:
                if disk_map[nn] == ".":
                    # Count from here
                    nn_loc = nn
                    test_file_size = 0
                    carry_on = True
                    while carry_on:
                        nn_loc += 1
                        test_file_size += 1
                        if nn_loc > n:
                            carry_on = False
                        if carry_on and (disk_map[nn_loc] != disk_map[nn]):
                            carry_on = False

                    if file_size <= test_file_size:
                        for nnn in range(file_size):
                            disk_map[nn+nnn] = IDval
                            disk_map[n+1+nnn] = "."
                        # print(disk_map)
                        break
                    else:
                        nn += test_file_size
                else:
                    nn += 1
                    if nn > n:
                        keep_going = False

                if nn >= disk_size:
                    keep_going = False
        else:
            n -= 1

    print(disk_map)

    answer = 0
    for n in range(len(disk_map)):
        if disk_map[n] != ".":
            answer += n * disk_map[n]

    # first try: 6469637179774 is too high

    return answer


print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
