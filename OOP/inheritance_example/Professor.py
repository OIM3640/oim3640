from BabsonPerson import BabsonPerson
from Student import Student
from Person import Person


class Professor(BabsonPerson):
    """"""


def main():
    p1 = Professor("Zhi Li", "OIM 3640")
    print(p1)
    print(p1.id)
    print(isinstance(p1, BabsonPerson))
    print(isinstance(p1, Person))
    print(isinstance(p1, Student))


if __name__ == "__main__":
    main()
