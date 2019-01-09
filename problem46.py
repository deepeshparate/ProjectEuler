# odd composite are numbers with factors other tha prime
# 9, 15, 21, 25, 27
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


primes = list()
composite = list()
primes.append(2)
for i in range(3, 6000, 2):
    x = prime(i)
    if x == 1:
        primes.append(i)
    if x == 0:
        composite.append(i)

extra = []

for x in composite:
    for i in range(0, len(primes)):
        for j in range(1, 100):
            if (primes[i] + 2*(j*j)) == x:
                if x not in extra:
                    extra.append(x)
                    break

print len(extra)
print len(composite)

result = list(set(composite)^set(extra))
print sorted(result)
end = time.clock()
print "time:", end - start
