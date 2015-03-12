from math import floor

def change(c, m):
    d = m - c
    dollars = int(floor(d))
    coins = int((d - floor(d)) * 100)
    twenties = 0
    tens = 0
    fives = 0
    ones = 0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    if dollars > 0:
        twenties = dollars / 20
        tens = (dollars % 20) / 10
        fives = (dollars % 10) / 5
        ones = (dollars % 5)
    if coins > 0:
        quarters = coins / 25
        dimes = (coins % 25) / 10
        nickels = (coins % 10) / 5
        pennies = (coins % 5)
    return "Twenties: " + str(twenties) + "\n" + "Tens: " + str(tens) + "\n" + "Fives: " + str(fives) + "\n" + "Ones: " + str(ones) + "\n" + "Quarters: " + str(quarters) + "\n" + "Dimes: " + str(dimes) + "\n" + "Nickels: " + str(nickels) + "\n" + "Pennies: " + str(pennies) + "\n"


c = float(raw_input("How much did the item cost? $"))
m = float(raw_input("How much money did you give? $"))

print change(c, m)