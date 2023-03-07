"""
words.txt:
    aaaa
    bbbb
    cccc
    zzz (*)
    zzy (*)

    - (*) means it is a friendly word

first_name:
    zhi

returned value:
    0.4 (2 / 5)

"""


def ratio(first_name: str) -> float:
    """
    1. create a variable to count the friendly words, count_friendly
    2. create a variable to count the total words, count_total
    3. Iterate over the entire word list:
        1. remove ending `\n` in each line, assign it to variable, word
        2. check if the word is friendly - if the lengths are the same and the first letters are the same:
            1. if yes, increase the count_friendly
        3. increase the count_total
    4. return the ratio, which is count_friendly / count_total
    """
    count_friendly = 0 
    count_total = 0
    f = open('data/words.txt')  # open the file "words.txt" and read all the words
    for line in f:
        word = line.strip()  # get rid of the '\n' in the end of each line
        # word = line
        if len(word) == len(first_name) and word[0] == first_name.lower()[0]:
            count_friendly += 1
            print(word)
        count_total += 1
    return count_friendly / count_total


print(ratio('alex'))
