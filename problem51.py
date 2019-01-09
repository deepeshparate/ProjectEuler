import math
from collections import Counter
import time
start = time.clock()


def prime(n):
    if n == 1:
        return 0
    z = int(math.sqrt(n))
    for i in xrange(2, z+1):
        if n % i == 0:
            return 0
    return 1


primes = list()

# generating primes
for i in range(100001, 1000000, 2):
    x = prime(i)
    if x == 1:
        primes.append(i)


def prime_sequence(rep, num):
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    count = 0
    for i in arr:
        s = str(num)
        x = s.replace(str(rep), str(i))
        if x[:1] != str(0) and prime(int(x)) == 1:
            count = count + 1
    return count


zeros = []
ones = []
twos = []

for num in primes:
    s = str(num)
    c = Counter(s[:-1])
    if c["0"] == 3:
        zeros.append(num)
    if c["1"] == 3:
        ones.append(num)
    if c["2"] == 3 :
        twos.append(num)

for x in zeros:
    y = prime_sequence(0, x)
    if y == 8:
        print "lowest prime:", x
        exit()

for x in ones:
    y = prime_sequence(1, x)
    if y == 8:
        print "lowest prime:", x
        exit()

for x in zeros:
    y = prime_sequence(0, x)
    if y == 8:
        print "lowest prime:", x
        break

end = time.clock()
print "time:", end - start
