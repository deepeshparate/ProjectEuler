import itertools
import time
start = time.clock()



x = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))

y = sorted(x)

print x[999999]
end = time.clock()
print "time:", end - start