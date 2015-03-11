def calculate(t, r, v):
    m = r / 100 / 12
    p = v * (m *(m + 1) ** (t * 12)) / ((m + 1) ** (t * 12) - 1)
    return round(p, 2)

t = int(raw_input("Enter the mortgage period in years: "))
r = float(raw_input("Enter the interest rate: "))
v = float(raw_input("Enter the value of the loan: "))

print "The monthly rate for a " + str(t) + "-year mortgage is $" + str(calculate(t, r, v)) + "."