class MoreThanTenError(Exception):
    """"""


def f(n):
    if n > 10:
        raise MoreThanTenError
    return n * 2


try:
    number = int(input("Please enter an integer: "))
    result = 2024 / number
    res = f(number)
    print(res)
except ValueError as e:
    print("You should enter an integer.")
    print(e)
except ZeroDivisionError as e:
    print("You just entered 0. ")
    print(e)
except MoreThanTenError:
    print('The input is more than 10.')
except Exception:
    print("A more genearl error")
finally:
    print("No matter what happens, we will still get here.")


print("Hello, world!")  # I want to see this no matter what
