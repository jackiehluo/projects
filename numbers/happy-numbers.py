n = int(raw_input("Enter a number: "))
visited = set()

while True:
    if n == 1:
        print "It's a happy number! :)"
        break
    n = sum(int(i) ** 2 for i in str(n))
    if n in visited:
        print "It's not a happy number. :("
        break
    visited.add(n)