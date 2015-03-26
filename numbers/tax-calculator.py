def calculate(cost, rate):
	tax = round(cost * (rate / 100), 2)
	total = round(cost * (1 + rate / 100), 2)
	return tax, total

cost = float(raw_input("Enter the cost: $"))
rate = float(raw_input("Tax Percentage: "))
try:
	tax, total = calculate(cost, rate)
	print "Tax: $" + str(tax)
	print "Total: $" + str(total)
except:
	print "Something went wrong. Did you enter tax out of a hundred? For example, sales tax might be 8.25, not 0.00825."