from Student import UG, Grad


class Grades:
    """A mapping from students to a list of grades"""

    def __init__(self):
        """Initializes an empty grade book"""
        self.students = []  # list of Student objects
        self.grades = {}  # maps id -> list of grades
        self.is_sorted = True  # True if self.students is sorted

    def add_student(self, student):
        """Adds a new student to the grade book"""
        if student in self.students:
            raise ValueError("Duplicate student")
        self.students.append(student)
        self.grades[student.id] = []
        self.is_sorted = False

    def add_grade(self, student, grade):
        """Adds a new grade to a student's record"""
        try:
            self.grades[student.id].append(grade)
        except KeyError:
            raise ValueError("Student not in grade book")

    def get_grades(self, student):
        """Returns a copy of a student's list of grades"""
        try:  # return copy of student's grades
            return self.grades[student.id][:]
        except KeyError:
            raise ValueError("Student not in grade book")

    def all_students(self):
        """Returns a sorted list of all students in the grade book"""
        if not self.is_sorted:
            self.students.sort()
            self.is_sorted = True

        # return copy of list of students
        return self.students[:]


def gradeReport(course):
    """Generates a grade report for a given course"""
    report = []
    for s in course.all_students():
        tot = 0.0
        num_grades = 0
        for g in course.get_grades(s):
            tot += g
            num_grades += 1
        try:
            average = tot / num_grades
            report.append(str(s) + "'s mean grade is " + str(average))
        except ZeroDivisionError:
            report.append(str(s) + " has no grades")
    return "\n".join(report)


def main():
    ug1 = UG("Aryan Subramanian", 2025)
    ug2 = UG("Moises Yi", 2024)
    ug3 = UG("Xinjia Chen", 2026)
    ug4 = UG("Jasmin Zhang", 2024)

    g1 = Grad("Matt Damon")
    g2 = Grad("Ben Affleck")

    oim3640 = Grades()
    oim3640.add_student(g1)
    oim3640.add_student(ug2)
    oim3640.add_student(ug1)
    oim3640.add_student(g2)
    oim3640.add_student(ug4)
    oim3640.add_student(ug3)

    oim3640.add_grade(g1, 100)
    oim3640.add_grade(g2, 25)
    oim3640.add_grade(ug1, 95)
    oim3640.add_grade(ug2, 85)
    oim3640.add_grade(ug3, 90)

    print("After first test:")
    print(gradeReport(oim3640))

    oim3640.add_grade(g1, 90)
    oim3640.add_grade(g2, 45)
    oim3640.add_grade(ug1, 80)
    oim3640.add_grade(ug2, 100)

    print()
    print("After second test:")
    print(gradeReport(oim3640))

    for student in oim3640.students:
        print(student.speak("I am excited to see the results!"))


if __name__ == "__main__":
    main()
