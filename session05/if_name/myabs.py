def my_abs(number):
    """"""
    if number < 0:
        return -number
    else:
        return number


def square(a):
    return a**2


def main():
    print(my_abs(-10))
    print(my_abs(5))
    print(square(4))


# We don't want main() to be executed when this module is imported in other file
if __name__ == "__main__":
    main()
