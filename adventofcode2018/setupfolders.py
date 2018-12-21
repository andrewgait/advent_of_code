import os

begin = 6

for i in range(begin,26):
    basename = 'advent'+str(i)
    os.mkdir(basename)
    output = open(basename+'/'+basename+".py", "w")
    output.write('# Advent of code, day '+str(i)+'\n')
    output.write('\n')
    output.write('# open file\n')
    output.write('input = open("advent'+str(i)+'_input.txt", "r")\n')
    output.write('\n')
    output.write('# read string into array\n')
    output.write('for line in input:\n')
    output.close()
