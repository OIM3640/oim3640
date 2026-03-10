# a = [1, 2, 3]
# b = a #  making an alias
# b.append(4)
# print(f'a = {a}, b = {b}')
# print(a is b)


# a = [1, 2, 3]
# b = a[:] # b = a.copy(), making a copy
# b.append(4)
# print(f'a = {a}, b = {b}')
# print(a is b)

# s = 'a b     c   d\ne\nf'
# print(s)
# print(s.split())

# with open("data/Pride and Prejudice.txt", encoding="utf-8") as f:
#     text = f.read()
#     words = text.strip().split()
#     print(words[:10])


# names = ['Amelia', 'Renee', 'Aurora']
# scores = [95, 96, 94]

# name_scores = list(zip(names, scores))
# print(name_scores)

# print(name_scores[2][1])

# 
def histogram(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

# print(histogram('alejandro macia'))

with open("data/Pride and Prejudice.txt", encoding="utf-8") as f:
    text = f.read()
    print(histogram(text))
