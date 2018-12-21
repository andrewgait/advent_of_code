# Advent of code, day 11

# Note that this solves both parts, but that the loop will take AGES to
# actually do all the square sizes for part 2.  My assumption is that (for some
# reason that I haven't quite worked out yet) the max_power per square_size
# increases to a maximum at a particular square size (15 in this case) and
# then decreases from that point onwards.  If I had time to "prove" it then
# perhaps I would - it could be a derivative of the function with square size,
# somehow... ?
# (I have tested by running down from square_sizes of 300, and the power values
#  basically start as a large negative number and get steadily bigger)

# open file
#input_serials = [8, 18, 39, 42, 57, 71, 1718]
input_serials = [1718]

# function to get value at coordinate
def get_value(power_grid, x, y):
    return power_grid[x-1][y-1]

# function to get total in N*N square
def get_square_value(power_grid, N, x, y):
    sum = 0
    for i in range(x, x+N):
        for j in range(y, y+N):
            sum += power_grid[i][j]
    return sum

# function to do the calculation
def get_power_level(serial):
    # constants
    rackIDpad = 10
    powerlevelsubtract = 5
    # make the 300x300 grid
    grid_size = 300
    power_grid = []
    for i in range(0, grid_size):
        power_line = []
        for j in range(0, grid_size):
            # rackID
            rackID = (i+1) + rackIDpad
            # power level
            power_level = rackID * (j+1)
            # add input serial
            power_level += serial
            # multiply by rackID
            power_level *= rackID
            # get the hundreds digit
            divhundred = power_level // 100
            hundred_digit = divhundred - ((divhundred // 10) * 10)
            power_level = hundred_digit
            # subtract 5
            power_level -= powerlevelsubtract
            power_line.append(power_level)
        power_grid.append(power_line)

    # test some values from the description
    print('serial: ', serial, ' at (3,5):', get_value(power_grid, 3, 5))
    print('serial: ', serial, ' at (122,79):', get_value(power_grid, 122, 79))
    print('serial: ', serial, ' at (217,196):', get_value(power_grid, 217, 196))
    print('serial: ', serial, ' at (101,153):', get_value(power_grid, 101, 153))

    # Now loop and find the value of each 3x3 square
    max_power = -100000
    max_location = [0,0]
    square_size_at_max = 0
#    square_size = 3
    # loop over square size
    for square_size in range(grid_size):  # -1, 0, -1):
        for i in range(0, grid_size-square_size):
            for j in range(0, grid_size-square_size):
                power = get_square_value(power_grid, square_size, i, j)
                if (power > max_power):
                    max_power = power
                    max_location = [i+1, j+1]
                    square_size_at_max = square_size

        print('serial:', serial, 'square_size ', square_size,
              ' max_power ', max_power, ' at ', max_location,
              ' square_size_at_max: ', square_size_at_max)

    # print
    print('serial: ', serial, ' max_power ', max_power, ' at ', max_location,
          ' square_size: ', square_size_at_max)

# call the function with the inputs
for m in range(len(input_serials)):
    get_power_level(input_serials[m])
