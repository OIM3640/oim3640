# for i in range(4):
#     print("Iteration:", i)
#     print("Square:", i * i)
#     print()

# def double(number):
#     """Return double the input number."""
#     return number * 2


# print(double(5))
# print(double("5"))


# a = 5 # int is immutable
# b = a
# a = 10
# print(b)  # what is the value of b?
# print(a)


# a = [1, 2, 3] # list is mutable
# b = a
# a.append(4)
# print(b)
# print(a)


# x = 10

# def f():
#     message = 'hello'
#     x = 5
#     return message + str(x)

# print(f())
# print(x)
# print(message)


# Draw a square
"""
🧱🧱🧱🧱
🧱🧱🧱🧱
🧱🧱🧱🧱
🧱🧱🧱🧱
"""


# def draw_square(size):
#     for i in range(size):
#         # print("🧱" * size)
#         for j in range(size):
#             print("🧱", end="")
#         print() # move to the next line after inner loop

# print('Hi', end="")
# print('Hello')


def draw_square(size):
    for i in range(size):
        print("🧱" * size)


draw_square(4)


"""
Create a function to draw a triangle
🧱           1 = 0 + 1
🧱🧱         2 = 1 + 1
🧱🧱🧱       3 = 2 + 1
🧱🧱🧱🧱     4 = 3 + 1

In row i, how many bricks are there? i + 1
"""
# def draw_triangle(size):
#     for i in range(size):
#         print("🧱" * (i + 1))

def draw_triangle(size):
    for i in range(1, size+1):
        print("🧱" * i)

draw_triangle(4)


"""
Draw a triangle like this (size = 5)
          i
    #     0    4 spaces + 1 # = 5   5 - 0 -1 = 4 
   ##     1    3 spaces + 2 # = 5   5 - 1 - 1 = 3
  ###     2    2 spaces + 3 # = 5   5 - 2 - 1 = 2
 ####
#####
   
for i in range(size):
In row i, how many spaces are there? size - i - 1

how many #s are there?   i + 1
"""

def draw_triangle(size):
    for i in range(size):
        print(" " * (size - i - 1) + "#" * (i + 1))

draw_triangle(5)


# create a function to draw a pyramid
"""
    #
   ###
  #####
 #######
"""