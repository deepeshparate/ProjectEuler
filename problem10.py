import time
import math
start = time.clock()


def prime(num):
    z = int(math.sqrt(num))
    for i in xrange(2, z+1):
        if num % i == 0:
            return 0
    return 1


primes = list()
primes.append(2)


for j in range(3, 2000000, 2):
    x = prime(j)
    if x == 1:
        primes.append(j)

print sum(primes)
end = time.clock()
print "time:", end - start
