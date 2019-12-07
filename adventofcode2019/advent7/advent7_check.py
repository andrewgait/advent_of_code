# From https://github.com/KTConnolly/advent-of-code-2019/blob/master/day_7/run.py

from itertools import permutations


def read(file):
    with open(file, "r") as f:
        return [int(i) for i in f.readline().split(",")]


class Program:
    def __init__(self, code, setting):
        self.code = code.copy()
        self.inputs = [setting]
        self.i = 0

    def get_opcode(self):
        return self.code[self.i] % 100

    def get_modes(self):
        m1 = (self.code[self.i] // 100) % 10
        m2 = (self.code[self.i] // 1000) % 10
        m3 = (self.code[self.i] // 10000) % 10
        return m1, m2, m3

    def run(self, inputs):
        self.inputs += inputs

        while self.i < len(self.code):
            op = self.get_opcode()
            m1, m2, m3 = self.get_modes()

            if op == 99:
                break

            p1, p2, p3 = None, None, None

            if op in (1, 2, 7, 8):
                p1 = self.i + 1 if m1 == 1 else self.code[self.i + 1]
                p2 = self.i + 2 if m2 == 1 else self.code[self.i + 2]
                p3 = self.i + 3 if m3 == 1 else self.code[self.i + 3]
            elif op in (3, 4):
                p1 = self.i + 1 if m1 == 1 else self.code[self.i + 1]
            elif op in (5, 6):
                p1 = self.i + 1 if m1 == 1 else self.code[self.i + 1]
                p2 = self.i + 2 if m2 == 1 else self.code[self.i + 2]

            if op == 1:
                self.code[p3] = self.code[p1] + self.code[p2]
                self.i += 4

            elif op == 2:
                self.code[p3] = self.code[p1] * self.code[p2]
                self.i += 4

            elif op == 3:
                self.code[p1] = self.inputs.pop(0)
                self.i += 2

            elif op == 4:
                self.i += 2
                return self.code[p1]

            elif op == 5:
                self.i = self.code[p2] if self.code[p1] != 0 else self.i + 3

            elif op == 6:
                self.i = self.code[p2] if self.code[p1] == 0 else self.i + 3

            elif op == 7:
                self.code[p3] = int(self.code[p1] < self.code[p2])
                self.i += 4

            elif op == 8:
                self.code[p3] = int(self.code[p1] == self.code[p2])
                self.i += 4


def part_one():
    code = read("advent7_input.txt")
    outputs = []

    for settings in permutations(range(5)):
        amps = [Program(code, setting) for setting in settings]

        output = 0
        for amp in amps:
            output = amp.run(inputs=[output])

        outputs.append(output)

    return max(outputs)


def part_two():
    code = read("advent7_test_input4.txt")
    outputs = []

    for settings in permutations(range(5, 10)):
        amps = [Program(code, setting) for setting in settings]

        output = 0
        while True:
            for amp in amps:
                output = amp.run([output])

            if output:
                print(output)
                outputs.append(output)
            else:
                print(output)
                break

    return max(outputs)

print(part_one())
print(part_two())