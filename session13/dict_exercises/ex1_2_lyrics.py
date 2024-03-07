import string


def process_lyrics(lyrics_file_path):
    """open the lyrics file and return a list of words"""
    f = open(lyrics_file_path)
    # lines = f.readlines()
    # print(lines)
    # for word in line.split():
    #     print(word)
    lyrics = f.read().lower()
    # lyrics = (
    #     lyrics.replace(',', ' ')
    #     .replace('-', ' ')
    #     .replace('(', ' ')
    #     .replace(')', ' ')
    #     .replace('!', ' ')
    # )
    for punc in string.punctuation:
        lyrics = lyrics.replace(punc, ' ')
    word_list = lyrics.split()
    return word_list


def histogram(word_list):
    """convert a word list to a dictionary mapping word to frequency"""
    d = {}
    for word in word_list:
        d[word] = d.get(word, 0) + 1
    return d


def print_hist(h):
    """print items in a dictionary"""
    for k in sorted(h.keys()):
        print(k, h[k])


def print_lyrics_hist(word_list):
    """print word frequency in word_list and output result to a text file"""

    h = histogram(word_list)
    print_hist(h)

    # with open('data/result.txt', 'w') as f:
    #     for word, freq in h.items():
    #         f.write(f'{word}: {freq}\n')


def main():
    lyrics_word_list = process_lyrics("data/hey_jude.txt")
    print_lyrics_hist(lyrics_word_list)


if __name__ == "__main__":
    main()
