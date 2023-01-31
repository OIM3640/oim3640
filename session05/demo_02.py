r1 = 1
r2 = 31
r3 = 2023

# area1 = 3.14 * r1**2
# area2 = 3.14 * r2**2
# area3 = 3.14 * r3**2


# print(area1, area2, area3)

def double(a):
    """
    return the double of given value
    """
    return a * 2

r = 2
# print(double(r))

# radius is the parameter viriable
def compute_area(radius):
    """
    Calculate the area of a circle with a given radius and return it.

    This is docstring, which is a short description of this function.
    """
    area = 3.1415926 * radius ** 2
    # print(area)
    return area
    # if the function does not return any value explicitly, it will return None

# Given a radius, calculate the area of circle with double the given radius.
d = double(r)
# print(compute_area(d))

# compute_area(r1) # calling the function, r1 is the argument
# compute_area(r2)
# compute_area(r3)

# area1 = compute_area(r1)
# area2 = compute_area(r2)
# area3 = compute_area(r3)

# total_area = area1 + area2 + area3
# print(total_area)



# y = a * x + b


def print_lyrics():
    print("Hey Jude. Don't make it bad.")
    print("Take a sad song and make it better.")

def repeat_lyrics():
    print_lyrics()
    print('Na - na - na - na - na, na - na - na - na')
    print_lyrics()

# repeat_lyrics()

def give_me_a_break():
    str1 = 'break'
    return str1 # return immediately terminates the function
    print("another break")

print(give_me_a_break())
# print(str1)