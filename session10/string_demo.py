prefixes = "JKLMNOPQ"
suffix = "ack"
for letter in prefixes:
    # if the letter is O or Q:
    #   then print letter + "u" + suffix
    # else:
    #   then print letter + suffix
    if letter == "O" or letter == "Q":
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)
