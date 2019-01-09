import time
start = time.clock()


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


def check_ly(num):
    i = 50
    while i > 1:
        s = str(num)
        s_rev = s[::-1]
        x = int(s) + int(s_rev)
        pal = palindrome(x)
        if pal == 1:
            return 0
        num = x
        i = i - 1
    return 1


ly_numbers = []

for i in range(1, 10001):
    res = check_ly(i)
    if res == 1:
        ly_numbers.append(i)

print len(ly_numbers)

end = time.clock()
print "time:", end - start
