import time
start = time.clock()

temp1 = []
temp2 = []

for i in range(0, 100):
    temp1.append((i+1)**2)

sum_of_squares = 0

for j in range(len(temp1)):
    sum_of_squares = sum_of_squares + temp1[j]


for i in range(0, 100):
    temp2.append(i+1)

square_of_sum = 0
ss = 0

for j in range(len(temp2)):
    ss = ss + temp2[j]

square_of_sum = ss**2

result = square_of_sum - sum_of_squares
print result
end = time.clock()
print "time:", end - start
