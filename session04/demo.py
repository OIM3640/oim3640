print(3.14e-2)


length = len(str(2**10_000))

print(length)  # number of digits in 2**10,000


# import math


# print(math.pi)
# print(math.sqrt(4))


# import random

# print(random.random())

# String

print('I\'m "ok".')

print("I'm learning:\n\tPython\n\tHTML.")


print("\\\t\\")
print(r"\\\t\\")


print(
    """First line
second line
third line"""
)


username = "admin"
password = "123456"

username_input = input("Username >> ")
password_input = input("Password >> ")

if username == username_input and password == password_input:
    print("Correct! Welcome back!")
else:
    print("Get out of here, hacker!")
