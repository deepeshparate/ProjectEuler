import time
start = time.clock()

n = 600851475143

temp = []

i = 2
while i <= n:
    if n % i == 0:
        temp.append(i)
        n = n/i
    i = i + 1


print temp
prime = -1

for i in temp:
    num = i
    if i > prime:
        prime = num

end = time.clock()
print end - start
print prime
