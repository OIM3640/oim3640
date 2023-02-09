"""
Write a program, factorial.py to compute a factorial of an integer, n.
"""

def factorial(n):
    """
    Returns the factorial of n.

    1! = 1
    2! = 2 * 1
       = 2 * 1!
    3! = 3 * 2 * 1
       = 3 * 2!

    n! = n * (n-1)!
    """
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(3))