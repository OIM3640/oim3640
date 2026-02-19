# for i in range(5):
#     print(i)


# i = 0
# while i < 5:
#     print(i)
#     i += 1


# response = ""
# while response != "quit":
#     response = input("Enter command: ")
#     print(f"You said: {response}")

# Example: Input validation loop
# print("\n--- Input Validation Example ---")
# valid_input = False
# while not valid_input:
#     age = input("Enter your age (must be 0-120): ")
#     age_num = int(age)
#     if 0 <= age_num <= 120:
#         print(f"Valid age: {age_num}")
#         valid_input = True
#     else:
#         print("Age must be between 0 and 120. Try again.")


# Example: Simple Login System
# print("\n--- Simple Login System ---")
# username = "admin"
# password = "password123"

# while True:
#     user_input = input("Enter username: ")
#     pass_input = input("Enter password: ")

#     if user_input == username and pass_input == password:
#         print("Login successful!")
#         break
#     else:
#         print("Invalid username or password. Try again.")


# # creating a game loop
# def game_loop():
#     print("game on...")
#     return "game over"

# while True:
#     result = game_loop()
#     if result == "game over":
#         break


# break - exit the loop immediately
# words = ["hello", "world", "target", "python"]
# for w in words:
#     print('checking:', w)
#     if w == "target":
#         print("Found it!")
#         break


# words = ["hello", "world", "target", "python"]
# for w in words:
#     print('Checking:', w)
#     if w == "target":
#         print("Found it!\n")
#         continue
#     print("Not the target\n")

# continue - skip to the next iteration
# for num in range(10):
#     if num % 2 == 0:
#         continue
#     print(num)  # prints odd numbers only


def f(n):
    for num in range(n):
        if num % 2 == 0:
            continue
        return num


# print(f(10))


for line in open("data/words.txt"):
    print(line)
