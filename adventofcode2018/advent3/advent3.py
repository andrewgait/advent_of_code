# Advent of code, day 3

# open file
input = open("advent3_input.txt", "r")

# create a 2d zero array of 1200x1200  probably could use numpy here
size = 1000
cloth_array = []
cloth_ids = []
for i in range(size):
    cloth_line = []
    cloth_line2 = []
    for j in range(size):
        cloth_line.append(0)
        cloth_line2.append(0)

    cloth_array.append(cloth_line)
    cloth_ids.append(cloth_line2)

id_areas = []
# loop over input
for line in input:
    # read input: the form is "#N @ MM,NN: NXxNY"
    # use rsplit - split into segments, make array
    data = line.rsplit(' ', 3)

    # get lx and ly from the final element
    lengths = data[3].rsplit('x', 1)
    lx = int(lengths[0])
    ly = int(lengths[1])

    # get x and y from the penultimate element
    xy = data[2].rsplit(',', 1)
    x = int(xy[0])
    y = int(xy[1][:-1])

    # append the area of this claim to the id_areas array
    id_areas.append(lx*ly)

    for i in range(x,x+lx):
        for j in range(y,y+ly):
            cloth_array[i][j] += 1
            if (cloth_ids[i][j] == 0):
                cloth_ids[i][j] = int(data[0][1:])
            else:
                cloth_ids[i][j] = 99999


# array is filled now, so loop over and find values > 1
count_overlap = 0
for i in range(size):
    for j in range(size):
        if (cloth_array[i][j] > 1):
            count_overlap += 1

print('There are ', count_overlap, ' square inches claimed by multiple elves')

# loop over the id_areas array, compare to cloth_ids array
for n in range(len(id_areas)):
    count_id = 0
    for i in range(size):
        for j in range(size):
            if ((n+1) == cloth_ids[i][j]):
                count_id += 1

    # when finished, if this is untouched by other claims,
    # it should be the same as the value in id_areas at this location
    if (count_id == id_areas[n]):
        print('ID number ', n+1, 'appears to be untouched')

