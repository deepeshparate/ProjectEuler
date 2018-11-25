import time
temp = []
start = time.clock()

for i in range(0,1000):
    if i%3 == 0 or i%5 == 0:
        temp.append(i)

sums = 0
for j in range(len(temp)):
    sums = sums + temp[j]

end = time.clock()
print end - start
print sums
