def pig_latin(s):
	vowels = ["a", "e", "i", "o", "u"]
	string = []
	for w in s:
		if w[0].lower() in vowels:
			string.append(w + "way")
		else:
			string.append(w[1:] + w[0] + "ay")
	return " ".join(map(str, string))

s = raw_input("Translate to Pig Latin: ").split()
print pig_latin(s)