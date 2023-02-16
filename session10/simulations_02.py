# Write function(s) to repeat a simulation 10 times; in each simulation, roll 100 dice simultaneously and print the sum of the dice.

"""
I will create 2 function.

Function 1: one simulation, rolling 100 dice
Rolling 100 dice -> gerating 100 random numbers and sum up together
Pseudo code:
1. Create a variable to store the sum, initialize it to 0
2. Repeat the following step(s) 100 times:
    1. generate a random integer between 1 and 6 (inclusive)
    2. add the random integer to the sum variable
3. print the result

Function 2: repeat the simulation 10 times
1. Repeat the following step(s) 10 times
    1. call function 1
"""

import random


def roll_dice(n=100):  # parameters with default value
    """roll n dice, return the sum and the average"""
    # print('We found the sum!') # fake it till make it!
    result = 0
    for i in range(n):
        randon_number = random.randint(1, 6)
        result += randon_number
    # print(result)
    avg = result / n
    return result, avg


def repeat_simulations(m=10):
    """repeat the simulation m time"""
    for i in range(m):
        total, mean = roll_dice(10000)
        print(f'{total = }, {mean = }')


# Write function(s) to simulate rolling 100 dice multiple times simultaneously and count how many rolls it takes to reach a sum of 600.


def count_simulations():
    """Count how many rounds it takes to reach a sum of exactly 300 by rolling 100 dice"""
    counter = 0

    # result, _ = roll_dice()
    # print(f'{counter = }, {result = }')
    # counter += 1

    # while result <= 350:
    #     result, _ = roll_dice()
    #     print(f'{counter = }, {result = }')
    #     counter += 1

    # Repeat rolling dice until the sum is <greater than> 300
    while True:
        result, _ = roll_dice()
        print(f'{counter = }, {result = }')
        counter += 1
        if result == 300:
            break
    return counter


def main():
    """"""
    # roll_dice()
    # repeat_simulations(5)
    print(count_simulations())


if __name__ == "__main__":
    main()
