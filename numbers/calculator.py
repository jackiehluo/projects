def calculate(exp):
    n = []
    for c in exp:
        if c.isdigit():
            n.append(float(c))
        elif (c == "+" or c == "-" or c == "*" or c == "/"):
            op = c
    if op == "+":
        return n[0] + n[1]
    elif op == "-":
        return n[0] - n[1]
    elif op == "*":
        return n[0] * n[1]
    elif op == "/":
        return n[0] / n[1]

exp = [x for x in raw_input("Enter an expression using integers and a basic operation (+, -, *, /): ").split()]
print calculate(exp)