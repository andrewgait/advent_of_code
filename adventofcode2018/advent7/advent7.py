# Advent of code, day 7

# open file
#input = open("advent7_test_input.txt", "r")
#alphabet = 'ABCDEF'
#n_workers = 2
#set_time = 1

input = open("advent7_input.txt", "r")
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n_workers = 5
set_time = 61

array_sets = []
original_array_sets = []
counted = []
time_task = []
for n in range(len(alphabet)):
    array_sets.append(set())
    original_array_sets.append(set())
    counted.append(0)
    time_task.append(set_time+n)

print(time_task)

# read string into array
for line in input:
    # 9 spaces
    data = line.rsplit(' ', 9)
    step = data[1]
    next_step = data[7]

    n = alphabet.index(next_step)
    # print(n)
    array_sets[n].add(step)
    original_array_sets[n].add(step)

print(array_sets)

# part 2 (comment out to make part 1 work)
# can't get this to work properly yet.
# got the perl solution off the reddit to compare and get solution
entries = True
final_string = ''
work_array = []
time_left = []
currently_working = []
current_tasks = []
for n in range(n_workers):
    work_array.append([])
    time_left.append(0)
    currently_working.append(0)
    current_tasks.append(0)

previous_string = ''
n_working = 0
time = 0
this_string = []
started_tasks = []
while entries:
    count_empty = 0
    for n in range(len(array_sets)):
        if (len(array_sets[n]) == 0):
            count_empty += 1
            if (counted[n] == 0):
                counted[n] = 1
                this_string.append(alphabet[n])

    # find the time length for this task and add it
    print('this_string: ', this_string)

    tasks = len(this_string)

    for n in range(n_workers):
        # give the task to a worker that's not doing anything
        if (currently_working[n] == 0):
            if (n < len(this_string)):
                found = False
                for ll in range(len(this_string)):
                    for mm in range(len(work_array)):
                        if (len(work_array[mm]) > 0):
                            if (this_string[n] == work_array[mm][len(work_array[mm])-1]):
                                found = True

                currently_working[n] = 1
                if (not found):
                    work_array[n].append(this_string[n])
                    time_left[n] = time_task[alphabet.index(this_string[n])]-1
                else:
                    ind = (n+1) % len(this_string)
                    work_array[n].append(this_string[ind])
                    time_left[n] = time_task[alphabet.index(this_string[ind])]-1
            else:
                work_array[n].append(0)
        else:
            if (time_left[n] == 0):
                currently_working[n] = 0
                for m in range(len(array_sets)):
                    try:
                        array_sets[m].remove(work_array[n][len(work_array[n])-1])
                        string_index = this_string.index(work_array[n][len(work_array[n])-1])
                        del this_string[string_index]
                    except:
                        blah = []
#                time -= 1
                break
            else:
                # make sure the correct value gets appended
                work_array[n].append(work_array[n][len(work_array[n])-1])
                time_left[n] -= 1

    print('time_left: ', time_left)
    print('work_array: ', work_array)
    print('array_sets: ', array_sets)
    print('time: ', time)

    time += 1

    if (time > 1165):
        entries = False

    sum_size = 0
    time_left_total = 0
    for n in range(len(array_sets)):
        sum_size += len(array_sets[n])
    for m in range(n_workers):
        time_left_total += time_left[m]

    print('sum_size: ', sum_size)
    if ((sum_size == 0) and (len(started_tasks) == len(alphabet)) and (time_left_total == 0)):
        entries = False


print('time: ', time)

# comment out to here for part 1 to work

# part 1
# entries = True
# final_string = ''
# while entries:
#     # find the first entry that is empty
#     count_empty = 0
#     for n in range(len(array_sets)):
#         if (len(array_sets[n]) == 0):
#             count_empty += 1
#             # has it not been counted yet
#             if (counted[n] == 0):
#                 # count it, and append to final string now
#                 counted[n] = 1
#                 final_string += alphabet[n]
#                 # remove all instances from each set
#                 for m in range(len(array_sets)):
#                     try:
#                         array_sets[m].remove(alphabet[n])
#                     except:
#                         blah = []
#                         # print('not here')
#                 break
#
#     print(final_string)
#
#     if (count_empty == len(array_sets)):
#         entries = False







