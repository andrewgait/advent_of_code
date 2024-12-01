# Advent of code 2023, day 21
import numpy as np
from collections import deque
import networkx as netx

# open file
input = open("advent21_input.txt", "r")
input = open("advent21_input_test.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

garden_dict = {".": 0, "#": 1, "O": 2, "S": 3}
garden_rev_dict = {0: ".", 1: "#", 2: "O", 3: "S"}

def print_garden(garden_array, start):
    ny = len(garden_array)
    nx = len(garden_array[0])
    for y in range(ny):
        garden_line = ""
        for x in range(nx):
            if start[0] == y and start[1] == x and (garden_array[y][x] != garden_dict["O"]):
                garden_line += "S"
            else:
                garden_line += garden_rev_dict[garden_array[y][x]]
        print(garden_line)
    print(" ")


def part1():

    nx = 0
    ny = 0
    start = [0,0]
    garden_array = []
    for input in input_array:
        garden_array_line = []
        nx = 0
        for inp in input[:-1]:
            if inp == "S":
                start = [ny,nx]
            garden_array_line.append(garden_dict[inp])
            nx += 1
        garden_array.append(garden_array_line)
        ny += 1

    garden_array = np.array(garden_array)

    print_garden(garden_array, start)

    garden_array[start[0]][start[1]] = garden_dict["O"]

    n_steps = 6

    for n in range(n_steps):
        new_garden_array = np.zeros((ny,nx))
        new_Os = []
        for y in range(ny):
            new_garden_array_line = []
            for x in range(nx):
                if garden_array[y][x] == garden_dict["O"]:
                    # Set it to .
                    garden_array[y][x] == garden_dict["."]
                    # Check in every direction around this for .
                    if x-1 >= 0:
                        if garden_array[y][x-1] == garden_dict["."]:
                            new_garden_array[y][x-1] = garden_dict["O"]
                            new_Os.append([y,x-1])
                    if y-1 >= 0:
                        if garden_array[y-1][x] == garden_dict["."]:
                            new_garden_array[y-1][x] = garden_dict["O"]
                            new_Os.append([y-1,x])
                    if x+1 < nx:
                        if garden_array[y][x+1] == garden_dict["."]:
                            new_garden_array[y][x+1] = garden_dict["O"]
                            new_Os.append([y,x+1])
                    if y+1 < ny:
                        if garden_array[y+1][x] == garden_dict["."]:
                            new_garden_array[y+1][x] = garden_dict["O"]
                            new_Os.append([y+1,x])
                else:
                    if [y,x] not in new_Os:
                        new_garden_array[y][x] = garden_array[y][x]


        garden_array = new_garden_array.copy()
        n_possible = 0
        for y in range(ny):
            for x in range(nx):
                if garden_array[y][x] == garden_dict["O"]:
                    n_possible += 1
        print("Step ", n+1, n_possible)

    print_garden(new_garden_array, start)

    answer = 0
    for y in range(ny):
        for x in range(nx):
            if garden_array[y][x] == garden_dict["O"]:
                answer += 1


    return answer

def part2():

    nx = 0
    ny = 0
    start = [0,0]
    garden_array = []
    for input in input_array:
        garden_array_line = []
        nx = 0
        for inp in input[:-1]:
            if inp == "S":
                start = [ny,nx]
                garden_array_line.append(garden_dict["."])
            else:
                garden_array_line.append(garden_dict[inp])
            nx += 1
        garden_array.append(garden_array_line)
        ny += 1

    garden_array = np.array(garden_array)

    print_garden(garden_array, start)

    # n_steps = 1000

    # Feels like this must be possible using a deque in some way
    # though how can that be made quadruple-ended rather than double-ended?

    # The first step's answer is contained in the third step's answer, which
    # is contained in the fifth step's answer, and so on.

    # The below works for the low values but it's not viable for the final answer

    moves = [[-1,0],[0,1],[0,-1],[1,0]]

    n_steps = 10

    Os = [start]
    new_Os = set()
    new_Os.add((start[0],start[1]))
    # new_Os = deque()
    # new_Os.append((start[0],start[1]))
    for n in range(n_steps//2):
        # # new_Os = set()
        # # print(new_Os, Os)
        # # newly_added_Os = []
        # for Opt in Os:
        #     osy = Opt[0]
        #     osx = Opt[1]
        #     for move1 in moves:
        #         if garden_array[(osy+move1[0]) % ny][(osx+move1[1]) % nx] == garden_dict["."]:
        #             for move2 in moves:
        #                 if garden_array[(osy+move1[0]+move2[0]) % ny][(osx+move1[1]+move2[1]) % nx] == garden_dict["."]:
        #                     # new_Os.append((osy+move1[0]+move2[0], osx+move1[1]+move2[1]))
        #                     new_pt = (osy+move1[0]+move2[0], osx+move1[1]+move2[1])
        #                     new_Os.add(new_pt)
        #                     # if new_pt not in Os:
        #                     #     newly_added_Os.append(new_pt)
        #
        # # Os = list(newly_added_Os)
        # Os = list(new_Os)
        # print("Step ", 2*(n+1), len(new_Os))
        my_answer = do_moves(garden_array, nx, ny, moves, start[1], start[0], 0, 2*(n+1), new_Os)

        print("Step ", 2*(n+1), len(my_answer))  #, my_answer)

    # Sadly doing this is also far too slow and breaks the maximum recursion depth
    # answer = do_moves(garden_array, nx, ny, moves, start[1], start[0], 0, 2*(5000+1), new_Os)
     # len(my_answer)

    # Perhaps it's also possible that it can be done using graphs
    # If we go from start and make graphs whereby the weight of each # is max(n_steps) +  1
    # and the weight of each . is 1, then counting the number of paths with an even length
    # where the weight is less than max(n_steps) will give the answer?

    garden_graph = netx.Graph()

    n_steps = 1000

    # Add nodes
    for y in range(-n_steps, n_steps+1):
        for x in range(-n_steps, n_steps+1):
            test_y = start[0] + y
            test_x = start[0] + x
            nodestr = str(test_y)+"_"+str(test_x)
            garden_graph.add_node(nodestr) #, garden_array[test_y % ny][test_x % nx])

    print(netx.number_of_nodes(garden_graph))

    # Add edges
    for y in range(-n_steps, n_steps):
        for x in range(-n_steps, n_steps):
            test_y = start[0] + y
            test_x = start[0] + x
            nodestr = str(test_y)+"_"+str(test_x)
            test_y_1 = start[0] + y + 1
            nodedownstr = str(test_y_1)+"_"+str(test_x)
            test_x_1 = start[0] + x + 1
            noderightstr = str(test_y)+"_"+str(test_x_1)
            if ((garden_array[test_y % ny][test_x % nx] == garden_dict["."]) and
                (garden_array[test_y_1 % ny][test_x % nx]) == garden_dict["."]):
                garden_graph.add_edge(nodestr, nodedownstr, weight=1)
            else:
                garden_graph.add_edge(nodestr, nodedownstr, weight=n_steps+1)
            if ((garden_array[test_y % ny][test_x % nx] == garden_dict["."]) and
                (garden_array[test_y % ny][test_x_1 % nx]) == garden_dict["."]):
                garden_graph.add_edge(nodestr, noderightstr, weight=1)
            else:
                garden_graph.add_edge(nodestr, noderightstr, weight=n_steps+1)

    print(netx.number_of_edges(garden_graph))

    answer = 0
    start_str = str(start[1])+"_"+str(start[0])
    paths = netx.single_source_dijkstra_path(garden_graph, start_str, n_steps, "weight")

    for path in paths.values():
        path_weight = netx.path_weight(garden_graph, path, "weight")
        if path_weight % 2 == 0:
            answer += 1
            print(answer, path_weight)

    return answer

def do_moves(garden_array, nx, ny, moves, osy, osx, depth, max_depth, answer):
    # print("Adding value from ", osy, osx, " at ", depth)
    answer.add((osy, osx))
    if depth < max_depth:
        for move1 in moves:
            new_osy1 = (osy+move1[0])
            new_osx1 = (osx+move1[1])
            if garden_array[new_osy1 % ny][new_osx1 % nx] == garden_dict["."]:
                for move2 in moves:
                    new_osy2 = (new_osy1+move2[0])
                    new_osx2 = (new_osx1+move2[1])
                    if garden_array[new_osy2 % ny][new_osx2 % nx] == garden_dict["."]:
                        # answer += 1
                        # depth += 2
                        answer = do_moves(garden_array, nx, ny, moves,
                                          new_osy2, new_osx2, depth+2, max_depth, answer)

        depth += 2

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
