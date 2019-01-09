from math import sqrt
import time
start = time.clock()
# odd n are hexagonal and triangle


def pentagonal(num):
    p = (sqrt(24*num+1)+1)/6
    x = p.is_integer()
    return x


for n in range(143, 100000, 2):
    t = (n*(n + 1)/2)
    if pentagonal(t):
        print t

end = time.clock()
print "time:", end - start
