from BabsonPerson import BabsonPerson
from Person import Person


class Student(BabsonPerson):
    """A class representing a student at Babson College."""

    pass


class UG(Student):
    """A class representing an undergraduate student at Babson College."""

    def __init__(self, name, class_year):
        """
        Initializes a UG instance with a name and class year.
        """
        BabsonPerson.__init__(self, name)
        self.year = class_year

    def get_class_year(self):
        """Returns the class year of the student."""
        return self.year

    def speak(self, expression):
        """Returns a string that consists of the student's name and a given expression."""
        return BabsonPerson.speak(self, " Dude, " + expression)


class Grad(Student):
    """A class representing a graduate student at Babson College."""

    pass


def is_student(obj):
    """Returns True if the given object is an instance of Student, and False otherwise."""
    return isinstance(obj, Student)


def main():
    s1 = UG("Aryan Subramanian", 2025)
    s2 = UG("Moises Yi", 2024)
    s3 = UG("Xinjia Chen", 2026)
    s4 = Grad("Matt Damon")

    student_list = [s1, s2, s3, s4]

    print(s1)

    # print(s1.get_class_year())
    # print(s1.year)

    print(s2.speak("Where is the quiz?"))
    print(s3.speak("I have no clue!"))
    print(s4.speak("I am not sure why I am here."))

    print(is_student(s1))

    p1 = Person("Taylor Swift")
    print(is_student(p1))


if __name__ == "__main__":
    main()
