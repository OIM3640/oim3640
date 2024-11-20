"""
Design a class to represent a fractional number

0.5 ->

 1      x
---    ---
 2      y

"""


class Fraction:
    """
    Attributes:
        x:numerator
        y:denominator

    Methods:
        - __init__, ...
        - __add__, __sub__, etc
        - __eq__,
        - ...
    """

    def __init__(self, a, b):
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
        return f'{self.x:^3}\n{"-"*3}\n{self.y:^3}'

    def __add__(self, other):
        """Overload the `+` operator, return a new fractional number"""
        new_x = self.x * other.y + self.y * other.x
        new_y = self.y * other.y
        return Fraction(new_x, new_y)
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


frac_1 = Fraction(1, 2)
print(frac_1)
frac_2 = Fraction(1, 4)
print(frac_2)
# frac_3 = Fraction(2, 0)
# print(frac_3)
frac_4 = Fraction(4, 6)  # 2/3
print(frac_4)

result = frac_1 + frac_2
print(result)  # 3/4

frac_5 = Fraction(3, 5)

print(frac_5 == result) # Python is checking the RAM addresses of the two variables
