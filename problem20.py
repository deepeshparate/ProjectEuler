import time
start = time.clock()


def sum_digits(num):
    a = []
    x = str(num)
    for i in x:
        y = int(i)
        a.append(y)
    return sum(a)


n = 100
fact = 1

while n > 1:

    fact = fact * n

    n = n - 1


result = sum_digits(fact)

print result
end = time.clock()
print "time:", end - start
