def primes(n):
    factors = []
    i = 2
    while i ** 2 <= n:
        while (n % i) == 0:
            if i not in factors:
                factors.append(i)
            n /= i
        i += 1
    if n > 1:
       factors.append(n)
    return factors

n = int(raw_input("Enter a number for prime factorization: "))

print primes(n)