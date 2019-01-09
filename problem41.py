import math
import time
start = time.time()


def is_pandigital(num):
    n = str(num)
    l = len(n)
    s = ''
    for i in range(1, l+1):
        s = s + str(i)
    s = sorted(s)
    return s == sorted(n)


n = 7654321
primes = []
A = [True]*(n+1)
i = 2
while i*i <= n:
    if A[i]:
        for j in range(i*2, n+1, i):
            A[j] = False
    i += 1

for i in range(2, len(A)):
    if A[i]:
        primes.append(i)

for k in range(len(primes)-1, 0, -1):
    if is_pandigital(primes[k]):
        print primes[k]
        break

end = time.time()
print "time:", end - start
