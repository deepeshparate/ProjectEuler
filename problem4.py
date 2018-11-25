import time
start = time.clock()
temp = []


def palindrome(n):
    rev = 0
    n1 = n
    while n > 0:
        x = n % 10
        rev = x + rev*10
        n = n/10
    if n1 == rev:
        return 1
    else:
        return 0


for i in range(100, 1000):
    for j in range(100, 1000):
        mup = i*j
        y = palindrome(mup)
        if y == 1:
            temp.append(mup)

end = time.clock()
print "time:", end - start
print max(temp)
