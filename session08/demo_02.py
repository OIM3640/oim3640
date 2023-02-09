def f(age):
    if age >= 18:
        # print('teenager')
        return 'adult'
    if age >= 10:
        return 'teenager'
    return 'kid'


# print(f(20))
# print(f(5))
import time


def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        time.sleep(1)
        countdown(n - 1)


countdown(5)
