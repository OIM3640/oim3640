import math


def mysqrt(a):
    """
    Use Newton's method to compute square root of a positive number.
    """
    epsilon = 1e-5
    x = 1
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            break
        x = y
    return y


def square_root(n):
    """
    Print the square root of integers from 1 to n formattedly
    """
    # print("a   mysqrt(a)      math.sqrt(a)   diff          ")
    print(f"{'a':>3} {'mysqrt(a)':<14} {'math.sqrt(a)':<14} {'diff':<14}")
    print(f"{'-' * 3:3} {'-' * 13:14} {'-' * 13:14} {'-' * 17:17}")
    for a in range(1, n + 1):
        diff = abs(mysqrt(a) - math.sqrt(a))
        print(f"{a:>3d} {mysqrt(a):<14.12g} {math.sqrt(a):<14.12g} {diff:<14.12g}")


def main():
    # for i in range(1, 10):
    #     print('The square root of', i, 'is', mysqrt(i))
    square_root(10)


if __name__ == "__main__":
    main()
