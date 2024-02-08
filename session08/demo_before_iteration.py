def check(score):
    if score >= 60:
        print("Pass")
        return  # `return`immediately end this function
    if score >= 90:
        print("A")
    else:
        print("Fail")


# check(95)


def f(a, b, c=0):
    # return a * 10 + b
    return a * 100 + b * 10 + c


# res_1 = f(3, 5, 1)  # positional arguments
# print(res_1)

# res_2 = f(b=5, a=3, c=1)  # keyword arguments
# print(res_2)

# res_3 = f(3, 5)  # c is using default value
# print(res_3)


def f(a, b):
    print(a + b)


def f2(a, b):
    """
    Return sum of a and b, given a, b

    prompt user to enter a, b, return sum of them
    """
    a = int(input("Enter: "))
    b = int(input("enter: "))
    return a + b


print(f2(3, 5))

# print(f2())
