from __future__ import division
import time
start = time.clock()


def count_recurring(num):
    check_list = []
    remainder = 1 % num
    check_list.append(remainder)
    while remainder != 0:
        remainder = (remainder*10) % num
        if remainder in check_list:
            return len(check_list)-check_list.index(remainder)
        check_list.insert(remainder, remainder)
    return 0


print count_recurring(7)

l_streak = 0

d = 0

for i in range(1, 1000):

    x = count_recurring(i)

    if x > l_streak:
        l_streak = x
        d = i

print d
end = time.clock()
print "time:", end - start


