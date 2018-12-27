import time
start = time.clock()
start_num = 0
largest_count = 0


def seriescount(num):
    x = list()
    x.append(num)
    while num != 1:
        if num % 2 == 0:
            num = num/2
            x.append(num)
        else:
            num = 3*num + 1
            x.append(num)
    return len(x)


for i in range(2, 1000000):
    val = seriescount(i)
    if val > largest_count:
        largest_count = val
        start_num = i

end = time.clock()
print "time:", end - start
print start_num
