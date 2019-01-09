import itertools
import time
start = time.clock()


def check_pan(num):
    s = str(num)
    pan = 1023456789
    if sorted(s) == sorted(str(pan)):
        return 1
    return 0


pans = []

input = [long(x) for x in str(1023456789)]
pan_numbers = itertools.permutations(input)
x = [sum(j *(10**(9 - i)) for i, j in enumerate(k)) for k in pan_numbers]

for n in x:
    y = check_pan(n)
    if y == 1:
        s = str(n)
        two = int(s[1]+s[2]+s[3])
        three = int(s[2]+s[3]+s[4])
        five = int(s[3]+s[4]+s[5])
        seven = int(s[4]+s[5]+s[6])
        eleven = int(s[5]+s[6]+s[7])
        thirteen = int(s[6]+s[7]+s[8])
        seventeen = int(s[7]+s[8]+s[9])
        if two % 2 == 0:
            if three % 3 == 0:
                if five % 5 == 0:
                    if seven % 7 == 0:
                        if eleven % 11 == 0:
                            if thirteen % 13 == 0:
                                if seventeen % 17 == 0:
                                    pans.append(n)


print sum(pans)
end = time.clock()
print "time:", end - start
