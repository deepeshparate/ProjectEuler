import time
start = time.clock()
MonthDaysCount = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def count_days():
    day = 1
    day_count = 0

    for y in range(1900, 2000):
        for m in range(len(MonthDaysCount)):
            day += MonthDaysCount[m]
            if y % 4 == 0 and m == 1:
                day += 1
            if day % 7 == 0:
                day_count += 1
    return day_count


print count_days()
end = time.clock()
print "time:", end - start
