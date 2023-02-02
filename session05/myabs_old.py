def my_abs_3(n):
    """
    Print the absolute value of given number.
    """
    if n < 0:
        print(-n)
    else:
        print(n)


# my_abs_3(-3)
# my_abs_3(0)
# my_abs_3(2)

def my_abs_4(n):
    """
    Return the absolute value of a given number.
    """
    if n < 0:
        return -n
    else:
        return n

# print(my_abs_4(-3))

import math

# print(math.sqrt(my_abs_4(-4)))
# print(math.sqrt(my_abs_3(-4)))

print(math.sqrt(my_abs_4('-4')))

