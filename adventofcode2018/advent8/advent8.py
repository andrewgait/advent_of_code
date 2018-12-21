# Advent of code, day 8

# open file
input = open("advent8_input.txt", "r")
#input = open("advent8_test_input.txt", "r")

data = []
# read string into array
for line in input:
    # count the number of spaces
    spaces = line.count(' ')
    print(spaces)
    data = line.rsplit(' ', spaces)

size = len(data)
print(size)

node_val_array = []

def read_header_and_sum():
    global data
    global sum
    global node_val_array
#    print(data)
    children = int(data[0])
    entries = int(data[1])
    data = data[2:]
    child_node_val_array = []
    for i in range(children):
        child_node_val_array.append(read_header_and_sum())

#    print('child_node_val_array: ', child_node_val_array)
    node_val = 0
    if (children == 0):
        for j in range(entries):
            sum += int(data[j])
            node_val += int(data[j])
    else:
        # not sure exactly what to do here
        # smells of recursion
        for j in range(entries):
            sum += int(data[j])
            if ((int(data[j])-1) < len(child_node_val_array)):
                node_val += child_node_val_array[(int(data[j])-1)]

#    print('sum: ', sum)
#    print('node_val: ', node_val)
    data = data[entries:]

    return node_val

sum = 0
node_value = read_header_and_sum()

print('node_value is ', node_value)
print('sum total is ', sum)
print('len(data) is ', len(data))
