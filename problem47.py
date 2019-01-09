import math
import time
start = time.clock()


def prime(num):
    if num == 1:
        return 0
    z = int(math.sqrt(num))
    for i in xrange(2, z+1):
        if num % i == 0:
            return 0
    return 1


def factor(num):
    lst = []
    z = int(math.sqrt(num))
    for i in range(2, z+1):
        if num % i == 0:
            if prime(i) == 1:
                lst.append(i)
            if num/i != i and prime(num/i) == 1:
                lst.append(num/i)

    return len(lst)


result = list()

for i in range(1, 1000000):
    if factor(i) == 4 and factor(i+1) == 4 and factor(i+2) == 4 and factor(i+3) == 4:
        result.append(i)
        result.append(i+1)
        result.append(i+2)
        result.append(i+3)
        break


print result
end = time.clock()
print "time:", end - start
