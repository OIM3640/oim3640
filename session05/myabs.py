def my_abs(number):
    """
    Return the absolute value of a number

    number: an integer or a floating point number
    """
    if number < 0:
        return -number
    else:
        return number


# print(my_abs(-5))

# We want to keep the test code when running this current file, but we don't want to run the test code when we import this current module in other python program

print(f'__name__: {__name__}')

def main():
    """This will be the entry function. All the test code goes here"""
    print(my_abs(-5))


if __name__ == "__main__":
    # This will only run if the script is executed as the main program
    # This will not run if this script is imported as a module.
    main()
