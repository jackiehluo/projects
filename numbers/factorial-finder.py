def loop_factorial(n):
	product = 1
	for i in range(1, n + 1):
		product *= i
	return product

def recursive_factorial(n):
	if n == 0:
		return 1
	else:
		return n * recursive_factorial(n - 1)

n = int(raw_input("Enter the value n for n!: "))
try:
	print "Using a loop, the factorial is: " + str(loop_factorial(n))
	print "Using recursion, the factorial is: " + str(recursive_factorial(n))
except:
	print "Something went wrong. Did you enter a number?"