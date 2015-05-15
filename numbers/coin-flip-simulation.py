from random import randint

n = int(raw_input("Number of times to flip coin: "))

heads = 0
tails = 0

for i in range(n):
    side = randint(0, 1)
    if side == 0:
        heads += 1
    else:
        tails += 1

print "Heads:", heads
print "Tails:", tails