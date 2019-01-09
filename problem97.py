import time
start = time.clock()

x = pow(2, 7830457, 10000000000)
y = 28433 * x
z = y % 10000000000
result = z + 1
print result

end = time.clock()
print "time:", end - start
