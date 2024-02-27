# https://www.nytimes.com/puzzles/spelling-bee

from word_sol import uses_only


def at_least(word, n):
    """
    Return True if the word has at least n letters
    """
    return len(word) >= n


def must_use(word, letter):
    """Return True if word contains the letter"""
    return letter in word


def spell_bee(must, available):
    """
    Print all the qualified words
    """
    f = open("data/words.txt")
    for line in f:
        word = line.strip()
        # if the word has 4 or more letters and contains the center/required letter and uses only the available letters
        if at_least(word, 4) and must_use(word, must) and uses_only(word, available):
            print(word)


def main():
    centered_letter = "n"
    available = "uizped"
    spell_bee(must=centered_letter, available=available + centered_letter)


if __name__ == "__main__":
    main()
