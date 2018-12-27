import time
start = time.clock()


def fact(num):
    f = 1
    while num > 1:
        f = f * num
        num = num - 1
    return f


number_of_paths = fact(40)/(fact(40-20)*fact(20))

print number_of_paths

end = time.clock()
print "time:", end - start
