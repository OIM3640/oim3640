import time


def create_dict():
    """
    Return a dictionary of words from words.txt
    """
    d = {}
    f = open("data/words.txt")
    for line in f:
        word = line.strip()
        d[word] = 1
    return d


def check_in_container(word, container):
    """
    Return True if the word is in container
    """
    return word in container


def create_list():
    """
    Return a list of words from words.txt
    """
    words = []
    f = open("data/words.txt")
    for line in f:
        word = line.strip()
        words.append(word)
    return words


def main():
    word_dict = create_dict()
    word_list = create_list()

    word_to_check = input('Enter a word:')

    start = time.time()
    if check_in_container(word_to_check, word_dict):
        print('Yes')
    end1 = time.time()
    duration_dict = end1 - start
    print(f'Checking in dict takes {duration_dict}s.')

    if check_in_container(word_to_check, word_list):
        print('Yes')
    end2 = time.time()
    duration_list = end2 - end1
    print(f'Checking in list takes {duration_list}s.')


if __name__ == "__main__":
    main()
