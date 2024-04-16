# Design a class to represent a fractional number
"""
0.5 -> 

 1      x
---    ---
 2      y
"""


class Fraction:
    """
    Attributes:
        x (numerator): int
        y (denominator): int

    Methods:
        1. __init__: create an object of Fraction
        2. __str__: return a human-readable representation of the object
        3. to_float: return its equavilent value in float
        4. Dunder/special/magic methods: __add__, __sub__, __eq__, __contains__
    """

    def __init__(self, a, b):
        """"""
        if b == 0:
            raise ZeroDivisionError("Denominator cannot be zero!")

        import math

        gcd = math.gcd(a, b)
        if gcd > 1:
            a //= gcd
            b //= gcd
        self.x = a
        self.y = b

    def __str__(self):
        """return a human-readable representation of the object"""
        return f"{self.x:^3}\n---\n{self.y:^3}\n"

    def __add__(self, other):
        """Overload the '+' operator, return a new fractional number"""
        new_x = self.x * other.y + self.y * other.x
        new_y = self.y * other.y
        new_frac = Fraction(new_x, new_y)
        return new_frac

    def __sub__(self, other):
        """Overload the '-' operator, return a new fractional number"""
        new_x = self.x * other.y - self.y * other.x
        new_y = self.y * other.y
        new_frac = Fraction(new_x, new_y)
        return new_frac

    def __eq__(self, other):
        """"""
        return self.x == other.x and self.y == other.y
    
    def __contains__(self, number):
        """overload the `in` operator """
        return number == self.x or number == self.y

    def __mult__(self, other):
        """"""

    

    def to_float(self) -> float:
        return self.x / self.y


frac_1 = Fraction(1, 2)  # 1/2
frac_2 = Fraction(1, 4)  # 1/4

print(frac_1)
print(frac_2)
# frac_3 = Fraction(1, 0)  # raise an Error
frac_4 = Fraction(4, 6)  # 4/6 -> 2/3
print(frac_4)
s = frac_1 + frac_2
print(s)  # 3/4
print(frac_1 + frac_4)  # 1/2 + 2/3 = 7/6

print(frac_4 - frac_2)  # 2/3 - 1/4 = 5/12

frac_5 = Fraction(6, 9)
print(frac_4 == frac_5)

print(1 in frac_1)
print(2 in frac_1)

print(frac_1.to_float())
print(frac_4.to_float())

print(len(frac_1))