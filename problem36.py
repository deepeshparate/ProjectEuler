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


palindromes = []

for i in range(1, 1000001):

    pal = palindrome(i)
    if pal == 1:
        palindromes.append(i)


result = list()

for i in palindromes:

    binary = '{0:b}'.format(i)

    pal_check = palindrome(int(binary))

    if pal_check == 1:
        result.append(i)

print sum(result)
end = time.clock()
print "time:", end - start


