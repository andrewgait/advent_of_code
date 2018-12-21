# Advent of code, day 19

# open file
input = open("advent19_input.txt", "r")
#input = open("advent19_test_input.txt", "r")

# define the 16 different functions (from day 16)
def op_func(opcode, registers):
    new_registers = []
    for i in range(len(registers)):
        new_registers.append(registers[i])

    name = opcode[0]
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

first_line = True
ip_value = None
instructions = []
# read string into array
for line in input:
    if (first_line):
        data = line.split(' ', 1)
        ip_value = int(data[1])
        first_line = False
    else:
        data = line.split(' ', 3)
        instruction_line = []
        for i in range(len(data)):
            if (i==0):
                instruction_line.append(data[i])
            else:
                instruction_line.append(int(data[i]))

        instructions.append(instruction_line)


print('ip_value ', ip_value)
print('instructions ', instructions)

# initial register size 6
register = [0,0,0,0,0,0]  # part 1
# register = [1,0,0,0,0,0]  # part 2

current_ip_value = ip_value

cheat = True
while (current_ip_value < len(instructions)):
#time = 0
#while (time < 10):
#    register[ip_value] = current_ip_value
    # this takes forever in part 2 (I have no idea why)
    # so there must be a repeating pattern that can be dealt with somehow

    # ok so looking at the pattern, it loops along instructions 3->11 A LOT
    # so basically what happens is that instruction 4 increments register
    # 3 by 1 if it's less than register 5, which is 10.5 million... lol
    # so can I just set register 4 to register 5 minus 1 and get away with that?
    # NOPE... apparently not


    inst = register[ip_value]
    #print('instruction: ', inst, ': ', instructions[inst])
    new_register = op_func(instructions[inst], register)

    # print(register, new_register)

    new_register[ip_value] += 1

    register = []
    for i in range(6):
        register.append(new_register[i])

    current_ip_value = new_register[ip_value]
    #time += 1

print('part 1: ', new_register)

current_ip_value = ip_value
register=[1,0,0,0,0,0]
# part 2

# so by cheating (or searching for help) I know the answer is the sum of the (prime) factors
# of the number that ends up in the highest register at the start, this number is 10551417
# sum(factors(10551417)) = 1 + 3 + 3517139 + 10551417 = 14068560

# I have no real idea how to code this up though.