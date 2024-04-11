from datetime import datetime


def days_until_birthday(birthday):
    """How long until my next birthday?"""


def double_day(b1, b2):
    """Compute the day when one person is twice as old as the other.

    b1: datetime birthday of the younger person
    b2: datetime birthday of the older person
    """


def datetime_exercises():
    """Exercise solutions."""

    # print today's day of the week

    # compute the number of days until the next birthday
    # (note that it usually gets rounded down)
    birthday = datetime(2002, 10, 29)
    print('Days until birthday', end=' ')
    print(days_until_birthday(birthday))

    # compute the day one person is twice as old as another
    b1 = datetime(2023, 12, 25)
    b2 = datetime(2010, 11, 1)
    print('Double Day', end=' ')
    print(double_day(b1, b2))


if __name__ == '__main__':
    datetime_exercises()
