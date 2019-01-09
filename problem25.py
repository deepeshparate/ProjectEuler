import time
start = time.clock()

fib = [0]*100000

fib[0] = 1
fib[1] = 1

for i in range(2,10000):

    thousand = []

    fib[i] = fib[i-1] + fib[i-2]

    s = str(fib[i])

    if len(s) == 1000:
        print fib[i]
        print i+1
        break

end = time.clock()
print "time:", end - start
