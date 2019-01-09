import math
import time
start = time.clock()
res_a = 0

res_b = 0

n = 0

max_n = -1


def prime(num):
    if num < 0:
        num = -1 * num
    z = int(math.sqrt(num))

    for i in xrange(2,z+1):
        if num % i == 0:
            return 0
    return 1


for a in range(-999, 1000):
    # print "a", a
    for b in range(-1000, 1001):
        # print "b", b
        for n in range(0, 200):
            # print "n", n
            eqn = (n*n) + (a*n) + b
            p = prime(eqn)
            if p == 1:
                if n > max_n:
                    max_n = n
                    res_a = a
                    res_b = b
                    n = n + 1
            elif p == 0:
                # print "breaking out of n next printed value should be of b"
                break


result = res_a * res_b

print result
print max_n
print res_b
print res_a
end = time.clock()
print "time:", end - start
