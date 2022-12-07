# Advent of code 2022, day 7

# open file
input = open("advent7_input.txt", "r")
# input = open("advent7_test_input1.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1firstgo():
    # This method works if all the directories have distinct names
    # Unfortunately this is not the case in the actual input!
    dir_total = 0
    current_dir = "/"
    dirsize_dict = {}
    dircontainsdir_dict = {}

    for input_line in input_array:

        if input_line[0] == "$":
            dirsize_dict[current_dir] = dir_total
            if current_dir not in dircontainsdir_dict.keys():
                dircontainsdir_dict[current_dir] = []
            # A command is coming, i.e. ls or cd
            if input_line[2:4] == "cd":
                current_dir = input_line[5:-1]
                dir_total = 0
            # No action needed for ls in this instance
        else:
            # The first thing in the list is either a number
            # or dir, which we can use to check other dirs inside
            if input_line[0:3] == "dir":
                # add this to dict
                dircontainsdir_dict[current_dir].append(input_line[4:-1])
            else:
                # The first thing is a number, add it to total
                splitspace = input_line.split(" ")
                dir_total += int(splitspace[0])

    dirsize_dict[current_dir] = dir_total

    full_total = 0

    print(dirsize_dict)
    print(dircontainsdir_dict)
    for key, value in dircontainsdir_dict.items():
        key_total = 0
        key_total += dirsize_dict[key]
        n_dirs = len(dircontainsdir_dict[key])
        if n_dirs != 0:
            for n in range(n_dirs):
                key_total += dirsize_dict[dircontainsdir_dict[key][n]]

        if key_total <= 100000:
            full_total += key_total

    answer = full_total

    return answer


# Answer taken from reddit thread looking at the one I understood best...

class Path:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = {}

def calculate_sizes(directory:Path):
    directory.total_size = 0
    for child in directory.children.values():
        directory.total_size += calculate_sizes(
            child) if child.children else child.size
    return directory.total_size

def find_sizes(directory:Path, small_sizes, suitable_sizes, space_needed):
    for child in directory.children.values():
        if child.children:
            find_sizes(child, small_sizes, suitable_sizes, space_needed)
    if directory.total_size <= 100000:
        small_sizes.append(directory.total_size)
    if directory.total_size >= space_needed:
        suitable_sizes.append(directory.total_size)


def part1and2():
    with open("advent7_input.txt") as file:
        root = Path("/", 0, None)
        cur = root
        for line in file:
            line = line.split()
            if line[0] == "$":
                if line[1] == "cd":
                    cur = root if (line[2] == "/") else cur.parent if (
                        line[2] == "..") else cur.children[line[2]]
            else:
                cur.children[line[1]] = Path(
                    line[1], 0 if line[0] == "dir" else int(line[0]), cur)

    calculate_sizes(root)
    small_sizes = []
    suitable_sizes = []
    space_needed = 30000000 - 70000000 + root.total_size
    find_sizes(root, small_sizes, suitable_sizes, space_needed)
    print(sum(small_sizes))
    print(min(suitable_sizes))

    return sum(small_sizes), min(suitable_sizes)

part1, part2 = part1and2()

print("My attempt gave ", part1firstgo())
print("Part 1 answer: ", part1)
print("Part 2 answer: ", part2)
