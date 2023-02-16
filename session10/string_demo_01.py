prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    # if letter == "Q" or letter == "O":
    # if letter in ['Q', 'O']:
    if letter in 'QO':
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)

