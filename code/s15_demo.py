def histogram(s):
    """Return a dictionary mapping each character in s to the number of times it appears in s."""
    d = {}
    for c in s:
        # d[c] += 1 # This line will raise a KeyError if c is not already a key in d
        d[c] = d.get(c, 0) + 1 # This line will work even if c is not already a key in d
    return d

print(histogram('bookkeeper'))