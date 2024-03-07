def add_three(num):
    num += 3
    return num


a = 5
print(add_three(a))
print(a)


# If you are passing a sequence as an argument to a function, using tuples reduces the potential for unexpected behavior due to aliasing.


def add_two(lst):
    lst += [2]
    return lst


s = [0, 1]
print(add_two(s))
print(s)


def add_four(t):
    t += (4,)
    return t


t = (0, 1)
print(add_four(t))
print(t)
