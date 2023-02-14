# Calculate the sum of integers from 1 to 10.

def sum10():
    """
    Calculate the sum of integers from 0 to 10, return the sum
    """
    result = 0 

    # repeat adding number to result 
    for i in range(11):
        print(f'Iteration {i}:')
        print(f'  before adding {i}, the current result is {result}.')
        result += i # same as result = result + i
        print(f'  after adding {i}, the result becomes {result}.')
        print()

    return result

# print(sum10())


def sum1000():
    """
    Calculate the sum of integers from 1 to 1000, return the sum.
    """
    result = 0 

    # repeat adding number to result 
    for i in range(1, 1001):
        # print(f'Iteration {i}:')
        # print(f'  before adding {i}, the current result is {result}.')
        result += i # same as result = result + i
        # print(f'  after adding {i}, the result becomes {result}.')
        # print()

    return result


# print(sum1000())

def sum_up(n):
    """
    Calculate the sum of integers from 1 to n, and return the sum
    """
    result = 0

    for i in range(1, n + 1):
        result += i

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
        - ...


When to use while loop:
    - if we only know when / what condition to stop, and we don't know exactly how many times of iterations
"""
import time
def countdown(n):
    """
    Count down numbers from n to 1, then blastoff!
    """
    # Pseudo-code:
    # Repeat the following task(s) until the condition n>0 is not True any more:
    #   - print n
    #   - pause one sec
    #   - decrease n

    while n > 0:
        print(n)
        time.sleep(1)
        n -= 1
    print("Blastoff!")

    
countdown(5)