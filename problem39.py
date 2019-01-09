import collections
import time
start = time.clock()

result = {}


def sides(p):
    count = 0
    for c in range(1, p/2):
        for b in range(1, c):
            a = p - b - c
            if a*a + b*b == c*c and a < b < c:
                    count = count + 1
    result[p]=count


print sides(120)
# print result


for i in range(120, 1001):
    sides(i)

value = collections.Counter(result)
print value.most_common(1)
end = time.clock()
print "time:", end - start

