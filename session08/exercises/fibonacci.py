def fibonacci(n):
    """
    1, 1, 2, 3, 5, 8, 13, ...

    fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
    """
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


for i in range(1, 10):
    print(fibonacci(i))
