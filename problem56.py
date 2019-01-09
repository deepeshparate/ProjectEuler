import time
start = time.clock()


def find_sum(x):
    s = str(x)
    sums = 0
    for i in range(0, len(s)):
        sums = sums + int(s[i])
    return sums


max_sum = 0

for a in range(1, 100):
    for b in range(1, 100):
        x = a**b
        y = find_sum(x)
        if y > max_sum:
            max_sum = y

print max_sum

end = time.clock()
print "time:", end - start
