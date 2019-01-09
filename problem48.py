import time
start = time.clock()
result = []

for i in range(1, 1001):
    x = i**i
    result.append(x)

print sum(result)
end = time.clock()
print "time:", end - start
