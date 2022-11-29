import os

begin = 1

for i in range(begin,26):
    basename = 'advent'+str(i)
    if not os.path.isdir(basename):
        os.mkdir(basename)
    output = open(basename+'/'+basename+".py", "w")
    output.write('# Advent of code 2022, day '+str(i)+'\n')
    output.write('\n')
    output.write('# open file\n')
    output.write('input = open("advent'+str(i)+'_input.txt", "r")\n')
    output.write('\n')
    output.write('input_array = []\n')
    output.write('# read string into array\n')
    output.write('for line in input:\n')
    output.write('    input_array.append(line)\n')
    output.write('\n')
    output.write('def part1():\n')
    output.write('\n')
    output.write('    answer = 0\n')
    output.write('\n')
    output.write('    return answer\n')
    output.write('\n')
    output.write('def part2():\n')
    output.write('\n')
    output.write('    answer = 0\n')
    output.write('\n')
    output.write('    return answer\n')
    output.write('\n')
    output.write('print("Part 1 answer: ", part1())\n')
    output.write('print("Part 2 answer: ", part2())\n')
    output.close()
