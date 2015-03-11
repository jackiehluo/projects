def next(n):
    prime = False
    while prime == False:
        n += 1
        prime = True
        for i in primes:
            if n % i == 0:
                prime = False
        if prime == True:
            primes.append(n)
            return n

run = True
n = 1
primes = [2]

print "The first prime is 2."

while run == True:
    ans = raw_input("Would you like the next prime? ")
    if ans.lower() == "yes":
        n = next(n)
        print n
    else:
        print "Good to know! Thanks for the interest."
        run = False