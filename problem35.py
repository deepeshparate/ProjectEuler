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
primes.append(2)

for i in range(3, 1000000, 2):
    y = prime(i)
    if y == 1:
        primes.append(i)

circular = []


def circular_prime(num):
    s = str(num)
    length = len(s)
    while length>0:
        x = s[:1]
        y = s[1:]
        s = y + x
        new_num = prime(int(s))
        if new_num == 0:
            return 0
        length = length - 1
    circular.append(num)


for i in range(0, len(primes)):
    x = circular_prime(primes[i])

print len(circular)
end = time.clock()
print "time:", end - start

