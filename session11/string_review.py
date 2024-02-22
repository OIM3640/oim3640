def has_vowel(s):
    """Return True if s contains any vowel letter, otherwise return False"""
    for c in s:
        if c in "aeiou":
            return True

    return False


# print(has_vowel("babson"))  # True
# print(has_vowel("bbc"))  # False


def any_uppercase6(s):
    for c in s:
        if c.isupper():
            break  # exit the for loop, not gonna excute the rest of the loop
            return True
    return False


print(any_uppercase6("iPhone"))
