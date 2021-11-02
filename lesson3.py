incoming_number = 867
inverted_number = 0
while incoming_number > 0:
    number = incoming_number % 10
    incoming_number = incoming_number // 10
    inverted_number = inverted_number * 10 + number
print(inverted_number)
