import time
start = time.clock()


def sum_digits(num):
    a = []
    x = str(num)
    for j in x:
        y = int(j)
        a.append(y)
    return sum(a)


product = 1

i = 1

while i < 1001:
    product = product * 2
    i = i + 1

result = sum_digits(product)

print result
end = time.clock()
print "time:", end - start
