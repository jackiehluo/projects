from decimal import *

n = int(raw_input("Enter the number of digits of e: "))

getcontext().prec = n
print Decimal(1).exp()