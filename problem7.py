import time
import math

start = time.clock()
temp = []


def prime(num):
    z = int(math.sqrt(num))
    for i in xrange(2, z+1):
        if num % i == 0:
            return 0
    return 1


for i in range(2, 50000):
    x = prime(i)
    if x == 1:
        temp.append(i)

for i in range(50001, 100000):
    y = prime(i)
    if y == 1:
        temp.append(i)

for i in range(100001, 105000):
    x = prime(i)
    if x == 1:
        temp.append(i)


print len(temp)
print temp[10000]
end = time.clock()
print "time:", end - start
