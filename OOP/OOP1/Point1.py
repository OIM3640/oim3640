class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """

    def __init__(self, x=0, y=0):
        """
        Initialize a Point object with given x and y, also called constructor
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Return a human-readable representation of the object
        (3, 4)
        """
        return f"({self.x}, {self.y})"

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


# idea 3
p1 = Point(
    3, 4
)  # create an object/instance of Point, actually is calling the constructor
# print(p1.x, p1.y)
# print(p1)

p1.move(1, 1)
# print(p1)

p2 = Point()
# print(p2.x, p2.y)

"""
Another example of OOP: creating humans in GTA
"""


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weapons = [] 


    def __str__(self):
        return f"{self.name}, age = {self.age}"

    def talk(self):
        if self.age > 21:
            print(f"{self.name} says: Hi! Where is the drink?")
        else:
            print(f"{self.name} says: Hi! I am {self.age} years old.")

    def greet(self, other):
        print(f"{self.name} greets: Hello, {other.name}!")


    def rob(self, other):
        """"""
        print(f"{self.name} robs {other.name}.")


    def buy_weapon(self, weapon):
        self.weapons.append(weapon)

    def ride(self, vehicle):
        """"""


class Weapon:
    """"""
    def __init__(self, power, bullets):
        """"""

class Vehicle:
    """"""

class Shotgun(Weapon):
    """"""


marissa = Human("Marissa", 20)
adrien = Human("Adrien", 22)


print(marissa)
print(adrien)

marissa.talk()
adrien.talk()

marissa.greet(adrien)
adrien.rob(marissa)



adrien.buy_weapon('handgun')
adrien.buy_weapon('AK47')
print(adrien.weapons)