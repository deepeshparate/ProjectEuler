import time
start = time.clock()

words = dict()

# initializing few values

words[1] = "one"
words[2] = "two"
words[3] = "three"
words[4] = "four"
words[5] = "five"
words[6] = "six"
words[7] = "seven"
words[8] = "eight"
words[9] = "nine"
words[10] = "ten"
words[11] = "eleven"
words[12] = "twelve"
words[13] = "thirteen"
words[14] = "fourteen"
words[15] = "fifteen"
words[16] = "sixteen"
words[17] = "seventeen"
words[18] = "eighteen"
words[19] = "nineteen"
words[20] = "twenty"
words[30] = "thirty"
words[40] = "forty"
words[50] = "fifty"
words[60] = "sixty"
words[70] = "seventy"
words[80] = "eighty"
words[90] = "ninety"

already = [30, 40, 50, 60, 70, 80, 90]

for i in range(21, 100):
    if i in already:
        continue
    first = i/10*10
    second = i % 10
    words[i] = words.get(first) + words.get(second)

words[100] = "onehundred"

for i in range(101, 1000):
    x = i/100
    y = i % 100
    if y == 0:
        z = str(words.get(x)) + "hundred"
    else:
        z = str(words.get(x)) + "hundredand" + str(words.get(y))
    words[i] = z


words[1000] = "onethousand"

s = str()

for key, value in words.items():
    s = s + str(value)


print len(s)
end = time.clock()
print "time:", end - start
