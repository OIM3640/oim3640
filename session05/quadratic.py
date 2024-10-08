import math


def solve_quadratic(a, b, c):
    """Simple version of quadratic equation solver
    a: float
    b: float
    c: float

    Return two roots of the quadratic equation"""
    discriminant = b**2 - 4 * a * c  # calculate the discriminant

    x_1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x_2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return x_1, x_2


# print(solve_quadratic(1, 2, 1))

# aa = float(input("Enter a number: >>> "))
# bb = float(input("Enter a number: >>> "))
# cc = float(input("Enter a number: >>> "))

# print(solve_quadratic(aa, bb, cc))

















def solve_quadratic(a, b, c):
    """
    Solve a quadratic equation of the form a*x^2 + b*x + c = 0 and return two roots if they exist.

    a: float
    b: float
    c: float

    Returns:
    - tuple of two floats: If there are two real roots.
    - float: If it is a linear equation (a = 0) and has one solution.
    - None: If there is no real number solution.
    """
    if a == 0 and b == 0:
        # print('Hey, this is not a quadratic equation!')
        # return None
        raise ValueError("This is not an equation.")
    if a == 0:
        print("This is a linear function.")
        return -c / b

    discriminant = b**2 - 4 * a * c  # calculate the discriminant

    if discriminant >= 0:  # equation has solutions
        x_1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x_2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x_1, x_2
    else:
        print("No real number solution.")
        return None
        # raise ValueError('No real number solution!')


def main():
    print(solve_quadratic(2, 2, 2))
    print(solve_quadratic(1, 4, 1))

    try:
        a = float(input("Enter the coefficient of x^2: "))
        b = float(input("Enter the coefficient of x: "))
        c = float(input("Enter the constant term: "))

        result = solve_quadratic(a, b, c)

        if result is not None:
            if isinstance(result, float):
                print(f"The solution is {result:.2f}.")
            else:
                root_1, root_2 = result
                print(f"Two roots are {root_1:.2f} and {root_2:.2f}.")
        else:
            print("Sorry 😎. No real number solution.")
    except ValueError:
        print("Invalid input or equation. Please enter valid numeric coefficients.")


if __name__ == "__main__":
    main()
