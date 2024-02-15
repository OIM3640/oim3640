# for i in range(1, 10):
#     if i % 3 == 0:
#         continue
#     print(i)


# print("😊" * 5)

# for i in range(1, 5):
#     print("😊" * i)


# n = 5
# while n != 0:
#     print(n)
#     n = n - 2


# print("after while", n)


# Use for loop
# when you know the exact number of iterations

# for i in range(4):
#     print("hi")

# when you know the range of an integer sequence

# for i in range(3, 10, 2):
#     print(i)


# when you need to iterate over a collection/sequence, such as a string, list, tuple, dictionary, set ...

# for whatever in "Yashashvi":  # a string
#     print(whatever)

# for num in [5332, 6435, 745, 523]:  # a list
#     print(num)

# Use while loop
# when you need to create an infinite loop

# while True:
#     start_game()


# when you don't know the exact number of iterations beforehand, and want to continue until
# ... the specific condition is no longer true
# import time

# i = 5
# while i > 0:
#     print(i)
#     time.sleep(1)
#     i -= 1

# print("blastoff!")


# or until a break statement is encountered

while True:
    user_input = input("Please enter your password: ")
    if user_input == "123456":
        print("You are logged in. Welcome!")
        break
    else:
        print("Try one more time.")
