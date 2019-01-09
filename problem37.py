import math
import time
start = time.clock()


def prime(num):
    if num == 1:
        return 0
    z = int(math.sqrt(num))

    for i in xrange(2,z+1):
        if num % i == 0:
            return 0
    return 1


primes = list()


for i in range(11, 1000000, 2):
    x = prime(i)
    if x == 1:
        primes.append(i)


def circular_prime(num):

    s = str(num)
    # right trunc check
    for i in range(1, len(s)):

        y = prime(int(s[:i]))
        if y == 0:
            return 0
    # left trunc check
    for i in range(1, len(s)):

        y = prime(int(s[i:]))
        if y == 0:
            return 0

    return 1


result = list()

for i in primes:
    res = circular_prime(i)
    if res == 1:
        result.append(i)

print sum(result)
end = time.clock()
print "time:", end - start

