r1 = 1
r2 = 31
r3 = 2023

area1 = 3.14159 * r1 * r1
area2 = 3.14159 * r2 * r2
area3 = 3.14159 * r3 * r3

# print(area1, area2, area3)

# radius is a parameter variable
def compute_area(radius):
    """
    This is the docstring, which a short summary of the function.

    Calculate the area of a circle, and return it.
    """
    # We always assume the parameter variable(s) values are given
    pi = 3.14159
    area = pi * radius**2
    # We could print the result
    # print(area)
    # if the function does not explicitly return any value, it will return None
    return area


# area1 = compute_area()
# area2 = compute_area()
# area1 = compute_area(r1) # calling function
# area2 = compute_area(r2)
# area3 = compute_area(r3)
# print(area1)

# print(area1 + area2 + area3)


def double(a):
    """
    return a * 2
    """
    # print(a * 2)
    return a * 2


# print(double(2))
# double(3)


print(compute_area(8))

# given a radius of 3, calculate the area of a circle with double the given radius
# radius = 3
# new_radius = double(radius)
# res = compute_area(new_radius)
# print(res)


def print_lyrics():
    print("Hey Jude. Don't make it bad.")
    print("Take a sad song and make it better.")


def repeat_lyrics():
    print_lyrics()
    print('Na - na - na - na - na, na - na - na - na')
    print_lyrics()


# repeat_lyrics()


def give_me_a_break():
    message = 'break'
    return message  # return immediately tereminates the function
    print('Another break!')  # this line is unreachable


print(give_me_a_break())
# print(message)
