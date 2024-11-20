# OOP, object oriented programming
# as opposed to procedural programming

# to represent a point on 2D space

# Solution 1
# x = 0
# y = 0

# Solution 2
# p1 = [3, 4]
# p2 = [5, 5]

# p1[0] += 1  # What is 0 here after a while?
# p1[1] -= 1

# print(p1)

# Solution


class Point:
    """Represent a point in 2-D space

    Attributes: x, y
    """

    def __init__(self, a, b):
        """Initialize an object of Point"""
        self.x = a
        self.y = b

    def __str__(self):
        """Return a human-readable representation of this object, eg. (3, 4)"""
        return f"({self.x}, {self.y})"

    def move_x(self, n):
        self.x += n

    def add_point(self, another_point):
        """
        e.g. self (3, 4), another_point (1, 1) -> (4, 5)
        """
        new_x = self.x + another_point.x
        new_y = self.y + another_point.y
        return Point(new_x, new_y)


p1 = Point(3, 4)

print(type(p1))
print(p1)
# print(p1.x, p1.y)
# p1.move_x(5)
# print(p1)

p2 = Point(5, 5)
print(p2)

print(p1.add_point(p2))  # (8, 9)
