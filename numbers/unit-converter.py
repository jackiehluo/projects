import urllib2
import json

def temp():
	i = raw_input("Converting from Fahrenheit (F), Celsius (C), or Kelvin (K): ")
	c = raw_input("Converting to Fahrenheit (F), Celsius (C), or Kelvin (K): ")
	v = float(raw_input("Temperature in " + i.upper() + ": "))
	if i.upper() == c.upper():
		print "That's the same unit! Try again."
		temp()
	if i.upper() == "F" and c.upper() == "C":
		print str((v - 32) * 5 / 9) + " " + c.upper()
	elif i.upper() == "F" and c.upper() == "K":
		print str((v + 459.67) * 5 / 9) + " " + c.upper()
	elif i.upper() == "C" and c.upper() == "F":
		print str((v * 5 / 9) + 32) + " " + c.upper()
	elif i.upper() == "C" and c.upper() == "K":
		print str(v + 273.15) + " " + c.upper()
	elif i.upper() == "K" and c.upper() == "F":
		print str((v * 9 / 5) - 459.67) + " " + c.upper()
	elif i.upper() == "K" and c.upper() == "C":
		print str(v - 273.15) + " " + c.upper()
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
	i = raw_input("Converting from teaspoons (T), tablespoons (TB), cups (C), pints (P), quarts (Q), or gallons (G): ")
	c = raw_input("Converting to teaspoons (T), tablespoons (TB), cups (C), pints (P), quarts (Q), or gallons (G): ")
	v = float(raw_input("Volume in " + i.upper() + ": "))
	if i.upper() == c.upper():
		print "That's the same unit! Try again."
		volume()
	print str(v * convert_from[i.upper()] * convert_to[c.upper()]) + " " + c.upper()

def mass():
	i = raw_input("Converting from kilograms (KG) or pounds (LB): ")
	c = raw_input("Converting to kilograms (KG) or pounds (LB): ")
	v = float(raw_input("Mass in " + i.upper() + ": "))
	if i.upper() == c.upper():
		print "That's the same unit! Try again."
		mass()
	if i.upper() == "KG" and c.upper() == "LB":
		print str(v * 2.2046) + " " + c.upper()
	elif i.upper() == "LB" and c.upper() == "KG":
		print str(v / 2.2046) + " " + c.upper()
	else:
		print "Unfortunately, that's not a valid conversion! Please choose F, C, or K."
		mass()

def currency():
	p = urllib2.urlopen("http://openexchangerates.org/api/latest.json?app_id=9f0710764c064370932f4f2496968c62")
	r = p.read().decode(encoding='UTF-8')
	d = json.loads(r)
	print "Please use three-letter currency codes! For example, USD is the U.S. currency."
	i = raw_input("Converting from the currency: ")
	c = raw_input("Converting to the currency: ")
	v = float(raw_input("Value in " + i.upper() + ": "))
	try:
		convert_from = d["rates"][i.upper()]
		convert_to = d["rates"][c.upper()]
		print str(round(((convert_to / convert_from) * v), 2)) + " " + c.upper()
	except:
		print "Unfortunately, that's not a valid conversion! Please enter valid currency codes."
		currency()

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