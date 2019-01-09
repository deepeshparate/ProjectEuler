
import time
import math
start = time.clock()


def amicable(num):
    lst = []
    z = int(math.sqrt(num))
    for i in range(1, z+1):
        if num % i == 0:
            lst.append(i)
            if num/i != i and num/i != num:
                lst.append(num/i)

    return sum(lst)


amicable_list = list()

for i in range(1, 10000):

    a = amicable(i)

    if amicable(a) == i and a != i:
        amicable_list.append(a)
        amicable_list.append(i)


print sum(set(amicable_list))
end = time.clock()
print "time:", end - start
