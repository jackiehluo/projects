from collections import Counter

def count_vowels(s):
	vowels = ["A", "E", "I", "O", "U"]
	v = []
	for c in s.upper():
		if c in vowels:
			v.append(c)
	counts = Counter(v)
	total = 0
	for k, v in counts.items():
		print k + ": " + str(v)
		total += v
	print "Total: "+ str(total)

s = raw_input("Enter a string: ")
count_vowels(s)