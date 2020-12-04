# Advent of code, day 4

# open file
input = open("advent4_input.txt", "r")
# input = open("advent4_test_input.txt", "r")
# input = open("advent4_valid_input.txt", "r")
# input = open("advent4_invalid_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def get_passport_array(input_array):
    n = len(input_array)

    passport_array = []
    passport_dict = dict()

    for i in range(n):
        # make a dict add lines until we hit a blank line
        if input_array[i][0] == "\n":
            passport_array.append(passport_dict)
            passport_dict = dict()
        else:
            splitspace = input_array[i].split(" ")
            for j in range(len(splitspace)):
                splitcolon = splitspace[j].split(":")
                passport_dict[splitcolon[0]] = splitcolon[1].rstrip("\n")

    print(len(passport_array), passport_array)

    return passport_array

def part1():
    passport_array = get_passport_array(input_array)

    count_valid = 0

    n_pass = len(passport_array)
    for i in range(n_pass):
#         print(len(passport_array[i]))
#         print(("cid" in passport_array[i]))
        if ((len(passport_array[i]) == 8) or (
            ((len(passport_array[i]) == 7) and
             ("cid" not in passport_array[i])))):
            count_valid += 1

    return count_valid

def part2():

    # Do the same again...
    passport_array = get_passport_array(input_array)

    count_valid = 0

    valid_hcl = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                 "a", "b", "c", "d", "e", "f"]

    valid_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    valid_pid = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    n_pass = len(passport_array)
    for i in range(n_pass):
#         print(len(passport_array[i]))
#         print(("cid" in passport_array[i]))
        passdict = passport_array[i]
        if ((len(passdict) == 8) or (
            ((len(passdict) == 7) and
             ("cid" not in passport_array[i])))):
            # ... except now we have more values to check
            valid = True

            # From the instructions:
            # byr (Birth Year) - four digits; at least 1920 and at most 2002.
            if (len(passdict["byr"]) != 4):
                valid = False
            else:
                if (int(passdict["byr"]) < 1920) or (int(passdict["byr"]) > 2002):
                    valid = False
            # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
            if (len(passdict["iyr"]) != 4):
                valid = False
            else:
                if (int(passdict["iyr"]) < 2010) or (int(passdict["iyr"]) > 2020):
                    valid = False
            # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
            if (len(passdict["eyr"]) != 4):
                valid = False
            else:
                if (int(passdict["eyr"]) < 2020) or (int(passdict["eyr"]) > 2030):
                    valid = False
            # hgt (Height) - a number followed by either cm or in:
            #
            #     If cm, the number must be at least 150 and at most 193.
            #     If in, the number must be at least 59 and at most 76.
            #
            if ((passdict["hgt"][-2:] != "cm") and (passdict["hgt"][-2:] != "in")):
                valid = False
            else:
                if (passdict["hgt"][-2:] == "cm"):
                    if ((int(passdict["hgt"][0:-2]) < 150) or (int(passdict["hgt"][0:-2]) > 193)):
                        valid = False
                if (passdict["hgt"][-2:] == "in"):
                    if ((int(passdict["hgt"][0:-2]) < 59) or (int(passdict["hgt"][0:-2]) > 76)):
                        valid = False
            # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
            if (len(passdict["hcl"]) != 7):
                valid = False
            elif (passdict["hcl"][0] != "#"):
                valid = False
            else:
                for i in range(6):
                    if (passdict["hcl"][i+1] not in valid_hcl):
                        valid = False
            # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
            if (passdict["ecl"] not in valid_ecl):
                valid = False
            # pid (Passport ID) - a nine-digit number, including leading zeroes.
            if (len(passdict["pid"]) != 9):
                valid = False
            else:
                for i in range(9):
                    if (passdict["pid"][i] not in valid_pid):
                        valid = False

            # If it's got through all of this then it's valid
            if valid:
                count_valid += 1

    return count_valid

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
