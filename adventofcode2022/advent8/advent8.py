# Advent of code 2022, day 8
import numpy as np

# open file
input = open("advent8_input.txt", "r")
# input = open("advent8_test_input1.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def tree_is_visible(tree_array, x, y, nx, ny):
    not_vis_dir = 0
    for xx in range(x-1, -1, -1):
        if tree_array[y][x] <= tree_array[y][xx]:
            not_vis_dir += 1
            break
    for xx in range(x+1, nx):
        if tree_array[y][x] <= tree_array[y][xx]:
            not_vis_dir += 1
            break
    for yy in range(y-1, -1, -1):
        if tree_array[y][x] <= tree_array[yy][x]:
            not_vis_dir += 1
            break
    for yy in range(y+1, ny):
        if tree_array[y][x] <= tree_array[yy][x]:
            not_vis_dir += 1
            break

    if not_vis_dir == 4:
        return 0
    else:
        return 1

def part1():

    tree_array = []

    for input_line in input_array:
        tree_line= []
        for n in range(len(input_line)-1):
            tree_line.append(int(input_line[n]))
        tree_array.append(tree_line)

    print(tree_array)
    ny = len(tree_array)
    nx = len(tree_array[0])
    visible = 0
    for y in range(ny):
        for x in range(nx):
            if y == 0 or y == ny-1 or x == 0 or x == nx-1:
                visible +=1
            else:
                visible += tree_is_visible(tree_array, x, y, nx, ny)

    answer = visible

    return answer

def scenic_score(tree_array, x, y, nx, ny):
    l_score = 0
    for xx in range(x-1, -1, -1):
        l_score += 1
        if tree_array[y][x] <= tree_array[y][xx]:
            break
    r_score = 0
    for xx in range(x+1, nx):
        r_score += 1
        if tree_array[y][x] <= tree_array[y][xx]:
            break
    u_score = 0
    for yy in range(y-1, -1, -1):
        u_score += 1
        if tree_array[y][x] <= tree_array[yy][x]:
            break
    d_score = 0
    for yy in range(y+1, ny):
        d_score += 1
        if tree_array[y][x] <= tree_array[yy][x]:
            break

    # print("scores: x y", x, y, l_score, r_score, u_score, d_score)
    return l_score * r_score * u_score * d_score

def part2():

    tree_array = np.zeros(shape=(len(input_array),
                                 len(input_array[0])-1), dtype=int)

    m = 0
    for input_line in input_array:
        for n in range(len(input_line)-1):
            tree_array[m][n] = int(input_line[n])
        m += 1

    print(tree_array)
    ny = len(tree_array)
    nx = len(tree_array[0])
    max_score = 0
    # The edges all score 0 so don't bother with them
    for y in range(1,ny-1):
        for x in range(1,nx-1):
            score = scenic_score(tree_array, x, y, nx, ny)
            if score > max_score:
                max_score = score

    answer = max_score

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
