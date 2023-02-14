# Calculate the sum of integers from 1 to 10.

def sum10():
    """
    calculate the sum of integers from 1 to 10, and return the sum
    """
    result = 0

    for i in range(1, 11):
        print(f'Iteration {i}:')
        print(f'  Before adding {i}, current result is {result}.')

        result += i

        print(f'  After adding {i}, result becomes {result}.')
        print()

    return result


# print(sum10())

def sum1000():
    """
    calculate the sum of integers from 1 to 1000, and return the sum    
    """
    result = 0

    for i in range(1, 1001):
        # print(f'Iteration {i}:')
        # print(f'  Before adding {i}, current result is {result}.')

        result += i

        # print(f'  After adding {i}, result becomes {result}.')
        # print()

    return result

# print(sum1000())

def sum_up(n):
    """
    calculate the sum of integers from 1 to n, and return the sum
    """
    result = 0
    for i in range(1, n+1):
        result = result + i

    return result
    
# print(sum_up(1000))


"""
When to use for loop:
    - when we know exactly how many times to repeat a certain code block
    - when we iterate over a collection of items
        - a string
        - a list
        - a tuple
        - a dictionary

When to use while loop:
    - if we only know when / what condition to stop, and we don't know how many times
"""

def countdown(n):
    """ Count down numbers from n"""
    # Pseudo code:
    # Repeat the following task(s) until n > 0 is not True:
    #   - print n out
    #   - decrease n by 1
    while n > 0:
        print(n)
        n = n - 1 # same as n -= 1
    print("Blastoff!")

countdown(5)