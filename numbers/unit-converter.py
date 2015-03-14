def temp():
	i = raw_input("Converting from Fahrenheit (F), Celsius (C), or Kelvin (K): ")
	c = raw_input("Converting to Fahrenheit (F), Celsius (C), or Kelvin (K): ")
	v = float(raw_input("Temperature in " + i.upper() + ": "))
	if i.upper() == c.upper():
		print "That's the same unit! Try again."
		temp()
	if i.upper() == "F" and c.upper() == "C":
		print (v - 32) * 5 / 9
	elif i.upper() == "F" and c.upper() == "K":
		print (v + 459.67) * 5 / 9
	elif i.upper() == "C" and c.upper() == "F":
		print (v * 5 / 9) + 32
	elif i.upper() == "C" and c.upper() == "K":
		print v + 273.15
	elif i.upper() == "K" and c.upper() == "F":
		print (v * 9 / 5) - 459.67
	elif i.upper() == "K" and c.upper() == "C":
		print v - 273.15
	else:
		print "Unfortunately, that's not a valid conversion! Please choose F, C, or K."
		temp()

def volume():
	convert_from = {
	"T": 0.015625,
	"TB": 0.0625,
	"C": 1,
	"P": 2,
	"Q": 4,
	"G": 16
	}
	convert_to = {
	"T": 48,
	"TB": 16,
	"C": 1,
	"P": 0.5,
	"Q": 0.25,
	"G": 0.0625
	}
	i = raw_input("Converting from teaspoons (T), tablespoons (TB), cups (C), pints (P), quarts (Q), gallons (G): ")
	c = raw_input("Converting to teaspoons (T), tablespoons (TB), cups (C), pints (P), quarts (Q), gallons (G): ")
	v = float(raw_input("Volume in " + i.upper() + ": "))
	if i.upper() == c.upper():
		print "That's the same unit! Try again."
		volume()
	print v * convert_from[i.upper()] * convert_to[c.upper()]


category = raw_input("Would you like to convert temperature (T), volume (V), mass (M), or currency (C)? ")

if category.upper() == "T":
	temp()
elif category.upper() == "V":
	volume()
elif category.upper() == "M":
	mass()
elif category.upper() == "C":
	currency()
else:
	print "Unfortunately, that's not a valid conversion! Please choose T, V, M, or C."