# Advent of code, day 16

# open file
input = open("advent16_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)


def get_version_and_typeID(binary_str, read_loc):
    version = int(binary_str[read_loc:read_loc+3], 2)
    typeID = int(binary_str[read_loc+3:read_loc+6], 2)
    read_loc += 6
    return version, typeID, read_loc


def get_literal_value(binary_str, read_loc):
    literal_str = ""
    while binary_str[read_loc] == "1":
        literal_str += binary_str[read_loc+1:read_loc+5]
        read_loc += 5
    # read location should now be zero
    literal_str += binary_str[read_loc+1:read_loc+5]

    read_loc += 5
    literal_value = int(literal_str, 2)
    return literal_value, read_loc


def get_packet(binary_str, read_loc, total_version):
    version, typeID, read_loc = get_version_and_typeID(binary_str, read_loc)
    # print(version, typeID)
    total_version += version

    if typeID == 4:
        literal_value, read_loc = get_literal_value(binary_str, read_loc)
        # print(literal_value, read_loc)
    else:
        if binary_str[read_loc] == "0":
            # next 15 bits represents the total length of sub-packets
            total_packet_length = int(binary_str[read_loc+1:read_loc+16], 2)
            read_loc += 16
            read_loc_start = read_loc
            length_read = 0
            while length_read < total_packet_length:
                total_version, read_loc = get_packet(binary_str, read_loc, total_version)
                length_read = read_loc - read_loc_start
        elif binary_str[read_loc] == "1":
            # next 11 bits are a number that represents the number of sub-packets
            number_of_sub_packets = int(binary_str[read_loc+1:read_loc+12], 2)
            read_loc += 12
            for n in range(number_of_sub_packets):
                total_version, read_loc = get_packet(binary_str, read_loc, total_version)

    return total_version, read_loc


def get_packet_part2(binary_str, read_loc, total_version, result):
    version, typeID, read_loc = get_version_and_typeID(binary_str, read_loc)
    # print(version, typeID)
    total_version += version

    if typeID == 4:
        literal_value, read_loc = get_literal_value(binary_str, read_loc)
        # print(literal_value, read_loc)
        result = literal_value
    else:
        result_array = []
        if binary_str[read_loc] == "0":
            # next 15 bits represents the total length of sub-packets
            total_packet_length = int(binary_str[read_loc+1:read_loc+16], 2)
            read_loc += 16
            read_loc_start = read_loc
            length_read = 0
            while length_read < total_packet_length:
                total_version, read_loc, result = get_packet_part2(binary_str, read_loc, total_version, result)
                length_read = read_loc - read_loc_start
                result_array.append(result)
        elif binary_str[read_loc] == "1":
            # next 11 bits are a number that represents the number of sub-packets
            number_of_sub_packets = int(binary_str[read_loc+1:read_loc+12], 2)
            read_loc += 12
            for n in range(number_of_sub_packets):
                total_version, read_loc, result = get_packet_part2(binary_str, read_loc, total_version, result)
                result_array.append(result)

        # hopefully what we need is in result array
        if typeID == 0:
            result = sum(result_array)
        elif typeID == 1:
            result = 1
            for n in range(len(result_array)):
                result *= result_array[n]
        elif typeID == 2:
            result = min(result_array)
        elif typeID == 3:
            result = max(result_array)
        elif typeID == 5:
            result = 0
            if (result_array[0] > result_array[1]):
                result = 1
        elif typeID == 6:
            result = 0
            if (result_array[0] < result_array[1]):
                result = 1
        elif typeID == 7:
            result = 0
            if (result_array[0] == result_array[1]):
                result = 1

    return total_version, read_loc, result


def part1():

    answer = 0

    # input_array = ["8A004A801A8002F478"]
    # input_array = ["620080001611562C8802118E34"]
    # input_array = ["C0015000016115A2E0802F182340"]
    # input_array = ["A0016C880162017C3686B18A3D4780"]

    # convert hexadecimal into binary (leading zeroes needed...)
    thelen = (len(input_array[0]))*4
    binary_str = str(bin(int(input_array[0], 16)))[2:]
    while ((len(binary_str)) < thelen):
        binary_str = '0' + binary_str

    print(binary_str)

    read_loc = 0
    total_version = 0

    total_version, read_loc = get_packet(binary_str, read_loc, total_version)

    answer = total_version

    return answer

def part2():

    answer = 0

    # input_array = ["8A004A801A8002F478"]
    # input_array = ["620080001611562C8802118E34"]
    # input_array = ["C0015000016115A2E0802F182340"]
    # input_array = ["A0016C880162017C3686B18A3D4780"]
    # input_array = ["9C0141080250320F1802104A08"]

    # convert hexadecimal into binary (leading zeroes needed...)
    thelen = (len(input_array[0]))*4
    binary_str = str(bin(int(input_array[0], 16)))[2:]
    while ((len(binary_str)) < thelen):
        binary_str = '0' + binary_str

    print(binary_str)

    read_loc = 0
    total_version = 0
    result = 0

    total_version, read_loc, result = get_packet_part2(binary_str, read_loc, total_version, result)

    answer = result

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
