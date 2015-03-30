def palindrome(s):
	if s.lower() == s.lower()[::-1]:
		return "It's a palindrome."
	else:
		return "It's not a palindrome."

s = raw_input("Enter a string: ")
print palindrome(s)