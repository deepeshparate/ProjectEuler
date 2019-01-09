import time
start = time.clock()

distinct = []

for a in range(2,101):
    for b in range(2, 101):
        x = a**b
        if x not in distinct:
            distinct.append(x)


print len(distinct)
end = time.clock()
print "time:", end - start

