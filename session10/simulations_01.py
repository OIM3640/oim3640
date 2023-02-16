# Write function(s) to repeat a simulation 10 times; in each simulation, roll 100 dice simultaneously and print the sum of the dice.
"""
Pseudoe code:

Function 1: one simulation, rolling 100 dice

1. Create a variable to store the sum, initialize it to 0
2. repeat the following step(s) 100 times, simulating rolling one die
    1. get a random integer in range [1, 6]
    2. add the random integer to the sum variable
3. print the result


Function 2: repeat simulation 10 times
1. repeat the following step(s) 10 times (for, while)
    1. call function 1
"""
# [
#     {"sum": 350, 'avg': 3.50},
#     {"sum": 351, 'avg': 3.51},
#     {"sum": 350, 'avg': 3.50},
#     {"sum": 350, 'avg': 3.50},
#  ]

import random


def roll_dice(n=100):  # default value
    """roll n dice, return the sum and the average"""
    # print('We found the sum!') # fake it till make it
    result = 0
    for i in range(n):
        random_number = random.randint(1, 6)
        result += random_number
    avg = result / n
    return result, avg


def repeat_simulations(m=10):
    """repeat simulation m times"""
    for i in range(m):
        s, mean = roll_dice()
        print(f'{s = }, {mean = }')


# Write function(s) to simulate rolling 100 dice multiple times simultaneously and count how many rolls it takes to reach a sum of 600.


def count_simulations():
    """count how many rolls it takes to reach a sum of 600 by rolling 100 dice"""
    counter = 0
    
    # 1. Keep trying until we get 600
    while True:
        result, _ = roll_dice()
        print(f'{result=}')
        counter += 1
        if result == 300:
            break
    return counter


def main():
    """"""
    # roll_dice()
    repeat_simulations()
    # print(count_simulations())


if __name__ == "__main__":
    main()
