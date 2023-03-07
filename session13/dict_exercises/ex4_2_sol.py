def has_duplicates(s):
    """Checks whether any element appears more than once in a sequence.

    Simple version using a for loop.

    t: sequence
    """
    d = {}
    for x in s:
        if x in d:
            return True
        d[x] = True
    return False


def main():
    t = [1, 2, 3]
    print(has_duplicates(t))
    t.append(1)
    print(has_duplicates(t))


if __name__ == "__main__":
    main()
