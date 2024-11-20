class Human:
    def __init__(self, name, age, health=100):
        self.name = name
        self.age = age
        self.health = health
        self.guns = []

    def __str__(self):
        return f"{self.name} ({self.age} yrs old, health level: {self.health})"

    def talk(self):
        print(f"{self.name} says: Hi")

    def greet(self, other):
        print(f"{self.name} greets: Hello, {other.name}!")

    def buy_gun(self, weapon):
        self.guns.append(weapon)

    def rob(self, other):
        """"""

    def ride(self, car):
        """"""

class Weapon:
    def __init__(self, name, bullets=10):
        self.name = name
        self.bullets = bullets

    def shoot(self, person):
        pass

    def __str__(self):
        return self.name


class Vehicle:
    """"""

class SUV(Vehicle):
    """"""

class Sedan(Vehicle):
    """"""

def main():
    michael = Human("Michael", 45)
    franklin = Human("Franklin", 22)
    print(michael)
    print(franklin)

    michael.talk()
    michael.greet(franklin)

    handgun = Weapon("Handgun")
    michael.buy_gun(handgun)

    shotgun = Weapon("Shotgun", 7)
    franklin.buy_gun(shotgun)

    machinegun = Weapon("Machine gun")
    michael.buy_gun(machinegun)
    
    for gun in michael.guns:
        print(gun)


main()
