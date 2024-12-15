# Advent of code 2024, day 10

# open file
input = open("advent10_input.txt", "r")
# input = open("advent10_test_input1.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    width = len(input_array[0])-1
    height = len(input_array)

    topo_grid = []
    for input in input_array:
        topo_line = []
        for n in range(len(input)-1):
            topo_line.append(int(input[n]))
        topo_grid.append(topo_line)

    print(topo_grid)
    answer = 0

    # Loop through the grid
    for h in range(height):
        for w in range(width):
            if topo_grid[h][w] == 0:
                current_val = 0
                locations = set()
                locations.add((h,w))
                score = 0
                # Find all next value next to current location
                while len(locations) != 0:
                    new_locations = set()
                    print(current_val, locations)

                    for location in locations:
                        if location[0]-1 >= 0:
                            if topo_grid[location[0]-1][location[1]] == current_val+1:
                                new_locations.add((location[0]-1,location[1]))
                        if location[0]+1 < height:
                            if topo_grid[location[0]+1][location[1]] == current_val+1:
                                new_locations.add((location[0]+1,location[1]))
                        if location[1]-1 >= 0:
                            if topo_grid[location[0]][location[1]-1] == current_val+1:
                                new_locations.add((location[0],location[1]-1))
                        if location[1]+1 < width:
                            if topo_grid[location[0]][location[1]+1] == current_val+1:
                                new_locations.add((location[0],location[1]+1))

                    current_val += 1
                    if current_val == 9:
                        print(current_val)
                        print(new_locations)
                        score += len(new_locations)

                    locations = set()
                    for new_location in new_locations:
                        locations.add(new_location)

                print(w, h, score)

                answer += score

    return answer

def part2():

    width = len(input_array[0])-1
    height = len(input_array)

    topo_grid = []
    for input in input_array:
        topo_line = []
        for n in range(len(input)-1):
            topo_line.append(int(input[n]))
        topo_grid.append(topo_line)

    print(topo_grid)
    answer = 0

    # Loop through the grid
    for h in range(height):
        for w in range(width):
            if topo_grid[h][w] == 0:
                current_val = 0
                locations = []
                locations.append((h,w))
                score = 0
                # Find all next value next to current location
                while len(locations) != 0:
                    new_locations = []
                    print(current_val, locations)

                    for location in locations:
                        if location[0]-1 >= 0:
                            if topo_grid[location[0]-1][location[1]] == current_val+1:
                                new_locations.append((location[0]-1,location[1]))
                        if location[0]+1 < height:
                            if topo_grid[location[0]+1][location[1]] == current_val+1:
                                new_locations.append((location[0]+1,location[1]))
                        if location[1]-1 >= 0:
                            if topo_grid[location[0]][location[1]-1] == current_val+1:
                                new_locations.append((location[0],location[1]-1))
                        if location[1]+1 < width:
                            if topo_grid[location[0]][location[1]+1] == current_val+1:
                                new_locations.append((location[0],location[1]+1))

                    current_val += 1
                    if current_val == 9:
                        print(current_val)
                        print(new_locations)
                        score += len(new_locations)

                    locations = []
                    for new_location in new_locations:
                        locations.append(new_location)

                print(w, h, score)

                answer += score

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
