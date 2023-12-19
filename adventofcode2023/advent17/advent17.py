# Advent of code 2023, day 17
import numpy as np
import networkx as netx

# open file
input = open("advent17_input.txt", "r")
# input = open("advent17_input_test.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    nx = len(input_array[0][:-1])
    ny = len(input_array)
    city_blocks = []

    for y in range(ny):
        city_line = []
        for x in range(nx):
            city_line.append(int(input_array[y][x]))
        city_blocks.append(city_line)

    # start at [0,0]
    starts = ["h_0_0", "v_0_0"] # (0,0)
    ends = ["h_"+str(nx-1)+"_"+str(ny-1), "v_"+str(nx-1)+"_"+str(ny-1)] # (nx-1,ny-1)

    print(city_blocks)
    print(starts, ends)

    citygraph = netx.DiGraph()

    # A simple graph of all the nodes connected in the "normal" way
    # takes too long to search
    # So instead we make a graph with nodes for going vertical and horizontal
    # to deal with being forced to turn before going at most 3 points in any direction
    # (Credit: I saw this described on the subreddit boards...)

    # Add nodes
    for y in range(ny):
        for x in range(nx):
            citygraph.add_node("h_"+str(x)+"_"+str(y))
            citygraph.add_node("v_"+str(x)+"_"+str(y))

    # Add edges
    for y in range(ny):
        for x in range(nx):
            # connect h_x_y to up to six v_x_yy horizontally
            for yy in range(y-3,y+4):
                if yy >=0 and yy < ny and yy != y:
                    sum_weight = 0
                    if yy < y:
                        for yyy in range(yy,y):
                            sum_weight += city_blocks[yyy+1][x]
                    if yy > y:
                        for yyy in range(y,yy):
                            sum_weight += city_blocks[yyy][x]
                    vnode = "v_"+str(x)+"_"+str(yy)
                    hnode = "h_"+str(x)+"_"+str(y)
                    citygraph.add_edge(vnode, hnode, weight=sum_weight)
                    # print("edge from ", vnode, " to ", hnode, " weight ", sum_weight)
            # connect v_x_y to up to six h_xx_y vertically
            for xx in range(x-3,x+4):
                if xx >=0 and xx < nx and xx != x:
                    sum_weight = 0
                    if xx < x:
                        for xxx in range(xx,x):
                            sum_weight += city_blocks[y][xxx+1]
                    if xx > x:
                        for xxx in range(x,xx):
                            sum_weight += city_blocks[y][xxx]
                    hnode = "h_"+str(xx)+"_"+str(y)
                    vnode = "v_"+str(x)+"_"+str(y)
                    citygraph.add_edge(hnode, vnode, weight=sum_weight)
                    # print("edge from ", hnode, " to ", vnode, " weight ", sum_weight)

    print(netx.number_of_nodes(citygraph))
    print(netx.number_of_edges(citygraph))

    answer = 100000000000
    for start in starts:
        for end in ends:
            shortest_path = netx.shortest_path(citygraph, start, end, 'weight')
            path_weight = netx.path_weight(citygraph, shortest_path, 'weight')
            print(start, end, path_weight)
            if path_weight < answer:
                answer = path_weight

    return answer


def part2():

    nx = len(input_array[0][:-1])
    ny = len(input_array)
    city_blocks = []

    for y in range(ny):
        city_line = []
        for x in range(nx):
            city_line.append(int(input_array[y][x]))
        city_blocks.append(city_line)

    # start at [0,0]
    starts = ["h_0_0", "v_0_0"] # (0,0)
    ends = ["h_"+str(nx-1)+"_"+str(ny-1), "v_"+str(nx-1)+"_"+str(ny-1)] # (nx-1,ny-1)

    print(city_blocks)
    print(starts, ends)

    citygraph = netx.DiGraph()

    # A simple graph of all the nodes connected in the "normal" way
    # takes too long to search
    # So instead we make a graph with nodes for going vertical and horizontal
    # to deal with being forced to turn before going at least 4 and at most 10 points in any direction

    # Add nodes
    for y in range(ny):
        for x in range(nx):
            citygraph.add_node("h_"+str(x)+"_"+str(y))
            citygraph.add_node("v_"+str(x)+"_"+str(y))

    # Add edges
    for y in range(ny):
        for x in range(nx):
            # print(" ")
            # connect h_x_y to up to fourteen v_x_yy horizontally
            # (seven in each direction between four and ten inclusive)
            for yy in range(y-10,y+11):
                if yy >=0 and yy < ny and abs(yy-y) > 3:
                    sum_weight = 0
                    if yy < y:
                        for yyy in range(yy,y):
                            sum_weight += city_blocks[yyy+1][x]
                    if yy > y:
                        for yyy in range(y,yy):
                            sum_weight += city_blocks[yyy][x]
                    vnode = "v_"+str(x)+"_"+str(yy)
                    hnode = "h_"+str(x)+"_"+str(y)
                    citygraph.add_edge(vnode, hnode, weight=sum_weight)
                    # print("edge from ", vnode, " to ", hnode, " weight ", sum_weight)
            # connect v_x_y to up to fourteen h_x_yy vertically
            # (seven in each direction between four and ten inclusive)
            for xx in range(x-10,x+11):
                if xx >=0 and xx < nx and abs(xx-x) > 3:
                    sum_weight = 0
                    if xx < x:
                        for xxx in range(xx,x):
                            sum_weight += city_blocks[y][xxx+1]
                    if xx > x:
                        for xxx in range(x,xx):
                            sum_weight += city_blocks[y][xxx]
                    hnode = "h_"+str(xx)+"_"+str(y)
                    vnode = "v_"+str(x)+"_"+str(y)
                    citygraph.add_edge(hnode, vnode, weight=sum_weight)
                    # print("edge from ", hnode, " to ", vnode, " weight ", sum_weight)

    print(netx.number_of_nodes(citygraph))
    print(netx.number_of_edges(citygraph))

    answer = 100000000000
    for start in starts:
        for end in ends:
            shortest_path = netx.shortest_path(citygraph, start, end, 'weight')
            path_weight = netx.path_weight(citygraph, shortest_path, 'weight')
            print(start, end, path_weight)
            if path_weight < answer:
                answer = path_weight

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
