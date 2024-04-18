from BabsonPerson import BabsonPerson
from Student import Student
from Person import Person


class Professor(BabsonPerson):
    """"""
    def __init__(self, name, course):
        BabsonPerson.__init__(self, name)
        self.course = course

    def speak(self, expression):
        new_expression = f'In course {self.course}, we say {expression}'
        return BabsonPerson.speak(self, new_expression)


def main():
    p1 = Professor("Zhi Li", "OIM 3640")
    print(p1)
    print(p1.id)
    p2 = Professor('Shankar', 'OIM 3690')
    print(p2.id)
    # print(isinstance(p1, BabsonPerson))
    # print(isinstance(p1, Person))
    # print(isinstance(p1, Student))
    print(p1.speak('Python is great!'))
    print(p2.speak('Everybody with me!'))


if __name__ == "__main__":
    main()
