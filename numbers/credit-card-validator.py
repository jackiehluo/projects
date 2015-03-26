def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10
 
def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0

card_number = raw_input("Please enter the card number: ")
valid = is_luhn_valid(card_number)
if valid == True:
    print "Your card is valid."
else:
    print "I'm sorry, that card is invalid."