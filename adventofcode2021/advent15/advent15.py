# Advent of code, day 15
import networkx as nx
import numpy as np

# open file
input = open("advent15_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    answer = 0

    grid = []
    risk = []
    nj = len(input_array)
    ni = len(input_array[0]) - 1
    for j in range(nj):
        grid_line = []
        risk_line = []
        for i in range(ni):
            grid_line.append(int(input_array[j][i]))
            risk_line.append(0)
        grid.append(grid_line)
        risk.append(risk_line)

    print(grid)

    # Just traverse the grid in order and sum the risk at each point
    # (compare minimums...)
    # this does assume that going left or up is impossible...
    for j in range(nj):
        for i in range(ni):
            if (i == 0) and (j == 0):
                risk[j][i] = 0
            elif (i == 0):
                risk[j][i] = risk[j-1][i] + grid[j][i]
            elif (j == 0):
                risk[j][i] = risk[j][i-1] + grid[j][i]
            else:
                min_risk = 0
                if (risk[j][i-1] < risk[j-1][i]):
                    min_risk = risk[j][i-1]
                else:
                    min_risk = risk[j-1][i]
                risk[j][i] = min_risk + grid[j][i]

    answer = risk[nj-1][ni-1]

    return answer


# Answer above works fine if always going down or right, but as going up or left
# is possible too, must implement something like Dijkstra; borrowing a networkx solution from
# https://github.com/julian-west/adventofcode/blob/master/2021/day_15/d15_solution.py
def get_neighbors(x, y, m, n):
    """Get values of neighbouring coordinates on the grid"""
    potential = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(x, y) for x, y in potential if 0 <= x <= m and 0 <= y <= n]


def create_graph(grid, m, n):
    """Create a networkx directed weighted graph from the grid"""
    g = nx.grid_2d_graph(m, n, create_using=nx.DiGraph)
    for x in range(m):
        for y in range(n):
            for neighbour in get_neighbors(x, y, m, n):
                g.add_edge(neighbour, (x, y), weight=grid[x][y])
    return g


def create_big_grid(small_grid, size = 5):
    """Create a bigger grid from the small grid"""
    return np.block(
        [[(small_grid + i + j - 1) % 9 + 1 for j in range(size)] for i in range(size)]
    )


def part2():

    with open("advent15_input.txt", "r") as input:
        input = input.read().splitlines()
        grid = np.array([[int(x) for x in list(row)] for row in input])

    answer = 0

    grid = create_big_grid(grid)

    m, n = grid.shape
    g = create_graph(grid, m, n)
    answer = nx.shortest_path_length(g, (0, 0), target=(m - 1, n - 1), weight="weight")

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
