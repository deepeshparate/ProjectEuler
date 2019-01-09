import time
start = time.clock()

def fact(num):
    f = 1
    while num > 1:
        f = f * num
        num = num - 1
    return f


result = []


for i in range(3, 2000000):
    s = str(i)
    l = len(s)
    sums = 0
    for k in s:
        x = fact(int(k))
        sums = sums + x
    if sums == i:
        result.append(i)

print result
print sum(result)
end = time.clock()
print "time:", end - start


