import time
start = time.clock()


def fact(num):
    f = 1
    while num > 1:
        f = f * num
        num = num - 1
    return f


count = 0

for n in range(1, 101):
    for r in range(1, n+1):
        value = fact(n)/((fact(r))*(fact(n-r)))
        if value > 1000000:
            count = count + 1

print count

end = time.clock()
print "time:", end - start