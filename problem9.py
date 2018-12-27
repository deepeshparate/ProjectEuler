import time
start = time.clock()
values = []


for i in range(1, 500):
    for j in range(1, 500):
        k = 1000 - i - j
        if i*i + j*j == k*k:
            values.append(i)
            values.append(j)
            values.append(k)


result = values[0]*values[1]*values[2]

print result
end = time.clock()
print "time:", end - start
