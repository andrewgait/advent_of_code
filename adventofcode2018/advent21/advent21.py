# Advent of code, day 21
import matplotlib.pyplot as plt

# open file
input = open("advent21_input.txt", "r")

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
# register = [0,0,0,0,0,0]  # part 1
test_register = 0  # 11592302 (part 1 answer)

register = [test_register,0,0,0,0,0]  # part 1

current_ip_value = ip_value

register1_inst28 = []

time = 0
repeating = False
while ((current_ip_value < len(instructions)) and (not repeating)):

    inst = register[ip_value]
    new_register = op_func(instructions[inst], register)

    if (inst == 28):
#        print('instruction: ', inst, ': ', instructions[inst], ' time: ', time)
#        print(register, new_register)
        if (len(register1_inst28) > 1):
            try:
                index = register1_inst28.index(register[1])
                repeating = True
                print('last registers: ', register1_inst28[-2:])
            except:
                dummy = 0
#                print(register[1], ' not found in list')
#                print('last registers: ', register1_inst28[-2:])
                if ((len(register1_inst28) % 100) == 0):
                    print('len(register1_inst28) = ', len(register1_inst28))

        register1_inst28.append(register[1])


    new_register[ip_value] += 1

    register = []
    for i in range(6):
        register.append(new_register[i])

    current_ip_value = new_register[ip_value]
    time += 1

print('part 1: ', new_register, ' in time ', time)

# The answer for part 1 was reverse-engineered
# from observing the results starting at test_register = 0
# if the loop hits instruction 28 with register 0 = register 1
# then it ends up outside it a few instructions later.
# (this seems to be something of a lucky guess, but the time
#  was so small (< 2000) that I figured it was the correct answer)
# So the number picked was the number I saw in register 1 the first time
# instruction 28 was reached in my initial tests.

# The answer for part 2 must surely depend on how stuff gets into
# register 0.  Which is not clear from the instruction set or from any tests so far

# draw a plot of the values for part 2... ?
plt.plot(register1_inst28)
plt.ylabel('register 1 value')
plt.xlabel('kind of time')
plt.show()
