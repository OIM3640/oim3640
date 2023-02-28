from word_sol import uses_only


def spelling_bee(center_letter, available_letters):
    """
    print all the words for spelling bee puzzle
    """
    f = open('data/words.txt')

    for line in f:
        word = line.strip()
        # if the word contains at least 4 letters and the word includes the center letter and the word uses only the avialable letters:
        #   print the word
        if (
            len(word) >= 4
            and center_letter in word
            and uses_only(word, available_letters)
        ):
            print(word)


spelling_bee(center_letter='r', available_letters='aijbdlr')
