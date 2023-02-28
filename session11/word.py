# import os
# print(os.getcwd())


# Assume words.txt is under data folder
# f = open('data/words.txt')
# line = f.readline()
# print(line)

# f = open('data/words.txt')

# number_of_words = 0

# for line in f:
#     word = line.strip()
#     number_of_words += 1

# print(number_of_words)


def find_long_words():
    """
    prints only the words with more than 20 characters
    """
    f = open('data/words.txt')  # Assume words.txt is under data folder

    for line in f:
        word = line.strip()
        if len(word) > 20:
            print(word, len(word))


# find_long_words()


def has_no_e(word):
    """
    returns True if the given word doesn't have the letter "e" in it
    """
    # if 'e' not in word.lower():
    #     return True
    # else:
    #     return False
    return 'e' not in word.lower()


# print(has_no_e('Babson')) # True
# print(has_no_e('College')) # False
# print(has_no_e('EA sports')) # False


def find_words_no_e():
    """
    returns the percentage of the words that don't have the letter "e"
    """
    counter_words_no_e = 0
    counter_total = 0

    # Check each word, aka for letter in word list
    #   increase counter_total
    #   if the word has no e:
    #       increase counter_words_no_e
    #
    # After checking all words, aka finishing for loop
    # return counter_words_no_e / counter_total

    f = open('data/words.txt')

    for line in f:
        word = line.strip()
        counter_total += 1
        if has_no_e(word):
            counter_words_no_e += 1

    return counter_words_no_e / counter_total


perc_no_e = find_words_no_e()
print(f'The percentage of the words with no "e" is {perc_no_e:.2%}.')


def avoids(word, forbidden):
    """
    returns True if the given word does not use any of the forbidden letters
    """
    pass


# print(avoids('Babson', 'abcde'))
# print(avoids('College', 'e'))
# print(avoids('Boston', 'xyz'))


def find_words_no_vowels():
    """
    returns the percentage of the words that don't have vowel letters
    """
    pass


# perc_no_vowel = find_words_no_vowels()
# print(f'The percentage of the words without vowel letters is {perc_no_vowel*100:.2f}%.')


def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the string available.
    """
    pass


# print(uses_only('Babson', 'aBbsonxyz'))
# print(uses_only('college', 'aBbsonxyz'))


def find_words_only_use_planet():
    """"""
    pass


# print('Number of words that use only letters from "planets" is', find_words_only_use_planet())


def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    pass


# please write test cases


def find_words_using_all_vowels():
    """
    return the number of the words that use all the vowel letters
    """
    pass


# print('The number of words that use all the vowels:', find_words_using_all_vowels())


def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    pass


# print(is_abecedarian('abs'))
# print(is_abecedarian('college'))


def find_abecedarian_words():
    """
    returns the number of abecedarian words
    """
    pass


# print(find_abecedarian_words())


def is_abecedarian_using_recursion(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    pass


# print(is_abecedarian_using_recursion('abcdef'))


def is_abecedarian_using_while(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    pass


# print(is_abecedarian_using_while('abcdef'))
