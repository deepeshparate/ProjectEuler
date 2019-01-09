import time
start = time.clock()


def check_pan(num):
    s = num
    pan = 123458769
    pan_digit = sorted(str(pan))
    if sorted(s) == pan_digit:
        return 1
    return 0


max_no = 0

for integer in range(1, 10000):
    x = str()
    for n in range(1, 500):
        mul = integer * n
        x = x + str(mul)
        if len(x) > 9:
            break
        y = check_pan(x)
        if y == 1 and int(x) > max_no:
            max_no = int(x)

print max_no
end = time.clock()
print "time:", end - start
