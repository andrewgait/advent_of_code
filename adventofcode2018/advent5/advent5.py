# Advent of code, day 5

# open file
input = open("advent5_input.txt", "r")

# read string into array
for line in input:
    polymerstring = line

# get rid of the newline at the end of the array
polymerstring = polymerstring[:-1]

# test it
# polymerstring = 'dabAcCaCBAcCcaDAaA'

print('first array is length ', len(polymerstring))
print(polymerstring[len(polymerstring)-1], polymerstring[len(polymerstring)-2])

def do_react(polymerstring):
    found_unit = True
    while found_unit:
        found_unit = False
        new_polymerstring = []
        for i in range(len(polymerstring)-1):
            if ((polymerstring[i].isupper()) and (polymerstring[i+1].islower()) and
                (polymerstring[i] == polymerstring[i+1].upper()) or
                ((polymerstring[i].islower()) and (polymerstring[i+1].isupper()) and
                (polymerstring[i] == polymerstring[i+1].lower()))):
                found_unit = True
                # append the rest of the string to this and start again
    #            print('found at location ', i, polymerstring[i], polymerstring[i+1])
                for j in range(i+2, len(polymerstring)):
                    new_polymerstring.append(polymerstring[j])
                break
            else:
                new_polymerstring.append(polymerstring[i])
                if (i == len(polymerstring)-2):
                    new_polymerstring.append(polymerstring[i+1])

        # set the old string to be tested to the new one
        polymerstring = new_polymerstring

    #    print(polymerstring)
    return len(polymerstring)


alphabet = '0abcdefghijklmnopqrstuvwxyz'

# loop over alphabet
min_length = 50000
min_letter = 0
for n in range(len(alphabet)):
    # remove all instances
    modified_string = []
    for j in range(len(polymerstring)):
        if ((polymerstring[j] != alphabet[n]) and
            (polymerstring[j] != alphabet[n].upper())):
            modified_string.append(polymerstring[j])

    # now react this string
    size = do_react(modified_string)

    # print the current string length
    print('Remove letter ', alphabet[n], ' string is length ', size)
    if (size < min_length):
        min_length = size
        min_letter = alphabet[n]

