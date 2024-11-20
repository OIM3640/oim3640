# Create a class for weird integers

# 3 + 2 = 32
# 3 - 2 = 1


class WeirdInt:
    """
    Attributes:
        - value

    Methods:
        - __init__, __str__
        - __add__, overloading `+` operator
        - etc.
    """

    def __init__(self, v):
        self.value = v

    def __str__(self):
        return str(self.value)

    def __add__(self, another):
        """Overload the `+` operator"""
        return WeirdInt(int(str(self.value) + str(another.value)))

    def __sub__(self, another):
        """Overload the - operator"""
        return WeirdInt(self.value - another.value)

    def __mul__(self, another):
        """"""
        return 0


a = WeirdInt(3)
b = WeirdInt(2)
print(a)
print(b)

result = a + b
print(result)

print(a - b)
print(a * b)
print(a / b)  # error
