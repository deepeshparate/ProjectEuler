from math import sqrt
import time
start = time.clock()


def pentagonal(num):
    p = (sqrt(24*num+1)+1)/6
    x = p.is_integer()
    return x


pent_list = list()

for n in range(1, 10000):
    p = (n*((3*n) - 1))/2
    pent_list.append(p)

D = pent_list[len(pent_list)-1]-pent_list[0]

for i in range(0, len(pent_list)):
    for j in range(i+1, len(pent_list)):
        if pentagonal(pent_list[j] - pent_list[i]) and pentagonal(pent_list[j] + pent_list[i]):
            if D > pent_list[j] - pent_list[i]:
                D = pent_list[j] - pent_list[i]


print D
end = time.clock()
print "time:", end - start


