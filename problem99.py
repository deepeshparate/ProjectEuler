import math
import time
start = time.clock()
base = []
exponents = []

f = open('problem99.txt')

for line in f:
    line = line.strip()
    x = line.split(",")
    base.append(int(x[0]))
    exponents.append(int(x[1]))

line_num = 0
max_value = 0

for i in range(0, len(base)):
    y = exponents[i]*math.log(base[i], 10)
    if y > max_value:
        max_value = y
        line_num = i + 1

print line_num
end = time.clock()
print "time:", end - start
