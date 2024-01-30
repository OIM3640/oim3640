r1 = 4
r2 = 42
r3 = 2024

# area1 = 3.14159 * r1 * r1
# area2 = 3.14159 * r2 * r2
# area3 = 3.14159 * r3 * r3

# print(area1, area2, area3)


def compute_area(radius):
    """
    (This is docstring, which should be a short summary of this function)

    Given radius, calcuate the area of a circle and return it.
    """
    pi = 3.14

    # radius is parameter variable; we should treat it as given inside of the funciton

    area = pi * radius * radius
    # print(area)
    # if the function does not explicitly return any value, it will return None
    return area


area1 = compute_area(r1)  # calling a function
# print(area1)
area2 = compute_area(r2)

# print(area1 + area2)

# define a function call add that takes two arguments and return the sum


def add(a, b):
    """
    Return the sum of a and b
    a: int or float
    b: int or float
    """
    result = a + b
    return result


total = add(area1, area2)
print(total)

print(add("Hi,", "world!"))
