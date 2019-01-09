import time
start = time.time()
pan = 123458769
pan_digit = sorted(str(pan))
#result = [0]*999999999
result = set()
for x in range(1, 10000):
    for y in range(1, 10000):
        z = x * y
        #if result[z] == z:
         #   break
        s = str(z) + str(x) + str(y)
        if len(s) == 9:
            if sorted(s) == pan_digit:
                #result.insert(z, z)
                result.add(z)

print sum(result)
end = time.time()
print "time:", end - start



