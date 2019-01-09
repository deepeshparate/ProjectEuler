# 0123456789101112131415161718192021
import time
start = time.clock()

digit = str()
s = str(123456789)

digit = digit + s
zero = str(0)
one = str(1)
two = str(2)
three = str(3)
four = str(4)
five = str(5)
six = str(6)
seven = str(7)
eight = str(8)
nine = str(9)

for i in range(1, 50000):
    a = str(i) + zero
    b = str(i) + one
    c = str(i) + two
    d = str(i) + three
    e = str(i) + four
    f = str(i) + five
    g = str(i) + six
    h = str(i) + seven
    j = str(i) + eight
    k = str(i) + nine
    digit = digit + a + b + c + d + e + f + g + h + j + k
    if len(digit) == 1000000:
        break

x1 = digit[0]
x2 = digit[9]
x3 = digit[99]
x4 = digit[999]
x5 = digit[9999]
x6 = digit[99999]
x7 = digit[999999]

result = int(x1) * int(x2) * int(x3) * int(x4) * int(x5) * int(x6) * int(x7)

print result
end = time.clock()
print "time:", end - start
