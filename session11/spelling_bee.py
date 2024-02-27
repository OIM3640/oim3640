# https://www.nytimes.com/puzzles/spelling-bee

from word_sol import uses_only


def spell_bee(must, available):
    f = open('data/words.txt')
    for line in f:
        word = line.strip()
        # if the word has 4 or more letters and contains the center/required letter and uses only the available letters
        if len(word) >= 4 and must in word and uses_only(word, available):
            print(word)


def main():
    must_use = "e"
    available = "otblci"
    spell_bee(must=must_use, available=available + must_use)


if __name__ == "__main__":
    main()
