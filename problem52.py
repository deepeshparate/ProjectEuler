import time
start = time.clock()

# x = 142857
for n in range(1, 1000000):
    x = sorted(str(2*n))
    x1 = sorted(str(3*n))
    x2 = sorted(str(4*n))
    x3 = sorted(str(5*n))
    x4 = sorted(str(6*n))
    if x == x1 == x2 == x3 == x4:
        print "result",n
        break

end = time.clock()
print "time:", end - start