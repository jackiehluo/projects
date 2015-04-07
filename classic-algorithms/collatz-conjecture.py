def collatz(n):
    steps = 0
    while n != 1:
        steps += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
    return str(steps)

n = int(raw_input("Enter a number: "))
print collatz(n) + " steps"