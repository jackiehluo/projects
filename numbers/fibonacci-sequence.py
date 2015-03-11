from math import sqrt

def fibonacci(n):
    return ((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5))

n = int(raw_input("Enter a digit n for the nth Fibonacci number: "))

print int(fibonacci(n))