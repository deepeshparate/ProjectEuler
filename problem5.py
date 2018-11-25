import time
start = time.clock()
x = 1


while x >= 1:
    if x % 2 == 0 and x % 3 == 0 and x % 4 == 0 and x % 5 == 0 and x % 6 == 0 and x % 7 == 0 and x % 8 == 0 and x % 9 == 0 and x % 10 == 0 and x % 11 == 0 and x % 12 == 0 and x % 13 == 0 and x % 14 == 0 and x % 15 == 0 and x % 16 == 0 and x % 17 == 0 and x % 18 == 0 and x % 19 == 0 and x % 20 == 0:
        print x
        break
    x = x+1

end = time.clock()
print "time:", end - start
