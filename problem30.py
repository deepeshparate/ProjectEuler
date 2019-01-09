import time
start = time.clock()

numbers = []


def power_five(num):
    s = str(num)
    sums = 0
    for i in s:
        x = int(i)**5
        sums = sums + x
    if num == sums:
        return 1
    else:
        return 0


for i in range(2, 1000000):
    x = power_five(i)
    if x == 1:
        numbers.append(i)

print sum(numbers)
end = time.clock()
print "time:", end - start
