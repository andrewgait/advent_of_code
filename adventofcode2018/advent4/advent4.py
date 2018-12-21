# Advent of code, day 4

# open file
input = open("advent4_input.txt", "r")

# unsorted array
data = []
month = []

# read file into array
n=0
for line in input:
    data.append(line)
    # while we are here, get the month value
    month.append((n, int(line[6:8]), int(line[9:11]),
                  int(line[12:14]), int(line[15:17])))
    n += 1

input.close()
print(month)

monthsort = sorted(month, key=lambda month: month[1])

print('monthsort: ', monthsort)

daysortfull = []

# loop and now sort by day
start_month = monthsort[0][1]
dayline = []
for i in range(len(monthsort)):
    if (monthsort[i][1] == start_month):
        dayline.append(monthsort[i])
    else:
        # move on to the next one, after sorting the current
        daylinesort = []
        daylinesort = sorted(dayline, key=lambda dayline: dayline[2])
        for j in range(len(daylinesort)):
            daysortfull.append(daylinesort[j])
        # start the next one
        start_month = monthsort[i][1]
        dayline = []
        dayline.append(monthsort[i])

# The last thing that went into dayline needs to be sorted and added
daylinesort = sorted(dayline, key=lambda dayline: dayline[2])
for j in range(len(daylinesort)):
    daysortfull.append(daylinesort[j])

print('daysort: ', daysortfull)

# loop and now sort by hour
hoursortfull = []
start_day = daysortfull[0][2]
hourline = []
for i in range(len(daysortfull)):
    if (daysortfull[i][2] == start_day):
        hourline.append(daysortfull[i])
    else:
        # move on to the next one, after sorting the current
        hourlinesort = []
        hourlinesort = sorted(hourline, key=lambda hourline: hourline[3])
        for j in range(len(hourlinesort)):
            hoursortfull.append(hourlinesort[j])
        # start the next one
        start_day = daysortfull[i][2]
        hourline = []
        hourline.append(daysortfull[i])

# The last thing that went into hourline needs to be sorted and added
hourlinesort = sorted(hourline, key=lambda hourline: hourline[3])
for j in range(len(hourlinesort)):
    hoursortfull.append(hourlinesort[j])

print('hoursort: ', hoursortfull)

# loop and now sort by minute... wait, no.
minutesortfull = []
start_day = hoursortfull[0][2]
minuteline = []
minuteline23 = []
for i in range(len(hoursortfull)):
    if (hoursortfull[i][2] == start_day):
        minuteline.append(hoursortfull[i])
    else:
        # move on to the next one, after sorting the current
        minutelinesort = []
        minuteline23 = []
        # Be careful!  In this case there could be e.g. 2350 and 0050.
        # 2350 needs to come last.
        minutelinesort = sorted(minuteline,
                                key=lambda minuteline: minuteline[4])
        for j in range(len(minutelinesort)):
            # do it here: if there's a 23, save it for the end
            if (minutelinesort[j][3] == 23):
                minuteline23 = minutelinesort[j]
            else:
                minutesortfull.append(minutelinesort[j])

        if (len(minuteline23) > 0):
            minutesortfull.append(minuteline23)

        # start the next one
        start_day = hoursortfull[i][2]
        start_hour = hoursortfull[i][3]
        minuteline = []
        minuteline.append(hoursortfull[i])

# The last thing that went into minuteline needs to be sorted and added
minutelinesort = []
minuteline23 = []
minutelinesort = sorted(minuteline,
                        key=lambda minuteline: minuteline[4])
for j in range(len(minutelinesort)):
    # do it here: if there's a 23, save it for the end
    if (minutelinesort[j][3] == 23):
        minuteline23 = minutelinesort[j]
    else:
        minutesortfull.append(minutelinesort[j])

if (len(minuteline23) > 0):
    minutesortfull.append(minuteline23)

print('minutesort: ', minutesortfull)

output = open('advent4_sortedinput.txt', 'w')

for i in range(len(minutesortfull)):
    output.write(data[minutesortfull[i][0]])

output.close()

# assuming the sorted is correct now, read this and get the required data

# guard id has a max of 4 digits
size = 10000
guard_sleep_array = []
for i in range(size):
    guard_sleep_array.append(0)

# guard never goes to sleep before 00:00
current_id = 0
shiftsleep = 0
for i in range(len(minutesortfull)):
    dataline = data[minutesortfull[i][0]]
    # what does this line say?
    lastword = dataline.rsplit(' ', 1)[1]
    if (lastword == "shift\n"):
        guard_sleep_array[current_id] += shiftsleep
        shiftsleep = 0
        current_id = int(dataline.rsplit(' ', 5)[3][1:])
    elif (lastword == "asleep\n"):
        startsleep = minutesortfull[i][4]
    elif (lastword == "up\n"):
        endsleep = minutesortfull[i][4]
        sleep = endsleep - startsleep
        shiftsleep += sleep

# do the last one as well
guard_sleep_array[current_id] += shiftsleep

# loop again to find id of guard
max_sleep = 0
guard_id = 0
for i in range(len(minutesortfull)):
    if (guard_sleep_array[i] > max_sleep):
        max_sleep = guard_sleep_array[i]
        guard_id = i

print('guard ', guard_id, ' is asleep most, for ', max_sleep, ' minutes')

sleep_array = []
for i in range(60):
    sleep_array.append(0)

count_on = False
for i in range(len(minutesortfull)):
    dataline = data[minutesortfull[i][0]]
    lastword = dataline.rsplit(' ', 1)[1]
    if (lastword == "shift\n"):
        current_id = int(dataline.rsplit(' ', 5)[3][1:])
        if (current_id == guard_id):
            count_on = True
        else:
            count_on = False
    elif (lastword == "asleep\n"):
        startsleep = minutesortfull[i][4]
    elif (lastword == "up\n"):
        endsleep = minutesortfull[i][4]
        if (count_on):
            for j in range(startsleep,endsleep):
                sleep_array[j] +=1

print(sleep_array)
max_minute = 0
minute = 0
for i in range(60):
    if (sleep_array[i] > max_minute):
        max_minute = sleep_array[i]
        minute = i

print('asleep most at minute ', minute, ' guard_id*minute = ', guard_id*minute)

full_sleep_array = []
for i in range(size):
    sleep_line = []
    for j in range(60):
        sleep_line.append(0)

    full_sleep_array.append(sleep_line)

for i in range(len(minutesortfull)):
    dataline = data[minutesortfull[i][0]]
    lastword = dataline.rsplit(' ', 1)[1]
    if (lastword == "shift\n"):
        current_id = int(dataline.rsplit(' ', 5)[3][1:])
    elif (lastword == "asleep\n"):
        startsleep = minutesortfull[i][4]
    elif (lastword == "up\n"):
        endsleep = minutesortfull[i][4]
        for j in range(startsleep,endsleep):
            full_sleep_array[current_id][j] +=1

max_minute = 0
minute = 0
max_id = 0
for i in range(size):
    for j in range(60):
        if (full_sleep_array[i][j] > max_minute):
            max_minute = full_sleep_array[i][j]
            max_id = i
            minute = j

print('guard_id ', max_id, ' asleep most at minute ', minute)
print('for ', max_minute, ' minutes, guard_id*minute = ', max_id*minute)
