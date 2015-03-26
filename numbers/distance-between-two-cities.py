from geopy.geocoders import Nominatim
from geopy.distance import vincenty

def distance(start, end, unit):
	geolocator = Nominatim()
	one = geolocator.geocode(start)
	two = geolocator.geocode(end)
	if unit.upper() == "KM":
		return round(vincenty((one.latitude, one.longitude), (two.latitude, two.longitude)).miles * 1.60934, 1)
	elif unit.upper() == "MI":
		return round(vincenty((one.latitude, one.longitude), (two.latitude, two.longitude)).miles, 1)

print "You can find the distance between two points anywhere in the world! Enter a city and state/country or a specific address."
start = raw_input("Starting Point: ")
end = raw_input("Ending Point: ")
unit = raw_input("Distance in kilometers (KM) or miles (MI)? ")
try:
	print distance(start, end, unit), unit
except:
	print "Unfortunately, we can't find that distance. Did you enter the correct formats?"