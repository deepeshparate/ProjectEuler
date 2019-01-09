import math
import time
start = time.clock()

# to check if number is abundant


def divisors(num):
    div = []
    n = int(math.sqrt(num))

    for i in range(1, n+1):
        if num % i == 0:
            div.append(i)
            if num/i != i and num/i != num:
                div.append(num/i)

    if sum(div) > num:
        return 1
    else:
        return 0


n_abundant = []
abundant = []

# generate a list of abundant numbers
for i in range(2, 28124):
    x = divisors(i)
    if x == 1:
        abundant.append(i)


demo = set([i+j for i in abundant for j in abundant if 28124 >= i + j])

n_abundant = list(demo)

result = []

for i in range(1, 28124):
    if i not in n_abundant:
        result.append(i)

print sum(result)
end = time.clock()
print "time:", end - start
