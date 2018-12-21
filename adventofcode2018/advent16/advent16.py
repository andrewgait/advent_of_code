# Advent of code, day 16

# open file
input = open("advent16_part1_input.txt", "r")


# define the 16 different functions
def op_func(name, opcode, registers):
    new_registers = []
    for i in range(len(registers)):
        new_registers.append(registers[i])

    A = opcode[1]
    B = opcode[2]
    C = opcode[3]
    if (name == 'addr'):
        new_registers[C] = registers[A] + registers[B]
    elif (name == 'addi'):
        new_registers[C] = registers[A] + B
    elif (name == 'mulr'):
        new_registers[C] = registers[A] * registers[B]
    elif (name == 'muli'):
        new_registers[C] = registers[A] * B
    elif (name == 'banr'):
        new_registers[C] = registers[A] & registers[B]
    elif (name == 'bani'):
        new_registers[C] = registers[A] & B
    elif (name == 'borr'):
        new_registers[C] = registers[A] | registers[B]
    elif (name == 'bori'):
        new_registers[C] = registers[A] | B
    elif (name == 'setr'):
        new_registers[C] = registers[A]
    elif (name == 'seti'):
        new_registers[C] = A
    elif (name == 'gtir'):
        new_registers[C] = 1 if (A > registers[B]) else 0
    elif (name == 'gtri'):
        new_registers[C] = 1 if (registers[A] > B) else 0
    elif (name == 'gtrr'):
        new_registers[C] = 1 if (registers[A] > registers[B]) else 0
    elif (name == 'eqir'):
        new_registers[C] = 1 if (A == registers[B]) else 0
    elif (name == 'eqri'):
        new_registers[C] = 1 if (registers[A] == B) else 0
    elif (name == 'eqrr'):
        new_registers[C] = 1 if (registers[A] == registers[B]) else 0
    else:
        print('unknown opcode name ', name)

    return new_registers


# array of function names
func_names = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori',
              'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']

# testing
test_opcode = [9, 2, 1, 2]
test_register = [3, 2, 1, 1]
test_result_register = [3, 2, 2, 1]
print('test register: ', test_register, ' test_opcode ', test_opcode,
      'test result register: ', test_result_register)

sum_test = 0
for i in range(len(func_names)):
    new_register = op_func(func_names[i], test_opcode, test_register)
    print(func_names[i], ': ', new_register)
    if (new_register == test_result_register):
        sum_test += 1

print('there are ', sum_test, ' that match the result register in the test')

opcodes = []
input_registers = []
result_registers = []

# read string into array
threeormore = 0
matched_codes = set()
matched_once = set()
n_line = 0
for line in input:
    # first line has the register
    if (n_line % 4 == 0):
        input_register = []
        for i in range(4):
            input_register.append(int(line[9+3*i]))
        input_registers.append(input_register)
    elif (n_line % 4 == 1):
        str_opcode = line.split(' ', 3)
        opcode = []
        for i in range(4):
            opcode.append(int(str_opcode[i]))
        opcodes.append(opcode)
    elif (n_line % 4 == 2):
        result_register = []
        for i in range(4):
            result_register.append(int(line[9+3*i]))
        result_registers.append(result_register)
    # every 4th line is blank
    else:
#        print(input_register, opcode, result_register)
        sum_results = 0
        for i in range(len(func_names)):
            new_register = op_func(func_names[i], opcode, input_register)
            if (new_register == result_register):
                sum_results +=1
                location = i
                tuple = [(func_names[i], opcode[0])]
                matched_codes.add(tuple[0])

        if (sum_results >= 3):
            threeormore += 1

        if (sum_results == 1):
            tup1 = [(func_names[location], opcode[0])]
            matched_once.add(tup1[0])

    n_line += 1

print('there are ', threeormore, ' samples that behave like 3 or more opcodes')
print('len(matched_codes): ', len(matched_codes))

# convert sets to lists
matched_list = list(matched_codes)
matched_once_list = list(matched_once)

# iterate over stuff to work out the codes
while (len(matched_list) > 16):
    remove_index = []
    for i in range(len(matched_list)):
        for j in range(len(matched_once_list)):
            if ((matched_list[i][0] == matched_once_list[j][0]) and
                (matched_list[i][1] != matched_once_list[j][1])):
                remove_index.append(i)

    for n in range(len(remove_index)):
        del matched_list[remove_index[n]-n]

    matched_once_list = []
    # find codes or numbers(?) that are only there once now?
    for n in range(len(func_names)):
       sum = 0
       location = 0
       for i in range(len(matched_list)):
           if (matched_list[i][1] == n):
               sum += 1
               location = i

       if (sum == 1):
           matched_once_list.append(matched_list[location])



print(' ')
matched_list = sorted(matched_list, key = lambda x: x[1])
print('16 codes are: ', matched_list)

# what's the starting register?
part2_register = [0, 0, 0, 0]

input2 = open('advent16_part2_input.txt', 'r')

# read part2 input
for line in input2:
    str_opcode = line.split(' ', 3)
    opcode = []
    for i in range(4):
        opcode.append(int(str_opcode[i]))

    part2_register = op_func(matched_list[opcode[0]][0], opcode, part2_register)

print(' ')
print('register following part2 input is: ', part2_register)

