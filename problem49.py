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

for i in range(1000, 9999):
    y = prime(i)
    if y == 1:
        primes.append(i)

for a in range(0, len(primes)):
    for b in range(a + 1, len(primes)):
        for c in range(b+1, len(primes)):
            if primes[c] - primes[b] == primes[b] - primes[a]:
                sa = str(primes[a])
                sb = str(primes[b])
                sc = str(primes[c])
                if sorted(sa) == sorted(sb) and sorted(sb) == sorted(sc):
                    print primes[a], primes[b], primes[c]

end = time.clock()
print "time:", end - start