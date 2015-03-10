def pi(n):
    pi = 0
    for k in range(n):
        pi += (4. / (8. * k + 1.) - 2. / (8. * k + 4.) - 1. / (8. * k + 5.) - 1. / (8. * k + 6.)) / 16. ** k
    return pi

n = int(raw_input("Enter a number of digits for pi: "))
print pi(n)