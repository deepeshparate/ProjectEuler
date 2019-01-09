import time
start = time.clock()

# for getting range
count = 1
for i in range(5,1002,2):
    count = count + 1

print count


total_sum = 0

# top-right diagonal


one = list()

one.append(1)
one.append(9)
for i in range(2, 501):

    one.append(((one[i-1] - one[i-2]) + 8) + one[i-1])


# print one
# low-right diagonal


two = list()

two.append(1)
two.append(3)
for i in range(2, 501):

    two.append(((two[i-1] - two[i-2]) + 8) + two[i-1])


# print two

# top-left diagonal


three = list()

three.append(1)
three.append(7)
for i in range(2, 501):

    three.append(((three[i-1] - three[i-2]) + 8) + three[i-1])


# print three


# low-left diagonal


four = list()

four.append(1)
four.append(5)

for i in range(2, 501):

    four.append(((four[i-1] - four[i-2]) + 8) + four[i-1])


# print four


res = sum(one) + sum(two) + sum(three) + sum(four)

total_sum = res - 3

print total_sum
end = time.clock()
print "time:", end - start


