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

    word_to_check = input("Enter a word:")

    start1 = time.time()
    for _ in range(1000):
        if check_in_container(word_to_check, word_dict):
            pass
    end1 = time.time()
    duration_dict = end1 - start1
    print(f"Time taken to search in a dict: {duration_dict}s.")

    start2 = time.time()
    for _ in range(1000):
        if check_in_container(word_to_check, word_list):
            pass
    end2 = time.time()
    duration_list = end2 - start2
    print(f"Time taken to search in a dict: {duration_list}s.")


if __name__ == "__main__":
    main()
