import timeit

words = open("data/words.txt").read().split()
word_set = set(words)


def search_list():
    return "zebra" in words


def search_set():
    return "zebra" in word_set


print("List:", timeit.timeit(search_list, number=1000))
print("Set: ", timeit.timeit(search_set, number=1000))
# List: 0.8500s  Set: 0.0003s
