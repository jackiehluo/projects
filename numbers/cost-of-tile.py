def cost(w, h, t):
    a = w * h
    return round(a * t, 2)

print "We'll find the cost of tiling your room."

w = float(raw_input("Width (feet): "))
h = float(raw_input("Height (feet): "))
t = float(raw_input("Cost of tile per square foot: "))

print "$" + str(cost(w, h, t))