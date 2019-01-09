import math
from fractions import Fraction
import time
start = time.clock()

nums = []
dens = []
for num in range(10, 100):
    for den in range(10, 100):
        if (num % 10 == 0 and den % 10 == 0):
            break
        val = Fraction(num, den)
        if val < 1:
            ns = str(num)
            ds = str(den)
            if ns[1] == ds[0]:
                x1 = ns[:1]
                y1 = ds[1:]
                if y1 != str(0):
                    if Fraction(int(x1), int(y1)) == Fraction(num, den):
                        nums.append(num)
                        dens.append(den)

resd = 1
resn = 1
for i in range(0, len(nums)):
    x = Fraction(nums[i], dens[i])
    resd = resd * x.denominator
    resn = resn * x.numerator


print resd/resn
end = time.clock()
print "time:", end - start







