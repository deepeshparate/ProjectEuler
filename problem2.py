import time
start = time.clock()

temp = [0] * 300
temp[0] = 1
temp[1] = 2

for i in range(2, 10000):
    x = temp[i-1] + temp[i-2]
    if x < 4000000:
        temp[i] = x
    else:
        break

sums = 0

for j in range(len(temp)):
    if temp[j] % 2 == 0:
        sums = sums + temp[j]

end = time.clock()
print end - start
print sums
