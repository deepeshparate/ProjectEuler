import time
import math

start = time.clock()
triangles = []


def factor(num):
    count = 0
    z = int(math.sqrt(num))
    for i in range(1, z+1):
        if num % i == 0:
            count += 1
            if num/i != i:
                count += 1

    return count


for i in range(1, 50000):
    n = (i*(i+1))/2
    triangles.append(n)


for i in range(0, len(triangles)):
    x = triangles[i]
    y = factor(x)
    if y > 500:
        print triangles[i]
        break

end = time.clock()
print "time:", end - start
