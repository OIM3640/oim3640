def histogram(s):
    """
    Return a dict mapping letter to frequency in s
    """
    d = {}
    for c in s:
        # if c not in d:
        #     d[c] = 1
        # else:
        #     d[c] += 1
        d[c] = d.get(c, 0) + 1
    return d


def main():
    print(histogram('bookkeeper'))


if __name__ == '__main__':
    main()
