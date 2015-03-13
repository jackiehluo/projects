def to_binary(n):
	return bin(n)

def to_decimal(n):
	return int(n, 2)

choice = raw_input("Would you like to convert from decimal to binary (A) or binary to decimal (B)? ")

if choice.upper() == "A":
	n = int(raw_input("Please enter your number: "))
	print to_binary(n)
elif choice.upper() == "B":
	n = raw_input("Please enter your number: ")
	print to_decimal(n)
else:
	print "I'm sorry, I didn't understand your response. Please choose A or B!"