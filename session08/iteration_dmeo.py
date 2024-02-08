# i = 0

# while i < 4:
#     print('Hi')
#     i += 1

# for i in range(4):
#     print("Hi")

# calculate the sum of all the integers from 0 to 100

# total = 0

# for i in range(101):
#     print(f"Iteration {i}:")
#     print(f"   before adding {i}, the current total is {total}")

#     total += i

#     print(f"   after adding {i}, the total becomes {total}")
#     print()

# print(total)

# Create a function, sum_up_100(), that calculates the sum of all the integers from 0 to 100


def sum_up_100():
    """calculate the sum of all the integers from 0 to 100"""
    total = 0

    for i in range(101):
        # print(f"Iteration {i}:")
        # print(f"   before adding {i}, the current total is {total}")

        total += i

        # print(f"   after adding {i}, the total becomes {total}")
        # print()

    return total


print(sum_up_100())

# Create a function, sum_up(n), that takes an argument, n, and calculate the sum of all the integers from 0 to n


def sum_up(n):
    """
    takes an argument, n, and calculate the sum of all the integers from 1 to n
    """
    total = 0
    for i in range(1, n + 1):
        total += i

    return total


print(sum_up(100))


def sum_up_while(n):
    """
    takes an argument, n, and calculate the sum of all the integers from 1 to n using while loop
    """
    total = 0

    i = 0

    while i < n + 1:
        total += i
        i += 1

    return total


print(sum_up_while(100))
