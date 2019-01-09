import time
start = time.clock()
coins = [1, 2, 5, 10, 20, 50, 100, 200]

ways = 0

for hundred in range(0, 3):
    for fifty in range(0, 5):
        for twenty in range(0, 11):
            for ten in range(0, 21):
                for five in range(0, 41):
                    for two in range(0, 101):
                        for one in range(0, 201):
                            val = hundred*100 + fifty*50 + twenty*20 + ten*10 + five*5 + two*2 + one
                            if val == 200:
                                ways = ways + 1
                            # to reduce unnecessary iterations
                            elif val > 200:
                                break

# adding one to ways as 200 itself is an option
ways = ways + 1
print ways
end = time.clock()
print "time:", end - start
